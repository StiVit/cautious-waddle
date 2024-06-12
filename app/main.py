from database import Base, engine, SessionLocal
import uvicorn
from fastapi import FastAPI
from src.models import Item

Base.metadata.create_all(bind=engine)
# FastAPI app instance
app = FastAPI()


# CRUD operations
# Create (Create)
@app.post("/items/")
async def create_item(name: str, description: str):
	db = SessionLocal()
	db_item = Item(name=name, description=description)
	db.add(db_item)
	db.commit()
	db.refresh(db_item)
	return db_item


# Read (GET)
@app.get("/items/{item_id}")
async def read_item(item_id: int):
	db = SessionLocal()
	item = db.query(Item).filter(Item.id == item_id).first()
	return item


# Update (PUT)
@app.put("/items/{item_id}")
async def update_item(item_id: int, name: str, description: str):
	db = SessionLocal()
	db_item = db.query(Item).filter(Item.id == item_id).first()
	db_item.name = name
	db_item.description = description
	db.commit()
	return db_item


# Delete (DELETE)
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
	db = SessionLocal()
	db_item = db.query(Item).filter(Item.id == item_id).first()
	db.delete(db_item)
	db.commit()
	return {"message": "Item deleted successfully"}


if __name__ == "__main__":
	uvicorn.run(app)