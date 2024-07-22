# config.py
class Config:
    def __init__(self, stt_api_key, tts_api_key, llm_api_key, system_prompt):
        self.stt_api_key = stt_api_key
        self.tts_api_key = tts_api_key
        self.llm_api_key = llm_api_key
        self.system_prompt = system_prompt
