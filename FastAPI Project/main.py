from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello!!!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # 'item_id' is taken from the path and converted to int
    return {"item_id": item_id}