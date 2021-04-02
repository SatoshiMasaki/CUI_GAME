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


class WE30_01( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "キミと見る景色芳乃さくら"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《魔法》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】このカードは相手の効果に選ばれない。
【自】このカードがアタックした時、あなたは他の自分の《魔法》のキャラを1枚選び、そのターン中、パワーを＋X。Xは他のあなたの《魔法》のキャラの枚数×500に等しい。
【自】このカードが手札から舞台に置かれたターン中、あなたのアンコールステップの始めに、あなたは自分の山札の上から2枚を、控え室に置き、相手にXダメージ与える。Xはそれらのカードのトリガーアイコンのソウルの合計に等しい。(ダメージキャンセルは発生する)
'''


class WE30_02( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "想いを紡ぐ恋心立夏"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《新聞》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】［①あなたの山札の上から1枚をクロック置場に置き、このカードを思い出にする］バトル中のこのカードがリバースした時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室のレベル1以下のキャラを1枚選び、手札に戻す。
'''


class WE30_03( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "共に歩む未来姫乃"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《新聞》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】 他のあなたの《新聞》のキャラが2枚以上なら、このカードのパワーを＋1500し、このカードは次の能力を得る。『【永】 このカードのバトル中、相手は『助太刀』を手札からプレイできない。』
【自】［手札を1枚控え室に置く］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分のクロックの上から1枚を、ストック置場に置く。
'''


class WE30_04( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "大切な人の隣にさら"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《新聞》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】 他のあなたの、《新聞》か《スポーツ》のキャラ1枚につき、このカードのパワーを＋500。
【自】［② 手札の、《新聞》か《スポーツ》のキャラを2枚控え室に置く］ この能力は1ターンにつき1回まで発動する。このカードが手札から舞台に置かれたターン中、あなたの前列の中央の枠のキャラがアタックした時、あなたはコストを払ってよい。そうしたら、このカードを【スタンド】する。
'''


class WE30_05( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ウェディングドレスの美琴"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《新聞》', '《愛》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】 このカードが手札から舞台に置かれた時、あなたは自分の、《新聞》か《愛》のキャラを1枚選び、そのターン中、パワーを＋Ｘ。Ｘはあなたの、《新聞》か《愛》のキャラの枚数×500に等しい。
'''


class WE30_06( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“あさきゆめみし君と”音姫"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《魔法》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】 このカードが手札から舞台に置かれた時、あなたは自分の山札を上から3枚まで見て、カードを1枚まで選び、手札に加え、残りのカードを控え室に置く。
【自】CXコンボ このカードがアタックした時、クライマックス置場に「この日を忘れない」があるなら、あなたは他の自分のキャラを1枚とこのカードを選び、そのターン中、次の能力を与える。『【自】 この能力は1ターンにつき1回まで発動する。このカードの与えたダメージがキャンセルされた時、あなたは相手に1ダメージを与えてよい。』 (ダメージキャンセルは発生する)
'''


class WE30_07( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "桜風の季節エリカ＆由夢"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《王族》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】 舞台にこのカードがいるなら、このカードは《魔法》を得る。
【自】 あなたのクライマックスがクライマックス置場に置かれた時、あなたは自分のキャラを1枚選び、そのターン中、パワーを＋1000。
【起】集中［① このカードをレストする］ あなたは自分の山札の上から4枚をめくり、控え室に置く。それらのカードのクライマックス1枚につき、あなたは自分の控え室のキャラを1枚まで選び、手札に戻す。
'''

    def permanetEffect(self, player1, player2, position):
        featList = list( self.feature )
        featList.append( "魔法" )
        self.feature = tuple( featList )

        player1.permanentEffect.appendEffect( player1, player2, (player1, position),
                                              (player1, position), ("appendFeature", "魔法") )

    def startUpEffect(self, player1, player2, _):
        print( "集中を使います" )
        if self.player.MYFIELD["Stock"].costCheck( 1 ) and self.status == util.Status.STAND:
            self.player.useCost( 1 )
            self.status = util.Status.REST

            salvage_count = player1.cardEffect.CharaEffect.concentration( player1, player2, 4 )
            for i in range( salvage_count ):
                player1.cardEffect.UtilEffect.salvageCard( player1, player2, util.CardType.CHARA )
        else:
            print( "ストックが足りません" )

    def useCX(self, player1, player2, position):
        def limit():
            return True

        def effect():
            return 1000

        try:
            if player2.turnPlayer is False:
                print( "{} : CXが置かれたとき、自分のキャラ1枚のパワーを+1000できる".format( self.name ) )
                flag = util.effectConfirm()
                if flag == 1:
                    player1.MYFIELD["Stage"].showStage()
                    while True:
                        select_filed = util.selectNumberChecker( 1, 5, "パンプするキャラを選んでください" )
                        if player1.charaExistCheck( select_filed - 1 ):
                            player1.MYFIELD["Stage"][select_filed - 1][0].power += 1000
                            player1.untilTurnEndEffect.adaptField( player1, player2, (player1, position),
                                                                   [(player1, select_filed - 1)], [limit],
                                                                   [("increasePower", effect)] )
                            break
                        else:
                            print( "キャラがいません" )
                else:
                    pass
        except Exception as err:
            util.debug( err )


class WE30_08( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "踏み出した一歩小恋"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】［手札を1枚控え室に置く］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「打ち上げ花火」を1枚選び、手札に戻す。
【自】 このカードが【リバース】した時、このカードのバトル相手のレベルが0以下なら、あなたは相手のクロックの上から1枚を、控え室に置いてよい。そうしたら、あなたはそのキャラをクロック置場に置く。
'''

    def cipEffect(self, player1, _, __):
        flag = False
        for card in player1.MYFIELD["Waiting_Room"]:
            if card.name == "打ち上げ花火":
                flag = True
                break
        if flag:
            print( "{} : 手札を一枚控室に置く。控室の「打ち上げ花火」を手札に加える".format( self.name ) )
            effect_flag = util.effectConfirm()
            if effect_flag == 1:
                player1.MYFIELD["Hand"].showHand()
                select_card = util.selectNumberChecker( 1, len( player1.MYFIELD["Hand"] ), "カードを選んでください" )
                player1.MYFIELD["Waiting_Room"].append( player1.MYFIELD["Hand"].pop( select_card - 1 ) )
                for i, card in enumerate( player1.MYFIELD["Waiting_Room"] ):
                    if card.name == "打ち上げ花火":
                        player1.MYFIELD["Hand"].append( player1.MYFIELD["Waiting_Room"].pop( i ) )
                        break

    def loseBattle(self, player1, player2, _, opposite_position):
        if player2.MYFIELD["Stage"][opposite_position][0].level <= self.level:
            print( "{} : 相打ちストック送り".format( self.name ) )
            flag = util.effectConfirm()
            if flag == 1:
                if len( player2.MYFIELD["Clock"] ) != 0:
                    player2.MYFIELD["Waiting_Room"].append( player2.MYFIELD["Clock"].pop() )
                player2.MYFIELD["Stage"][opposite_position][0].status = util.Status.STAND
                player2.MYFIELD["Stage"].leaveStageChara( player2, player1, opposite_position,
                                                          player2.MYFIELD["Clock"] )


class WE30_09( EVENT ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "打ち上げ花火"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 0
        self.counter = False
        self.useCardLimit = None

    ''''''

    def cardLimit(self, player1, _):
        if player1.MYFIELD["Stage"].searchFeature( player1, "音楽" ):
            return True
        else:
            print( "「音楽」のキャラがいないため、発動できません" )
            return False

    def counterEffect(self, player1, _, __):
        if player1.MYFIELD["Stage"].searchFeature( player1, "音楽" ):
            feature_flag = False
            for i in range( 4 ):
                player1.MYFIELD["Deck"].turnOver( player1 )
                print( "{} : {}".format( i + 1, player1.MYFIELD["Event_Zone"][i].name ) )
                if "音楽" in player1.MYFIELD["Event_Zone"][i].feature:
                    feature_flag = True
            if feature_flag:
                select_card = util.selectNumberChecker( 1, 4, "カードを選んでください" )
                if "音楽" in player1.MYFIELD["Event_Zone"][select_card - 1].feature:
                    player1.MYFIELD["Hand"].append( player1.MYFIELD["Event_Zone"].pop( select_card - 1 ) )
                    for i in range( 3 ):
                        player1.MYFIELD["Waiting_Room"].append( player1.MYFIELD["Event_Zone"].pop() )
                else:
                    print( "「音楽」のキャラを選んでください" )
            else:
                for i in range( 4 ):
                    player1.MYFIELD["Waiting_Room"].append( player1.MYFIELD["Event_Zone"].pop() )
        else:
            print( "「音楽」のキャラがいないため、発動できません" )
            player1.MYFIELD["Hand"].append( player1.MYFIELD["Event_Zone"].pop() )

    def autoEffect(self, player1, player2):
        if player1.MYFIELD["Stage"].searchFeature( player1, "音楽" ):
            feature_flag = False
            for i in range( 4 ):
                player1.MYFIELD["Deck"].turnOver( player1 )
                print( "{} : {}".format( i + 1, player1.MYFIELD["Event_Zone"][i].name ) )
                if player1.MYFIELD["Event_Zone"][i].cardType == util.CardType.CHARA and \
                        "音楽" in player1.MYFIELD["Event_Zone"][i].feature:
                    feature_flag = True
            if feature_flag:
                select_card = util.selectNumberChecker( 1, 4, "カードを選んでください" )
                if "音楽" in player1.MYFIELD["Event_Zone"][select_card - 1].feature:
                    player1.MYFIELD["Hand"].append( player1.MYFIELD["Event_Zone"].pop( select_card - 1 ) )
                    for i in range( 3 ):
                        player1.MYFIELD["Waiting_Room"].append( player1.MYFIELD["Event_Zone"].pop() )
                else:
                    print( "「音楽」のキャラを選んでください" )
            else:
                for i in range( 4 ):
                    player1.MYFIELD["Waiting_Room"].append( player1.MYFIELD["Event_Zone"].pop() )
        else:
            print( "「音楽」のキャラがいないため、発動できません" )
            # player1.MYFIELD["Hand"].append(player1.MYFIELD["Event_Zone"].pop())


class WE30_10( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ウェディングドレスのことり"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《魔法》', '《音楽》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】 このカードがアタックした時、あなたは自分の、《魔法》か《音楽》のキャラを1枚選び、そのターン中、パワーを＋Ｘ。Ｘはあなたの、《魔法》か《音楽》のキャラの枚数×500に等しい。
【自】［①］ このカードが手札から舞台に置かれたターン中、このカードのバトル相手が【リバース】した時、あなたはコストを払ってよい。そうしたら、あなたはそのキャラをクロック置場に置く。
'''

    def selfAttackTrigger(self, player1, player2, position):
        def limit():
            return True

        def effect():
            return count_feat * 500

        count_feat = player1.MYFIELD["Stage"].countFeature( player1, ("魔法", "音楽") )
        print( "{} : 魔法か音楽のキャラひとりをパワー+X。Xは魔法か音楽のキャラひとりにつき+500".format( self.name ) )
        player1.MYFIELD["Stage"].showStage()
        while True:
            select_card = util.selectNumberChecker( 1, 5, "カードを選んでください : " )
            if player1.charaExistCheck( select_card - 1 ):
                if "魔法" in player1.MYFIELD["Stage"][select_card - 1][0].feature or "音楽" in \
                        player1.MYFIELD["Stage"][select_card - 1][0].feature:
                    player1.untilTurnEndEffect.adaptField( player1, player2, (player1, position),
                                                           [(player1, select_card - 1)], [limit],
                                                           [("increasePower", effect)] )
                    break
                else:
                    print( "特徴「音楽」「魔法」をもちません" )
            else:
                print( "キャラがいません" )

    def winBattle(self, player1, player2, _, enemyPosition):
        flag = player1.MYFIELD["Stock"].costCheck( 1 )
        if flag is True and player2.charaExistCheck( enemyPosition ) is True:
            print( "{} : このカードのバトル相手がリバースしたとき、1コストを払うことでバトル相手をクロックに置く".format( self.name ) )
            flag = util.effectConfirm()
            if flag == 1:
                player1.useCost( 1 )
                container = []
                player2.MYFIELD["Stage"][enemyPosition][0].status = util.Status.STAND
                player2.MYFIELD["Stage"].leaveStageChara( player2, player1, enemyPosition, container )
                player2.MYFIELD["Clock"].appendClock( player2, container.pop() )


class WE30_11( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "雪の日の登校シャルル"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《新聞》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】 他のあなたのバトル中のキャラが【リバース】した時、あなたは自分の、《新聞》か《生徒会》のキャラを1枚選び、そのターン中、パワーを＋1500。
【起】［① このカードを【レスト】する］ あなたは自分の、《新聞》か《生徒会》のキャラを1枚選び、そのターン中、次の能力を与える。『【自】 このカードのバトル相手が【リバース】した時、あなたは自分の控え室のキャラを1枚選び、手札に戻してよい。』
'''


class WE30_12( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "とっても幸せ葵"
        self.color = None
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《新聞》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】 このカードがアタックした時、このカードの正面のキャラのレベルが3以上なら、そのターン中、このカードのパワーを＋6000。
【自】 アンコール ［手札の、《新聞》か《ウェイトレス》のキャラを1枚控え室に置く］ （このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、このカードがいた枠に【レスト】して置く）
'''


class WE30_13( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“楽しい”時間すもも"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《委員長》', '《演劇》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたのストックが2枚以下なら、このカードのパワーを＋1500
【自】［①］ アンコールステップの始めに、他のあなたの前列の【レスト】しているキャラがいないなら、あなたはコストを払ってよい。そうしたら、このカードを【レスト】する。
'''


class WE30_14( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "世話焼き桜姫"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 6500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】 応援 このカードの前のあなたのレベル3以上のキャラすべてに、パワーを＋2000。
【自】 このカードが手札から舞台に置かれた時、あなたは自分のクロックの下から1枚と控え室の《魔法》のキャラを1枚選び、入れ替えてよい。
'''


class WE30_15( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "仲良し雪月花杏＆小恋＆茜"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》', '《演劇》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】 あなたの後列のキャラが1枚以下なら、このカードはアタックできない。
【自】CXコンボ このカードのバトル相手が【リバース】した時、あなたのクライマックス置場に「もう、忘れない」があるなら、あなたは自分の後列のキャラを1枚選び、自分の山札を見て特徴を持たないかそのキャラと同じ特徴を1つ以上持つキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''

    def startAttackPhase(self, player1, _, __):
        if player1.turnPlayer is True:
            if player1.charaExistCheck( 3 ) and player1.charaExistCheck( 4 ):
                pass
            else:
                print( "{} : 後列のキャラが一枚以下ならこのカードをレストする".format( self.name ) )
                self.status = util.Status.REST

    def CXcombo(self, player1, player2, position, useCard):
        def searchCard(_, __, ___, ____):
            print( "{} : 自分の後列のキャラを選び、そのキャラと同じ特徴か特徴をもたないキャラを山札から一枚選び手札に加える".format( self.name ) )
            for i in range( 3, 5 ):
                if player1.charaExistCheck( i ):
                    print( "{} : {}".format( i - 2, player1.MYFIELD["Stage"][i][0].name ) )
                    for feat in player1.MYFIELD["Stage"][3][0].feature:
                        print( " : ", feat )
            select_card = util.selectNumberChecker( 1, 2, "後列のキャラを選んでください" )
            if player1.charaExistCheck( select_card + 2 ):
                player1.MYFIELD["Deck"].showDeck()
                while True:
                    index = util.selectNumberChecker( 1, len( player1.MYFIELD["Deck"] ), "カードを選んでください" )
                    if player1.charaExistCheck( index + 2 ):
                        for feature in player1.MYFIELD["Stage"][select_card + 2][0].feature:
                            if len( player1.MYFIELD["Deck"][index - 1].feature ) == 0 or \
                                    feature in player1.MYFIELD["Deck"][index - 1].feature:
                                player1.MYFIELD["Deck"].turnOver( index - 1 )
                                player1.MYFIELD["Hand"].append( player1.MYFIELD["Event_Zone"].pop() )
                                player1.MYFIELD["Deck"].shuffle()
                                break
                            else:
                                print( "このカードは選べません" )
                        break
                    else:
                        print( "キャラがいません" )

        if isinstance( useCard, WE30_21 ):
            player1.untilTurnEndEffect.adaptField( player1, player2, (player1, position),
                                                   [(player1, position)], [lambda: True],
                                                   [("appendEffect", searchCard, "winBattle")] )


class WE30_16( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "スキーウェアの美夏"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《メカ》', '《バナナ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】［手札を1枚クロック置場に置く］ このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見て《メカ》か《バナナ》か《委員長》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''


class WE30_17( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "色づく恋模様音夢＆美春"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ('\n',)
        self.power = 6500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》', '《バナナ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】 このカードが手札から舞台に置かれた時、あなたは相手の前列のキャラを1枚選び、次の相手のターンの終わりまで、パワーを＋1000。
'''


class WE30_18( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "無邪気なレディーさくら　"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】 この能力は1ターンにつき1回まで発動する。バトル中のこのカードが【リバース】した時、あなたは自分の山札の上から1枚を公開する。そのカードのレベルが2以上なら、あなたはこのカードを【レスト】してよい。（クライマックスのレベルは0として扱う。公開したカードは元に戻す）
'''


class WE30_19( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "この日を忘れない"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None

    ''''''


class WE30_20(CHARA):  # TODO サイドアタック不可の実装
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "体操着のななか"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】 このカードはサイドアタックできない。
【永】 このカードの正面のキャラに、『【自】 アンコール ［手札のキャラを1枚控え室に置く］』を与える。
'''

    def permanentEffect(self, player1, player2, position):
        oppositePosition = player1.MYFIELD["Stage"].oppositePosition( position + 1 )
        player1.permanentEffect.adaptField(
            player1, player2, (player1, position), [(player2, oppositePosition - 1)],
            [lambda: True], [("appendEffect", player2.cardEffect.CharaEffect.handEncore, "effectEncore")]
        )


class WE30_21( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "もう、忘れない"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = (util.TriggerType.SOUL_ONE, util.TriggerType.BOOK)
        self.useCardLimit = None

    ''''''

    def permanentEffect(self, player):
        for i in range( 5 ):
            if len( player.MYFIELD["Stage"][i] ) != 0:
                player.MYFIELD["Stage"][i][0].power += 1000
                player.MYFIELD["Stage"][i][0].soul += 1
                print( "{} に効果を使いました".format( player.MYFIELD["Stage"][i][0].name ) )
                print( "パワー : {}".format( player.MYFIELD["Stage"][i][0].power ) )
                print( "ソウル : {}".format( player.MYFIELD["Stage"][i][0].soul ) )
        return [[1000, 1000, 1000, 1000, 1000], [1, 1, 1, 1, 1]]


class WE30_22( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "特別留学生エリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《王族》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】 他のあなたの《王族》のキャラが2枚以上なら、このカードのパワーを＋1500し、このカードは『【自】 アンコール ［手札のキャラを1枚控え室に置く］』を得る。
'''


class WE30_23( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "大はしゃぎ!まひる　　"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《たとえ話》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】［① あなたの山札の上から1枚をクロック置場に置き、このカードを思い出にする］ バトル中のこのカードが【リバース】した時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見て《たとえ話》か《委員長》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''


class WE30_24( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "へーよーぶらざー"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('宝',)
        self.useCardLimit = None

    ''''''


class WE30_25( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "世話好き音夢"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 6000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》', '《風紀委員》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】 他のあなたの、《魔法》か《バナナ》か《風紀委員》のキャラ1枚につき、このカードのパワーを＋1000。
【自】［①］ このカードのバトル相手でレベル2以上のキャラが【リバース】した時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室のキャラを1枚選び、手札に戻す。
'''


class WE30_26( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ことりの歌"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('宝',)
        self.useCardLimit = None

    ''''''


class WE30_27( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "水着の眞子＆萌"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》', '《鍋》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】 相手のターン中、他のあなたの前列の中央の枠のキャラに、パワーを＋1000。
【起】集中［① このカードをレストする］ あなたは自分の山札の上から4枚をめくり、控え室に置く。それらのカードのクライマックス1枚につき、あなたは自分の山札を見て《音楽》か《鍋》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''

    def turnstarteffect(self, player1, player2, position):
        if player1.turnPlayer is False:
            print( "{} : 相手ターン中、自分の舞台の前列中央のキャラを+1000する".format( self.name ) )
            player1.untilTurnEndEffect.adaptField( player1, player2, (player1, position),
                                                   [(player1, 1)], [lambda: True],
                                                   [("increasePower", lambda: 1000)] )

    def startUpEffect(self, player1, player2, position):
        if player1.MYFIELD["Stock"].costCheck( 1 ):
            player1.useCost( 1 )
            self.status = util.Status.REST
            search_count = player1.cardEffect.CharaEffect.concentration( player1, player2, position )
            if search_count != 0:
                print( "山札から「音楽」のキャラをサーチします" )
                player1.MYFIELD["Deck"].showDeck()
                while True:
                    index = util.selectNumberChecker( 1, len( player1.MYFIELD["Deck"] ), "カードを選んでください" )
                    if "音楽" in player1.MYFIELD["Deck"][index - 1].feature:
                        player1.MYFIELD["Deck"].turnOver( player1, index - 1 )
                        player1.MYFIELD["Hand"].append( player1.MYFIELD["Event_Zone"].pop() )
                        break
                    else:
                        print( "音楽のキャラを選んでください" )


class WE30_28( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“大好きなところ”鈴"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《動物》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは2枚まで引き、自分の手札を1枚選び、控え室に置く。
【自】CXコンボ[②手札を1枚控え室に置く]このカードがアタックした時、クライマックス置場に「あたしたちが付き合おう」があり、他のあなたのカード名に「理樹」を含むキャラがいるなら、あなたはコストを払ってよい。そうしたら、そのターン中、このカードのパワーを＋2000し、このカードは次の能力を得る。『【自】このカードのバトル相手がリバースした時、相手に1ダメージを与え、あなたはそのキャラをクロック置場に置く。』(ダメージキャンセルは発生する)
'''


class WE30_29( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“のほほん担当”小毬"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《お菓子》', '《童話》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたはイベントと「助太刀」を手札からプレイできない。
【永】他のあなたのカード名に「鈴」を含むキャラがいるなら、このカードは《動物》を得る。
'''


class WE30_30( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“かわいいこいぬさん”クド"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《動物》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたの控え室のクライマックスが2枚以下なら、あなたの手札のこのカードのレベルを-1。
【自】このカードが手札から舞台に置かれた時、あなたは自分のクロックの上から1枚を、控え室に置いてよい。
【自】アンコール[手札の《動物》のキャラを1枚控え室に置く]］(このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、このカードがいた枠にレストして置く)
'''


class WE30_31( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“約束のパートナー”沙耶"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《武器》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたの控え室のクライマックスが2枚以下なら、あなたの手札のこのカードのレベルを-1。
【永】相手の後列のキャラ1枚につき、このカードのパワーを+1000。
【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から3枚まで見て、カードを1枚まで選び、手札に加え、残りのカードを控え室に置く。
'''


class WE30_32( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“ビューティー☆はるちゃん”葉留佳"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 1
        self.feature = ('《ビー玉》', '《双子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたのカード名に「葉留佳」か「佳奈多」を含むキャラが2枚以上なら 、このカードのパワーを＋1000。
【自】 [手札を1枚控え室に置く]このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分のクロック上から1枚を、ストック置場に置く。
【自】CXコンボ[②]このカードがアタックした時、クライマックス置場に「Best Shot!」があり、他のあなたのカード名に「佳奈多」を含むキャラがいるなら、あなたはコストを払ってよい。そうしたら、相手に2ダメージを与え、そのターン中、このカードのパワーを＋1000。(ダメージキャンセルは発生する)
'''


class WE30_33( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“姉さん女房”唯湖"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの前列の中央の枠のキャラに、パワーを＋500。
【起】集中［① このカードをレストする］ あなたは自分の山札の上から4枚をめくり、控え室に置く。それらのカードのクライマックス1枚につき、あなたは自分の控え室のキャラを1枚まで選び、手札に戻す。
'''


class WE30_34( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“ビーエルガール”美魚"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《本》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは他の自分のキャラを1枚選び、そのターン中、パワーを+1500。
【自】［手札を1枚控え室に置く］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「この美しき二人」を1枚選び、手札に戻し、そのターン中、このカードは《妄想》を得る。
'''


class WE30_35( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“頑張り屋”佐々美"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 2500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《スポーツ》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】［②手札のレベル1以下のキャラを1枚控え室に置く］あなたがこのカードの「助太刀」を使った時、あなたはコストを払ってよい。そうしたら、あなたは相手の、レベルが相手のレベルより高いキャラを1枚選び、山札の下に置く。 　
【起】●助太刀2500 レベル2［①手札のこのカードを控え室に置く］(あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋2500)
'''


class WE30_36( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“融通の利かない”佳奈多"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《委員長》', '《双子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】このカードはサイドアタックできない。
【自】CXコンボこのカードがバトル相手がリバースした時、クライマックス置場に「Best Shot!」があるなら、あなた自分の控え室のキャラを1枚選び、手札に戻してよい。
'''


class WE30_37( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“リトルバスターズ”幼き日の恭介"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 6500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ()
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】このカードは、色条件を満たさずに手札からプレイできる。
【自】このカードがリバースした時、このカードのバトル相手のレベルが相手のレベルより高いなら、あなたはそのキャラをストック置場に置いてよい。そうしたら、あなたは相手のストックの下から1枚を、控え室に置く。
'''


class WE30_38( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“リトルバスターズ”幼き日の理樹"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 4500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ()
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】このカードは、色条件を満たさずに手札からプレイできる。
【永】応援 このカードの前のあなたのキャラすべてに、パワーを＋X。Xはそのキャラのレベル×500に等しい。
【自】[① 手札のクライマックスを1枚控え室に置く]このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室のクライマックスを1枚選び、手札に戻す。
'''


class WE30_39( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“リトルバスターズ”幼き日の鈴"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《動物》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚見て、山札の上か控え室に置く。
【自】[手札のクライマックスを1枚控え室に置く]このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室のレベル1以下のキャラを1枚選び、手札に戻す。
'''


class WE30_40( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“リトルバスターズ”幼き日の真人"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《筋肉》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、他のあなたの、《筋肉》か《スポーツ》のキャラがいるなら、このカードのパワーを+2000。
【自】[①他のあなたのスタンドしている、《筋肉》か《スポーツ》のキャラを1枚レストする]このカードが手札から舞台に置かれたターン中、このカードのバトル相手がリバースした時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見て、《筋肉》か《スポーツ》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''


class WE30_41( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“リトルバスターズ”幼き日の謙吾"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《スポーツ》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、相手の控え室のクライマックスが3枚以上なら、このカードをレストする。
【自】相手のアタックフェイズの始めに、あなたはこのカードを、前列のキャラのいない枠で、正面に相手のキャラがいる枠に動かしてもよい。
'''


class WE30_42( EVENT ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "この美しき二人"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 1
        self.counter = False
        self.useCardLimit = None

    ''''''


class WE30_43( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“猫にスパイ”鈴＆沙耶"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《動物》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚を公開する。そのカードが《動物》か《武器》かカード名に「理樹」を含むキャラなら手札に加え、あなたは自分の手札を1枚選び、控え室に置く。(そうでないなら元に戻す)
【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から2枚を、控え室に置く。それらのカードにクライマックスがあるなら、そのターン中、このカードのパワーを+3000。
'''


class WE30_46( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "あたしたちが付き合おう"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('宝',)
        self.useCardLimit = None

    ''''''


class WE30_49( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "いつかの未来のために"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.useCardLimit = None

    ''''''


class WE30_54( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "リトルバスターズ！"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('扉',)
        self.useCardLimit = None

    ''''''


class WE30_55( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "鬼召集！"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.useCardLimit = None

    ''''''


class WE30_P05( CHARA ):
    def __init__(self, player):
        self.player = player
        self.name = "真夏の恋 小恋＆音夢＆ななか"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ("音楽", "魔法")
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

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
            print( "{} : 手札のこのカードのレベルを-1".format( self.name ) )
            self.level -= 1
        else:
            print( "この効果は使えません" )

    def cipEffect(self, _, __, ___):
        if self.level == 2:
            self.level += 1

    def turnStartEffect(self, player1, player2, position):
        if player1.turnPlayer is False:
            if position == 0 or position == 1 or position == 2:
                print( "{} : 相手のターンのはじめにこのカードが前列にいるなら、"
                       "自分のキャラひとりのパワーを+4000できる".format( self.name ) )
                flag = util.effectConfirm()
                if flag == 1:
                    player1.MYFIELD["Stage"].showStage()
                    while True:
                        select_card = util.selectNumberChecker( 1, 5, "カードを選んでください" )
                        if player1.charaExistCheck( select_card - 1 ):

                            player1.untilTurnEndEffect.adaptField(
                                player1, player2, (player1, position), [(player1, select_card - 1)], [lambda: True],
                                [("increasePower", lambda: 4000)]
                            )
                            break
                        else:
                            print("キャラがいません")
