# main.py
import asyncio
from config import Config
from setup import Setup
from stream import StreamConversation

def main():
    # Define configuration
    config = Config(
        stt_api_key='your_deepgram_api_key',
        tts_api_key='your_tts_api_key',
        llm_api_key='your_openai_api_key',
        system_prompt="Your system prompt here"
    )

    # Setup SDK
    setup = Setup(config)
    setup.initialize()

    # Stream conversation
    stream_conversation = StreamConversation(setup)

    # Example of using PyAudio streams
    input_stream = PyAudioInputStream()
    output_stream = PyAudioOutputStream()

    asyncio.run(stream_conversation.process_audio(input_stream, output_stream))

if __name__ == "__main__":
    main()
