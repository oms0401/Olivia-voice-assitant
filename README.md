# Olivia - LiveKit Voice Avatar Assistant 🤖💬

*Meet Olivia, your intelligent real-time voice AI companion*

![Olivia Avatar Demo](assets/olivia-demo-header.png)

A sophisticated real-time, interactive voice AI assistant powered by LiveKit Agents, OpenAI's GPT-4o Realtime API, Tavily web search, and a lifelike video avatar by Tavus. Olivia engages in natural conversations, provides intelligent responses with web search capabilities, and presents herself through a synchronized video avatar for an immersive user experience.


---

## ✨ Core Features

🎯 **Real-time Conversational AI**: Seamless, low-latency voice interaction with natural turn-taking  
🧠 **OpenAI GPT-4o Realtime**: Cutting-edge language model for intelligent, context-aware responses  
👤 **Tavus Avatar Integration**: Realistic, lip-synced video avatar for engaging visual interaction  
🔍 **Web Search Capability**: Real-time information retrieval using Tavily Search API  
🎙️ **Advanced Voice Processing**: Silero VAD for accurate speech detection and turn management  
🔇 **Noise Cancellation**: LiveKit's Basic Voice Cancellation (BVC) for crystal-clear audio  
📝 **Conversation Logging**: Automatic transcript saving to JSON for analysis and review  

---

## 🚀 Quick Start Guide

### Prerequisites

Ensure you have the following requirements met:

- **Python 3.9+** installed on your system
- **LiveKit Server** access (Cloud or self-hosted)
  - LiveKit Cloud: [Sign up here](https://cloud.livekit.io)
  - Self-hosted: Follow [LiveKit Server docs](https://docs.livekit.io/deploy/)

### Required API Keys

You'll need accounts and API keys from:

1. **OpenAI Platform**: [Get API Key](https://platform.openai.com)
2. **Tavily AI**: [Get API Key](https://tavily.ai)  
3. **Tavus Dashboard**: [Get API Key & Configure Persona](https://tavus.io)
   - Ensure your Tavus persona has `pipeline_mode: echo`
   - Configure `transport_layer` with `transport_type: livekit`
   - Note your concurrent conversation limits

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/olivia-voice-avatar.git
cd olivia-voice-avatar
```

### 2. Set Up Virtual Environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt

# Or install manually:
pip install "livekit-agents[openai,tavus,silero,noise-cancellation]~=1.0" langchain-community python-dotenv
```

---

## ⚙️ Configuration

Create a `.env` file in your project root:

```env
# LiveKit Configuration
LIVEKIT_URL="ws://localhost:7880"  # Or your LiveKit Cloud URL
LIVEKIT_API_KEY="LK_YOUR_API_KEY"
LIVEKIT_API_SECRET="LK_YOUR_API_SECRET"

# OpenAI Configuration
OPENAI_API_KEY="sk-YOUR_OPENAI_API_KEY"

# Tavily Search Configuration
TAVILY_API_KEY="tvly-YOUR_TAVILY_API_KEY"

# Tavus Avatar Configuration
TAVUS_API_KEY="YOUR_TAVUS_API_KEY"
TAVUS_PERSONA_ID="p2fbd605"    # Replace with your Persona ID
TAVUS_REPLICA_ID="r4c41453d2"  # Replace with your Replica ID
```

---

## ▶️ Running Olivia

### 1. Start LiveKit Server
Ensure your LiveKit server is running and accessible at your configured `LIVEKIT_URL`.

### 2. Launch the Agent
```bash
python main.py run
```

You should see logs indicating Olivia is ready and waiting for connections.

---

## 🤝 Interacting with Olivia

### Recommended: LiveKit Agents Playground

1. Open the [LiveKit Agents Playground](https://agents-playground.livekit.io)
2. Enter your LiveKit credentials (`LIVEKIT_URL`, `LIVEKIT_API_KEY`, `LIVEKIT_API_SECRET`)
3. Enable your microphone
4. Join a room - Olivia will automatically join
5. Start speaking! Olivia will greet you and respond to your queries

### Alternative Clients

- **LiveKit React Starter App**: For web integration
- **LiveKit Mobile SDKs**: iOS and Android examples
- **Custom Clients**: Use any LiveKit-compatible client

---

## 📁 Project Architecture

```
olivia-voice-avatar/
├── main.py              # Main agent entry point and session management
├── prompt.py            # AI personality prompts and conversation guides
├── tools.py             # Web search tools and function definitions
├── .env                 # Environment variables (create this)
├── requirements.txt     # Python dependencies
├── summary.json         # Generated conversation transcripts
└── assets/             # Demo media and screenshots
    ├── olivia-demo-header.png
    └── olivia-conversation-demo.mp4
```

### Key Components

- **`main.py`**: Orchestrates the LiveKit agent session, coordinates LLM, avatar, and audio processing
- **`prompt.py`**: Defines Olivia's personality, behavior guidelines, and conversation context
- **`tools.py`**: Implements web search functionality using Tavily API for real-time information retrieval
- **`summary.json`**: Runtime-generated conversation logs for analysis and debugging

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### "Maximum concurrent conversations reached" (Tavus)
- **Cause**: Your Tavus account has hit active session limits
- **Solution**: 
  - Log into Tavus Dashboard and manually end active conversations
  - Ensure proper session cleanup in your code (`session.aclose()`)
  - Consider upgrading your Tavus plan for higher limits

#### "Audio content shorter than expected" (OpenAI Realtime)
- **Cause**: Fragmented or silent audio streams
- **Solution**:
  - Verify microphone functionality and audio quality
  - Check VAD configuration parameters
  - Ensure consistent audio input from client

#### Agent Not Responding
- **Checklist**:
  - ✅ All environment variables correctly set in `.env`
  - ✅ LiveKit server running and accessible
  - ✅ Client publishing audio track to room
  - ✅ Check agent logs for API errors or exceptions
  - ✅ Verify API key permissions and quotas

#### Avatar Not Syncing
- **Troubleshooting**:
  - Confirm Tavus persona configuration (`pipeline_mode: echo`)
  - Verify `transport_type: livekit` in transport layer settings
  - Check network connectivity and latency

---

## 📊 Analytics & Monitoring

Olivia automatically generates conversation analytics:

- **Transcript Logging**: Complete conversation history in `summary.json`
- **Performance Metrics**: Response times, search queries, and interaction patterns  
- **Error Tracking**: API failures, connection issues, and system performance
- **Usage Analytics**: Session duration, user engagement, and feature utilization

---

## 🛠️ Development & Customization

### Extending Olivia's Capabilities

1. **Add New Tools**: Extend `tools.py` with additional function definitions
2. **Customize Personality**: Modify prompts in `prompt.py` to change Olivia's behavior
3. **Integrate APIs**: Add new service integrations for expanded functionality
4. **Avatar Customization**: Configure different Tavus personas and replicas

### Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **LiveKit**: For the robust real-time communication infrastructure
- **OpenAI**: For the advanced GPT-4o Realtime API
- **Tavus**: For lifelike avatar technology
- **Tavily**: For comprehensive web search capabilities

---

## 📞 Support & Community

- **Issues**: [GitHub Issues](https://github.com/your-username/olivia-voice-avatar/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/olivia-voice-avatar/discussions)
- **Documentation**: [Project Wiki](https://github.com/your-username/olivia-voice-avatar/wiki)

---

*Made with ❤️ by the Olivia development team*