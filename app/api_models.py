from typing import Optional

from pydantic import BaseModel


# Request models

class MenuRequest(BaseModel):
    title: str
    description: Optional[str] = None


class DishRequest(MenuRequest):
    price: float


# Response models

class MenuSchema(BaseModel):
    id: str
    title: str
    description: str
    submenus_count: int
    dishes_count: int


class SubmenuSchema(BaseModel):
    id: str
    title: str
    description: str
    dishes_count: int
    menu_id: str


class DishSchema(BaseModel):
    id: str
    title: str
    description: str
    price: str
    submenu_id: str
