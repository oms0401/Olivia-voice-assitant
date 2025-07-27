import logging
from livekit.agents import function_tool, RunContext
from langchain_tavily import TavilySearch
import os 
from dotenv import load_dotenv

load_dotenv()

@function_tool()
async def search_web(
    context: RunContext,
    query: str
) -> str:
    """
    Search the web using Tavily.
    """
    try:

        tavily_search = TavilySearch(api_key=os.getenv("TAVILY_API_KEY"))
        results = tavily_search.run(query)
        logging.info(f"Search results for '{query}': {results}")
        return results
    except Exception as e:
        logging.error(f"Error searching the web for '{query}': {e}")
        return f"An error occurred while searching the web for '{query}'."

