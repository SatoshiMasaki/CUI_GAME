import random
from collections import OrderedDict, UserList
import util
import deckRecipe
import cardEffect
import time
import sys
import re


# TODO : 情報コマンドの改善


class Deck(UserList):
    def __init__(self):
        super().__init__()
        self.data = []

    def createDeck(self, deckdata):
        for card in deckdata:
            self.data.append(card)

    def turnOver(self, player1, *index):
        if len(index) != 0:
            player1.MYFIELD["Event_Zone"].append(self.data.pop(index[0]))
        else:
            player1.MYFIELD["Event_Zone"].append(self.data.pop(0))

        if len(self.data) == 0:
            player1.refrash()

    def draw(self, player):
        print("引いたカード : ", self.data[0].name)
        time.sleep(1)
        player.MYFIELD["Hand"].append(self.data.pop(0))
        if len(self.data) == 0:
            player.refrash()

    def shuffle(self):
        print("シャッフルします")
        temp_list = []

            temp_list.append(self.data.pop())
        for card in random.sample(temp_list, len(temp_list)):
            self.data.append(card)
        print("デッキ枚数 : {}枚".format(len(self.data)))

    def showDeck(self):
        for i, card in enumerate(self.data):
            print("{} : {}".format(i + 1, card.name))


class Stage(UserList):
    def __init__(self, initlist=None):
        super().__init__(initlist)
        self.data = []
        for i in range(5):
            self.data.append([])

    def appearanceChara(self, player1, player2, position, useCard):
        self.data[position].append(useCard)
        if hasattr(player1.MYFIELD["Stage"][position][0], "permanentEffect"):
            player1.MYFIELD["Stage"][position][0].permanentEffect(player1, player2, position)
        player1.permanentEffect.adaptCharactor(player1, player2, position)
        if hasattr(player1.MYFIELD["Stage"][position][0], "cipEffect"):
            player1.MYFIELD["Stage"][position][0].cipEffect(player1, player2, position)

    def leaveStageChara(self, player1, player2, existCharaPosition, moveToPosition):
        player1.permanentEffect.exitCharaSolve(player1, player2, existCharaPosition)
        player1.untilTurnEndEffect.exitCharaSolve(player1, player2, existCharaPosition)
        moveToPosition.append(player1.MYFIELD["Stage"][existCharaPosition].pop())

    def moveChara(self, player1, player2, beforePosition, afterPosition):
        self.leaveStageChara(player1, player2, beforePosition, player1.MYFIELD["Stage"][afterPosition])

    def countFeature(self, player1, feature):
        """

        :param player1:
        :param feature: 検索したい特徴をタプルで渡す
        :return:
        """
        countFeature = 0
        for i in range(5):
            for feat in feature:
                if player1.charaExistCheck(i):
                    if feat in player1.MYFIELD["Stage"][i][0].feature:
                        countFeature += 1
                        break
        return countFeature

    def countLevel(self, player1, level):
        """
        :param player1: 手番のプレイヤー
        :param level: 検索したいレベルをタプルで渡す
        :return:
        """
        countLevel = 0
        for i in range(5):
            for levels in level:
                if player1.charaExistCheck(i):
                    if player1.MYFIELD["Stage"][i][0].level == levels:
                        countLevel += 1
                        break
        return countLevel

    def searchName(self, player1, name):
        name = re.compile(".*{}.*".format(name))
        for i in range(5):
            if player1.charaExistCheck(i) and name.match(player1.MYFIELD["Stage"][i][0].name):
                return True
        return False

    def searchFeature(self, player1, feature):
        for i in range(5):
            if player1.charaExistCheck(i) and feature in player1.MYFIELD["Stage"][i][0].feature:
                return True
        return False

    def showStage(self):
        for i, stagelabel in enumerate(util.stageLabel):
            if len(self.data[i]) == 1:
                print("{} : {} {}".format(i + 1, stagelabel, self.data[i][0].name))
                print("レベル : {}".format(self.data[i][0].level))
                print("パワー : {}".format(self.data[i][0].power))
                print("ステータス : {}".format(self.data[i][0].status))
            else:
                print("{} : {} {}".format(i + 1, stagelabel, "なし"))

    def oppositePosition(self, position):
        if position == 1:
            return 3
        elif position == 2:
            return 2
        elif position == 3:
            return 1
        else:
            util.debug("oppositePositionでエラーがはっせいしました")
            print(position)

    def statusToStand(self, position):
        self.data[position][0].status = util.Status.STAND

    def statusToRest(self, position):
        self.data[position][0].status = util.Status.REST

    def statusToReverse(self, position):
        self.data[position][0].status = util.Status.REVERSE


class Clock(UserList):
    def __init__(self, initlist=None):
        super().__init__(initlist)
        self.data = []

    def levelCheck(self):
        if len(self.data) >= 7:
            pass

    def clockCount(self):
        print("クロック数 : ", len(self.data))

    def showClock(self):
        for i, card in enumerate(self.data):
            print("{} : {}".format(i + 1, card.name))

    def appendClock(self, player1, card):
        self.data.append(card)
        if len(self.data) >= 7:
            player1.levelUp()


class Level(UserList):
    def __init__(self, initlist=None):
        super().__init__(initlist)
        self.data = []

    def levelCount(self):
        print("レベル : ", len(self.data))

    def showLevel(self):
        for i, card in enumerate(self.data):
            print("{} : {}".format(i + 1, card.name))


class Stock(UserList):
    def __init__(self, initlist=None):
        super().__init__(initlist)
        self.data = []

    def costCheck(self, stockLength):
        if len(self.data) >= stockLength:
            return True
        else:
            print("コストが足りません")
            return False

    def stockUnderNumber(self, stockLength):
        if len(self.data) < stockLength:
            return True
        else:
            return False

    def stockCount(self):
        print("ストック数 : ", len(self.data))


class WaitingRoom(UserList):
    def __init__(self, initlist=None):
        super().__init__(initlist)
        self.data = []

    def waitingRoomsCXCount(self):
        cx_count = 0
        for card in self.data:
            if card.cardType == util.CardType.CX:
                cx_count += 1
        print("CXの枚数 : ", cx_count)

    def showWaitingRoom(self):
        for i, card in enumerate(self.data):
            print("{} : {}".format(i + 1, card.name))


class Memory(UserList):
    def __init__(self, initlist=None):
        super().__init__(initlist)
        self.data = []


