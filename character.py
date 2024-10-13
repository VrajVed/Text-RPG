#Defining the player class with certain attributes
# TODO --> Add reputation system, money
class Character:


    #STATS OF ANY CHARACTER
    def __init__(self, STR, DEX, CHR, WIS, INT, SEX):
        self.STR = STR
        self.DEX = DEX
        self.CHR = CHR
        self.WIS = WIS
        self.INT = INT
        self.SEX = SEX


    #CLASS METHODS (ACTIONS THAT ANY CHARACTERS CAN TAKE)
    def attack(self, target) -> None:
        target.hp -= self.STR
        target.hp = max(target.hp,0)
