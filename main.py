from dotenv import load_dotenv
from livekit.plugins import tavus
from livekit import agents
from livekit.plugins import openai
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    noise_cancellation,
    silero,
)
import json
import os
from prompt import AGENT_PROMPT,SESSION_PROMPT
from tools import search_web

load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=AGENT_PROMPT,
            tools=[search_web]
            )



async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        llm=openai.realtime.RealtimeModel(
            model="gpt-4o-realtime-preview",
            voice='coral',
            temperature=0.8
        )
    )

    async def write_transcript():

        filename = "summary.json"

        with open(filename,'w') as f:
            json.dump(session.history.to_dict(),f, indent=2)

        print(f"Transcript for {ctx.room.name} saved to {filename}")    
    
    ctx.add_shutdown_callback(write_transcript)

    
    tavus_avatar = tavus.AvatarSession(persona_id="pe13ed370726", replica_id="r9d30b0e55ac")
    await tavus_avatar.start(session, room=ctx.room)

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
            audio_enabled=True,
        ),
    )

    await ctx.connect()

    await session.generate_reply(
        instructions=SESSION_PROMPT
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))