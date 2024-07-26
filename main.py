import logging

import uvicorn
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import endpoints
from process_csv import run_script
from app.utils.logger_config import setup_logger
from app.utils.config import back_env
from app.analysis.total_revenue_period import measure_total_revenue

Base.metadata.create_all(bind=engine)
# FastAPI app instance
app = FastAPI()

app_logger = setup_logger('app_logger', logging.INFO if back_env == "DEV" else logging.DEBUG)

# Include routers
app.include_router(endpoints.router, prefix="/api", tags=["items"])

if __name__ == "__main__":
    host = "localhost"
    port = 8000
    app_logger.info('App running successfully')
    run_script()
    app_logger.info(f"Total revenue for 2024-01-01: 2024-07-01 = {measure_total_revenue('2024-01-01', '2024-07-01')}")
    uvicorn.run(app, host=host, port=port)
