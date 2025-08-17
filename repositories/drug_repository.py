from ..models import Drug
from typing import List, Optional

"""
Репозиторий: Drug_Repository
"""

class Drug_Repository:
    """
    Репозиторий для управления drug repository.
    """
    def __init__(self):
        self._items = []

    def add(self, drug: Drug) -> None:
        # Добавляет препарат в хранилище
        pass

    def find_by_id(self, id: int) -> Drug:
        # Возвращает препарат по id
        return None

    def get_all(self, ) -> list[Drug]:
        # Возвращает все препараты
        return []

