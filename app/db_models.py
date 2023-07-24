from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship

from database import Base


class Menu(Base):
    __tablename__ = "menus"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String)
    submenus = relationship("Submenu", back_populates="menu", cascade="all, delete-orphan", lazy="selectin")

class Submenu(Base):
    __tablename__ = "submenus"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String)
    menu_id = Column(Integer, ForeignKey("menus.id"))
    menu = relationship(
        "Menu",
        back_populates="submenus",
        foreign_keys=[menu_id],
        primaryjoin="Submenu.menu_id==Menu.id"
    )
    dishes = relationship("Dish", back_populates="submenu", cascade="all, delete-orphan", lazy="selectin")

class Dish(Base):
    __tablename__ = "dishes"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Numeric(precision=10, scale=2))
    submenu_id = Column(Integer, ForeignKey("submenus.id"))
    submenu = relationship(
        "Submenu",
        back_populates="dishes",
        foreign_keys=[submenu_id],
        primaryjoin="Dish.submenu_id==Submenu.id"
    )
