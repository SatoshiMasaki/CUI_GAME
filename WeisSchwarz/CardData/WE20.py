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


class WE20_29(CHARA):
    def __init__(self, player):
        self.player = player
        self.name = "笑顔のために すもも"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ("委員長", "演劇")
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    def permanentEffect(self, player1, player2, position):
        pass  # 他のレベル0キャラ1枚につき+500

    def cipEffect(self, player1, player2, position):
        pass  # 山札の上から1枚を見て、上か下に置く
