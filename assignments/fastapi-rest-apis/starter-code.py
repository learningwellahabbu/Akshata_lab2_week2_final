"""
FastAPI REST API Starter Code
Greetings for building a REST API with FastAPI and Uvicorn
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Create a FastAPI application instance
app = FastAPI(title="My REST API", version="1.0.0")

# Define a Pydantic model for data validation
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float

# In-memory storage for items
items_db: List[Item] = []

# TODO: Implement your API endpoints here

# Example GET endpoint (remove or modify as needed)
@app.get("/")
def read_root():
    """Root endpoint that returns a welcome message"""
    return {"message": "Welcome to FastAPI!"}

# TODO: Add POST endpoint to create items
# TODO: Add GET endpoint to retrieve items
# TODO: Add PUT endpoint to update items
# TODO: Add DELETE endpoint to remove items

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
