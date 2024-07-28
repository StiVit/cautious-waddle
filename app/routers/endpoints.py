from click import DateTime
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from app.utils.logger_config import setup_logger
from app.utils.config import back_env
from app import date_formating
import logging

# Initialize the API router
router = APIRouter()

# Load environment variables from a .env file
load_dotenv()

# Setup logger with appropriate logging level based on the environment
endpoint_logger = setup_logger("endpoint_logger", logging.INFO if back_env == "DEV" else logging.DEBUG)


@router.post("/transactions/", response_model=schemas.Transaction)
async def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    """
    Create a new transaction.

    Parameters:
    transaction: The transaction details to be created.
    db: The database session dependency.

    Returns:
    The created transaction.
    """
    endpoint_logger.info("Transaction successfully created")
    return crud.create_transaction(db=db, transaction=transaction)


@router.post("/products/", response_model=schemas.Product)
async def create_product(product: schemas.ProductCreate, db=Depends(get_db)):
    """
    Create a new product.

    Parameters:
    product: The product details to be created.
    db: The database session dependency.

    Returns:
    The created product.
    """
    endpoint_logger.info("Product successfully created")
    return crud.create_product(db=db, product=product)


@router.get("/transactions/{transaction_id}", response_model=schemas.Transaction)
async def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    """
    Get a transaction by ID.

    Parameters:
    transaction_id: The ID of the transaction to retrieve.
    db: The database session dependency.

    Returns:
    The transaction details if found.
    """
    db_transaction = crud.get_transaction(db=db, transaction_id=transaction_id)

    if db_transaction is None:
        endpoint_logger.info(f"Transaction {transaction_id} not found")
    else:
        endpoint_logger.info(f"Transaction {transaction_id} successfully found")
        return db_transaction


@router.get("/products/{product_id}", response_model=schemas.Product)
async def read_product(product_id: int, db: Session = Depends(get_db)):
    """
    Get a product by ID.

    Parameters:
    product_id: The ID of the product to retrieve.
    db: The database session dependency.

    Returns:
    The product details if found.
    """
    db_product = crud.get_product(db=db, product_id=product_id)

    if db_product is None:
        endpoint_logger.info(f"Product {product_id} not found")
    else:
        endpoint_logger.info(f"Product {product_id} successfully found")
        return db_product


@router.put("/transactions/{transaction_id}", response_model=schemas.Transaction)
async def update_transaction(transaction_id: int, transaction: schemas.TransactionUpdate,
                             db: Session = Depends(get_db)):
    """
    Update a transaction by ID.

    Parameters:
    transaction_id: The ID of the transaction to update.
    transaction: The updated transaction details.
    db: The database session dependency.

    Returns:
    The updated transaction details if found.
    """
    db_transaction = crud.update_transaction(db=db, transaction_id=transaction_id, transaction=transaction)

    if db_transaction is None:
        endpoint_logger.info(f"Transaction {transaction_id} not found")
    else:
        endpoint_logger.info(f"Transaction {transaction_id} successfully changed")
        return db_transaction


@router.put("/products/{product_id}", response_model=schemas.Product)
async def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    """
    Update a product by ID.

    Parameters:
    product_id: The ID of the product to update.
    product: The updated product details.
    db: The database session dependency.

    Returns:
    The updated product details if found.
    """
    db_product = crud.update_product(db=db, product_id=product_id, product=product)

    if db_product is None:
        endpoint_logger.info(f"Product {product_id} not found")
    else:
        endpoint_logger.info(f"Product {product_id} successfully changed")
        return db_product


@router.delete("/transactions/{transaction_id}", response_model=dict)
async def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    """
    Delete a transaction by ID.

    Parameters:
    transaction_id: The ID of the transaction to delete.
    db: The database session dependency.

    Returns:
    A success message if the transaction is deleted.
    """
    db_transaction = crud.get_transaction(db=db, transaction_id=transaction_id)

    if db_transaction is None:
        endpoint_logger.info(f"Transaction {transaction_id} not found")
    else:
        endpoint_logger.info(f"Transaction {transaction_id} successfully deleted")
        crud.delete_transaction(db=db, transaction_id=transaction_id)
        return {"message": "Transaction deleted successfully"}


@router.get("/transactions/period/{start_date}/{end_date}", response_model=float)
async def measure_total_revenue(start_date: str, end_date: str, db: Session = Depends(get_db)):
    """
    Measure total revenue for a given period.

    Parameters:
    start_date: The start date of the period.
    end_date: The end date of the period.
    db: The database session dependency.

    Returns:
    The total revenue for the specified period.
    """
    try:
        total_revenue = crud.get_revenue_for_period(db, start_date, end_date)
        endpoint_logger.info(f"Total revenue for: {start_date} - {end_date} = {total_revenue}")
        return total_revenue
    finally:
        db.close()


@router.get("/transactions/days/{start_date}/{days_number}", response_model=float)
async def total_revenue_days(days_number: int, start_date: str, db: Session = Depends(get_db)):
    """
    Measure total revenue for a period defined by start date and number of days.

    Parameters:
    days_number: The number of days from the start date.
    start_date: The start date of the period.
    db: The database session dependency.

    Returns:
    The total revenue for the specified period.
    """
    end_date = date_formating.add_days(start_date, days_number)
    print(end_date)
    try:
        total_revenue = crud.get_revenue_for_period(db, start_date, end_date)
        endpoint_logger.info(f"Total revenue for: {start_date} - {end_date} = {total_revenue}")
        return total_revenue
    finally:
        db.close()


@router.get("/transactions/months/{start_date}/{months_number}", response_model=float)
async def total_revenue_months(months_number: int, start_date: str, db: Session = Depends(get_db)):
    """
    Measure total revenue for a period defined by start date and number of months.

    Parameters:
    months_number: The number of months from the start date.
    start_date: The start date of the period.
    db: The database session dependency.

    Returns:
    The total revenue for the specified period.
    """
    end_date = date_formating.add_months(start_date, months_number)
    print(end_date)
    try:
        total_revenue = crud.get_revenue_for_period(db, start_date, end_date)
        endpoint_logger.info(f"Total revenue for: {start_date} - {end_date} = {total_revenue}")
        return total_revenue
    finally:
        db.close()
