"""
Лекарственная форма (dosage form) — физическое состояние препарата. Определяет способ применения, биодоступность и путь введения.
"""

class DosageForm:
    """
    Лекарственная форма (dosage form) — физическое состояние препарата. Определяет способ применения, биодоступность и путь введения.
    """
    def __init__(self, id: int, name: str, code: str, category: str, route_of_administration: RouteOfAdministration):
        self.id = id
        self.name = name
        self.code = code
        self.category = category
        self.route_of_administration = route_of_administration

    def __repr__(self):
        return f'<DosageForm {self.id}>'
