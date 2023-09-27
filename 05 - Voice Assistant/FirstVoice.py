import pyaudio
import websockets
import asyncio
import base64
import json
from api_secrets import API_KEY_ASSEMBLYAI


FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"


async def send_recieve():
    async with websockets.connect(
        URL,
        ping_timeout=20,
        ping_interval=5,
        extra_headers={"Authorization": API_KEY_ASSEMBLYAI}
    ) as _ws:
        await asyncio.sleep(0.1)
        session_begins = await _ws.recv()
        print(session_begins)
        print("sending messages")

        async def send():
            while True:
                print("sending")

        async def recieve():
            while True:
                pass

        send_result, recieve_result = asyncio.gather(send(), recieve())


asyncio.run(send_recieve)
