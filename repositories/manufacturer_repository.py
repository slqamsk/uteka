from ..models import Manufacturer
from typing import List, Optional

"""
Репозиторий: Manufacturer_Repository
"""

class Manufacturer_Repository:
    """
    Репозиторий для управления manufacturer repository.
    """
    def __init__(self):
        self._items = []

    def add(self, manufacturer: Manufacturer) -> None:
        # Добавляет производителя в хранилище
        pass

    def find_by_id(self, id: int) -> Manufacturer:
        # Возвращает производителя по id или None
        return None

    def get_all(self, ) -> list[Manufacturer]:
        # Возвращает полный список производителей
        return []

