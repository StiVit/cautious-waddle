# app/schemas.py

from pydantic import BaseModel
from datetime import date
from app.enumerations.region import Region
from app.enumerations.payment_method import PaymentMethod
from app.enumerations.product_category import ProductCategory


class TransactionBase(BaseModel):
    date: date
    product_id: int
    units_sold: int
    total_revenue: float
    region: Region
    payment_method: PaymentMethod


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(TransactionBase):
    pass


class Transaction(TransactionBase):
    transaction_id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    product_category: ProductCategory
    product_name: str
    unit_price: float


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    product_id: int

    class Config:
        orm_mode = True
