# stream.py
import pyaudio
import asyncio
from setup import Setup
import time

class StreamConversation:
    def __init__(self, setup):
        self.setup = setup
        self.stt_engine = setup.stt_engine
        self.tts_engine = setup.tts_engine
        self.llm_engine = openai

    async def process_audio(self, input_stream, output_stream):
        # Define audio stream parameters
        chunk_size = 1024
        sample_format = pyaudio.paInt16
        channels = 1
        rate = 44100

        # Initialize PyAudio
        p = pyaudio.PyAudio()

        # Open input stream
        stream_in = p.open(format=sample_format, channels=channels,
                           rate=rate, input=True, frames_per_buffer=chunk_size)

        # Open output stream
        stream_out = p.open(format=sample_format, channels=channels,
                            rate=rate, output=True, frames_per_buffer=chunk_size)

        print("Listening...")

        while True:
            data = stream_in.read(chunk_size)
            input_stream.write(data)
            text = await self.speech_to_text(data)
            if text:
                response_text = await self.query_llm(text)
                audio_response = await self.text_to_speech(response_text)
                output_stream.write(audio_response)

    async def speech_to_text(self, audio_data):
        start_time = time.time()
        response = await self.stt_engine.transcription.prerecorded({'buffer': audio_data})
        text = response.get('results', [{}])[0].get('alternatives', [{}])[0].get('transcript', '')
        end_time = time.time()
        print(f"STT Time: {end_time - start_time}")
        return text

    async def query_llm(self, text):
        start_time = time.time()
        response = openai.Completion.create(
            engine="davinci",
            prompt=self.setup.config.system_prompt + text,
            max_tokens=150
        )
        end_time = time.time()
        print(f"LLM Response Time: {end_time - start_time}")
        return response['choices'][0]['text']

    async def text_to_speech(self, text):
        start_time = time.time()
        response = await self.tts_engine.speech.synthesize({'text': text})
        end_time = time.time()
        print(f"TTS Time: {end_time - start_time}")
        return response['audio']
