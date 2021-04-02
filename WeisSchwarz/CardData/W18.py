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


class W18_023(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "息抜きデート サラ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ("魔法", "スポーツ")
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    def startUpEffect(self, player1, _, __):
        flag = player1.MYFIELD["Stock"].costCheck(1)
        if flag:
            player1.useCost(1)
            self.status = util.Status.REST
            count = player1.cardEffect.CharaEffect.concentration(player1, _, 4)
            if count != 0:
                print("{} : クロックからカードを1枚回収する。その後山札の上から1枚をクロックに置く".format(self.name))
                player1.MYFIELD["Clock"].showClock()
                select_card = util.selectNumberChecker(1, len(player1.MYFIELD["Clock"]), "カードを選んでください")
                player1.MYFIELD["Hand"].append(player1.MYFIELD["Clock"].pop(select_card - 1))
                player1.MYFIELD["Deck"].turnOver(player1)
                player1.MYFIELD["Clock"].append(player1.MYFIELD["Event_Zone"].pop())


class W18_071(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "フラワーズは大忙し！　葵"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ("新聞", "ウェイトレス")
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    def permanentEffect(self, player1, player2, position):
        def limit():
            if position == 3 or position == 4:
                return True
            else:
                return False

        def effect():
            return player1.cardEffect.CharaEffect.handEncore

        player1.permanentEffect.adaptField(
            player1, player2, (player1, position), [(player1, position - 3), (player1, position - 2)],
            [limit, limit], [("appendEffect", effect(), "effectEncore"), ("appendEffect", effect(), "effectEncore")]
        )

    def startUpEffect(self, player1, _, __):
        if player1.MYFIELD["Stock"].costCheck(2) and self.status == util.Status.STAND:
            player1.useCost(2)
            self.status = util.Status.REST
            for card in player1.MYFIELD["Waiting_Room"]:
                player1.MYFIELD["Deck"].append(card)
            player1.MYFIELD["Deck"].shuffle()

