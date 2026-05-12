from unit import Unit

class Character(Unit):
    game_classes = {"warrior", "mage", "hunter"}

    def __init__(self,strength: int,dexterity: int,constitution: int,wisdom: int,intelligence: int,charisma: int,character_class: str,):
        super().__init__(strength, dexterity, constitution,wisdom, intelligence, charisma,)

        if character_class not in self.game_classes:
            raise ValueError(f"Недопустимый класс '{character_class}'. ")

        self.character_class = character_class

        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()
        self.mana = self.calculate_max_mana()

    def calculate_max_health(self) -> int:
        return int(self.constitution * 10 + self.strength // 2)

    def calculate_damage(self):
        if self.character_class == "warrior":
            return int(self.strength * 2.2 + self.constitution // 3)
        if self.character_class == "mage":
            return int(self.intelligence * 2.5 + self.wisdom // 2)
        if self.character_class == "hunter":
            return int(self.dexterity * 1.9 + self.strength // 3)
        return 0

    def calculate_defense(self):
        if self.character_class == "warrior":
            return int(self.constitution * 1.8 + self.strength // 4)
        if self.character_class == "mage":
            return int(self.wisdom * 1.3 + self.intelligence // 6)
        if self.character_class == "hunter":
            return int(self.dexterity * 1.6 + self.constitution // 5)
        return 0

    def calculate_max_mana(self):
        if self.character_class == "warrior":
            return int(self.intelligence + self.strength // 2)
        if self.character_class == "mage":
            return int(self.intelligence * 3 + self.wisdom)
        if self.character_class == "hunter":
            return int(self.dexterity * 1.5 + self.wisdom // 2)
        return 0