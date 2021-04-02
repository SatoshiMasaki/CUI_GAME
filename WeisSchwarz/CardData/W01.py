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


class W01_029(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "パジャマの茜"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ()
        self.status = util.Status.STAND
        self.counter = True
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    def counterEffect(self, player1, player2, attacked_chara):
        player1.untilTurnEndEffect.adaptField(player1, player2, (player1, attacked_chara),
                                              [(player1, attacked_chara)], [lambda: True],
                                              [("increasePower", lambda: 2000)])
        if player1.MYFIELD["Stage"].searchName(player1, "小恋") or player1.MYFIELD["Stage"].searchName(player1, "杏"):
            print("パジャマの茜 : このカードのカウンターを発動したとき、"
                  "自分の場に「小恋」か「杏」を名前に含むキャラがいる場合、山札の上から一枚ストックに置く")
            player1.MYFIELD["Stock"].append(player1.MYFIELD["Deck"].turnOver(player1))


class W01_069(EVENT):
    def __init__(self, player=None):
        super().__init__()
        self.player = player
        self.name = "かけがえのない仲間"
        self.color = util.Color.RED
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 2
        self.counter = False
        self.useCardLimit = None

    def autoEffect(self, player1, player2):
        print("控室から二枚キャラを回収します")
        for i in range(2):
            player1.cardEffect.UtilEffect.salvageCard(player1, player2, util.CardType.CHARA)


class W01_084(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "杉並"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 1000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ("新聞", "オカルト")
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    def loseBattle(self, player1, _, __, ___):
        print("{} : 自リバース時、カードを一枚引く".format(self.name))
        player1.MYFIELD["Deck"].draw(player1)


class W01_E18(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "小川で遊ぼう"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 0
        self.counter = False
        self.useCardLimit = None

    def autoEffect(self, player1, _):
        print("カードを二枚引きます")
        player1.MYFIELD["Deck"].draw(player1)
        player1.MYFIELD["Deck"].draw(player1)
        print("カードを二枚手札から山札の上に戻します。カードを選んでください")
        for i in range(2):
            while True:
                for i, card in enumerate(player1.MYFIELD["Hand"]):
                    print("{} : ".format(i + 1), card.name)
                selectCard = int(input("カードを選んでください"))
                if util.varSizeChecker(1, len(player1.MYFIELD["Hand"]), selectCard):
                    player1.MYFIELD["Deck"].insert(0, player1.MYFIELD["Hand"].pop(selectCard - 1))
                    break
                else:
                    print("数値を入力してください")
