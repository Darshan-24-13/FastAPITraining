from fastapi import FastAPI

from .config import settings
from .database import ping_database
from .routers import user

app = FastAPI(title=settings.APP_NAME)
app.include_router(user.router)


@app.on_event("startup")
def on_startup():
    if not ping_database():
        raise RuntimeError("Could not connect to MongoDB")

    print(f"[startup] Connected to MongoDB. App: {settings.APP_NAME}")


@app.get("/", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "app": settings.APP_NAME
    }