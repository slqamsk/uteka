from ..models import Ingredient_DrugClass, Ingredient, DrugClass
from typing import List, Optional

"""
Репозиторий: Ingredient_DrugClass_Repository
"""

class Ingredient_DrugClass_Repository:
    """
    Репозиторий для управления ingredient drugclass repository.
    """
    def __init__(self):
        self._items = []

    def add(self, link: Ingredient_DrugClass) -> None:
        # Добавляет связь 'вещество ↔ группа'
        pass

    def remove(self, link: Ingredient_DrugClass) -> None:
        # Удаляет связь
        pass

    def find_by_ingredient(self, ingredient: Ingredient) -> list[Ingredient_DrugClass]:
        # Все связи для заданного вещества
        return []

    def find_by_drug_class(self, drug_class: DrugClass) -> list[Ingredient_DrugClass]:
        # Все связи для заданной терапевтической группы
        return []

    def find_by_ingredient_and_class(self, ingredient: Ingredient, drug_class: DrugClass) -> Ingredient_DrugClass:
        # Конкретная связь
        return None

    def get_all(self, ) -> list[Ingredient_DrugClass]:
        # Возвращает все связи
        return []

