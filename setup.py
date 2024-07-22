# setup.py
from deepgram import Deepgram
import openai
from config import Config

class Setup:
    def __init__(self, config):
        self.config = config
        self.stt_engine = None
        self.tts_engine = None
        self.llm_engine = None

    def initialize(self):
        # Initialize STT
        self.stt_engine = Deepgram(self.config.stt_api_key)
        
        # Initialize LLM
        openai.api_key = self.config.llm_api_key

        # Initialize TTS (example with Deepgram, could be OpenAI)
        self.tts_engine = Deepgram(self.config.tts_api_key)
        
        print("Setup complete.")
