import json
from fastapi import WebSocket, FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def get():
    file_html_page = open('index.html', 'r', encoding='utf-8')
    html_page = file_html_page.read()
    return HTMLResponse(html_page)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    message_number = 0
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        message_number += 1
        message = json.loads(data)
        message['message_number'] = message_number
        await websocket.send_text(json.dumps(message))