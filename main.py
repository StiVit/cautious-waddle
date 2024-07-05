import uvicorn
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import endpoints

Base.metadata.create_all(bind=engine)
# FastAPI app instance
app = FastAPI()


# Include routers
app.include_router(endpoints.router, prefix="/api", tags=["items"])

if __name__ == "__main__":
    host = "localhost"
    port = 8000
    uvicorn.run(app, host = host, port=port)