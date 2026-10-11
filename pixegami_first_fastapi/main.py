from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse 

app=FastAPI()

items = [{"name": "Ricardo"}, {"surname": "Solano"}, {"wife_name": "Dulce"}, {"wife_surname": "Alpuche"}]

@app.get("/")
def root():
    return items

@app.get("/hola_mundo")
def hola_mundo():
    return HTMLResponse(content="<h1>Hola Mundo</h1>")

@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return items


@app.get("/item/{item_id}")
def get_item(item_id: int):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/items/")
def get_item_by_category(category: str):
    return category