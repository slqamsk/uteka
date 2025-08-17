"""
Путь введения лекарства (например, перорально, внутривенно). Используется для связи с лекарственной формой и клинической логикой.
"""

class RouteOfAdministration:
    """
    Путь введения лекарства (например, перорально, внутривенно). Используется для связи с лекарственной формой и клинической логикой.
    """
    def __init__(self, id: int, name: str, code: str, description: str):
        self.id = id
        self.name = name
        self.code = code
        self.description = description

    def __repr__(self):
        return f'<RouteOfAdministration {self.id}>'
