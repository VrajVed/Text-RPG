#define weapons here
class weapon:

    def __init__(self, name: str, weaponType: str, damage: int, value: int) -> None:
        self.name = name
        self.weaponType = weaponType
        self.damage = damage
        self.value = value


#defining various weapons
Iron_Sword = weapon(name='Iron Sword', weaponType='sword',damage=7,value=10)
