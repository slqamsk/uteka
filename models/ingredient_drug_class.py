"""
Связывает действующее вещество с терапевтической группой. Позволяет одному веществу относиться к нескольким группам.
"""

class Ingredient_DrugClass:
    """
    Связывает действующее вещество с терапевтической группой. Позволяет одному веществу относиться к нескольким группам.
    """
    def __init__(self, ingredient: Ingredient, drug_class: DrugClass, role: str, evidence_level: str):
        self.ingredient = ingredient
        self.drug_class = drug_class
        self.role = role
        self.evidence_level = evidence_level

    def __repr__(self):
        return f'<Ingredient_DrugClass {self.id}>'
