# from typing import List, Optional
# from sqlalchemy import select
from app.item.models.item import Item

# from core.db import Transactional, session


class ItemService:
    def __init__(self):
        ...

    # async def get_item_list(
    #     self,
    #     limit: int = 12,
    #     prev: Optional[int] = None,
    # ) -> List[Item]:
    #     query = select(Item)

    #     if prev:
    #         query = query.where(Item.id < prev)

    #     if limit > 12:
    #         limit = 12

    #     query = query.limit(limit)
    #     result = await session.execute(query)
    #     return result.scalars().all()

    # @Transactional()
    # async def create_item(
    #     self, name: str, price: float, is_offer: bool
    # ) -> None:
    #     item = Item(name=name, price=price, is_offer=is_offer)
    #     session.add(item)

    def get_item(self, item_id: int) -> Item:
        # result = await session.execute(select(Item).where(Item.id == item_id))
        # item = result.scalars().first()
        # if not item:
        #     raise ItemNotFoundException

        item = Item(id=item_id, name="fer", price=12.5, is_offer=True)

        return item

    # async def update_item(
    #     self, item_id: int, name: str, price: float, is_offer: bool
    # ) -> None:
    #     result = await session.execute(select(Item).where(Item.id == item_id))
    #     item = result.scalars().first()
    #     if not item:
    #         raise ItemNotFoundException

    #     item.name = name
    #     item.price = price
    #     item.is_offer = is_offer

    # async def delete_item(self, item_id: int) -> None:
    #     result = await session.execute(select(Item).where(Item.id == item_id))
    #     item = result.scalars().first()
    #     if not item:
    #         raise ItemNotFoundException

    #     session.delete(item)
