#app/schemas.py

from pydantic import BaseModel
from datetime import date
from enumerations import payment_method, product_category, region

class TransactionBase(BaseModel):
    date: date
    product_id: int
    units_sold: int
    total_revenue: float
    region: region.Region
    payment_method: payment_method.PaymentMethod

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id:int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    product_category: product_category.ProductCategory
    product_name: str
    unit_price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id:int

    class Config:
        orm_mode = True