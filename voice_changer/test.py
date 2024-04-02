import asyncio
import websockets
import pyaudio

CHUNK = 1024  # 每次读取的音频数据的长度
FORMAT = pyaudio.paFloat32  # 音频数据的格式
CHANNELS = 1  # 音频通道数
RATE = 44100  # 采样率

p = pyaudio.PyAudio()
# 用来播放接收到的音频数据
stream_recv = p.open(format=FORMAT,
                   channels=CHANNELS,
                   rate=RATE,
                   output=True,
                   frames_per_buffer=CHUNK)

async def send_audio():
    uri = "ws://localhost:8000/ws/audio"
    async with websockets.connect(uri) as websocket:
        p = pyaudio.PyAudio()
        # 用来录制音频数据
        stream_send = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        try:
            while True:
                data = stream_send.read(CHUNK) # 读取音频数据
                await websocket.send(data) # 发送音频数据
                try:
                    recieved_data = await asyncio.wait_for(websocket.recv(), timeout=1.0)
                    # 接收音频数据
                    print(len(recieved_data))
                    stream_recv.write(recieved_data) # 播放接收到的音频数据
                except asyncio.TimeoutError:
                    print('No data received from server for 1 second')
        except Exception as e:
            print(f'Error: {e}')
        finally:
            stream_send.stop_stream()
            stream_send.close()
            p.terminate()

asyncio.run(send_audio())