from enum import Enum, IntEnum
import time
from collections import UserList
import re
import pygame
from mutagen.mp3 import MP3
from typing import NamedTuple


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


class CardType(IntEnum):
    CHARA = 1
    EVENT = 2
    CX = 3


class AttackType(IntEnum):
    FRONT = 1
    SIDE = 2
    DIRECT = 3


class Status(IntEnum):
    STAND = 1
    REST = 2
    REVERSE = 3


class TriggerType(IntEnum):
    SOUL_ONE = 1
    SOUL_TWO = 2
    GATE = 3
    BOOK = 4
    WIND = 5
    POOL = 6
    SHOT = 7
    TREASURE = 8
    STANDBY = 9


class EffectType(Enum):
    AUTO_EFFECT = 1
    STARTUP_EFFECT = 2
    CX_COMBO = 3
    COUNTER = 4


class Color(IntEnum):
    YELLOW = 1
    GREEN = 2
    RED = 3
    BLUE = 4


class EncoreType(IntEnum):
    Hand = 1
    Clock = 2


class AppendEffect(NamedTuple):
    appendEffect: object
    appendEffectLabel: str


class untilTurnEndEffect(UserList):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.pattern_increase = re.compile("increase.*")
        self.pattern_decrease = re.compile("decrease.*")
        self.pattern_append = re.compile("append.*")
        self.pattern_power = re.compile(".*Power")
        self.pattern_level = re.compile(".*Level")
        self.pattern_soul = re.compile(".*Soul")
        self.pattern_feature = re.compile(".*Feature")
        self.pattern_effect = re.compile(".*Effect")
        self.pattern_encore = re.compile(".*Encore.*")
        self.data = []

    def useEffect(self, useDict, player1, _, position):
        if self.pattern_increase.match(useDict["effect"][0]):
            if self.pattern_power.match(useDict["effect"][0]):
                player1.MYFIELD["Stage"][position][0].power += useDict["effect"][1]()
        elif self.pattern_decrease.match(useDict["effect"][0]):
            if self.pattern_power.match(useDict["effect"][0]):
                player1.MYFIELD["Stage"][position][0].power -= useDict["effect"][1]()
            if self.pattern_level.match(useDict["effect"][0]):
                player1.MYFIELD["Stage"][position][0].level -= useDict["effect"][1]()
        elif self.pattern_append.match(useDict["effect"][0]):
            if self.pattern_effect.match(useDict["effect"][0]):
                player1.MYFIELD["Stage"][position][0].appendEffect = AppendEffect(useDict["effect"][1], useDict["effect"][2])
                if self.pattern_encore.match(useDict["effect"][2]):
                    player1.MYFIELD["Stage"][position][0].hasEffectEncore = True

        useDict["targetInstance"] = useDict["target"][0].MYFIELD["Stage"][useDict["target"][1]][0]
        self.flag = True

    def recoveryEffect(self, useDict, player1, _, position):
        if self.pattern_increase.match(useDict["effect"][0]):
            if self.pattern_power.match(useDict["effect"][0]):
                player1.MYFIELD["Stage"][position][0].power -= useDict["effect"][1]()
        elif self.pattern_decrease.match(useDict["effect"][0]):
            if self.pattern_power.match(useDict["effect"][0]):
                player1.MYFIELD["Stage"][position][0].power += useDict["effect"][1]()
            if self.pattern_level.match(useDict["effect"][0]):
                player1.MYFIELD["Stage"][position][0].level += useDict["effect"][1]()
        elif self.pattern_append.match(useDict["effect"][0]):
            if self.pattern_effect.match(useDict["effect"][0]):
                player1.MYFIELD["Stage"][position][0].appendEffect = None
                if self.pattern_encore.match(useDict["effect"][2]):
                    player1.MYFIELD["Stage"][position][0].hasEffectEncore = False
        self.flag = False

    def adaptField(self, player1, player2, Influencer, targetPosition, limit, effect):
        """
        永続効果持ちのキャラをプレイしたときに、インスタンスから使用する関数
        :param player1: 手番のプレイヤーオブジェクト
        :param player2: 相手番のプレイヤーオブジェクト
        :param Influencer: 永続効果を持つキャラの(player, position)
        :param targetPosition: 永続効果の影響を受ける(player, position)のリスト
        :param limit: 永続効果が適応される条件の関数。player.MYFIELD[""]の関数
        :param effect: 永続効果の(effect_name, effect(), append_effect_name)のリスト
        :return:
        """
        outer_dict = {"Influencer": Influencer}
        inner_list = []

        # self.dataに入れる辞書の作成。
        for effect_, target, limit_ in zip(effect, targetPosition, limit):
            inner_dict = {"limit": limit_, "effect": effect_, "target": target, "targetInstance": None}
            inner_list.append(inner_dict)

            # 自身への効果の適用
            self.data.append(outer_dict)
            if limit_() is True and Influencer[0] == target[0] and Influencer[1] == target[1]:
                inner_dict["targetInstance"] = target[0].MYFIELD["Stage"][target[1]][0]
                self.useEffect(inner_dict, player1, player2, target[1])
            # ターゲットへの適用
            if limit_() is True and target[0].charaExistCheck(target[1]) is True:
                if Influencer[0] == target[0] and Influencer[1] == target[1]:
                    pass
                else:
                    inner_dict["targetInstance"] = target[0].MYFIELD["Stage"][target[1]][0]
                    self.useEffect(inner_dict, player1, player2, target[1])
        outer_dict["targetList"] = inner_list

    def adaptCharactor(self, player1, player2, position):
        for i, data_ in enumerate(self.data):
            for j, data__ in enumerate(data_["targetList"]):
                if data__["target"][0] is player1 and data__["target"][1] == position:
                    if data__["limit"]():
                        if player1.MYFIELD["Stage"][position][0] is not data__["targetInstance"]:
                            data__["targetInstance"] = player1.MYFIELD["Stage"][position][0]
                            self.useEffect(self.data[i]["targetList"][j], player1, player2, position)

    def adjustEffect(self, player1, player2, position):
        for i, data_ in enumerate(self.data):
            for j, data__ in enumerate(data_["targetList"]):
                if data__["target"][0] is player1 and data__["target"][1] is position and player1.charaExistCheck(position):
                    if data__["targetInstance"] is None and data__["limit"]() is True:
                        data__["targetInstance"] = player1.MYFIELD["Stage"][position][0]
                        self.useEffect(self.data[i]["targetList"][j], player1, player2, position)
                    elif data__["targetInstance"] is player1.MYFIELD["Stage"][position][0] and data__["limit"] is False:
                        data__["targetInstance"] = None
                        self.recoveryEffect(self.data[i]["targetList"][j], player1, player2, position)

    def exitCharaSolve(self, player1, player2, position):
        # 影響を受ける側の解決処理。
        for i, data_ in enumerate(self.data):
            for j, data__ in enumerate(data_["targetList"]):
                if data__["target"][0] == player1 and data__["target"][1] == position and data__["targetInstance"] is not None and data__["limit"]() is True:
                    if player1.MYFIELD["Stage"][position][0] is not data__["targetInstance"]:
                        data__["targetInstance"] = None
                        self.recoveryEffect(self.data[i]["targetList"][j], player1, player2, position)

    def turnEndSolve(self, player1, player2):
        for i, data_ in enumerate(self.data):
            for j, data__ in enumerate(data_["targetList"]):
                if data__["target"][0].charaExistCheck(data__["target"][1]) and data__["limit"]() is True:
                    if player1 == data__["target"][0]:
                        self.recoveryEffect(self.data[i]["targetList"][j], player1, player2, data__["target"][1])
                    else:
                        self.recoveryEffect(self.data[i]["targetList"][j], player2, player1, data__["target"][1])
        self.data.clear()


