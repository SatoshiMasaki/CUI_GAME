import util


class Card:
    def __init__(self, player, name, color, cardType, trigger, effect):
        self.player = player
        self.name = name
        self.color = color
        self.cardType = cardType
        self.trigger = trigger
        self.effect = effect
        self.useCardLimit = False


class CHARA(Card):
    def __init__(self, player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                 counter):
        super().__init__(player, name, color, cardType, trigger, effect)
        self.power = power
        self.level = level
        self.cost = cost
        self.soul = soul
        self.feature = feature
        self.status = status
        self.counter = counter
        self.appendEffect = None  # util.AppendEffect()
        self.attackLimit = False


class EVENT(Card):
    def __init__(self, player, name, color, cardType, trigger, effect, level, cost, counter):
        super().__init__(player, name, color, cardType, trigger, effect)
        self.level = level
        self.cost = cost
        self.counter = counter

    def autoEffect(self, player1, player2):
        pass


class CX(Card):
    def __init__(self, player, name, color, cardType, trigger, effect):
        super().__init__(player, name, color, cardType, trigger, effect)


class W01_029(CHARA):
    def __init__(self, player=None, name="パジャマの茜", color=util.Color.GREEN, cardType=util.CardType.CHARA,
                 trigger=(util.TriggerType.SOUL_ONE,), effect=None,
                 power=500, level=1, cost=0, soul=1, feature=(), status=util.Status.STAND,
                 counter=True):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def counterEffect(self, player1, player2, attacked_chara):
        player1.untilTurnEndEffect.adaptField(player1, player2, (player1, attacked_chara),
                                               [(player1, attacked_chara)], [lambda: True],
                                               [("increasePower", lambda: 2000)])
        if player1.MYFIELD["Stage"].searchName(player1, "小恋") or player1.MYFIELD["Stage"].searchName(player1, "杏"):
            print("パジャマの茜 : このカードのカウンターを発動したとき、"
                  "自分の場に「小恋」か「杏」を名前に含むキャラがいる場合、山札の上から一枚ストックに置く")
            player1.MYFIELD["Stock"].append(player1.MYFIELD["Deck"].turnOver(player1))


class W01_069(EVENT):
    def __init__(self, player=None, name="かけがえのない仲間", color=util.Color.RED, cardType=util.CardType.EVENT,
                 trigger=(), effect=None,
                 level=2, cost=2, counter=True):
        super().__init__(player, name, color, cardType, trigger, effect, level, cost, counter)

    def autoEffect(self, player1, player2):
        print("控室から二枚キャラを回収します")
        for i in range(2):
            player1.cardEffect.UtilEffect.salvageCard(player1, player2, util.CardType.CHARA)


class W01_084(CHARA):
    def __init__(self, player=None, name="杉並", color=util.Color.BLUE, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=1000, level=1, cost=1, soul=1, feature=("オカルト",), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def loseBattle(self, player1, _, __, ___):
        print("{} : 自リバース時、カードを一枚引く".format(self.name))
        player1.MYFIELD["Deck"].draw(player1)


class W01_E18(EVENT):
    def __init__(self, player=None, name="小川で遊ぼう", color=util.Color.BLUE, cardType=util.CardType.EVENT,
                 trigger=(), effect=None,
                 level=0, cost=0, counter=True):
        super().__init__(player, name, color, cardType, trigger, effect, level, cost, counter)

    def autoEffect(self, player1, player2):
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


class W09_033(CHARA):
    def __init__(self, player=None, name="白河 ことり", color=util.Color.GREEN, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=4000, level=0, cost=0, soul=1, feature=("魔法", "音楽"), status=util.Status.STAND, counter=None,):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

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
    def __init__(self, player=None, name="“3バカ”杉並＆義之＆渉", color=util.Color.BLUE, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=1000, level=0, cost=0, soul=1, feature=("オカルト", "音楽"), status=util.Status.STAND, counter=None,):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)
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
    def __init__(self, player=None, name="気配り上手な奥さん ことり", color=util.Color.GREEN,
                 cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=2500, level=0, cost=0, soul=1, feature=("魔法", "音楽"), status=util.Status.STAND, counter=None,):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def permanentEffect(self, player1, player2, position):
        def limit():
            if len(player1.MYFIELD["Stock"]) < 4:
                return True
            else:
                return False

        # def effect():
        #     return 1000

        player1.permanentEffect.adaptField(
            player1, player2, (player1, position), [(player1, position)], [limit], [("increasePower", lambda: 1000)])


