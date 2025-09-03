# Import statements - bringing in the tools we need
from fastapi import FastAPI     # Main framework
from pydantic import BaseModel  # For data validation
from typing import Optional     # For optional parameters

# Create you FastAPI application interface
# This is like opening a restaurant - we're creating the "place" where requests come
app = FastAPI(title="My First API", version="0.1.0")

# Data model - defines what an "Item" looks like
# This is like a menu item description
class Item(BaseModel):
    name: str       # Required: item name
    price: float    # Required: item price
    is_offer: Optional[bool] = None     # Optional: is it on sale?

# Route definitions - these are like different menu options

@app.get("/health")     # Get request to /health
def health():
    """Check if our API is running - like asking 'are you open?'"""
    return {"status": "OK"}

@app.get("/")           # Get request to / (root/homepage)
def read_root():
    """Welcome message - like a greeting at the door"""
    return{"message": "Hello, FastAPI! Welcome to my first API!"} 

@app.get("/items/{item_id}")        # Get request with a parameter
def read_item(item_id: int, q: Optional[str] = None):
    """Get a specific item by ID - like ordering item #5 from the menu"""
    return{"item_id": item_id, "q":q}

@app.post("/items")         # Post request to create new items
def create_item(item: Item): 
    """Create a new item - like adding a new dish to the menu"""
    return{"created": item, "message": "Item created successfully!"}
