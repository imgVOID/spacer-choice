from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.db import init_db 
from api.endpoints import celestial, auth 


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    A context manager for managing the application lifecycle.
    """
    print("🚀 DB iniitialization...")
    await init_db()

    yield 

    print("🛑 Stop...")


app = FastAPI(
    title="Celestial API",
    description="Service for retrieving and managing celestial body coordinates.",
    version="1.0.0",
    lifespan=lifespan 
)

app.include_router(auth.router)

app.include_router(celestial.router)

# uvicorn main:app --reload
