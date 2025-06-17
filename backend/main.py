from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .agent import chat

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"status": "ok"}


@app.post("/agent")
async def agent_endpoint(message: str):
    results = []
    async for chunk in chat(message):
        results.append(chunk)
    return {"response": "\n".join(results)}
