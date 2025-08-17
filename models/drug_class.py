"""
Терапевтическая или фармакологическая группа, к которой может относиться действующее вещество.
"""

class DrugClass:
    """
    Терапевтическая или фармакологическая группа, к которой может относиться действующее вещество.
    """
    def __init__(self, id: int, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return f'<DrugClass {self.id}>'
