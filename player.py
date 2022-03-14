

class Player:
    def __init__(self, name: str, skills: dict[str, int], position: tuple[float, float]) -> None:
        self.name: str = name
        self.skills: dict[str, int] = skills
        self.health: int = 100
        self.level: int = 1
        self.experience: int = 0
        self.money: int = 100
        self.position: tuple[float, float] = position

    def show_skills(self):
        for key in self.skills.keys():
            print(f"{key} : {self.skills[key]}")


if __name__ == "__main__":
    p = Player('Olav', {'Strength': 8, 'Stamina': 7, 'Agility': 9, 'Wisdom': 6}, (128, 128))
    p.show_skills()
