from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import AskRequest, AskResponse
from settings import settings
from router import answer_question, reload_knowledge

app = FastAPI(title="DroneTech Coach API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health() -> dict:
    return {"status": "ok", "env": settings.app_env}

@app.post("/ask", response_model=AskResponse)
def ask(payload: AskRequest) -> AskResponse:
    return answer_question(payload)

@app.post("/admin/reload-knowledge")
def admin_reload_knowledge() -> dict:
    count = reload_knowledge()
    return {"status": "reloaded", "chunks": count}
