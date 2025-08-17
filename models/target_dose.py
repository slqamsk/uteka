"""
Целевая доза — требуемое количество действующего вещества в день. Используется как входной параметр при подборе комбинаций лекарств.
"""

class TargetDose:
    """
    Целевая доза — требуемое количество действующего вещества в день. Используется как входной параметр при подборе комбинаций лекарств.
    """
    def __init__(self, ingredient: Ingredient, amount: float, unit: Unit):
        self.ingredient = ingredient
        self.amount = amount
        self.unit = unit

    def __repr__(self):
        return f'<TargetDose {self.id}>'
