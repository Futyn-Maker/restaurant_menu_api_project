from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import crud
from db_models import Menu, Submenu, Dish


async def get_menu_or_404(menu_id: int, db: AsyncSession) -> Menu:
    menu = await crud.get_menu(db, menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail="menu not found")
    return menu


async def get_submenu_or_404(submenu_id: int, db: AsyncSession) -> Submenu:
    submenu = await crud.get_submenu(db, submenu_id)
    if not submenu:
        raise HTTPException(status_code=404, detail="submenu not found")
    return submenu


async def get_dish_or_404(dish_id: int, db: AsyncSession) -> Dish:
    dish = await crud.get_dish(db, dish_id)
    if not dish:
        raise HTTPException(status_code=404, detail="dish not found")
    return dish
