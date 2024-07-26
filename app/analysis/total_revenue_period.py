from app.database import get_db
from app.crud import get_revenue_for_period
from contextlib import contextmanager


@contextmanager
def get_db_context():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()


def measure_total_revenue(start_date: str, end_date: str) -> float:
    with get_db_context() as db:
        total_revenue = get_revenue_for_period(db, start_date, end_date)
        return total_revenue
