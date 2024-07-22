# observability.py
import time

class Observability:
    def __init__(self):
        self.stt_time = 0
        self.llm_time = 0
        self.tts_time = 0

    def log_stt_time(self, start, end):
        self.stt_time = end - start
        print(f"STT Time: {self.stt_time}")

    def log_llm_time(self, start, end):
        self.llm_time = end - start
        print(f"LLM Time: {self.llm_time}")

    def log_tts_time(self, start, end):
        self.tts_time = end - start
        print(f"TTS Time: {self.tts_time}")

    def log_total_time(self, start, end):
        total_time = end - start
        print(f"Total Time: {total_time}")
