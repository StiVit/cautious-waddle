# app/models.py

from sqlalchemy import Column, Integer, String, Date, Double, ForeignKey
from app.database import Base
from ..enumerations.region import Region
from ..enumerations.payment_method import PaymentMethod
from ..enumerations.product_category import ProductCategory
from sqlalchemy import Enum

# SQLAlchemy models
class Transaction(Base):
	__tablename__ = "transactions"
	
	transaction_id = Column(Integer, primary_key=True, index=True)
	date = Column(Date, index=True)
	product_id = Column(ForeignKey("products.product_id"), index=True)
	units_sold = Column(Integer, index=True)
	total_revenue = Column(Integer, index=True)
	region = Column(Enum(Region), index=True)
	payment_method = Column(Enum(PaymentMethod), index=True)


class Product(Base):
	__tablename__ =  "products"

	product_id = Column(Integer, primary_key=True, index=True)
	product_category = Column(Enum(ProductCategory), index= True)
	product_name = Column(String, index=True)
	unit_price = Column(Double, index=True)