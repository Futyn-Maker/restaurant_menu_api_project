from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import crud
from database import init_models, get_session
from db2api import menu_api, submenu_api, dish_api
from depends import get_menu_or_404, get_submenu_or_404, get_dish_or_404
from api_models import MenuRequest, DishRequest, MenuSchema, SubmenuSchema, DishSchema

@asynccontextmanager
async def make_db(app: FastAPI):
    await init_models()
    yield


app = FastAPI(title="Restaurant Menu API", lifespan=make_db)


# Menus endpoints

@app.post("/api/v1/menus/", response_model=MenuSchema, status_code=201)
async def create_new_menu(new_menu: MenuRequest, db: AsyncSession = Depends(get_session)):
    try:
        result = await crud.create_menu(db, new_menu.title, new_menu.description)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    return menu_api(result)


@app.get("/api/v1/menus/", response_model=list[MenuSchema])
async def get_all_menus(db: AsyncSession = Depends(get_session)):
    result = await crud.get_menus(db)
    return [menu_api(menu) for menu in result]


@app.get("/api/v1/menus/{menu_id}/", response_model=MenuSchema)
async def read_menu(menu_id: int, db: AsyncSession = Depends(get_session)):
    result = await get_menu_or_404(menu_id, db)
    return menu_api(result)


@app.patch("/api/v1/menus/{menu_id}/", response_model=MenuSchema)
async def update_menu_details(menu_id: int, new_menu: MenuRequest, db: AsyncSession = Depends(get_session)):
    menu = await get_menu_or_404(menu_id, db)
    try:
        result = await crud.update_menu(db, menu, new_menu.title, new_menu.description)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    return menu_api(result)


@app.delete("/api/v1/menus/{menu_id}/", response_model=MenuSchema)
async def delete_menu_by_id(menu_id: int, db: AsyncSession = Depends(get_session)):
    menu = await get_menu_or_404(menu_id, db)
    await crud.delete_menu(db, menu)
    return menu_api(menu)


# Submenus endpoints

@app.post("/api/v1/menus/{menu_id}/submenus/", response_model=SubmenuSchema, status_code=201)
async def create_new_submenu(menu_id: int, new_submenu: MenuRequest, db: AsyncSession = Depends(get_session)):
    await get_menu_or_404(menu_id, db)
    try:
        result = await crud.create_submenu(db, new_submenu.title, new_submenu.description, menu_id)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    return submenu_api(result)


@app.get("/api/v1/menus/{menu_id}/submenus/", response_model=list[SubmenuSchema])
async def get_all_submenus(menu_id: int, db: AsyncSession = Depends(get_session)):
    result = await crud.get_submenus(db, menu_id)
    return [submenu_api(submenu) for submenu in result]


@app.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/", response_model=SubmenuSchema)
async def read_submenu(menu_id: int, submenu_id: int, db: AsyncSession = Depends(get_session)):
    result = await get_submenu_or_404(submenu_id, db)
    return submenu_api(result)


@app.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}/", response_model=SubmenuSchema)
async def update_submenu_details(menu_id: int, submenu_id: int, new_submenu: MenuRequest, db: AsyncSession = Depends(get_session)):
    submenu = await get_submenu_or_404(submenu_id, db)
    try:
        result = await crud.update_submenu(db, submenu, new_submenu.title, new_submenu.description)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    return submenu_api(result)


@app.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}/", response_model=SubmenuSchema)
async def delete_menu_by_id(menu_id: int, submenu_id: int, db: AsyncSession = Depends(get_session)):
    submenu = await get_submenu_or_404(submenu_id, db)
    await crud.delete_submenu(db, submenu)
    return submenu_api(submenu)


# Dishes endpoints

@app.post("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/", response_model=DishSchema, status_code=201)
async def create_new_dish(menu_id: int, submenu_id: int, new_dish: DishRequest, db: AsyncSession = Depends(get_session)):
    await get_submenu_or_404(submenu_id, db)
    try:
        result = await crud.create_dish(db, new_dish.title, new_dish.description, new_dish.price, submenu_id)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    return dish_api(result)


@app.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/", response_model=list[DishSchema])
async def get_all_dishes(menu_id: int, submenu_id: int, db: AsyncSession = Depends(get_session)):
    result = await crud.get_dishes(db, submenu_id)
    return [dish_api(dish) for dish in result]


@app.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}/", response_model=DishSchema)
async def read_dish(menu_id: int, submenu_id: int, dish_id: int, db: AsyncSession = Depends(get_session)):
    result = await get_dish_or_404(dish_id, db)
    return dish_api(result)


@app.patch("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}/", response_model=DishSchema)
async def update_dish_details(menu_id: int, submenu_id: int, dish_id: int, new_dish: DishRequest, db: AsyncSession = Depends(get_session)):
    dish = await get_dish_or_404(dish_id, db)
    try:
        result = await crud.update_dish(db, dish, new_dish.title, new_dish.description, new_dish.price)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    return dish_api(result)


@app.delete("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}/", response_model=DishSchema)
async def delete_dish_by_id(menu_id: int, submenu_id: int, dish_id: int, db: AsyncSession = Depends(get_session)):
    dish = await get_dish_or_404(dish_id, db)
    await crud.delete_dish(db, dish)
    return dish_api(dish)
