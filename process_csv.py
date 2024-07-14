import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.models import Transaction, Product
from app.enumerations.payment_method import PaymentMethod
from app.enumerations.region import Region
from app.enumerations.product_category import ProductCategory
from sqlalchemy import exists


# TODO: add docstrings
# TODO: add logs

def format_data(df):
    products = df[['Product Category', 'Product Name', 'Unit Price']].drop_duplicates().reset_index(drop=True)
    products["product_id"] = products.index + 1

    transactions = df[['Transaction ID', 'Date', 'Units Sold', 'Total Revenue', 'Region', 'Payment Method']]

    products = products.rename(columns={
        'Product Category': 'product_category',
        'Product Name': 'product_name',
        'Unit Price': 'unit_price'
    })

    transactions = transactions.rename(columns={
        'Transaction ID': 'transaction_id',
        'Date': 'date',
        'Units Sold': 'units_sold',
        'Total Revenue': 'total_revenue',
        'Region': 'region',
        'Payment Method': 'payment_method',
        'product_id': 'product_id'
    })

    transactions['date'] = pd.to_datetime(transactions["date"])
    transactions['region'] = transactions['region'].apply(lambda x: Region[x.replace(" ", "_").upper()])
    transactions['payment_method'] = transactions['payment_method'].apply(
        lambda x: PaymentMethod[x.replace(" ", "_").upper()])
    products['product_category'] = products['product_category'].apply(
        lambda x: ProductCategory[x.replace(" ", "_").upper()])

    return products, transactions


def run_script():
    df = pd.read_csv("dataset/Online Sales Data.csv")
    products, transactions = format_data(df=df)

    def insert_data(session: Session, products: pd.DataFrame, transactions: pd.DataFrame):
        # Insert products
        for _, row in products.iterrows():
            session.add(Product(
                product_id=row['product_id'],
                product_category=row['product_category'],
                product_name=row['product_name'],
                unit_price=row['unit_price']
            ))

        # Insert transactions
        for _, row in transactions.iterrows():
            session.add(Transaction(
                transaction_id=row['transaction_id'],
                date=row['date'],
                # product_id=row['product_id'],
                units_sold=row['units_sold'],
                total_revenue=row['total_revenue'],
                region=row['region'],
                payment_method=row['payment_method']
            ))

        session.commit()

    session = SessionLocal()
    data_exists = session.query(exists().where(Transaction.transaction_id.isnot(None))).scalar()

    if data_exists:
        insert_data(session=session, products=products, transactions=transactions)
        session.close()
    else:
        # TODO: Add log for this
        print("database not empty")