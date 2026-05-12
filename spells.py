from abc import ABC, abstractmethod

class Spell(ABC):
    def __init__(self, name: str, damage: int, mana_cost: int):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self):
        pass


class Fireball(Spell):
    def __init__(self):
        super().__init__("Fireball", 35, 15)

    def cast(self):
        return self.damage


class IceLance(Spell):
    def __init__(self):
        super().__init__("Ice Lance", 25, 10)

    def cast(self) -> int:
        return self.damage


class LightningBolt(Spell):
    def __init__(self) -> None:
        super().__init__("Lightning Bolt", 40, 20)

    def cast(self):
        return self.damage