class Hand(UserList):
    def __init__(self, initlist=None):
        super().__init__(initlist)
        self.data = []

    def showHand(self):
        self.data = util.sortCardList(self.data)
        for i, card in enumerate(self.data):
            print("{} : {}".format(i + 1, card.name))

    def existCXCheck(self):
        flag = False
        for card in self.data:
            if card.cardType == util.CardType.CX:
                flag = True
                break
        return flag


class CX(UserList):
    def __init__(self, initlist=None):
        super().__init__(initlist)
        self.data = []


class EventZone(UserList):
    def __init__(self, initlist=None):
        super().__init__(initlist)
        self.data = []


class WeisField:
    def __init__(self, permanentEffect, untilTurnEndEffect, _cardEffect):
        self.MYFIELD = OrderedDict()
        self.MYFIELD["Deck"] = Deck()
        self.MYFIELD["Stage"] = Stage()
        self.MYFIELD["Clock"] = Clock()
        self.MYFIELD["Level"] = Level()
        self.MYFIELD["Stock"] = Stock()
        self.MYFIELD["Waiting_Room"] = WaitingRoom()
        self.MYFIELD["Memory"] = Memory()
        self.MYFIELD["Hand"] = Hand()
        self.MYFIELD["CX"] = CX()
        self.MYFIELD["Event_Zone"] = EventZone()

        self.level = 0
        self.standCount = 0
        self.canUseRed = False
        self.canUseBlue = False
        self.canUseGreen = False
        self.canUseYellow = False
        self.MAIN_DECK = None
        self.cxConf = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]  # パワー→ソウル
        self.cardEffect = _cardEffect
        self.permanentEffect = permanentEffect
        self.untilTurnEndEffect = untilTurnEndEffect
        self.turnPlayer = False
        self.numberOfTurns = 0

    def useCardCheck(self, card):
        if card.level > self.level:
            print("レベルが足りません")
            return False
        elif card.cost > len(self.MYFIELD["Stock"]):
            print("ストックが足りません")
            print("----------")
            return False
        elif card.level != 0 and self.oneColorCheck(
                card.color) is False:
            print("色が足りません")
            print("このカードは {} です".format(card.color))
            print("----------")
            return False
        else:
            return True

    def fullColorCheck(self):
        canUseColor = []
        for flagColor in [util.Color.YELLOW, util.Color.GREEN, util.Color.RED, util.Color.BLUE]:
            if len(self.MYFIELD["Level"]) != 0:
                for levelsCard in self.MYFIELD["Level"]:
                    if levelsCard.color == flagColor:
                        canUseColor.append(flagColor)
                        break

            if len(self.MYFIELD["Clock"]) != 0:
                for stocksCard in self.MYFIELD["Clock"]:
                    if stocksCard.color == flagColor:
                        canUseColor.append(flagColor)
                        break
        if util.Color.YELLOW in canUseColor:
            self.canUseYellow = True
            print("黄色 : 使えます")
        else:
            self.canUseYellow = False
            print("黄色 : 使えません")
        if util.Color.GREEN in canUseColor:
            self.canUseGreen = True
            print("緑 : 使えます")
        else:
            self.canUseGreen = False
            print("緑 : 使えません")
        if util.Color.RED in canUseColor:
            self.canUseRed = True
            print("赤 : 使えます")
        else:
            self.canUseRed = False
            print("赤 : 使えません")
        if util.Color.BLUE in canUseColor:
            self.canUseBlue = True
            print("青 : 使えます")
        else:
            self.canUseBlue = False
            print("青 : 使えません")

    # 特定の一色についての確認
    def oneColorCheck(self, color):
        if color is util.Color.YELLOW:
            return self.canUseYellow
        if color is util.Color.GREEN:
            return self.canUseGreen
        if color is util.Color.RED:
            return self.canUseRed
        if color is util.Color.BLUE:
            return self.canUseBlue

    def useCost(self, cost):
        if cost == 0:
            pass
        else:
            for i in range(cost):
                self.MYFIELD["Waiting_Room"].append(self.MYFIELD["Stock"].pop())
                print("コストを使用しました")
                util.soundMp3("decision1")

    def triggerCheck(self, attackSoul, player1):
        print("----------")
        print("トリガーチェック")
        print(self.MYFIELD["Deck"][0].name)
        self.MYFIELD["Deck"].turnOver(player1)
        if len(self.MYFIELD["Event_Zone"][0].trigger) == 0:
            print("トリガーはありません")
            self.MYFIELD["Stock"].append(self.MYFIELD["Event_Zone"].pop())
            return attackSoul
        elif len(self.MYFIELD["Event_Zone"][0].trigger) == 1 and \
                util.TriggerType.SOUL_TWO in self.MYFIELD["Event_Zone"][0].trigger:
            self.MYFIELD["Stock"].append(self.MYFIELD["Event_Zone"].pop())
            return attackSoul + 2
        elif len(self.MYFIELD["Event_Zone"][0].trigger) == 1 and \
                util.TriggerType.SOUL_ONE in self.MYFIELD["Event_Zone"][0].trigger:
            self.MYFIELD["Stock"].append(self.MYFIELD["Event_Zone"].pop())
            return attackSoul + 1
        elif util.TriggerType.GATE in self.MYFIELD["Event_Zone"][0].trigger:
            if util.TriggerType.SOUL_ONE in self.MYFIELD["Event_Zone"][0].trigger:
                player1.cardEffect.utilEffect.salvageChara()
                self.MYFIELD["Stock"].append(self.MYFIELD["Event_Zone"].pop())
                return attackSoul + 1
            else:
                self.cardEffect.utilEffect.salgvageCard(player1, None, util.CardType.CHARA)
                self.MYFIELD["Stock"].append(self.MYFIELD["Event_Zone"].pop())
                return attackSoul
        elif util.TriggerType.BOOK in self.MYFIELD["Event_Zone"][0].trigger:
            if util.TriggerType.SOUL_ONE in self.MYFIELD["Event_Zone"][0].trigger:
                self.MYFIELD["Deck"].draw(self)
                self.MYFIELD["Stock"].append(self.MYFIELD["Event_Zone"].pop())
                return attackSoul + 1
            else:
                self.MYFIELD["Deck"].draw(self)
                self.MYFIELD["Stock"].append(self.MYFIELD["Event_Zone"].pop())
                return attackSoul
        elif util.TriggerType.TREASURE in self.MYFIELD["Event_Zone"][0].trigger:
            if util.TriggerType.SOUL_ONE in self.MYFIELD["Event_Zone"][0].trigger:
                print("宝トリガーの効果を使います")
                self.MYFIELD["Hand"].append(self.MYFIELD["Event_Zone"].pop())
                self.MYFIELD["Deck"].turnOver(player1)
                self.MYFIELD["Stock"].append(self.MYFIELD["Event_Zone"].pop())
                return attackSoul + 1
            else:
                return attackSoul
        else:
            pass
        # TODO : トリガーの追加
        # elif self.MYFIELD["Event_Zone"][0].trigger in util.TriggerType.WIND:
        #     if self.MYFIELD["Event_Zone"][0].trigger in util.TriggerType.SOUL_ONE:
        #         pass
        #     else:
        #         pass
        # elif self.MYFIELD["Event_Zone"][0].trigger in util.TriggerType.POOL:
        #     if self.MYFIELD["Event_Zone"][0].trigger in util.TriggerType.SOUL_ONE:
        #         pass
        #     else:
        #         pass
        # elif self.MYFIELD["Event_Zone"][0].trigger in util.TriggerType.SHOT:
        #     if self.MYFIELD["Event_Zone"][0].trigger in util.TriggerType.SOUL_ONE:
        #         pass
        #     else:
        #         pass
        # elif self.MYFIELD["Event_Zone"][0].trigger in util.TriggerType.STANDBY:
        #     if self.MYFIELD["Event_Zone"][0].trigger in util.TriggerType.SOUL_ONE:
        #         pass
        #     else:
        #         pass

        self.MYFIELD["Stock"].append(self.MYFIELD["Event_Zone"].pop())

    def damage_check(self, damage):
        print("----------")
        print("ダメージチェック : ", "{}点".format(damage))
        time.sleep(0.5)

        cancel_conf = False
        for i in range(damage):
            if cancel_conf:
                break
            self.MYFIELD["Deck"].turnOver(self)
            print(self.MYFIELD["Event_Zone"][i].name)
            time.sleep(0.5)
            if self.MYFIELD["Event_Zone"][i].cardType == util.CardType.CX:
                print("キャンセルが発生しました")
                time.sleep(0.5)
                # カードを控室へ
                while True:
                    if len(self.MYFIELD["Event_Zone"]) != 0:
                        self.MYFIELD["Waiting_Room"].append(self.MYFIELD["Event_Zone"].pop())
                    else:
                        cancel_conf = True
                        break
            else:
                pass

        if len(self.MYFIELD["Event_Zone"]) != 0:
            print("ダメージが通りました")
            time.sleep(0.5)
            while True:
                if len(self.MYFIELD["Event_Zone"]) != 0:
                    self.MYFIELD["Clock"].append(self.MYFIELD["Event_Zone"].pop(0))
                else:
                    break

            if 7 <= len(self.MYFIELD["Clock"]):
                self.levelUp()

    def charaExistCheck(self, position):
        if len(self.MYFIELD["Stage"][position]) == 0:
            return False
        else:
            return True

    def charaStatusCheck(self, position, status):
        if status == util.Status.STAND:
            if self.charaExistCheck(position):
                if self.MYFIELD["Stage"][position][0].status == util.Status.STAND:
                    return True
                else:
                    return False
        elif status == util.Status.REST:
            if self.charaExistCheck(position):
                if self.MYFIELD["Stage"][position][0].status == util.Status.REST:
                    return True
                else:
                    return False
        elif status == util.Status.REVERSE:
            if self.charaExistCheck(position):
                if self.MYFIELD["Stage"][position][0].status == util.Status.REVERSE:
                    return True
                else:
                    return False

    def levelUp(self):
        for i, card in enumerate(self.MYFIELD["Clock"]):
            if i == 7:
                break
            print("{} : {}".format(i + 1, card.name))
        select_number = util.selectNumberChecker(1, 7, "レベル置き場に置くカードを選んでください") - 1
        self.MYFIELD["Level"].append(self.MYFIELD["Clock"].pop(select_number))
        for i in range(6):
            self.MYFIELD["Waiting_Room"].append(self.MYFIELD["Clock"].pop(0))
        self.level += 1
        if len(self.MYFIELD["Level"]) == 4:
            print("レベル４になりました。あなたの負けです")
            print("----------")
            sys.exit()

    def refrash(self):
        print("リフレッシュ処理を行います")
        for i in range(len((self.MYFIELD["Waiting_Room"]))):
            self.MYFIELD["Deck"].append(self.MYFIELD["Waiting_Room"].pop(0))
        self.MYFIELD["Deck"].shuffle()
        print("ペナルティの1点ダメージが入ります")
        self.MYFIELD["Clock"].append(self.MYFIELD["Deck"].pop(0))

    def useCounter(self, player1, player2, attacked_chara):
        can_counter = False
        for i, card in enumerate(self.MYFIELD["Hand"]):
            if card.cardType == util.CardType.CX:
                pass
            else:
                if card.counter is True:
                    if card.level > self.level:
                        pass
                    elif card.cost > len(self.MYFIELD["Stock"]):
                        pass
                    # elif card.level != 0 and self.oneColorCheck(card.color) is False:
                    #     pass
                    else:
                        can_counter = True
                    break
        if can_counter:
            self.MYFIELD["Hand"].showHand()
            print("{} : 助太刀を使わない".format(len(self.MYFIELD["Hand"]) + 1))
            while True:
                try:
                    select_card = int(input("カードを選んでください : "))
                    if util.varSizeChecker(1, len(self.MYFIELD["Hand"]) + 1, select_card):
                        if select_card == len(self.MYFIELD["Hand"]) + 1:
                            print("助太刀を使いません")
                            break
                        else:
                            if hasattr(self.MYFIELD["Hand"][select_card - 1], "counterEffect"):
                                # 助太刀を使う
                                self.MYFIELD["Hand"][select_card - 1].counterEffect(player1, player2, attacked_chara)
                                self.MYFIELD["Waiting_Room"].append(self.MYFIELD["Hand"].pop(select_card - 1))
                                break
                            else:
                                print("このカードは使えません")
                    else:
                        print("範囲内の数値を入力してください")
                except ValueError as err:
                    print(err)

    def handEncore(self):
        print("手札アンコールを使います")
        self.MYFIELD["Hand"].showHand()
        while True:
            number = util.selectNumberChecker(1, len(self.MYFIELD["Hand"]), "カードを選んでください")
            if self.MYFIELD["Hand"][number - 1].cardType == util.CardType.CHARA:
                self.MYFIELD["Waiting_Room"].append(self.MYFIELD["Hand"].pop(number - 1))
                break
            else:
                print("キャラカードを選んでください")

    def encore(self, player_name, player1, player2):
        """
            キャラの効果アンコールの関数名はeffectEncore
        """
        print("{}のプレイヤーの処理です".format(player_name))
        print("----------")
        for i in range(3):
            reverse_check = False

            if self.charaStatusCheck(i, util.Status.REVERSE):
                reverse_check = True

            if reverse_check:
                has_encore = False
                stock_encore = False
                while True:
                    if hasattr(self.MYFIELD["Stage"][i][0], "effectEncore"):
                        has_encore = True
                    elif self.MYFIELD["Stage"][i][0].appendEffect is not None and self.MYFIELD["Stage"][i][0].appendEffect.appendEffectLabel == "effectEncore":
                        has_encore = True

                    if len(self.MYFIELD["Stock"]) >= 3:
                        stock_encore = True

                    if has_encore == True and stock_encore == True:
                        print(self.MYFIELD["Stage"][i][0].name)
                        print("エフェクトアンコール : できる")
                        print("ストックアンコール : できる")
                        encoreYN = util.effectConfirm()

                        if encoreYN == 1:
                            encoreMeth = util.selectNumberChecker(1, 2,
                                                                   "アンコールの種類を選んでください \n"
                                                                   "1 : 特殊アンコール\n 2 : ストックアンコール")
                            if encoreMeth == 1:  # TODO : effectEncore()とappendEffect()の兼ね合い
                                if hasattr(self.MYFIELD["Stage"][i][0], "effectEncore"):
                                    self.MYFIELD["Stage"][i][0].encoreEffect(player1, player2, i)
                                elif self.MYFIELD["Stage"][i][0].appendEffect is not None and \
                                        self.MYFIELD["Stage"][i][0].appendEffect.appendEffectLabel == "effectEncore":
                                    self.MYFIELD["Stage"][i][0].appendEffect.appendEffect(player1, player2, i)
                                self.MYFIELD["Stage"][i][0].status = util.Status.REST
                                break
                            elif encoreMeth == 2:
                                self.useCost(3)
                                self.MYFIELD["Stage"][i][0].status = util.Status.REST
                                break
                            else:
                                print("範囲内の数値を選んでください")
                        elif encoreYN == 2:
                            break
                    elif has_encore is True:
                        print(self.MYFIELD["Stage"][i][0].name)
                        print("エフェクトアンコール : できる")
                        print("ストックアンコール : できない")
                        effectEncoreYN = util.selectNumberChecker(1, 2, "アンコールを使いますか？ \n1 : はい\n 2 : いいえ")

                        if effectEncoreYN == 1:
                            if hasattr(self.MYFIELD["Stage"][i][0], "effectEncore"):
                                self.MYFIELD["Stage"][i][0].encoreEffect(player1, player2, i)
                            elif self.MYFIELD["Stage"][i][0].appendEffect is not None and \
                                    self.MYFIELD["Stage"][i][0].appendEffect.appendEffectLabel == "effectEncore":
                                self.MYFIELD["Stage"][i][0].appendEffect.appendEffect(player1, player2, i)
                            self.MYFIELD["Stage"][i][0].status = util.Status.REST
                            break
                        elif effectEncoreYN == 2:
                            break
                        else:
                            print("範囲内の数値を入力してください")
                    elif stock_encore is True:
                        print(self.MYFIELD["Stage"][i][0].name)
                        print("エフェクトアンコール : できない")
                        print("ストックアンコール : できる")
                        stockEncoreYN = util.selectNumberChecker(1, 2, "アンコールを使いますか？ \n1 : はい\n 2 : いいえ")

                        if stockEncoreYN == 1:
                            self.useCost(3)
                            self.MYFIELD["Stage"][i][0].status = util.Status.REST

                            print("ストックアンコールをしました")
                            print("残りストック数 : {}".format(len(self.MYFIELD["Stock"])))
                            break
                        elif stockEncoreYN == 2:
                            break
                        else:
                            print("範囲内の数値を入力してください")
                    else:
                        break

        for i in range(3):
            if self.charaExistCheck(i):
                if self.MYFIELD["Stage"][i][0].status == util.Status.REVERSE:
                    self.MYFIELD["Stage"].leaveStageChara(player1, player2, i, self.MYFIELD["Waiting_Room"])


