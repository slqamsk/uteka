from ..models import DrugClass
from typing import List, Optional

"""
Репозиторий: DrugClass_Repository
"""

class DrugClass_Repository:
    """
    Репозиторий для управления drugclass repository.
    """
    def __init__(self):
        self._items = []

    def add(self, drug_class: DrugClass) -> None:
        # Добавляет группу в хранилище
        pass

    def find_by_id(self, id: int) -> DrugClass:
        # Возвращает группу по id
        return None

    def get_all(self, ) -> list[DrugClass]:
        # Возвращает все терапевтические группы
        return []

