# app/main.py
import uvicorn
from fastapi import FastAPI
from app.config import settings
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title=settings.app_name)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
