import uvicorn
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import items

Base.metadata.create_all(bind=engine)
# FastAPI app instance
app = FastAPI()


# Include routers
app.include_router(items.router, prefix="/api", tags=["items"])

if __name__ == "__main__":
    uvicorn.run("main:app", host = "127.0.0.1", port=8000, reload=True)