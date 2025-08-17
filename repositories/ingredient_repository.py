from ..models import Ingredient
from typing import List, Optional

"""
Репозиторий: Ingredient_Repository
"""

class Ingredient_Repository:
    """
    Репозиторий для управления ingredient repository.
    """
    def __init__(self):
        self._items = []

    def add(self, ingredient: Ingredient) -> None:
        # Добавляет вещество в хранилище
        pass

    def find_by_id(self, id: int) -> Ingredient:
        # Находит вещество по id
        return None

    def find_by_name(self, name: str) -> Ingredient:
        # Находит вещество по названию (регистронезависимо)
        return None

    def get_all(self, ) -> list[Ingredient]:
        # Возвращает все вещества
        return []

