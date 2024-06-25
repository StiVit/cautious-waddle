# app/models.py

from sqlalchemy import Column, Integer, String, Date, Double
from app.database import Base
from enumerations.region import Region
from enumerations.payment_method import PaymentMethod
from enumerations.product_category import ProductCategory

# SQLAlchemy models
class Transaction(Base):
	__tablename__ = "transactions"
	
	transaction_id = Column(Integer, primary_key=True, index=True)
	date = Column(Date, index=True)
	product_id = Column(String, index=True, key=True)
	units_sold = Column(Integer, index=True)
	total_revenue = Column(Integer, index=True)
	region = Column(Region, index=True)
	payment_method = Column(PaymentMethod, index=True)


class Product(Base):
	__tablename__ =  "products"

	product_category = Column(ProductCategory, index= True)
	product_name = Column(String, index=True)
	unit_price = Column(Double, index=True)