class GameController:
    @staticmethod
    def gameStartController(player1):
        print("1 : DC音楽\n2 : 杉並(緑)\n3 : テスト")
        deck_number = util.selectNumberChecker(1, 3, "使うデッキを選んでください")
        if deck_number == 1:
            MAIN_DECK = deckRecipe.DC_music(player1)

            player1.MYFIELD["Deck"].createDeck(random.sample(MAIN_DECK, len(MAIN_DECK)))
            for i in range(5):
                player1.MYFIELD["Hand"].append(player1.MYFIELD["Deck"].pop(0))
        if deck_number == 2:
            MAIN_DECK = deckRecipe.suginamiEncoreGreen(player1)

            player1.MYFIELD["Deck"].createDeck(random.sample(MAIN_DECK, len(MAIN_DECK)))
            for i in range(5):
                player1.MYFIELD["Hand"].append(player1.MYFIELD["Deck"].pop(0))
        if deck_number == 3:
            MAIN_DECK = deckRecipe.test(player1)

            player1.MYFIELD["Deck"].createDeck(random.sample(MAIN_DECK, len(MAIN_DECK)))
            for i in range(5):
                player1.MYFIELD["Hand"].append(player1.MYFIELD["Deck"].pop(0))

    @staticmethod
    def malligun(player1):
        print("マリガン :")
        count = 0
        while True:
            player1.MYFIELD["Hand"].showHand()
            select_number = util.selectNumberChecker(1, len(player1.MYFIELD["Hand"]), "捨てるカードを選んでください :",
                                                      "マリガンフェイズを終了します")
            if select_number == len(player1.MYFIELD["Hand"]) + 1:
                print("マリガンフェイズを終了します")
                print("-----")
                break
            else:
                player1.MYFIELD["Waiting_Room"].append(player1.MYFIELD["Hand"].pop(select_number - 1))
                print("----------")
                count += 1

        for i in range(count):
            player1.MYFIELD["Deck"].draw(player1)
        print("----------")
        print("手札 : ")
        player1.MYFIELD["Hand"].showHand()
        print("----------")
        time.sleep(1)

    # 各フェイズの定義
    @staticmethod
    def standPhase(player1, player2):
        player1.numberOfTurns += 1
        print("{} ターン目".format(player1.numberOfTurns))
        print("----------")
        player1.turnPlayer = True

        for i in range(5):
            if player1.charaExistCheck(i) and hasattr(player1.MYFIELD["Stage"][i][0], "turnStartEffect"):
                player1.MYFIELD["Stage"][i][0].turnStartEffect(player1, player2, i)

        for i in range(5):
            if player2.charaExistCheck(i) and hasattr(player2.MYFIELD["Stage"][i][0], "turnStartEffect"):
                player2.MYFIELD["Stage"][i][0].turnStartEffect(player2, player1, i)
        print("スタンドフェイズ")
        print("----------")

        for i in range(5):
            if player1.charaStatusCheck(i, util.Status.REST):
                player1.MYFIELD["Stage"].statusToStand(i)

    @staticmethod
    def drawPhase(player1):
        print("ドローフェイズ")
        print("----------")
        player1.MYFIELD["Deck"].draw(player1)
        print("----------")

    @staticmethod
    def clockPhase(player1):
        print("クロックフェイズ")
        print("----------")
        player1.MYFIELD["Hand"].showHand()
        print("{} : クロックフェイズを終了する".format(len(player1.MYFIELD["Hand"]) + 1))
        while True:
            try:
                select_number = int(input("カードを選んでください : "))
                print("----------")
                if select_number == len(player1.MYFIELD["Hand"]) + 1:
                    print("クロックフェイズを終了します")
                    print("----------")
                    break
                elif 1 <= select_number <= len(player1.MYFIELD["Hand"]) + 1:
                    player1.MYFIELD["Clock"].append(player1.MYFIELD["Hand"].pop(select_number - 1))
                    if len(player1.MYFIELD["Clock"]) >= 7:
                        player1.levelUp()
                    for i in range(2):
                        player1.MYFIELD["Deck"].draw(player1)
                    player1.MYFIELD["Hand"].showHand()
                    print("----------")
                    break
                else:
                    print("範囲内の数値を入力してください")
            except TypeError:
                print("数値を入力してください")
        print("クロック数 : ", len(player1.MYFIELD["Clock"]))
        print("----------")
        print("色判定")
        player1.fullColorCheck()
        print("----------")

    @staticmethod
    def cxPhase(player1, player2):
        def charasCXEffect(useCard):
            for i in range(5):
                if player1.charaExistCheck(i):
                    if hasattr(player1.MYFIELD["Stage"][i][0], "useCX"):
                        player1.MYFIELD["Stage"][i][0].useCX(player1, player2, i)
                    if hasattr(player1.MYFIELD["Stage"][i][0], "CXcombo"):
                        player1.MYFIELD["Stage"][i][0].CXcombo(player1, player2, i, useCard)

            for i in range(5):
                if player2.charaExistCheck(i):
                    if hasattr(player2.MYFIELD["Stage"][i][0], "useCX"):
                        player2.MYFIELD["Stage"][i][0].useCX(player2, player1, i)

        # スキップ処理
        CXcount = False
        if len(player1.MYFIELD["Hand"]) == 0:
            print("クライマックスフェイズをスキップします")
        else:
            for card in player1.MYFIELD["Hand"]:
                if card.cardType == util.CardType.CX:
                    CXcount = True
                    break
            if CXcount:
                print("クライマックスフェイズ")
                print("----------")
                player1.MYFIELD["Hand"].showHand()
                print("{} : クライマックスフェイズを終了する".format(len(player1.MYFIELD["Hand"]) + 1))
                finish = False
                while True:
                    if finish is True:
                        break
                    try:
                        select_number = util.selectNumberChecker(1, len(player1.MYFIELD["Hand"]) + 1, "カードを選んでください")
                        if select_number == len(player1.MYFIELD["Hand"]) + 1:
                            print("クライマックスフェイズを終了します")
                            print("----------")
                            break
                        else:
                            if player1.MYFIELD["Hand"][select_number - 1].cardType == util.CardType.CX:
                                player1.MYFIELD["CX"].append(player1.MYFIELD["Hand"].pop(select_number - 1))
                                player1.cxConf = player1.MYFIELD["CX"][0].permanentEffect(player1)
                                charasCXEffect(player1.MYFIELD["CX"][0])
                                finish = True
                                break
                            else:
                                print("このカードはCXではありません")
                    except Exception as err:
                        print(err)
            else:
                print("クライマックスフェイズをスキップします")
                print("----------")

    @staticmethod
    def endPhase(player1, player2):
        print("エンドフェイズ")
        print("----------")
        print("player1の処理です")
        print("----------")

        if player1.untilTurnEndEffect.flag is True:
            print("ターンエンド時の効果解決")
            player1.untilTurnEndEffect.turnEndSolve(player1, player2)

        if len(player1.MYFIELD["CX"]) == 1:
            player1.MYFIELD["Waiting_Room"].append(player1.MYFIELD["CX"].pop())
            for i, powerList in enumerate(player1.cxConf[0]):
                if player1.charaExistCheck(i):
                    player1.MYFIELD["Stage"][i][0].power -= powerList
            for i, soulList in enumerate(player1.cxConf[1]):
                if player1.charaExistCheck(i):
                    player1.MYFIELD["Stage"][i][0].soul -= soulList

        for i in range(5):
            if player1.charaStatusCheck(i, util.Status.REVERSE):
                player1.MYFIELD["Waiting_Room"].append(player1.MYFIELD["Stage"][i].pop())
        while True:
            if len(player1.MYFIELD["Hand"]) > 7:
                print("手札が{}枚です。捨てるカードを選んでください".format(len(player1.MYFIELD["Hand"])))
                player1.MYFIELD["Hand"].showHand()
                select_card = int(input(("手札が{}枚です。捨てるカードを選んでください".format(len(player1.MYFIELD["Hand"])))))
                if util.varSizeChecker(1, len(player1.MYFIELD["Hand"]), select_card):
                    player1.MYFIELD["Waiting_Room"].append(player1.MYFIELD["Hand"].pop(select_card - 1))
                else:
                    print("範囲内の数値を入力してください")
            else:
                break

        print("player2の処理です")
        print("----------")
        for i in range(5):
            if player2.charaStatusCheck(i, util.Status.REVERSE):
                player2.MYFIELD["Waiting_Room"].append(player2.MYFIELD["Stage"][i].pop())

            else:
                break
        print("----------")

        player1.turnPlayer = False

    @staticmethod
    def mainPhase(player1, player2):
        def useChara(useCard: object):
            if hasattr(useCard, "inHandEffect"):
                flag = util.effectConfirm()
                if flag == 1:
                    useCard.inHandEffect(player1, player2)
                    player1.MYFIELD["Hand"].append(useCard)
                else:
                    if useCard.useCardLimit is True and useCard.cardLimit() is False:
                        player1.MYFIELD["Hand"].append(useCard)
                    else:
                        if player1.useCardCheck(useCard):
                            player1.MYFIELD["Stage"].showStage()
                            select_field = util.selectNumberChecker(1, 5, "キャラを出す枠を選んでください")
                            if len(player1.MYFIELD["Stage"][select_field - 1]) == 0:
                                player1.useCost(useCard.cost)
                                player1.MYFIELD["Stage"].appearanceChara(player1, player2, select_field - 1, useCard)
                            else:
                                update_stage = util.selectNumberChecker(1, 2, "{}を控室に送りますか？".format(
                                    player1.MYFIELD["Stage"][select_field - 1][0].name))
                                if update_stage == 1:
                                    player1.useCost(useCard.cost)
                                    player1.MYFIELD["Waiting_Room"].append(
                                        player1.MYFIELD["Stage"][select_field - 1].pop())
                                    player1.MYFIELD["Stage"].appearanceChara(player1, player2, select_field - 1,
                                                                              useCard)
                                elif update_stage == 2:
                                    player1.MYFIELD["Hand"].append(useCard)
                        else:
                            player1.MYFIELD["Hand"].append(useCard)
            else:
                if player1.useCardCheck(useCard):
                    player1.MYFIELD["Stage"].showStage()
                    select_field = util.selectNumberChecker(1, 5, "キャラを出す枠を選んでください")
                    if len(player1.MYFIELD["Stage"][select_field - 1]) == 0:
                        player1.useCost(useCard.cost)
                        player1.MYFIELD["Stage"].appearanceChara(player1, player2, select_field - 1, useCard)
                    else:
                        update_stage = util.selectNumberChecker(1, 2, "{}を控室に送りますか？".format(
                            player1.MYFIELD["Stage"][select_field - 1][0].name))
                        if update_stage == 1:
                            player1.useCost(useCard.cost)
                            player1.MYFIELD["Waiting_Room"].append(player1.MYFIELD["Stage"][select_field - 1].pop())
                            player1.MYFIELD["Stage"].appearanceChara(player1, player2, select_field - 1, useCard)
                        elif update_stage == 2:
                            player1.MYFIELD["Hand"].append(useCard)
                else:
                    player1.MYFIELD["Hand"].append(useCard)

        def useStartUpEffect():
            player1.MYFIELD["Stage"].showStage()
            select_card = util.selectNumberChecker(1, 5, "舞台のカードを選んでください")
            if player1.charaExistCheck(select_card - 1) and hasattr(
                    player1.MYFIELD["Stage"][select_card - 1][0], "startUpEffect"):
                player1.MYFIELD["Stage"][select_card - 1][0].startUpEffect(player1, player2, select_card - 1)

        def useEvent(useCard):
            if player1.useCardCheck(useCard) is True:
                if useCard.useCardLimit is True and useCard.cardLimit(player1, player2) is False:
                    player1.MYFIELD["Hand"].append(useCard)
                else:
                    player1.useCost(useCard.cost)
                    player1.MYFIELD["Event_Zone"].append(useCard)
                    player1.MYFIELD["Event_Zone"][0].autoEffect(player1, player2)
                    player1.MYFIELD["Waiting_Room"].append(player1.MYFIELD["Event_Zone"].pop())
            else:
                player1.MYFIELD["Hand"].append(useCard)

        def useHand():
            player1.MYFIELD["Hand"].showHand()
            select_hand = util.selectNumberChecker(1, len(player1.MYFIELD["Hand"]), "カードを選んでください : ", "戻る")
            if select_hand == len(player1.MYFIELD["Hand"]) + 1:
                pass
            else:
                useCard = player1.MYFIELD["Hand"].pop(select_hand - 1)
                if useCard.cardType == util.CardType.CHARA:
                    useChara(useCard)
                if useCard.cardType == util.CardType.EVENT:
                    useEvent(useCard)
                if useCard.cardType == util.CardType.CX:
                    print("CXカードは使えません")
                    player1.MYFIELD["Hand"].append(useCard)

        def exChangeField():
            player1.MYFIELD["Stage"].showStage()

            before_position = util.selectNumberChecker(1, 5, "移動させるキャラを選んでください : ")
            after_position = util.selectNumberChecker(1, 5, "移動先を選んでください : ")

            if player1.charaExistCheck(before_position - 1):
                if player1.charaExistCheck(after_position - 1):
                    if before_position == after_position:
                        pass
                    else:
                        container = []
                        player1.MYFIELD["Stage"].leaveStageChara(player1, player2, before_position - 1, container)
                        player1.MYFIELD["Stage"].leaveStageChara(player1, player2, after_position - 1, container)

                        player1.MYFIELD["Stage"][after_position - 1].append(container.pop(0))
                        if hasattr(player1.MYFIELD["Stage"][after_position - 1][0], "permanentEffect"):
                            player1.MYFIELD["Stage"][after_position - 1][0].permanentEffect(player1, player2, after_position - 1)
                        player1.permanentEffect.adaptCharactor(player1, player2, after_position - 1)

                        player1.MYFIELD["Stage"][before_position - 1].append(container.pop(0))
                        if hasattr(player1.MYFIELD["Stage"][after_position - 1][0], "permanentEffect"):
                            player1.MYFIELD["Stage"][after_position - 1][0].permanentEffect(player1, player2, after_position - 1)
                        player1.permanentEffect.adaptCharactor(player1, player2, before_position - 1)
                else:
                    container = []
                    player1.MYFIELD["Stage"].leaveStageChara(player1, player2, before_position - 1, container)
                    player1.MYFIELD["Stage"][after_position - 1].append(container.pop())
                    if hasattr(player1.MYFIELD["Stage"][after_position - 1][0], "permanentEffect"):
                        player1.MYFIELD["Stage"][after_position - 1][0].permanentEffect(player1, player2, after_position - 1)
                    player1.permanentEffect.adaptCharactor(player1, player2, after_position - 1)
            else:
                print("キャラがいません")

        def checkField():
            select_player = util.selectNumberChecker(1, 2, "1 : 自分の場\n2 : 相手の場\n見たいプレイヤーを選んでください")
            print("----------")
            if select_player == 1:
                player1.MYFIELD["Stage"].showStage()
                player1.MYFIELD["Level"].levelCount()
                player1.MYFIELD["Level"].showLevel()
                player1.MYFIELD["Clock"].clockCount()
                player1.MYFIELD["Clock"].showClock()
                player1.MYFIELD["Stock"].stockCount()
                player1.fullColorCheck()
                player1.MYFIELD["Waiting_Room"].waitingRoomsCXCount()
                print("\n1 : 舞台のキャラの起動効果を使う\n2 : 舞台のキャラを入れ替える\n3 : 戻る")
                _select_number = util.selectNumberChecker(1, 3, "行動を選択してください ")
                if _select_number == 1:
                    useStartUpEffect()
                elif _select_number == 2:
                    exChangeField()
                elif _select_number == 3:
                    pass
            elif select_player == 2:
                player2.MYFIELD["Stage"].showStage()
                player2.MYFIELD["Level"].levelCount()
                player2.MYFIELD["Clock"].clockCount()
                player2.MYFIELD["Stock"].stockCount()
                player2.MYFIELD["Waiting_Room"].waitingRoomsCXCount()

        # 処理部分
        print("メインフェイズ")
        print("-----------")
        while True:
            main_phase_behaivor = "1 : 手札を使う\n2 : 場を確認する\n3 : メインフェイズを終了する"
            select_number = util.selectNumberChecker(1, 3, main_phase_behaivor)
            print("----------")

            if select_number == 1:
                useHand()
            elif select_number == 2:
                checkField()
            elif select_number == 3:
                print("メインフェイズを終了します")
                print("----------")
                break

    @staticmethod
    def attackPhase(player1, player2): # TODO appendEffectのloseBattle
        def solveBattle(attack_Charactor, attacked_Charactor):
            if player1.MYFIELD["Stage"][attack_Charactor - 1][0].power < player2.MYFIELD["Stage"][
                attacked_Charactor - 1][0].power:
                player1.MYFIELD["Stage"].statusToReverse(attack_Charactor - 1)
                if hasattr(player2.MYFIELD["Stage"][attacked_Charactor - 1][0], "winBattle"):
                    player2.MYFIELD["Stage"][attacked_Charactor - 1][0].winBattle(
                        player2, player1, attacked_Charactor - 1, attack_Charactor - 1
                    )
                elif player2.MYFIELD["Stage"][attacked_Charactor - 1][0].appendEffect is not None:
                    if player2.MYFIELD["Stage"][attacked_Charactor - 1][0].appendEffect.appendEffectLabel == "winBattle":
                        player2.MYFIELD["Stage"][attacked_Charactor - 1][0].appendEffect.appendEffect(
                            player2, player1, attacked_Charactor - 1, attack_Charactor - 1
                        )
                if hasattr(player1.MYFIELD["Stage"][attack_Charactor - 1][0], "loseBattle"):
                    player1.MYFIELD["Stage"][attack_Charactor - 1][0].loseBattle(
                        player1, player2, attacselfPosition, oppositePositiontor - 1
                    )
            elif player1.MYFIELD["Stage"][attack_Charactor - 1][0].power > player2.MYFIELD["Stage"][
                attacked_Charactor - 1][0].power:
                player2.MYFIELD["Stage"].statusToReverse(attacked_Charactor - 1)
                if hasattr(player1.MYFIELD["Stage"][attack_Charactor - 1][0], "winBattle"):
                    player1.MYFIELD["Stage"][attack_Charactor - 1][0].winBattle(
                        player1, player2, attack_Charactor - 1, attacked_Charactor - 1
                    )
                elif player1.MYFIELD["Stage"][attack_Charactor - 1][0].appendEffect is not None:
                    if player1.MYFIELD["Stage"][attack_Charactor - 1][0].appendEffect.appendEffectLabel == "winBattle":
                        player1.MYFIELD["Stage"][attack_Charactor - 1][0].appendEffect.appendEffect(
                            player1, player2, attack_Charactor - 1, attacked_Charactor - 1
                        )
                if hasattr(player2.MYFIELD["Stage"][attacked_Charactor - 1][0], "loseBattle"):
                    player2.MYFIELD["Stage"][attacked_Charactor - 1][0].loseBattle(
                        player2, player1, attacked_Charactor - 1, attack_Charactor - 1
                    )
            elif player1.MYFIELD["Stage"][attack_Charactor - 1][0].power == player2.MYFIELD["Stage"][
                attacked_Charactor - 1][0].power:
                player1.MYFIELD["Stage"].statusToReverse(attack_Charactor - 1)
                player2.MYFIELD["Stage"].statusToReverse(attacked_Charactor - 1)
                if hasattr(player1.MYFIELD["Stage"][attack_Charactor - 1][0], "winBattle"):
                    player1.MYFIELD["Stage"][attack_Charactor - 1][0].winBattle(
                        player1, player2, attack_Charactor - 1, attacked_Charactor - 1
                    )
                elif player1.MYFIELD["Stage"][attack_Charactor - 1][0].appendEffect is not None:
                    if player1.MYFIELD["Stage"][attack_Charactor - 1][0].appendEffect.appendEffectLabel == "winBattle":
                        player1.MYFIELD["Stage"][attack_Charactor - 1][0].appendEffect.appendEffect(
                            player1, player2, attack_Charactor - 1, attacked_Charactor - 1
                        )
                if hasattr(player1.MYFIELD["Stage"][attack_Charactor - 1][0], "loseBattle"):
                    player1.MYFIELD["Stage"][attack_Charactor - 1][0].loseBattle(
                        player1, player2, attack_Charactor - 1, attacked_Charactor - 1
                    )
                if hasattr(player2.MYFIELD["Stage"][attacked_Charactor - 1][0], "winBattle"):
                    player2.MYFIELD["Stage"][attacked_Charactor - 1][0].winBattle(
                        player2, player1, attacked_Charactor - 1, attack_Charactor - 1
                    )
                elif player1.MYFIELD["Stage"][attacked_Charactor - 1][0].appendEffect is not None:
                    if player1.MYFIELD["Stage"][attacked_Charactor - 1][0].appendEffect.appendEffectLabel == "winBattle":
                        player1.MYFIELD["Stage"][attacked_Charactor - 1][0].appendEffect.appendEffect(
                            player2, player1, attacked_Charactor - 1, attack_Charactor - 1
                        )
                if hasattr(player2.MYFIELD["Stage"][attacked_Charactor - 1][0], "loseBattle"):
                    player2.MYFIELD["Stage"][attacked_Charactor - 1][0].loseBattle(
                        player2, player1, attacked_Charactor - 1, attack_Charactor - 1
                    )

        def selectAttackChara():
            try:
                standCharaCheck = [False, False, False]
                while True:
                    for index in range(3):
                        if player1.charaStatusCheck(index, util.Status.STAND):
                            standCharaCheck[index] = True
                    if True in standCharaCheck:
                        selectAttackCharaNumber = 1
                        for standLabel, attackLabel in zip(standCharaCheck, util.attackLabel):
                            if standLabel:
                                print("{} : {}".format(selectAttackCharaNumber, attackLabel))
                                selectAttackCharaNumber += 1

                        attackNumber = util.selectNumberChecker(1, selectAttackCharaNumber - 1, "どのキャラで攻撃しますか")
                        attackCount = 0

                        for ind, flag in enumerate(standCharaCheck):
                            if flag:
                                attackCount += 1
                            if attackCount == attackNumber:
                                attack_charactor = ind + 1
                                attacked_charactor = player1.MYFIELD["Stage"].oppositePosition(attack_charactor)
                                return attack_charactor, attacked_charactor
                    else:
                        break
            except Exception as err:
                print("攻撃キャラの選択に失敗しました")
                print(err)

        def selectAttackMethod(_attackCharactor, _attackedCharactor):
            try:
                # アタック宣言ステップ
                while True:
                    if player2.charaExistCheck(_attackedCharactor - 1) is False:
                        print("1 : ダイレクトアタック")
                        _attackMethod = 3
                        _attackSoul = player1.MYFIELD["Stage"][_attackCharactor - 1][0].soul + 1
                        player1.MYFIELD["Stage"].statusToRest(_attackCharactor - 1)
                        player1.standCount -= 1
                        return _attackSoul, _attackMethod
                    else:
                        while True:
                            print(player2.MYFIELD["Stage"][_attackedCharactor - 1][0].name)
                            print("1 : フロントアタック\n2 : サイドアタック")
                            _attackMethod = util.selectNumberChecker(1, 2, "攻撃方法を選んでください")
                            if _attackMethod == 1:
                                _attackSoul = player1.MYFIELD["Stage"][_attackCharactor - 1][0].soul
                                player1.MYFIELD["Stage"].statusToRest(_attackCharactor - 1)
                                player1.standCount -= 1
                                return _attackSoul, _attackMethod
                            if _attackMethod == 2:
                                _attackSoul = player1.MYFIELD["Stage"][_attackCharactor - 1][0].soul - \
                                             player2.MYFIELD["Stage"][_attackedCharactor - 1][0].level
                                if _attackSoul < 0:
                                    _attackSoul = 0
                                player1.MYFIELD["Stage"].statusToRest(_attackCharactor - 1)
                                player1.standCount -= 1
                                return _attackSoul, _attackMethod
            except Exception as err:
                print("攻撃方法の選択に失敗しました")
                print(err)

        player1.standCount = 0
        for i in range(5):
            if player1.charaExistCheck(i):
                if hasattr(player1.MYFIELD["Stage"][i][0], "startAttackPhase"):
                    player1.MYFIELD["Stage"][i][0].startAttackPhase(player1, player2, i)

        for i in range(5):
            if player2.charaExistCheck(i):
                if hasattr(player2.MYFIELD["Stage"][i][0], "startAttackPhase"):
                    player2.MYFIELD["Stage"][i][0].startAttackPhase(player2, player1, i)

        for i in range(3):
            if player1.charaStatusCheck(i, util.Status.STAND):
                player1.standCount += 1

        while True:
            if player1.standCount == 0:
                break
            attackCharactor, attackedCharactor = selectAttackChara()
            attackSoul, attackMethod = selectAttackMethod(attackCharactor, attackedCharactor)

            player1.permanentEffect.adjustEffect(player1, player2, attackCharactor - 1)
            if player2.charaExistCheck(attackedCharactor - 1):
                player2.permanentEffect.adjustEffect(player2, player1, attackedCharactor - 1)

            if hasattr(player1.MYFIELD["Stage"][attackCharactor - 1][0], "selfAttackTrigger"):
                player1.MYFIELD["Stage"][attackCharactor - 1][0].selfAttackTrigger(player1, player2,
                                                                                    attackCharactor - 1)
            elif player1.MYFIELD["Stage"][attackCharactor - 1][0].appendEffect is not None:
                if player1.MYFIELD["Stage"][attackCharactor - 1][0].appendEffect.appendEffectLabel == "selfAttackTrigger":
                    player1.MYFIELD["Stage"][attackCharactor - 1][0].appendEffect(player1, player2, attackCharactor - 1)

            for i in range(3):
                if i == attackCharactor - 1:
                    continue
                if player1.charaExistCheck(i) and hasattr(player1.MYFIELD["Stage"][i][0], "otherAttackTrigger"):
                    player1.MYFIELD["Stage"][i][0].otherAttackTrigger(player1, player2, i, attackedCharactor - 1)
                elif player1.charaExistCheck(i) and player1.MYFIELD["Stage"][i][0].appendEffect is not None:
                    if player1.MYFIELD["Stage"][i][0].appendEffect.appendEffectLabel == "otherAttackTrigger":
                        player1.MYFIELD["Stage"][i][0].appendEffect(player1, player2, i, attackedCharactor - 1)

            attackSoul = player1.triggerCheck(attackSoul, player1)
            if attackMethod == 1:
                player2.useCounter(player2, player1, attackedCharactor - 1)
            player2.damage_check(attackSoul)
            if attackMethod == 1:
                solveBattle(attackCharactor, attackedCharactor)
        print("アンコールステップ")
        print("----------")
        player1.encore("手番", player1, player2)
        player2.encore("相手番", player2, player1)
        print("アンコールステップを終了します")
        print("----------")


