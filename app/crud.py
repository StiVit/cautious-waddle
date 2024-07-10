# app/crud.py

from sqlalchemy.orm import Session
from app.models.models import Transaction, Product
from app.schemas import TransactionCreate, ProductCreate, TransactionUpdate, ProductUpdate
from app.enumerations.region import Region
from app.enumerations.payment_method import PaymentMethod
from app.enumerations.product_category import ProductCategory

def get_transaction(db:Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()

def create_transaction(db:Session, transaction:TransactionCreate):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def create_product(db:Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_transaction(db:Session, transaction_id:int, transaction:TransactionUpdate):
    db_transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if db_transaction:
        db_transaction.date = transaction.date
        db_transaction.product_id = transaction.product_id
        db_transaction.units_sold = transaction.units_sold
        db_transaction.total_revenue = transaction.total_revenue
        if isinstance(transaction.region, Region):
            db_transaction.region = transaction.region
        if isinstance(transaction.payment_method, PaymentMethod):
            db_transaction.payment_method = transaction.payment_method
        db.commit()
        db.refresh(db_transaction)
    return db_transaction

def get_product(db:Session, product_id:int):
    return db.query(Product).filter(Product.product_id == product_id).first()

def update_product(db:Session, product_id:int, product:ProductUpdate):
    db_product = db.query(Product).filter(Product.product_id == product_id).first()
    if db_product:
        if isinstance(db_product.product_category, ProductCategory):
            db_product.product_category = product.product_category
        db_product.product_name = product.product_name
        db_product.unit_price = product.unit_price
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_transaction(db:Session, transaction_id: int):
    db_transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if db_transaction:
        db.delete(db_transaction)
        db.commit()
    return db_transaction