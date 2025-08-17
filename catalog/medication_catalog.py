from typing import List
from ..models import Ingredient, Drug, Unit, TargetDose
from ..repositories import (
    Manufacturer_Repository,
    DrugClass_Repository,
    Ingredient_Repository,
    Ingredient_DrugClass_Repository,
    DosageForm_Repository,
    RouteOfAdministration_Repository,
    Unit_Repository,
    Drug_Repository,
    Drug_Ingredient_Repository
)

"""
Единый каталог, объединяющий все репозитории и предоставляющий удобный интерфейс.
"""

class Medication_Catalog:
    """
    Единый каталог, объединяющий все репозитории и предоставляющий удобный интерфейс
    для доступа к данным и выполнения клинических операций.
    """
    def __init__(
        self,
        manufacturer_repo: Manufacturer_Repository,
        drug_class_repo: DrugClass_Repository,
        ingredient_repo: Ingredient_Repository,
        ingredient_drug_class_repo: Ingredient_DrugClass_Repository,
        dosage_form_repo: DosageForm_Repository,
        route_repo: RouteOfAdministration_Repository,
        unit_repo: Unit_Repository,
        drug_repo: Drug_Repository,
        drug_ingredient_repo: Drug_Ingredient_Repository
    ):
        self.manufacturer_repo = manufacturer_repo
        self.drug_class_repo = drug_class_repo
        self.ingredient_repo = ingredient_repo
        self.ingredient_drug_class_repo = ingredient_drug_class_repo
        self.dosage_form_repo = dosage_form_repo
        self.route_repo = route_repo
        self.unit_repo = unit_repo
        self.drug_repo = drug_repo
        self.drug_ingredient_repo = drug_ingredient_repo

    def get_drugs_containing(self, ingredient: Ingredient) -> List[Drug]:
        # Возвращает все препараты, содержащие указанное вещество
        links = self.drug_ingredient_repo.find_by_ingredient(ingredient)
        return [link.drug for link in links]

    def get_strength(self, drug: Drug, ingredient: Ingredient) -> tuple[Optional[float], Optional[Unit]]:
        # Возвращает дозу вещества в препарате
        link = self.drug_ingredient_repo.find_by_drug_and_ingredient(drug, ingredient)
        if link:
            return (link.strength, link.unit)
        return (None, None)

    def convert_dose(self, value: float, from_unit: Unit, to_unit: Unit) -> float:
        # Конвертирует дозу между единицами
        if self.unit_repo.can_convert(from_unit, to_unit):
            return self.unit_repo.convert(value, from_unit, to_unit)
        raise ValueError(f"Cannot convert {{from_unit.code}} to {{to_unit.code}}")
