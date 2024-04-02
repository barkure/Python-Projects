from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn
from change_pitch import change_pitch


app = FastAPI()

@app.websocket("/ws/audio")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_bytes()
            # data 接收到的音频流
            print(len(data))
            data_changed = change_pitch(data) # 调用 change_pitch 函数处理音频流
            try:
                await websocket.send_bytes(data_changed) # 发送处理后的音频流
            except Exception as e:
                print(f'Error: {e}')
    except WebSocketDisconnect:
        print("WebSocket connection closed")
    finally:
        await websocket.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)