from fastapi import FastAPI
from app.database import engine, Base
from app.routers import items

Base.metadata.create_all(bind=engine)
# FastAPI app instance
app = FastAPI()


# Include routers
app.include_router(items.router, prefix="/api", tags=["items"])