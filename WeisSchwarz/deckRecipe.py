import cardList
from CardData import W01, W09, W18, W23, W46, WE16, WE20, WE30


def DC_music(player):
    deck = []
    
    for i in range(4):
        deck.append(WE30.WE30_21(player=player))  # もう忘れない
        deck.append(W23.W23_050(player=player))  # まあ会えるよね
        deck.append(W09.W09_078(player=player))  # さんばか
        deck.append(WE30.WE30_10(player=player))  # ドレスことり
        deck.append(WE30.WE30_08(player=player))  # 踏み出した一歩 小恋
        deck.append(WE30.WE30_15(player=player))  # LV1 雪月花
        deck.append(WE30.WE30_20(player=player))  # LV1 ななか
        
    for i in range(3):
        deck.append(WE30.WE30_P05(player=player))  # LV3小恋&音夢&ななか
        deck.append(WE30.WE30_27(player=player))  # 眞子&萌 集中
        deck.append(W23.W23_040(player=player))  # みっくん
        deck.append(WE30.WE30_09(player=player))  # 打ち上げ花火
    
    for i in range(2):
        deck.append(W23.W23_026(player=player))  # LV3ななか
        deck.append(W23.W23_062(player=player))  # 助太刀美夏
        deck.append(W23.W23_076(player=player))  # レベル応援杏
        deck.append(W01.W01_029(player=player))  # パジャマの茜
        deck.append(W46.W46_104(player=player))  # LV0 葵
    
    for i in range(1):
        pass
    
    return deck
    
    
def suginamiEncoreGreen(player):
    deck = []
    for i in range(4):
        deck.append(W01.W01_084(player=player))  # 杉並
        deck.append(W18.W18_071(player=player))  # フラワーズ
        deck.append(W09.W09_033(player=player))  # 白河ことり
        deck.append(W46.W46_109(player=player))  # 出会いの一冊
        deck.append(WE30.WE30_21(player=player))  # もう忘れない

    for i in range(3):
        deck.append(W09.W09_078(player=player))  # さんばか
        deck.append(W09.W09_112(player=player))  # 気配りことり
        deck.append(WE30.WE30_10(player=player))  # ドレスことり
        deck.append(WE30.WE30_07(player=player))  # 由夢エリカ
        deck.append(W46.W46_099(player=player))  # LV3すもも
        deck.append(W01.W01_E18(player=player))  # 小川

    for i in range(2):
        deck.append(W46.W46_106(player=player))  # LV1すもも
        deck.append(W23.W23_062(player=player))  # 助太刀美夏
        deck.append(W18.W18_023(player=player))  # 集中サラ
        deck.append(W23.W23_026(player=player))  # LV3ななか
        deck.append(W23.W23_076(player=player))  # レベル応援杏
        deck.append(WE16.WE16_10(player=player))  # お料理姫乃

    return deck


def test(player):
    deck = []
    return deck
