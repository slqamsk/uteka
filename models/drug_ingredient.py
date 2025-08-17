"""
Описывает включение действующего вещества в состав препарата. Один препарат может содержать несколько веществ, одно вещество — в нескольких препаратах.
"""

class Drug_Ingredient:
    """
    Описывает включение действующего вещества в состав препарата. Один препарат может содержать несколько веществ, одно вещество — в нескольких препаратах.
    """
    def __init__(self, drug: Drug, ingredient: Ingredient, strength: float, unit: Unit):
        self.drug = drug
        self.ingredient = ingredient
        self.strength = strength
        self.unit = unit

    def __repr__(self):
        return f'<Drug_Ingredient {self.id}>'
