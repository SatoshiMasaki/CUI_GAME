import util


class cardEffect:
    def __init__(self):
        self.CharaEffect = charaEffect()
        self.UtilEffect = utilEffect()


class utilEffect:
    def __init__(self):
        pass

    def salvageCard(self, player1, _, cardType):
        cardTypeName = ["キャラ", "イベント", "CX"]
        print("{}カードを1枚控室から回収します".format(cardTypeName[cardType - 1]))
        for i, card in enumerate(player1.MYFIELD["Waiting_Room"]):
            print("{} : {}".format(i + 1, card.name))
        while True:
            select_salvage_card = util.selectNumberChecker(1, len(player1.MYFIELD["Waiting_Room"]), "カードを選んでください")
            if player1.MYFIELD["Waiting_Room"][select_salvage_card - 1].cardType == cardType:
                player1.MYFIELD["Hand"].append(player1.MYFIELD["Waiting_Room"].pop(select_salvage_card - 1))
                break
            else:
                print("{} ではありません".format(cardTypeName[cardType - 1]))


class charaEffect:
    def __init__(self):
        pass

    def handEncore(self, player1, _, __):
        print("手札アンコールを使います")
        player1.MYFIELD["Hand"].showHand()
        while True:
            number = util.selectNumberChecker(1, len(player1.MYFIELD["Hand"]), "カードを選んでください")
            if player1.MYFIELD["Hand"][number - 1].cardType == util.CardType.CHARA:
                player1.MYFIELD["Waiting_Room"].append(player1.MYFIELD["Hand"].pop(number - 1))
                break
            else:
                print("キャラカードを選んでください")

    @staticmethod
    def moveStage(player1, player2, position):
        flag = False
        for i in range(3):
            if i == position:
                continue

            if player1.charaExistCheck(i) is False:
                flag = True

        if flag is True:
            print("{} : 相手のアタックフェイズの初めに自分の前列の空いている枠に移動することができる。".format("3バカ"))
            effectUseFlag = util.effectConfirm()
            if effectUseFlag == 1:
                player1.MYFIELD["Stage"].showStage()
                select_field = util.selectNumberChecker(1, 3, "移動先を選んでください")
                if player1.charaExistCheck(select_field - 1) is False:
                    player1.MYFIELD["Stage"].moveChara(player1, player2, position, select_field - 1)
                else:
                    print("その場所には動かすことができません")

    @staticmethod
    def concentration(player1, _, turnOverCount):
        CX_count = 0
        for i in range(turnOverCount):
            player1.MYFIELD["Deck"].turnOver(player1)
            print(player1.MYFIELD["Event_Zone"][i].name)
            if player1.MYFIELD["Event_Zone"][i].cardType == util.CardType.CX:
                CX_count += 1
        for i in range(turnOverCount):
            player1.MYFIELD["Waiting_Room"].append(player1.MYFIELD["Event_Zone"].pop())
        print("{} 枚成功しました".format(CX_count))
        if CX_count != 0:
            util.soundMp3("decision4")
        return CX_count

    @staticmethod
    def recovery(player):
        print("1点回復します")
        if len(player.MYFIELD["Clock"]) != 0:
            player.MYFIELD["Waiting_Room"].append(player.MYFIELD["Clock"].pop())
