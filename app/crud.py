from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from db_models import Menu, Submenu, Dish


# Menus functions

async def create_menu(db: AsyncSession, title: str, description: str) -> Menu:
    menu = Menu(title=title, description=description)
    db.add(menu)
    await db.commit()
    await db.refresh(menu)
    return menu


async def get_menu(db: AsyncSession, menu_id: int) -> Menu:
    result = await db.execute(select(Menu).filter(Menu.id == menu_id))
    return result.scalars().first()


async def get_menus(db: AsyncSession) -> list[Menu]:
    result = await db.execute(select(Menu))
    return result.scalars().all()


async def update_menu(db: AsyncSession, menu: Menu, new_title: str, new_description: str) -> Menu:
    menu.title = new_title
    menu.description = new_description
    await db.commit()
    await db.refresh(menu)
    return menu


async def delete_menu(db: AsyncSession, menu: Menu):
    await db.delete(menu)
    await db.commit()


# Submenus functions

async def create_submenu(db: AsyncSession, title: str, description: str, menu_id: int) -> Submenu:
    submenu = Submenu(title=title, description=description, menu_id=menu_id)
    db.add(submenu)
    await db.commit()
    await db.refresh(submenu)
    return submenu


async def get_submenu(db: AsyncSession, submenu_id: int) -> Submenu:
    result = await db.execute(select(Submenu).filter(Submenu.id == submenu_id))
    return result.scalars().first()


async def get_submenus(db: AsyncSession, menu_id: int) -> list[Submenu]:
    result = await db.execute(select(Submenu).filter(Submenu.menu_id == menu_id))
    return result.scalars().all()


async def update_submenu(db: AsyncSession, submenu: Submenu, new_title: str, new_description: str) -> Submenu:
    submenu.title = new_title
    submenu.description = new_description
    await db.commit()
    await db.refresh(submenu)
    return submenu


async def delete_submenu(db: AsyncSession, submenu: Submenu):
    await db.delete(submenu)
    await db.commit()


# Dishes functions

async def create_dish(db: AsyncSession, title: str, description: str, price: float, submenu_id: int) -> Dish:
    dish = Dish(title=title, description=description, price=price, submenu_id=submenu_id)
    db.add(dish)
    await db.commit()
    await db.refresh(dish)
    return dish


async def get_dish(db: AsyncSession, dish_id: int) -> Dish:
    result = await db.execute(select(Dish).filter(Dish.id == dish_id))
    return result.scalars().first()


async def get_dishes(db: AsyncSession, submenu_id: int) -> list[Dish]:
    result = await db.execute(select(Dish).filter(Dish.submenu_id == submenu_id))
    return result.scalars().all()


async def update_dish(db: AsyncSession, dish: Dish, new_title: str, new_description: str, new_price: float) -> Dish:
    dish.title = new_title
    dish.description = new_description
    dish.price = new_price
    await db.commit()
    await db.refresh(dish)
    return dish


async def delete_dish(db: AsyncSession, dish: Dish):
    await db.delete(dish)
    await db.commit()
