"""
Лекарственное средство — торговый препарат с указанием формы и производителя.
"""

class Drug:
    """
    Лекарственное средство — торговый препарат с указанием формы и производителя.
    """
    def __init__(self, id: int, name: str, dosage_form: DosageForm, manufacturer: Manufacturer):
        self.id = id
        self.name = name
        self.dosage_form = dosage_form
        self.manufacturer = manufacturer

    def __repr__(self):
        return f'<Drug {self.id}>'
