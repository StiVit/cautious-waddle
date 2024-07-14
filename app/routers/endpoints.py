from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from app.models import models
# TODO: add logs (if env is DEVELOPMENT -> log.debug , else -> log.info or log.error)
router = APIRouter()


@router.post("/transactions/", response_model=schemas.Transaction)
async def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db=db, transaction=transaction)


@router.post("/products/", response_model=schemas.Product)
async def create_product(product: schemas.ProductCreate, db=Depends(get_db)):
    return crud.create_product(db=db, product=product)


@router.get("/transactions/{transaction_id}", response_model=schemas.Transaction)
async def read_transaction(transactoin_id: int, db: Session = Depends(get_db)):
    db_transaction = crud.get_transaction(db=db, transaction_id=transactoin_id)

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction no found")
    return db_transaction


@router.get("/products/{product_id}", response_model=schemas.Product)
async def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db=db, product_id=product_id)

    if db_product is None:
        raise HTTPException(status_code=404, detail="Product no found")
    return db_product


@router.put("/transaction/{transaction_id}", response_model=schemas.Transaction)
async def update_transaction(transaction_id: int, transaction: schemas.TransactionUpdate, db:Session = Depends(get_db)):
    db_transaction = crud.update_transaction(db=db, transaction_id=transaction_id, transaction=transaction)

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction no found")
    return db_transaction


@router.put("/product/{product_id}", response_model=schemas.Product)
async def update_product(product_id: int, product: schemas.ProductUpdate, db:Session = Depends(get_db)):
    db_product = crud.update_product(db=db, product_id=product_id, product=product)

    if db_product is None:
        raise HTTPException(status_code=404, detail="Product no found")
    return db_product


@router.delete("/transaction/{transaction_id}", response_model=dict)
async def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = crud.get_transaction(db=db, transaction_id=transaction_id)

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction no found")
    crud.delete_transaction(db=db, transaction_id=transaction_id)
    return {"message": "Transaction deleted successfully"}

