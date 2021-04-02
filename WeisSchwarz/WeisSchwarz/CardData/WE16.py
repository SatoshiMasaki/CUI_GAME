import util


class CHARA:
    def __init__(self):
        self.player = None
        self.name = None
        self.color = None
        self.cardType = None
        self.trigger = None
        self.power = None
        self.level = None
        self.cost = None
        self.soul = None
        self.feature = None
        self.status = None
        self.counter = False
        self.appendEffect = None  # util.AppendEffect()
        self.attackLimit = False
        self.useCardLimit = None


class EVENT:
    def __init__(self):
        self.player = None
        self.name = None
        self.color = None
        self.cardType = None
        self.trigger = None
        self.level = None
        self.cost = None
        self.counter = False
        self.useCardLimit = None

    def autoEffect(self, player1, player2):
        pass


class CX:
    def __init__(self):
        self.player = None
        self.name = None
        self.color = None
        self.cardType = None
        self.trigger = None


class WE16_10(CHARA):
    def __init__(self, player):
        self.player = player
        self.name = "お料理上手 姫乃"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ("新聞",)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    def startUpEffect(self, player1, player2, _):
        if player1.MYFIELD["Stock"].costCheck(1) and player1.MYFIELD["Hand"].existCXCheck():
            print("{} : 1コスト払い手札のCXを1枚控室に送ることで、控室のキャラを1枚回収する".format(self.name))
            player1.MYFIELD["Hand"].showHand()
            while True:
                cx_index = util.selectNumberChecker(1, len(player1.MYFIELD["Hand"]), "CXカードを選んでください : ")
                if player1.MYFIELD["Hand"][cx_index - 1].cardType == util.CardType.CX:
                    player1.useCost(1)
                    player1.cardEffect.UtilEffect.salvageCard(player1, player2, util.CardType.CHARA)
                    break
                else:
                    print("CXではありません")
