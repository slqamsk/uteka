from ..models import Drug_Ingredient, Drug, Ingredient
from typing import List, Optional

"""
Репозиторий: Drug_Ingredient_Repository
"""

class Drug_Ingredient_Repository:
    """
    Репозиторий для управления drug ingredient repository.
    """
    def __init__(self):
        self._items = []

    def add(self, link: Drug_Ingredient) -> None:
        # Добавляет запись о вхождении вещества в препарат
        pass

    def remove(self, link: Drug_Ingredient) -> None:
        # Удаляет запись
        pass

    def find_by_drug(self, drug: Drug) -> list[Drug_Ingredient]:
        # Все вещества в препарате (с дозировкой)
        return []

    def find_by_ingredient(self, ingredient: Ingredient) -> list[Drug_Ingredient]:
        # Все препараты с веществом
        return []

    def find_by_drug_and_ingredient(self, drug: Drug, ingredient: Ingredient) -> Drug_Ingredient:
        # Конкретное вхождение
        return None

    def get_all(self, ) -> list[Drug_Ingredient]:
        # Возвращает все записи состава
        return []