class permanentEffectDict(UserList):
    def __init__(self):
        """
        :param self.data: "influencer"と"target"のインデックスがある辞書のリスト
        アクセス例 : self.data[0]["target"][0]["limit"]
        """
        super().__init__()
        self.pattern_increase = re.compile("increase.*")
        self.pattern_decrease = re.compile("decrease.*")
        self.pattern_append = re.compile("append.*")
        self.pattern_power = re.compile(".*Power")
        self.pattern_level = re.compile(".*Level")
        self.pattern_soul = re.compile(".*Soul")
        self.pattern_feature = re.compile(".*Feature")
        self.pattern_effect = re.compile(".*Effect")
        self.pattern_encore = re.compile(".*Encore.*")
        self.data = []

    def useEffect(self, useDict, Influencer, player1, _, position): # TODO 各種追加
        if self.pattern_increase.match(useDict["effect"][0]):
            if self.pattern_power.match(useDict["effect"][0]):
                useDict["target"][0].MYFIELD["Stage"][position][0].power += useDict["effect"][1]()
            if self.pattern_level.match(useDict["effect"][0]):
                useDict["target"][0].MYFIELD["Stage"][position][0].level += useDict["effect"][1]()
        elif self.pattern_decrease.match(useDict["effect"][0]):
            if self.pattern_power.match(useDict["effect"][0]):
                useDict["target"][0].MYFIELD["Stage"][position][0].power -= useDict["effect"][1]()
            if self.pattern_level.match(useDict["effect"][0]):
                useDict["target"][0].MYFIELD["Stage"][position][0].level -= useDict["effect"][1]()
        elif self.pattern_append.match(useDict["effect"][0]):
            if self.pattern_effect.match(useDict["effect"][0]):
                useDict["target"][0].MYFIELD["Stage"][position][0].appendEffect = AppendEffect(useDict["effect"][1], useDict["effect"][2])
                if self.pattern_encore.match(useDict["effect"][2]):
                    useDict["target"][0].MYFIELD["Stage"][position][0].hasEffectEncore = True

        if Influencer[0] == player1 and Influencer[1] == position:
            print("{} の永続効果を自身に適用します".format(player1.MYFIELD["Stage"][position][0].name))
        else:
            useDict["targetInstance"] = useDict["target"][0].MYFIELD["Stage"][useDict["target"][1]][0]
            print("{} の永続効果を {} に適用します".format(Influencer[0].MYFIELD["Stage"][Influencer[1]][0].name, useDict["target"][0].MYFIELD["Stage"][position][0].name))

    def recoveryEffect(self, useDict, _, __, position):
        if self.pattern_increase.match(useDict["effect"][0]):
            if self.pattern_power.match(useDict["effect"][0]):
                useDict["target"][0].MYFIELD["Stage"][position][0].power -= useDict["effect"][1]()
            if self.pattern_level.match(useDict["effect"][0]):
                useDict["target"][0].MYFIELD["Stage"][position][0].level -= useDict["effect"][1]()
        elif self.pattern_decrease.match(useDict["effect"][0]):
            if self.pattern_power.match(useDict["effect"][0]):
                useDict["target"][0].MYFIELD["Stage"][position][0].power += useDict["effect"][1]()
            if self.pattern_level.match(useDict["effect"][0]):
                useDict["target"][0].MYFIELD["Stage"][position][0].level += useDict["effect"][1]()
        elif self.pattern_append.match(useDict["effect"][0]):
            if self.pattern_effect.match(useDict["effect"][0]):
                useDict["target"][0].MYFIELD["Stage"][position][0].appendEffect = None
                if self.pattern_encore.match(useDict["effect"][2]):
                    useDict["target"][0].MYFIELD["Stage"][position][0].hasEffectEncore = False

    def adaptField(self, player1, player2, Influencer, targetPosition, limit, effect):
        """
        永続効果持ちのキャラをプレイしたときに、インスタンスから使用する関数
        :param player1: 手番のプレイヤーオブジェクト
        :param player2: 相手番のプレイヤーオブジェクト
        :param Influencer: 永続効果を持つキャラの(player, position)
        :param targetPosition: 永続効果の影響を受ける(player, position)のリスト
        :param limit: 永続効果が適応される条件の関数。player.MYFIELD[""]の関数
        :param effect: 永続効果の(effect_name, effect(), append_effect_name)のリスト
        :return:
        """
        outer_dict = {"Influencer": Influencer}
        inner_list = []

        # self.dataに入れる辞書の作成。
        for effect_, target, limit_ in zip(effect, targetPosition, limit):
            inner_dict = {"limit": limit_, "effect": effect_, "target": target, "targetInstance": None}
            inner_list.append(inner_dict)

            # 自身への効果の適用
            self.data.append(outer_dict)
            if limit_() is True and Influencer[0] == target[0] and Influencer[1] == target[1]:
                inner_dict["targetInstance"] = target[0].MYFIELD["Stage"][target[1]][0]
                self.useEffect(inner_dict, Influencer, player1, player2, target[1])
            # ターゲットへの適用
            if limit_() is True and target[0].charaExistCheck(target[1]) is True:
                if Influencer[0] == target[0] and Influencer[1] == target[1]:
                    pass
                else:
                    inner_dict["targetInstance"] = target[0].MYFIELD["Stage"][target[1]][0]
                    self.useEffect(inner_dict, Influencer, player1, player2, target[1])
        outer_dict["targetList"] = inner_list

    def adaptCharactor(self, player1, player2, position):
        for i, data_ in enumerate(self.data):
            for j, data__ in enumerate(data_["targetList"]):
                if data__["target"][0] is player1 and data__["target"][1] == position:
                    if data__["limit"]():
                        if player1.MYFIELD["Stage"][position][0] is not data__["targetInstance"]:
                            data__["targetInstance"] = player1.MYFIELD["Stage"][position][0]
                            self.useEffect(self.data[i]["targetList"][j], self.data[i]["Influencer"], player1, player2, position)

    def adjustEffect(self, player1, player2, position):
        for i, data_ in enumerate(self.data):
            for j, data__ in enumerate(data_["targetList"]):
                if data__["target"][0] is player1 and data__["target"][1] is position and player1.charaExistCheck(position):
                    if data__["targetInstance"] is None and data__["limit"]() is True:
                        data__["targetInstance"] = player1.MYFIELD["Stage"][position][0]
                        self.useEffect(self.data[i]["targetList"][j], self.data[i]["Influencer"], player1, player2, position)
                    elif data__["targetInstance"] is player1.MYFIELD["Stage"][position][0] and data__["limit"] is False:
                        data__["targetInstance"] = None
                        self.recoveryEffect(self.data[i]["targetList"][j], player1, player2, position)

    def exitCharaSolve(self, player1, player2, position):
        # 影響を受ける側の解決処理。
        for i, data_ in enumerate(self.data):
            if data_["Influencer"][0] is player1 and data_["Influencer"][1] == position:
                continue
            for j, data__ in enumerate(data_["targetList"]):
                if data__["target"][0] == player1 and data__["target"][1] == position and data__["targetInstance"] is not None and data__["limit"]() is True:
                    if player1.MYFIELD["Stage"][position][0] is not data__["targetInstance"]:
                        data__["targetInstance"] = None
                        self.recoveryEffect(self.data[i]["targetList"][j], player1, player2, position)

        # 影響を与える側の処理
        if hasattr(player1.MYFIELD["Stage"][position][0], "permanentEffect"):
            exitCharaIndex = []
            print("{} の永続効果を停止します".format(player1.MYFIELD["Stage"][position][0].name))
            for i, data_ in enumerate(self.data):
                if data_["Influencer"][0] is player1 and data_["Influencer"][1] == position:
                    for j, data__ in enumerate(data_["targetList"]):
                        if data__["targetInstance"] is not None:
                            self.recoveryEffect(self.data[i]["targetList"][j], player1, player2, position)
                    exitCharaIndex.append(i)
            for i in reversed(exitCharaIndex):
                self.data.pop(i)


