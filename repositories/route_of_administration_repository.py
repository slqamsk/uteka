from ..models import RouteOfAdministration
from typing import List, Optional

"""
Репозиторий: RouteOfAdministration_Repository
"""

class RouteOfAdministration_Repository:
    """
    Репозиторий для управления routeofadministration repository.
    """
    def __init__(self):
        self._items = []

    def add(self, route: RouteOfAdministration) -> None:
        # Добавляет путь введения
        pass

    def find_by_id(self, id: int) -> RouteOfAdministration:
        # Возвращает путь по id
        return None

    def get_all(self, ) -> list[RouteOfAdministration]:
        # Возвращает все пути введения
        return []