def main():
    print("ゲームを開始します")
    print("----------")
    permanentEffect = util.permanentEffectDict()
    untilTurnEndEffect = util.untilTurnEndEffect()
    cardEffect_ = cardEffect.cardEffect()
    util.soundMp3("nyu1")
    player1 = WeisField(permanentEffect, untilTurnEndEffect, cardEffect_)
    player2 = WeisField(permanentEffect, untilTurnEndEffect, cardEffect_)
    GameController.gameStartController(player1)
    GameController.gameStartController(player2)
    GameController.malligun(player1)
    GameController.malligun(player2)

    turnCounter = 1

    while True:
        print("player1のターンです")
        print("----------")
        GameController.standPhase(player1, player2)
        GameController.drawPhase(player1)
        GameController.clockPhase(player1)
        GameController.mainPhase(player1, player2)
        GameController.cxPhase(player1, player2)
        GameController.attackPhase(player1, player2)
        GameController.endPhase(player1, player2)

        print("player2のターンです")
        print("----------")
        GameController.standPhase(player2, player1)
        GameController.drawPhase(player2)
        GameController.clockPhase(player2)
        GameController.mainPhase(player2, player1)
        GameController.cxPhase(player2, player1)
        GameController.attackPhase(player2, player1)
        GameController.endPhase(player2, player1)
        turnCounter += 1


if __name__ == '__main__':
    main()
