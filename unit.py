from abc import ABC, abstractmethod
import spells

class Unit(ABC):

    def __init__(self,strength: int,dexterity: int,constitution: int,wisdom: int,intelligence: int,charisma: int,):

        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.spells: list = []
        self.mana: int = 0

    @abstractmethod
    def calculate_max_health(self):
        pass

    @abstractmethod
    def calculate_damage(self):
        pass

    @abstractmethod
    def calculate_defense(self):
        pass

    def add_spell(self, spell: "spells"):
        self.spells.append(spell)

    def cast_spell(self, index: int):
        if index < 0 or index >= len(self.spells):
            raise IndexError(f"Так называемого {index} не найдено.")

        spell = self.spells[index]

        if self.mana < spell.mana_cost:
            raise RuntimeError(f"Недостаточно маны! Требуется: {spell.mana_cost}, доступно: {self.mana}")

        self.mana -= spell.mana_cost
        return spell.cast()