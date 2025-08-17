from ..models import Unit
from typing import List, Optional

"""
Репозиторий: Unit_Repository
"""

class Unit_Repository:
    """
    Репозиторий для управления unit repository.
    """
    def __init__(self):
        self._items = []

    def add(self, unit: Unit) -> None:
        # Добавляет единицу и индексирует по коду
        pass

    def find_by_id(self, id: int) -> Unit:
        # Возвращает единицу по id
        return None

    def find_by_code(self, code: str) -> Unit:
        # Находит единицу по коду UCUM
        return None

    def get_all(self, ) -> list[Unit]:
        # Возвращает все единицы
        return []

    def convert(self, value: float, from_unit: Unit, to_unit: Unit) -> float:
        # Конвертирует значение между единицами
        return 0.0

    def can_convert(self, from_unit: Unit, to_unit: Unit) -> bool:
        # Проверяет, можно ли конвертировать (по типу)
        return False