def effectConfirm():
    flag = selectNumberChecker(1, 2, "効果を使いますか？\n1 : はい\n2 : いいえ")
    return flag


def varSizeChecker(a, b, var):
    if a <= var <= b:
        return True
    else:
        return False


def selectNumberChecker(a, b, *sentence):
    """
    :param a: 最小値
    :param b: 最大値
    :param sentence:sentence[0]->説明文, sentence[1]->「戻る」コマンドの追加
    """
    if len(sentence) == 2:
        print("{} : {}".format(b + 1, sentence[1]))

    while True:
        try:
            if len(sentence) == 1:
                number = int(input(sentence[0] + " : "))
                if varSizeChecker(a, b, number):
                    return number
                else:
                    print("範囲内の数値を入力してください")
            elif len(sentence) == 2:
                number = int(input(sentence[0]))
                if varSizeChecker(a, b + 1, number):
                    return number
                else:
                    print("範囲内の数値を入力してください")
        except ValueError:
            print("数値を入力してください")


def sortCardList(card_list: list) -> list: # TODO 関数の作成
    """
    カードタイプのソートをしてから、各カードタイプごとに名前順に直す
    :param card_list:
    :return:
    """
    copy_list = card_list.copy()
    event_count = 0
    cx_count = 0
    for i, card in enumerate(card_list):
        if card.cardType == CardType.EVENT:
            copy_list.append(copy_list.pop(i))
            event_count += 1
    for i, card in enumerate(card_list):
        if card.cardType == CardType.CX:
            copy_list.append(copy_list.pop(i))
            cx_count += 1
    chara_count = len(copy_list) - (event_count + cx_count)
    for i, i_card in enumerate(copy_list):
        if i == chara_count - 1:
            break
        # キャラごとにソート
        for j, j_card in enumerate(copy_list):
            if i > j or i == j:
                continue
            elif i_card.name[0] > j_card.name[0]:
                copy_list[i], copy_list[j] = copy_list[j], copy_list[i]
    return copy_list


def debug(sentence):
    print(sentence)
    time.sleep(3)


def soundMp3(filename):
    filemp3 = "sound/{}.mp3".format(filename)
    pygame.mixer.init()
    pygame.mixer.music.load(filemp3)
    mp3_length = MP3(filemp3).info.length
    pygame.mixer.music.play(1)
    time.sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()


stageLabel = ["前列左 : ", "前列中央 : ", "前列右 : ", "後列左 : ", "後列右 : "]
attackLabel = ["前列左のキャラで攻撃する", "前列中央のキャラで攻撃する", "前列右のキャラで攻撃する"]
