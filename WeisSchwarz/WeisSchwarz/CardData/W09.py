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


class W09_033(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "白河ことり"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ("音楽", "魔法")
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    def cipEffect(self, player1, player2, position):
        print("白河 ことり : このカードが舞台に置かれたとき、相手は手札を見せてもよい。その中にCXが含まれる場合、このカードをレストする。")
        flag = util.selectNumberChecker(1, 2, "手札を公開しますか？\n1 : はい\n2 : いいえ")
        if flag == 1:
            player2.MYFIELD["Hand"].showHand()
            for card in player2.MYFIELD["Hand"]:
                if card.cardType == util.CardType.CX:
                    player1.MYFIELD["Stage"][position][0].status = util.Status.REST
                    break
        else:
            pass


class W09_078(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“3バカ”杉並＆義之＆渉"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ("オカルト", "音楽")
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
        self.flag = None

    def loseBattle(self, player1, _, position, __):
        if player1.MYFIELD["Stock"].costCheck(1):
            print("{} : リバース時、1コスト払うことでこのカードを思い出に送る".format(self.name))
            print("1 : 使う\n2 : 使わない")
            select_use_effect = util.selectNumberChecker(1, 2, "{} の効果を使いますか？".format(self.name))
            if select_use_effect == 1:
                player1.MYFIELD["Memory"].append(player1.MYFIELD["Stage"][position].pop())
                print("{}を思い出にしました".format(self.name))
            if select_use_effect == 2:
                pass

    def startAttackPhase(self, player1, player2, position):
        if player2.turnPlayer is False:
            pass
        else:
            if self.flag != player2.numberOfTurns:
                player2.cardEffect.CharaEffect.moveStage(player1, player2, position)
                self.flag = player2.numberOfTurns


class W09_112(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "気配り上手な奥さん ことり"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ("音楽", "魔法")
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    def permanentEffect(self, player1, player2, position):
        def limit():
            if len(player1.MYFIELD["Stock"]) < 4:
                return True
            else:
                return False

        player1.permanentEffect.adaptField(
            player1, player2, (player1, position), [(player1, position)], [limit], [("increasePower", lambda: 1000)]
        )
