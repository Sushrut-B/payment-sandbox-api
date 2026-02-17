from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .core.config import settings
from .db.database import engine, get_db, Base

# Create tables (temporary until Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    return {"status": "healthy", "project": settings.PROJECT_NAME}


@app.get("/")
def root():
    return {
        "message": settings.PROJECT_NAME,
        "docs": "/docs",
        "redoc": "/redoc",
    }
