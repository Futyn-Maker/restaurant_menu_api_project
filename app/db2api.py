from api_models import MenuSchema, SubmenuSchema, DishSchema
from db_models import Menu, Submenu, Dish


def menu_api(menu: Menu) -> MenuSchema:
    submenus_count = len(menu.submenus)
    dishes_count = sum(len(submenu.dishes) for submenu in menu.submenus)
    return MenuSchema(
        id=str(menu.id),
        title=menu.title,
        description=menu.description,
        submenus_count=submenus_count,
        dishes_count=dishes_count,
    )


def submenu_api(submenu: Submenu) -> SubmenuSchema:
    return SubmenuSchema(
        id=str(submenu.id),
        title=submenu.title,
        description=submenu.description,
        dishes_count=len(submenu.dishes),
        menu_id=str(submenu.menu_id),
    )


def dish_api(dish: Dish) -> DishSchema:
    return DishSchema(
        id=str(dish.id),
        title=dish.title,
        description=dish.description,
        price=str(dish.price),
        submenu_id=str(dish.submenu_id),
    )
