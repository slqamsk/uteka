from ..models import DosageForm
from typing import List, Optional

"""
Репозиторий: DosageForm_Repository
"""

class DosageForm_Repository:
    """
    Репозиторий для управления dosageform repository.
    """
    def __init__(self):
        self._items = []

    def add(self, form: DosageForm) -> None:
        # Добавляет форму в хранилище и в индекс
        pass

    def find_by_id(self, id: int) -> DosageForm:
        # Возвращает форму по id
        return None

    def find_by_name(self, name: str) -> DosageForm:
        # Находит форму по названию
        return None

    def get_all(self, ) -> list[DosageForm]:
        # Возвращает все формы
        return []

