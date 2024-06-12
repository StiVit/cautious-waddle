from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/items/", response_model=schemas.Item)
async def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@router.get("/items/{item_id}", response_model=schemas.Item)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item no found")
    return db_item

@router.put("/items/{item_id}", response_model=schemas.Item)
async def update_item(item_id: int, item = schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.update_item(db=db, item_id=item_id, item=item)

@router.delete("/items/{item_id}", response_model=schemas.Item)
async def delete_item(item_id:int, db: Session = Depends(get_db)):
    crud.delete_item(db=db, item_id=item_id)
    return {"message": "Item deleted successfully"}

