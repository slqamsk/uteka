"""
Производитель лекарственного средства (фармацевтическая компания)
"""

class Manufacturer:
    """
    Производитель лекарственного средства (фармацевтическая компания)
    """
    def __init__(self, id: int, name: str, country: str):
        self.id = id
        self.name = name
        self.country = country

    def __repr__(self):
        return f'<Manufacturer {self.id}>'