class WE16_10(CHARA):
    def __init__(self, player=None, name="お料理上手 姫乃", color=util.Color.RED, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=2000, level=0, cost=0, soul=1, feature=("新聞",), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

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


class W18_023(CHARA):
    def __init__(self, player=None, name="息抜きデート サラ", color=util.Color.GREEN, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=2000, level=0, cost=0, soul=1, feature=("魔法", "スポーツ"), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

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


class W18_046(CHARA):
    def __init__(self, player=None, name="公式新聞部部長 立夏", color=util.Color.RED, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=6000, level=0, cost=0, soul=1, feature=("新聞", "生徒会"), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def encoreEffect(self):
        pass


class W18_071(CHARA):
    def __init__(self, player=None, name="フラワーズは大忙し！　葵", color=util.Color.BLUE, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=2500, level=0, cost=0, soul=1, feature=("新聞", "ウェイトレス"), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

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


class WE20_29(CHARA):
    def __init__(self, player=None, name="笑顔のために すもも", color=util.Color.BLUE, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=6000, level=1, cost=1, soul=1, feature=("委員長", "演劇"), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def permanentEffect(self, player1, player2, position):
        pass  # 他のレベル0キャラ1枚につき+500

    def cipEffect(self, player1, player2, position):
        pass  # 山札の上から1枚を見て、上か下に置く


class W23_026(CHARA):
    def __init__(self, player=None, name="わたしの気持ち ななか", color=util.Color.GREEN, cardType=util.CardType.CHARA,
                 trigger=(util.TriggerType.SOUL_ONE,), effect=None,
                 power=9500, level=3, cost=2, soul=2, feature=("魔法", "音楽"), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def permanentEffect(self, player1, player2, position):
        def limit():
            return True

        def effect():
            return (player1.MYFIELD["Stage"].countFeature(player1, ("音楽", "魔法")) - 1) * 500

        player1.permanentEffect.adaptField(
            player1, player2, (player1, position), [(player1, position)],
            [limit], [("increasePower", effect)]
        )

    def cipEffect(self, player1, player2, _):
        if player1.MYFIELD["Stock"].costCheck(1):
            print("{} : 相手のストックをすべて控室に送る。その後相手は控室に送った枚数山札の上からストックに置く。"
                   .format(self.name))
            flag = util.effectConfirm()
            if flag == 1:
                player1.useCost(1)
                count = 0
                for i in range(len(player2.MYFIELD["Stock"])):
                    player2.MYFIELD["Waiting_Room"].append(player2.MYFIELD["Stock"].pop())
                    count += 1
                for i in range(count):
                    player2.MYFIELD["Deck"].turnOver(player2)
                    player2.MYFIELD["Stock"].append(player2.MYFIELD["Event_Zone"].pop())


class W23_030(CHARA):
    def __init__(self, player=None, name="ずっと変わらない 小恋", color=util.Color.GREEN, cardType=util.CardType.CHARA,
                 trigger=(util.TriggerType.SOUL_ONE,), effect=None,
                 power=8000, level=2, cost=1, soul=1, feature=("音楽",), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def CXcombo(self, player1, player2, position, useCard):
        pass


class W23_039(CHARA):
    def __init__(self, player=None, name="胸のドキドキ みっくん", color=util.Color.GREEN, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=500, level=0, cost=0, soul=1, feature=("音楽",), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def permanentEffect(self, player1, player2, position):
        def limit1():
            if player1.charaExistCheck(0):
                if "音楽" in player1.MYFIELD["Stage"][0][0].feature and player1.MYFIELD["Stage"][0][0] is not self:
                    return True
                else:
                    return False

        def limit2():
            if player1.charaExistCheck(1):
                if "音楽" in player1.MYFIELD["Stage"][1][0].feature and player1.MYFIELD["Stage"][1][0] is not self:
                    return True
                else:
                    return False

        def limit3():
            if player1.charaExistCheck(2):
                if "音楽" in player1.MYFIELD["Stage"][2][0].feature and player1.MYFIELD["Stage"][2][0] is not self:
                    return True
                else:
                    return False

        def limit4():
            if player1.charaExistCheck(3):
                if "音楽" in player1.MYFIELD["Stage"][3][0].feature and player1.MYFIELD["Stage"][3][0] is not self:
                    return True
                else:
                    return False

        def limit5():
            if player1.charaExistCheck(4) and player1.MYFIELD["Stage"][4][0] is not self:
                if "音楽" in player1.MYFIELD["Stage"][4][0].feature and player1.MYFIELD["Stage"][4][0] is not self:
                    return True
                else:
                    return False

        player1.permanentEffect.adaptField(
            player1, player2, (player1, position), [(player1, i) for i in range(5)],
            [limit1, limit2, limit3, limit4, limit5],
            [("increaseLevel", lambda: 1) for _ in range(5)]
        )

    def startAttackPhase(self, player1, player2, position):
        if player1.turnPlayer is False and player1.MYFIELD["Stage"].searchFeature(player1, "音楽"):
            if player1.MYFIELD["Stock"].costCheck(1):
                print("{} : 相手のアタックフェイズのはじめに、1コスト払うことで「音楽」のキャラひとりを+1500".format(self.name))
                flag = util.selectNumberChecker(1, 2, "効果を使いますか？")
                if flag == 1:
                    player1.MYFIELD["Stage"].showStage()
                    while True:
                        select_card = util.selectNumberChecker(1, 5, "キャラを選んでください")
                        if player1.charaExistCheck(select_card - 1):
                            if select_card - 1 == position:
                                if "音楽" in player1.MYFIELD["Stage"][select_card - 1][0].feature:
                                    player1.permanentEffect.adaptField(
                                        player1, player2, (player1, position), [(player1, select_card - 1)],
                                        lambda: True,
                                        [("increasePower", lambda: 1500)]
                                    )
                                    break
                                else:
                                    print("音楽のキャラを選んでください")
                            else:
                                print("自身へ効果を使うことはできません")

                        else:
                            print("キャラがいません")


class W23_050(CX):
    def __init__(self, player=None, name="また会えるよね", color=util.Color.GREEN, cardType=util.CardType.CX,
                 trigger=(util.TriggerType.TREASURE,),
                 effect=None):
        super().__init__(player, name, color, cardType, trigger, effect)

    def permanentEffect(self, player):
        for i in range(5):
            if len(player.MYFIELD["Stage"][i]) != 0:
                player.MYFIELD["Stage"][i][0].power += 1000
                player.MYFIELD["Stage"][i][0].soul += 1
                print("{} に効果を使いました".format(player.MYFIELD["Stage"][i][0].name))
                print("パワー : {}".format(player.MYFIELD["Stage"][i][0].power))
                print("ソウル : {}".format(player.MYFIELD["Stage"][i][0].soul))
        return [[1000, 1000, 1000, 1000, 1000], [1, 1, 1, 1, 1]]


class W23_062(CHARA):
    def __init__(self, player=None, name="帰ってきた笑顔 美夏", color=util.Color.RED, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=2500, level=2, cost=1, soul=1, feature=("メカ", "バナナ"), status=util.Status.STAND,
                 counter=True):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    # 2コス＋舞台のキャラ1枚。相手の早出しキャラ1枚を控室に送る
    def counterEffect(self, player1, player2, attacked_chara):
        print("{} : カウンター(2500)。2コスト、自分の舞台のキャラを1枚控室に置くことで、相手の早出しキャラを1枚控室に送る"
               .format(self.name))
        player1.untilTurnEndEffect.adaptField(player1, player2, (player1, attacked_chara),
                                               [(player1, attacked_chara)], [lambda: True],
                                               [("increasePower", lambda: 2500)]
                                              )

        charaExistFlag = False
        costFlag = False
        levelOverCharaExist = False
        for i in range(5):
            if player1.charaExistCheck(i) is True:
                charaExistFlag = True
                break
        for i in range(5):
            if player2.charaExistCheck(i) and player2.MYFIELD["Stage"][i][0].level > player2.level:
                levelOverCharaExist = True
        if player1.MYFIELD["Stock"].costCheck(2):
            costFlag = True
        if charaExistFlag and costFlag and levelOverCharaExist:
            confirmFlag = util.effectConfirm()
            if confirmFlag == 1:
                player1.useCost(2)

                # コストとして自分のキャラを控室に送る
                player1.MYFIELD["Stage"].showStage()
                while True:
                    select_chara = util.selectNumberChecker(1, 5, "控室に置くカードを選んでください : ")
                    if player1.charaExistCheck(select_chara - 1):
                        print("{} を控室に送ります".format(player1.MYFIELD["Stage"][select_chara - 1][0].name))
                        player1.MYFIELD["Stage"].leaveStageChara(
                            player1, player2, select_chara - 1, player1.MYFIELD["Waiting_Room"]
                        )
                        break
                    else:
                        print("キャラがいません")

                # 早出しキャラへの処理
                print("相手の早出しキャラを控室に送ります")
                player2.MYFIELD["Stage"].showStage()
                while True:
                    select_level_over_chara = util.selectNumberChecker(1, 5, "カードを選んでください")
                    if player2.charaExistCheck(select_level_over_chara - 1) and \
                            player2.MYFIELD["Stage"][select_level_over_chara - 1][0].level > player2.level:
                        print("{} を控室に送ります".format(player2.MYFIELD["Stage"][select_level_over_chara - 1][0].name))
                        if player2.MYFIELD["Stage"][select_level_over_chara - 1][0].status == util.Status.STAND:
                            player2.standCount -= 1
                        player2.MYFIELD["Stage"].leaveStageChara(
                            player2, player1, select_level_over_chara - 1, player2.MYFIELD["Waiting_Room"]
                        )
                        break
                    else:
                        print("このカードは選べません")


class W23_076(CHARA):
    def __init__(self, player=None, name="小さな神秘 杏", color=util.Color.BLUE, cardType=util.CardType.CHARA,
                 trigger=(util.TriggerType.SOUL_ONE,), effect=None,
                 power=3000, level=0, cost=-0, soul=1, feature=("魔法", "演劇"), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def permanentEffect(self, player1, player2, position):
        def limit():
            if position == 3 or position == 4:
                return True
            else:
                return False

        def effect1():
            return player1.MYFIELD["Stage"][position - 3][0].level * 500

        def effect2():
            return player1.MYFIELD["Stage"][position - 2][0].level * 500

        player1.permanentEffect.adaptField(
            player1, player2, (player1, position), [(player1, position - 3), (player1, position - 2)],
            [limit, limit], [("increasePower", effect1), ("increasePower", effect2)]
        )

    def cipEffect(self, player1, _, __):
        print("{} 登場時2コストで魔法をサーチすることができる".format(self.name))
        if player1.MYFIELD["Stock"].costCheck(2):
            flag = util.effectConfirm()
            if flag == 1:
                for i, card in enumerate(player1.MYFIELD["Deck"]):
                    print("{} : {}".format(i + 1, card.name))

                while True:
                    select_card = util.selectNumberChecker(1, len(player1.MYFIELD["Deck"]), "サーチするカードを選んでください")
                    if "魔法" in player1.MYFIELD["Deck"][select_card - 1].feature:
                        player1.useCost(2)
                        print("{} を手札に加えます".format(player1.MYFIELD["Deck"][select_card - 1].name))
                        player1.MYFIELD["Deck"].turnOver(player1, select_card - 1)
                        player1.MYFIELD["Hand"].append(player1.MYFIELD["Event_Zone"].pop())
                        player1.MYFIELD["Deck"].shuffle()
                        break
                    else:
                        print("魔法を選んでください")


class WE30_07(CHARA):
    def __init__(self, player=None, name="桜風の季節 エリカ＆由夢", color=util.Color.RED, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=1500, level=0, cost=0, soul=1, feature=("王族", "生徒会"), status=util.Status.STAND, counter=None):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def permanetEffect(self, player1, player2, position):
        featList = list(self.feature)
        featList.append("魔法")
        self.feature = tuple(featList)

        player1.permanentEffect.appendEffect(player1, player2, (player1, position),
                                              (player1, position), ("appendFeature", "魔法"))

    def startUpEffect(self, player1, player2, _):
        print("集中を使います")
        if self.player.MYFIELD["Stock"].costCheck(1) and self.status == util.Status.STAND:
            self.player.useCost(1)
            self.status = util.Status.REST

            salvage_count = player1.cardEffect.CharaEffect.concentration(player1, player2, 4)
            for i in range(salvage_count):
                player1.cardEffect.UtilEffect.salvageCard(player1, player2, util.CardType.CHARA)
        else:
            print("ストックが足りません")

    def useCX(self, player1, player2, position):
        def limit():
            return True

        def effect():
            return 1000

        try:
            if player2.turnPlayer is False:
                print("{} : CXが置かれたとき、自分のキャラ1枚のパワーを+1000できる".format(self.name))
                flag = util.effectConfirm()
                if flag == 1:
                    player1.MYFIELD["Stage"].showStage()
                    while True:
                        select_filed = util.selectNumberChecker(1, 5, "パンプするキャラを選んでください")
                        if player1.charaExistCheck(select_filed - 1):
                            player1.MYFIELD["Stage"][select_filed - 1][0].power += 1000
                            player1.untilTurnEndEffect.adaptField(player1, player2, (player1, position),
                                                                   [(player1, select_filed - 1)], [limit],
                                                                   [("increasePower", effect)])
                            break
                        else:
                            print("キャラがいません")
                else:
                    pass
        except Exception as err:
            util.debug(err)


class WE30_09(EVENT):
    def __init__(self, player=None, name="打ち上げ花火", color=util.Color.GREEN, cardType=util.CardType.EVENT,
                 trigger=(), effect=None,
                 level=1, cost=0, counter=True):
        super().__init__(player, name, color, cardType, trigger, effect, level, cost, counter)
        self.useCardLimit = True

    def cardLimit(self, player1, _):
        if player1.MYFIELD["Stage"].searchFeature(player1, "音楽"):
            return True
        else:
            print("「音楽」のキャラがいないため、発動できません")
            return False

    def counterEffect(self, player1, _, __):
        if player1.MYFIELD["Stage"].searchFeature(player1, "音楽"):
            feature_flag = False
            for i in range(4):
                player1.MYFIELD["Deck"].turnOver(player1)
                print("{} : {}".format(i + 1, player1.MYFIELD["Event_Zone"][i].name))
                if "音楽" in player1.MYFIELD["Event_Zone"][i].feature:
                    feature_flag = True
            if feature_flag:
                select_card = util.selectNumberChecker(1, 4, "カードを選んでください")
                if "音楽" in player1.MYFIELD["Event_Zone"][select_card - 1].feature:
                    player1.MYFIELD["Hand"].append(player1.MYFIELD["Event_Zone"].pop(select_card - 1))
                    for i in range(3):
                        player1.MYFIELD["Waiting_Room"].append(player1.MYFIELD["Event_Zone"].pop())
                else:
                    print("「音楽」のキャラを選んでください")
            else:
                for i in range(4):
                    player1.MYFIELD["Waiting_Room"].append(player1.MYFIELD["Event_Zone"].pop())
        else:
            print("「音楽」のキャラがいないため、発動できません")
            player1.MYFIELD["Hand"].append(player1.MYFIELD["Event_Zone"].pop())

    def autoEffect(self, player1, player2):
        if player1.MYFIELD["Stage"].searchFeature(player1, "音楽"):
            feature_flag = False
            for i in range(4):
                player1.MYFIELD["Deck"].turnOver(player1)
                print("{} : {}".format(i + 1, player1.MYFIELD["Event_Zone"][i].name))
                if player1.MYFIELD["Event_Zone"][i].cardType == util.CardType.CHARA and\
                        "音楽" in player1.MYFIELD["Event_Zone"][i].feature:
                    feature_flag = True
            if feature_flag:
                select_card = util.selectNumberChecker(1, 4, "カードを選んでください")
                if "音楽" in player1.MYFIELD["Event_Zone"][select_card - 1].feature:
                    player1.MYFIELD["Hand"].append(player1.MYFIELD["Event_Zone"].pop(select_card - 1))
                    for i in range(3):
                        player1.MYFIELD["Waiting_Room"].append(player1.MYFIELD["Event_Zone"].pop())
                else:
                    print("「音楽」のキャラを選んでください")
            else:
                for i in range(4):
                    player1.MYFIELD["Waiting_Room"].append(player1.MYFIELD["Event_Zone"].pop())
        else:
            print("「音楽」のキャラがいないため、発動できません")
            # player1.MYFIELD["Hand"].append(player1.MYFIELD["Event_Zone"].pop())


class WE30_10(CHARA):
    def __init__(self, player=None, name="ウェディングドレスのことり", color=util.Color.GREEN,
                 cardType=util.CardType.CHARA,
                 trigger=(util.TriggerType.SOUL_ONE,), effect=None,
                 power=10000, level=3, cost=2, soul=2, feature=("魔法", "音楽"), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def selfAttackTrigger(self, player1, player2, position):
        def limit():
            pass

        def effect():
            return count_feat * 500

        count_feat = player1.MYFIELD["Stage"].countFeature(player1, ("魔法", "音楽"))
        print("{} : 魔法か音楽のキャラひとりをパワー+X。Xは魔法か音楽のキャラひとりにつき+500".format(self.name))
        player1.MYFIELD["Stage"].showStage()
        while True:
            select_card = util.selectNumberChecker(1, 5, "カードを選んでください : ")
            if player1.charaExistCheck(select_card - 1):
                if "魔法" in player1.MYFIELD["Stage"][select_card - 1][0].feature or "音楽" in \
                        player1.MYFIELD["Stage"][select_card - 1][0].feature:
                    player1.untilTurnEndEffect.adaptField(player1, player2, (player1, position),
                                                           [(player1, select_card - 1)], [limit],
                                                           [("increasePower", effect)])
                    break
                else:
                    print("特徴「音楽」「魔法」をもちません")
            else:
                print("キャラがいません")

    def winBattle(self, player1, player2, _, enemyPosition):
        flag = player1.MYFIELD["Stock"].costCheck(1)
        if flag is True and player2.charaExistCheck(enemyPosition) is True:
            print("{} : このカードのバトル相手がリバースしたとき、1コストを払うことでバトル相手をクロックに置く".format(self.name))
            flag = util.effectConfirm()
            if flag == 1:
                player1.useCost(1)
                container = []
                player2.MYFIELD["Stage"][enemyPosition][0].status = util.Status.STAND
                player2.MYFIELD["Stage"].leaveStageChara(player2, player1, enemyPosition, container)
                player2.MYFIELD["Clock"].appendClock(player2, container.pop())


class WE30_P05(CHARA):
    def __init__(self, player=None, name="真夏の恋 小恋＆音夢＆ななか", color=util.Color.GREEN,
                 cardType=util.CardType.CHARA,
                 trigger=(util.TriggerType.SOUL_ONE,), effect=None,
                 power=10000, level=3, cost=2, soul=2, feature=("音楽", "魔法"), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def inHandEffect(self, player1, _):
        counter = 0
        CXflag = True
        levelFlag = False
        for card in player1.MYFIELD["Waiting_Room"]:
            if card.cardType == util.CardType.CX:
                counter += 1
                if counter == 3:
                    CXflag = False
                    break
        if player1.level == 2:
            levelFlag = True
        if CXflag and levelFlag:
            print("{} : 手札のこのカードのレベルを-1".format(self.name))
            self.level -= 1
        else:
            print("この効果は使えません")

    def cipEffect(self, _, __, ___):
        if self.level == 2:
            self.level += 1

    def turnStartEffect(self, player1, player2, position):
        if player1.turnPlayer is False:
            if position == 0 or position == 1 or position == 2:
                print("{} : 相手のターンのはじめにこのカードが前列にいるなら、"
                       "自分のキャラひとりのパワーを+4000できる".format(self.name))
                flag = util.effectConfirm()
                if flag == 1:
                    player1.MYFIELD["Stage"].showStage()
                    while True:
                        select_card = util.selectNumberChecker(1, 5, "カードを選んでください")
                        if player1.charaExistCheck(select_card - 1):

                            player1.untilTurnEndEffect.adaptField(
                                player1, player2, (player1, position), [(player1, select_card - 1)], [lambda: True],
                                [("increasePower", lambda: 4000)]
                            )
                            break
                        else:
                            print("キャラがいません")


class WE30_08(CHARA):
    def __init__(self, player=None, name="踏み出した一歩 小恋", color=util.Color.GREEN, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=1000, level=0, cost=0, soul=1, feature=("音楽",), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def cipEffect(self, player1, _, __):
        flag = False
        for card in player1.MYFIELD["Waiting_Room"]:
            if card.name == "打ち上げ花火":
                flag = True
                break
        if flag:
            print("{} : 手札を一枚控室に置く。控室の「打ち上げ花火」を手札に加える".format(self.name))
            effect_flag = util.effectConfirm()
            if effect_flag == 1:
                player1.MYFIELD["Hand"].showHand()
                select_card = util.selectNumberChecker(1, len(player1.MYFIELD["Hand"]), "カードを選んでください")
                player1.MYFIELD["Waiting_Room"].append(player1.MYFIELD["Hand"].pop(select_card - 1))
                for i, card in enumerate(player1.MYFIELD["Waiting_Room"]):
                    if card.name == "打ち上げ花火":
                        player1.MYFIELD["Hand"].append(player1.MYFIELD["Waiting_Room"].pop(i))
                        break

    def loseBattle(self, player1, player2, _, opposite_position):
        if player2.MYFIELD["Stage"][opposite_position][0].level <= self.level:
            print("{} : 相打ちストック送り".format(self.name))
            flag = util.effectConfirm()
            if flag == 1:
                if len(player2.MYFIELD["Clock"]) != 0:
                    player2.MYFIELD["Waiting_Room"].append(player2.MYFIELD["Clock"].pop())
                player2.MYFIELD["Stage"][opposite_position][0].status = util.Status.STAND
                player2.MYFIELD["Stage"].leaveStageChara(player2, player1, opposite_position, player2.MYFIELD["Clock"])


class WE30_15(CHARA):
    def __init__(self, player=None, name="仲良し雪月花 杏&小恋&茜", color=util.Color.BLUE, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=5500, level=1, cost=0, soul=1, feature=("音楽", "演劇"), status=util.Status.STAND, counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def startAttackPhase(self, player1, _, __):
        if player1.turnPlayer is True:
            if player1.charaExistCheck(3) and player1.charaExistCheck(4):
                pass
            else:
                print("{} : 後列のキャラが一枚以下ならこのカードをレストする".format(self.name))
                self.status = util.Status.REST

    def CXcombo(self, player1, player2, position, useCard):
        def searchCard(_, __, ___, ____):
            print("{} : 自分の後列のキャラを選び、そのキャラと同じ特徴か特徴をもたないキャラを山札から一枚選び手札に加える".format(self.name))
            for i in range(3, 5):
                if player1.charaExistCheck(i):
                    print("{} : {}".format(i - 2, player1.MYFIELD["Stage"][i][0].name))
                    for feat in player1.MYFIELD["Stage"][3][0].feature:
                        print(" : ", feat)
            select_card = util.selectNumberChecker(1, 2, "後列のキャラを選んでください")
            if player1.charaExistCheck(select_card + 2):
                player1.MYFIELD["Deck"].showDeck()
                while True:
                    index = util.selectNumberChecker(1, len(player1.MYFIELD["Deck"]), "カードを選んでください")
                    if player1.charaExistCheck(index + 2):
                        for feature in player1.MYFIELD["Stage"][select_card + 2][0].feature:
                            if len(player1.MYFIELD["Deck"][index - 1].feature) == 0 or \
                                    feature in player1.MYFIELD["Deck"][index - 1].feature:
                                player1.MYFIELD["Deck"].turnOver(index - 1)
                                player1.MYFIELD["Hand"].append(player1.MYFIELD["Event_Zone"].pop())
                                player1.MYFIELD["Deck"].shuffle()
                                break
                            else:
                                print("このカードは選べません")
                        break
                    else:
                        print("キャラがいません")

        if isinstance(useCard, WE30_21):
            player1.untilTurnEndEffect.adaptField(player1, player2, (player1, position),
                                                   [(player1, position)], [lambda: True],
                                                   [("appendEffect", searchCard, "winBattle")])


class WE30_20(CHARA):
    def __init__(self, player=None, name="体操着のななか", color=util.Color.GREEN, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=6500, level=0, cost=0, soul=1, feature=("音楽", "スポーツ"), status=util.Status.STAND, counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def permanentEffect(self, player1, player2, position):
        oppositePosition = player1.MYFIELD["Stage"].oppositePosition(position + 1)
        player1.permanentEffect.adaptField(
            player1, player2, (player1, position), [(player2, oppositePosition - 1)],
            [lambda: True], [("appendEffect", player2.cardEffect.CharaEffect.handEncore, "effectEncore")]
        )


class WE30_21(CX):
    def __init__(self, player=None, name="もう、忘れない", color=util.Color.BLUE, cardType=util.CardType.CX,
                 trigger=(util.TriggerType.SOUL_ONE, util.TriggerType.BOOK),
                 effect=None):
        super().__init__(player, name, color, cardType, trigger, effect)

    def permanentEffect(self, player):
        for i in range(5):
            if len(player.MYFIELD["Stage"][i]) != 0:
                player.MYFIELD["Stage"][i][0].power += 1000
                player.MYFIELD["Stage"][i][0].soul += 1
                print("{} に効果を使いました".format(player.MYFIELD["Stage"][i][0].name))
                print("パワー : {}".format(player.MYFIELD["Stage"][i][0].power))
                print("ソウル : {}".format(player.MYFIELD["Stage"][i][0].soul))
        return [[1000, 1000, 1000, 1000, 1000], [1, 1, 1, 1, 1]]


class WE30_27(CHARA):
    def __init__(self, player=None, name="水着の眞子&萌", color=util.Color.BLUE, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=1000, level=0, cost=0, soul=1, feature=("音楽", "鍋"), status=util.Status.STAND, counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def turnstarteffect(self, player1, player2, position):
        if player1.turnPlayer is False:
            print("{} : 相手ターン中、自分の舞台の前列中央のキャラを+1000する".format(self.name))
            player1.untilTurnEndEffect.adaptField(player1, player2, (player1, position),
                                                   [(player1, 1)], [lambda: True],
                                                   [("increasePower", lambda:1000)])

    def startUpEffect(self, player1, player2, position):
        if player1.MYFIELD["Stock"].costCheck(1):
            player1.useCost(1)
            self.status = util.Status.REST
            search_count = player1.cardEffect.CharaEffect.concentration(player1, player2, position)
            if search_count != 0:
                print("山札から「音楽」のキャラをサーチします")
                player1.MYFIELD["Deck"].showDeck()
                while True:
                    index = util.selectNumberChecker(1, len(player1.MYFIELD["Deck"]), "カードを選んでください")
                    if "音楽" in player1.MYFIELD["Deck"][index - 1].feature:
                        player1.MYFIELD["Deck"].turnOver(player1, index - 1)
                        player1.MYFIELD["Hand"].append(player1.MYFIELD["Event_Zone"].pop())
                        break
                    else:
                        print("音楽のキャラを選んでください")


class W46_099(CHARA):
    def __init__(self, player=None, name="幸せな時間 すもも", color=util.Color.BLUE, cardType=util.CardType.CHARA,
                 trigger=(util.TriggerType.SOUL_ONE,), effect=None,
                 power=10000, level=3, cost=2, soul=2, feature=("委員長", "演劇"), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def permanentEffect(self, player1, player2, position):
        """
        舞台のこのカードのレベルを-3。効果リバース無効。正面のキャラのレベル×1000パンプ
        """
        def increasePower():
            oppositePosition = player1.MYFIELD["Stage"].oppositePosition(position + 1)
            if player2.charaExistCheck(oppositePosition - 1):
                return player2.MYFIELD["Stage"][oppositePosition - 1][0].level * 1000
            return 0

        def decreaseLevel():
            return 3

        player1.permanentEffect.adaptField(
            player1, player2, (player1, position), [(player1, position)],
            [lambda: True], [("decreaseLevel", decreaseLevel)]
        )

        player1.permanentEffect.adaptField(
            player1, player2, (player1, position), [(player1, position)],
            [lambda: True], [("increasePower", increasePower)]
        )

    def cipEffect(self, player1, _, __):
        player1.cardEffect.CharaEffect.recovery(player1)

    def selfAttackTrigger(self, player1, _, position):
        if isinstance(player1.MYFIELD["Stage"][position][0], type(self)):
            pass
        else:
            exist_SUMOMO = False
            costCheck = False
            if player1.MYFIELD["Stock"].costCheck(0):
                costCheck = True
            for card in player1.MYFIELD["Hand"]:
                if card.name == "守りたい笑顔 すもも":
                    exist_SUMOMO = True
                    break

            if costCheck and exist_SUMOMO:
                print("{} : 中央のキャラのアタック時3コストと手札の「守りたい笑顔 すもも」を控室に置くことで、このカードをスタンドする".format(self.name))
                flag = util.effectConfirm()
                if flag == 1:
                    player1.useCost(0)
                    for i, card in enumerate(player1.MYFIELD["Hand"]):
                        if card.name == "守りたい笑顔 すもも":
                            player1.MYFIELD["Waiting_Room"].append(player1.MYFIELD["Hand"].pop(i))
                            break
                    for i in range(5):
                        if player1.MYFIELD["Stage"][i][0].name == "幸せな時間 すもも":
                            player1.MYFIELD["Stage"][i][0].status = util.Status.STAND
                            player1.standCount += 1
                            print("スタンドしました")
                            break

    def CXcombo(self, player1, player2, position, useCard):
        def effect():
            return self.selfAttackTrigger

        if isinstance(useCard, W46_109):
            player1.untilTurnEndEffect.adaptField(player1, player2, (player1, position),
                                                   [(player1, 1)], [lambda: True],
                                                   [("appendEffect", effect, "selfAttackTrigger")])


class W46_104(CHARA):
    def __init__(self, player=None, name="新しい一年の始まり 葵", color=util.Color.BLUE, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=2500, level=0, cost=0, soul=1, feature=("魔法", "委員長"), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def cipEffect(self, player1, _, __):
        if len(player1.MYFIELD["Stock"]) >= 1:
            print("{} : 登場時1コスト、手札のCXを一枚控室に置くことで、控室のCXを回収する".format(self.name))
            flag = util.effectConfirm()
            if flag == 1:
                player1.useCost(1)
                player1.MYFIELD["Hand"].showHand()
                while True:
                    select_card = util.selectNumberChecker(1, len(player1.MYFIELD["Hand"]), "カードを選んでください")
                    if player1.MYFIELD["Hand"][select_card - 1].cardType == util.CardType.CX:
                        print("控室のCXを回収します")
                        print("----------")
                        player1.MYFIELD["Waiting_Room"].showWaitingRoom()
                        while True:
                            select_salvage_card = util.selectNumberChecker(
                                1, len(player1.MYFIELD["Waiting_Room"]), "カードを選んでください"
                            )
                            if player1.MYFIELD["Waiting_Room"][select_salvage_card - 1].cardType == util.CardType.CX:
                                player1.MYFIELD["Hand"].append(
                                    player1.MYFIELD["Waiting_Room"].pop(select_salvage_card - 1)
                                   )
                                break
                            else:
                                print("CXカードを選んでください")
                        break
                    else:
                        print("CXカードを選んでください")


class W46_106(CHARA):
    def __init__(self, player=None, name="守りたい笑顔 すもも", color=util.Color.BLUE, cardType=util.CardType.CHARA,
                 trigger=(), effect=None,
                 power=5500, level=1, cost=0, soul=1, feature=("委員長", "演劇"), status=util.Status.STAND,
                 counter=False):
        super().__init__(player, name, color, cardType, trigger, effect, power, level, cost, soul, feature, status,
                          counter)

    def permanentEffect(self, player1, player2, position):
        def limit():
            return True

        def increaseEffect():
            return player1.MYFIELD["Stage"].countLevel(player1, (0,)) * 500

        def decreaseEffect():
            return 1

        player1.permanentEffect.adaptField(
            player1, player2, (player1, position), [(player1, position)],
            [limit], [("increasePower", increaseEffect)]
        )
        player1.permanentEffect.adaptField(
            player1, player2, (player1, position), [(player1, position)],
            [limit], [("decreaseLevel", decreaseEffect)]
        )


class W46_109(CX):
    def __init__(self, player=None, name="出会いの一冊", color=util.Color.BLUE, cardType=util.CardType.CX,
                 trigger=(util.TriggerType.SOUL_TWO,),
                 effect=None):
        super().__init__(player, name, color, cardType, trigger, effect)

    def permanentEffect(self, player):
        color_flag = False
        for card in player.MYFIELD["Waiting_Room"]:
            if card.color == util.Color.BLUE:
                color_flag = True
                break
        if color_flag is True:
            print("{} : 控室の青のカードを1枚ストックに置く".format(self.name))
            flag = util.effectConfirm()
            if flag == 1:
                player.MYFIELD["Waiting_Room"].showWaitingRoom()
                while True:
                    select_card = util.selectNumberChecker(1, len(player.MYFIELD["Waiting_Room"]), "カードを選んでください : ")
                    if player.MYFIELD["Waiting_Room"][select_card - 1].color == util.Color.BLUE:
                        player.MYFIELD["Stock"].append(player.MYFIELD["Waiting_Room"].pop(select_card - 1))
                        break
                    else:
                        print("青のカードを選んで下さい")

        print("{} : 自分のキャラすべてのソウルを+1".format(self.name))
        for i in range(5):
            if len(player.MYFIELD["Stage"][i]) != 0:
                player.MYFIELD["Stage"][i][0].soul += 1
                print("{} に効果を使いました".format(player.MYFIELD["Stage"][i][0].name))
                print("パワー : {}".format(player.MYFIELD["Stage"][i][0].power))
                print("ソウル : {}".format(player.MYFIELD["Stage"][i][0].soul))
        return [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
