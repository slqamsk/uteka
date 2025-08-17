"""
Единица измерения дозы (мг, мл, МЕ и т.п.) с поддержкой стандартов и конвертации.
"""

class Unit:
    """
    Единица измерения дозы (мг, мл, МЕ и т.п.) с поддержкой стандартов и конвертации.
    """
    def __init__(self, id: int, name: str, code: str, type: str, base_unit: Unit, conversion_factor: float):
        self.id = id
        self.name = name
        self.code = code
        self.type = type
        self.base_unit = base_unit
        self.conversion_factor = conversion_factor

    def __repr__(self):
        return f'<Unit {self.id}>'
