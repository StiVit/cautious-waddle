import logging

import uvicorn
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import endpoints
from process_csv import run_script
from app.utils.logger_config import setup_logger
from app.utils.config import back_env
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware


Base.metadata.create_all(bind=engine)
# FastAPI app instance
app = FastAPI()

# Initialize the limiter
limiter = Limiter(key_func=get_remote_address)

app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

app_logger = setup_logger('app_logger', logging.INFO if back_env == "DEV" else logging.DEBUG)

# Include routers
app.include_router(endpoints.router, prefix="/api", tags=["transactions", "products"])

if __name__ == "__main__":
    host = "localhost"
    port = 8000
    app_logger.info('App running successfully')
    run_script()
    uvicorn.run(app, host=host, port=port)
