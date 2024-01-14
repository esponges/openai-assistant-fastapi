from fastapi import APIRouter
from app.item.services.item import ItemService

item_router = APIRouter()


@item_router.get("/{item_id}")
def read_item(item_id: int):
    return ItemService().get_item(item_id)


@item_router.put("/{item_id}")
def update_item(item_id: int):
    return {"item_id": item_id}
