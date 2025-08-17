"""
Действующее вещество (active pharmaceutical ingredient, API), обладающее фармакологической активностью.
"""

class Ingredient:
    """
    Действующее вещество (active pharmaceutical ingredient, API), обладающее фармакологической активностью.
    """
    def __init__(self, id: int, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<Ingredient {self.id}>'
