from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Pydantic model for an item (e.g., Book)
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# In-memory storage
items = {}

@app.get("/items", response_model=List[Item])
def list_items():
    return list(items.values())

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items[item.id] = item
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return item

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
