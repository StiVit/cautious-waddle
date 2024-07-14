import logging

import uvicorn
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import endpoints
from process_csv import run_script
from app.utils.logging import setup_logger

Base.metadata.create_all(bind=engine)
# FastAPI app instance
app = FastAPI()

app_logger = setup_logger('app_logger', logging.INFO)

# Include routers
app.include_router(endpoints.router, prefix="/api", tags=["items"])

if __name__ == "__main__":
    host = "localhost"
    port = 8000
    app_logger.info('This is an info message')
    run_script()
    uvicorn.run(app, host=host, port=port)
