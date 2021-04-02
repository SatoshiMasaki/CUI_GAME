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


class W23_001( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "柔らかな笑顔 音姫"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】記憶あなたの思い出が2枚以上なら、このカードのパワーを＋1000し、ソウルを＋1。
【自】このカードがアタックした時、クライマックス置場に「幸せの予感」があるなら、あなたは自分の控え室の「柔らかな笑顔 音姫」を1枚まで選び、思い出にし、そのターン中、このカードのパワーを＋1000。
'''


class W23_002( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "オトナになった証拠さくら"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】この能力は1ターンにつき1回まで発動する。あなたが【起】を使った時、そのターン中、このカードのパワーを＋1000。
【起】［あなたの《魔法》のキャラを1枚レストする］そのターン中、このカードのパワーを＋1000。
'''


class W23_003( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "甘いひととき音姫"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《生徒会》', '《魔法》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】［① 手札を1枚控え室に置く］このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見て《魔法》のキャラを1枚まで選んで相手に見せ、手札に加える。その山札をシャッフルする。
'''


class W23_004( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "優しい温もりシャルル"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《生徒会》', '《魔法》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】他のあなたの《魔法》のキャラがアタックした時、そのターン中、このカードのパワーを＋1000。
【自】アンコール［手札のキャラ1枚を控え室に置く］(このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、このカードがいた枠にレストして置く)
'''


class W23_005( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "新しい魔法リッカ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《生徒会》', '《魔法》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【起】 集中 ［①］あなたは自分の山札の上から4枚をめくり、控え室に置く。それらのカードのクライマックス1枚につき、あなたは自分の《生徒会》のキャラを1枚選び、そのターン中、パワーを＋2000。
'''


class W23_006( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "最後の刻アイシア"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 5000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》', '《オモチャ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたのキャラすべてに、パワーを＋Ｘ。Ｘはそのキャラのコスト×500に等しい。
【自】あなたのクライマックス置場に「抑えられない想い」が置かれた時、そのターン中、相手は『【自】アンコール』を使えない。(ルールによる『【自】アンコール［③］』も使えない)
'''


class W23_007( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "みんなの幸せまひる"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《たとえ話》', '《和服》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたの手札が4枚以下なら、このカードのパワーを＋1000し、ソウルを＋2。
【自】この能力は1ターンにつき1回まで発動する。このカードが手札から舞台に置かれたターン中、このカードの与えたダメージがキャンセルされた時、あなたは相手に1ダメージを与えてよい。(ダメージキャンセルは発生する)
【自】バトル中のこのカードがリバースした時、このカードを思い出にする。
'''


class W23_T04( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "懐かしい感じリッカ　"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《生徒会》', '《魔法》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】応援 このカードの前のあなたのキャラすべてに、パワーを＋Ｘ。Ｘはそのキャラのコスト×500に等しい。　
【自】［① 手札を1枚控え室に置く］このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見て《生徒会》のキャラを1枚まで選んで相手に見せ、手札に加える。その山札をシャッフルする。
'''


class W23_009( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“正義の魔法使い”由姫"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》', '《お菓子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードがアタックした時、あなたは他の自分のキャラを選び、そのターン中、パワーを＋Ｘ。Ｘはそのキャラのソウル×1000に等しい。
'''


class W23_T05( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "お茶目なエリザベス　"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》', '《王族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】アンコール［あなたの山札の上から1枚をクロック置場に置く］(このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、このカードがいた枠にレストして置く)
'''


class W23_011( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "小さな頃みたいに音姫"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 3500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】応援 このカードの前のあなたのキャラすべてに、パワーを＋1000。　
【自】相手のキャラが、控え室から手札に戻った時、あなたは自分の山札の上から1枚を、ストック置場に置いてよい。
'''


class W23_T08( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "期待の眼差しアイシア"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》', '《オモチャ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】［①］このカードの与えたダメージがキャンセルされた時、あなたはコストを払ってよい。そうしたら、あなたは1枚引く。
'''


class W23_013( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "想い出のアルバム真哉&amp;亜沙&amp;夕陽"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8000
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('《愛》', '《たとえ話》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】記憶 あなたの思い出が3枚以上なら、このカードのソウルを+1し、このカードは『【自】アンコール 手札のキャラを1枚控え室に置く』を得る。
'''


class W23_014( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "白い奇跡の夜美咲　"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ()
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードがアタックした時、あなたは他の自分のキャラを1枚選び、そのターン中、パワーを+X。Xはそのキャラのソウル×1000に等しい。
'''


class W23_T01( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "王都のプリンセスさくら　"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》', '《ドレス》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、そのターン中、このカードのパワーを＋1500。
'''


class W23_T02( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "素敵な彼氏と和泉子　"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《宇宙人》', '《シャケ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚を公開する。そのカードがクライマックスなら、あなたは自分のキャラを1枚選び、そのターン中、ソウルを＋2。(公開したカードは元に戻す)
'''


class W23_017( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "大はしゃぎ!まひる　　"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《たとえ話》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    ''''''


class W23_018( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“家族”の団欒さくら　"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》', '《先生》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】バトル中のこのカードがリバースした時、このカードを山札の下に置く。
'''


class W23_019( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "幸せな時間アイシア　"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》', '《オモチャ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】相手がダメージをキャンセルした時、そのターン中、このカードのパワーを+1500。
'''


class W23_T06( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "いつかの記憶シャルル　"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 7000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    ''''''


class W23_021( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ずっと一緒に音姫"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 2500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【起】●助太刀3000 レベル2［① 手札のこのカードを控え室に置く］(あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋3000)
'''


class W23_T09( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "熱弁をふるう巴　"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8500
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('《魔法》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたのターン中、このカードのパワーを＋1000。
'''


class W23_023( EVENT ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ふたりだけのひみつ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 1
        self.counter = False
        self.useCardLimit = None

    ''''''


class W23_024( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "幸せの予感"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.useCardLimit = None

    ''''''


class W23_025( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "抑えられない想い"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None

    ''''''


class W23_026( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "わたしの気持ちななか"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《音楽》', '《魔法》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《音楽》のキャラ1枚につき、このカードのパワーを＋500。
【自】［①］このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは相手のストックすべてを、控え室に置き、相手は自分の山札の上から同じ枚数をストック置場に置く。
'''

    def permanentEffect(self, player1, player2, position):
        def limit():
            return True

        def effect():
            return (player1.MYFIELD["Stage"].countFeature( player1, ("音楽", "魔法") ) - 1) * 500

        player1.permanentEffect.adaptField(
            player1, player2, (player1, position), [(player1, position)],
            [limit], [("increasePower", effect)]
        )

    def cipEffect(self, player1, player2, _):
        if player1.MYFIELD["Stock"].costCheck( 1 ):
            print( "{} : 相手のストックをすべて控室に送る。その後相手は控室に送った枚数山札の上からストックに置く。"
                   .format( self.name ) )
            flag = util.effectConfirm()
            if flag == 1:
                player1.useCost( 1 )
                count = 0
                for i in range( len( player2.MYFIELD["Stock"] ) ):
                    player2.MYFIELD["Waiting_Room"].append( player2.MYFIELD["Stock"].pop() )
                    count += 1
                for i in range( count ):
                    player2.MYFIELD["Deck"].turnOver( player2 )
                    player2.MYFIELD["Stock"].append( player2.MYFIELD["Event_Zone"].pop() )


class W23_027( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "こそばゆい未来姫乃"
        self.color = util.Color.GREEN
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

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札を上から3枚まで見て、カードを1枚まで選び、手札に加える。残りのカードを控え室に置く。
【自】［手札を1枚控え室に置く］あなたのクライマックス置場に「かけがえのない家族」が置かれた時、前列にこのカードがいるなら、あなたはコストを払ってよい。そうしたら、あなたは自分のクロック置場の《魔法》のキャラを1枚選び、舞台の好きな枠に置く。
'''


class W23_028( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "大好きな歌ことり"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》', '《魔法》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたのレベル1以下のキャラすべてに、パワー+500。　
【自】◆シフト レベル0(あなたのメインフェイズの始めに、あなたは自分の手札の緑のカードを1枚とクロック置場のこのカードを選び、入れ替えてよい)
'''


class W23_029( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "二人だけのデートことり"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》', '《魔法》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】この能力は1ターンにつき2回まで発動する。あなたのキャラが手札からクロック置場に置かれた時、そのターン中、このカードのパワーを＋3000。
'''


class W23_030( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ずっと変わらない小恋"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《音楽》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードがアタックした時、クライマックス置場に「また会えるよね」があるなら、あなたは自分の控え室の《音楽》のキャラを1枚まで選び、ストック置場に置き、自分の《音楽》のキャラを1枚選び、そのターン中、パワーを＋2500。
'''


class W23_031( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "恋愛実践中！サラ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【起】［手札の《スポーツ》のキャラを1枚控え室に置く］そのターン中、このカードのパワーを＋3500。
'''


class W23_032( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "温もりを感じて茜"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8500
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ()
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードのバトル相手でレベル2以上のキャラがリバースした時、あなたは自分の山札の上から1枚を、ストック置場に置いてよい。
'''


class W23_033( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "マイペースな母娘茜&amp;翠"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ()
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの特徴を持たないキャラすべてに、パワーを+500。　
【永】あなたが自分の手札か舞台のキャラの【起】のコストを払う時、このカードの下のマーカーを、ストック1枚のかわりに控え室に置いてよい。
【自】[あなたのスタンドしているキャラを2枚レストする]このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札の上から1枚を、このカードの下にマーカーとして置く。
'''


class W23_034( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "みんなでセッション！小恋"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《音楽》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《音楽》のキャラが3枚以上なら、このカードのパワーを＋1000。　
'''


class W23_035( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "みんなでセッション！ななか"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》', '《魔法》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】［手札を1枚クロック置場に置く］このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分のクロック置場の《音楽》のキャラを1枚選び、手札に戻す。
'''


class W23_035( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "みんなでセッション！渉"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【起】［あなたの《音楽》のキャラを1枚レストする］そのターン中、このカードのパワーを＋1000。
'''


class W23_037( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "真面目でひたむきサラ　"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 8500
        self.level = 1
        self.cost = 2
        self.soul = 1
        self.feature = ('《魔法》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    ''''''


class W23_038( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "桜色の奇跡ことり"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《音楽》', '《魔法》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】この能力は1ターンにつき2回まで発動する。あなたのキャラが手札からクロック置場に置かれた時、そのターン中、このカードのパワーを+3000。　
【自】アンコール [あなたの山札の上から1枚をクロック置場に置く] (このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、このカードがいた枠にレストして置く) 
'''


class W23_039( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "不器用なすれ違い叶"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ()
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】応援 このカードの前のあなたのキャラすべてに、パワーを+500。　
【起】[手札を1枚控え室に置き、このカードをレストする]あなたは自分の控え室のレベル0以下のカード名に「工藤」を含むキャラを1枚選び、舞台の好きな枠に置く。
'''


class W23_040( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "胸のドキドキみっくん"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《音楽》のキャラすべてに、レベルを+1。　
【自】[①]相手のアタックフェイズの始めに、あなたはコストを払ってよい。そうしたら、あなたは他の自分の《音楽》のキャラを1枚選び、そのターン中、パワーを+1500。
'''

    def permanentEffect(self, player1, player2, position):
        def limit1():  # TODO まとめたい
            if player1.charaExistCheck( 0 ):
                if "音楽" in player1.MYFIELD["Stage"][0][0].feature and player1.MYFIELD["Stage"][0][0] is not self:
                    return True
                else:
                    return False

        def limit2():
            if player1.charaExistCheck( 1 ):
                if "音楽" in player1.MYFIELD["Stage"][1][0].feature and player1.MYFIELD["Stage"][1][0] is not self:
                    return True
                else:
                    return False

        def limit3():
            if player1.charaExistCheck( 2 ):
                if "音楽" in player1.MYFIELD["Stage"][2][0].feature and player1.MYFIELD["Stage"][2][0] is not self:
                    return True
                else:
                    return False

        def limit4():
            if player1.charaExistCheck( 3 ):
                if "音楽" in player1.MYFIELD["Stage"][3][0].feature and player1.MYFIELD["Stage"][3][0] is not self:
                    return True
                else:
                    return False

        def limit5():
            if player1.charaExistCheck( 4 ) and player1.MYFIELD["Stage"][4][0] is not self:
                if "音楽" in player1.MYFIELD["Stage"][4][0].feature and player1.MYFIELD["Stage"][4][0] is not self:
                    return True
                else:
                    return False

        player1.permanentEffect.adaptField(
            player1, player2, (player1, position), [(player1, i) for i in range( 5 )],
            [limit1, limit2, limit3, limit4, limit5],
            [("increaseLevel", lambda: 1) for _ in range( 5 )]
        )

    def startAttackPhase(self, player1, player2, position):
        if player1.turnPlayer is False and player1.MYFIELD["Stage"].searchFeature( player1, "音楽" ):
            if player1.MYFIELD["Stock"].costCheck( 1 ):
                print( "{} : 相手のアタックフェイズのはじめに、1コスト払うことで「音楽」のキャラひとりを+1500".format( self.name ) )
                flag = util.selectNumberChecker( 1, 2, "効果を使いますか？" )
                if flag == 1:
                    player1.MYFIELD["Stage"].showStage()
                    while True:
                        select_card = util.selectNumberChecker( 1, 5, "キャラを選んでください" )
                        if player1.charaExistCheck( select_card - 1 ):
                            if select_card - 1 == position:
                                if "音楽" in player1.MYFIELD["Stage"][select_card - 1][0].feature:
                                    player1.permanentEffect.adaptField(
                                        player1, player2, (player1, position), [(player1, select_card - 1)],
                                        lambda: True,
                                        [("increasePower", lambda: 1500)]
                                    )
                                    break
                                else:
                                    print( "音楽のキャラを選んでください" )
                            else:
                                print( "自身へ効果を使うことはできません" )

                        else:
                            print( "キャラがいません" )


class W23_041( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "憧れのバンドともちゃん"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】この能力は1ターンにつき2回まで発動する。あなたのキャラが手札からクロック置場に置かれた時、そのターン中、このカードのパワーを+2000。
'''


class W23_042( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "海でのんびり姫乃"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》', '《水着》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードがアタックした時、あなたは他の自分のキャラを1枚選び、そのターン中、レベルを+1し、パワーを+1000。
'''


class W23_043( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "浴衣で盆踊り小恋"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》', '《和服》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】このカードはダイレクトアタックできない。
'''


class W23_044( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "まひるの“家族”ミキ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《ナース》', '《たとえ話》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】[あなたのスタンドしているキャラを2枚レストする]このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分のキャラを1枚選び、そのターン中、次の能力を与える。『【自】このカードのバトル相手がリバースした時、あなたは自分の山札から1枚を、ストック置場に置いてよい。』
'''


class W23_045( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "想いを言葉にことり"
        self.color = None
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》', '《魔法》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】［手札を1枚クロック置き場に置く］あなたがこのカードの『助太刀』を使った時、あなたはコストを払ってよい。そうしたら、あなたは自分のバトル中のキャラを1枚選び、そのターン中、パワー＋3000。
【起】●助太刀1000 レベル1［手札のこのカードを控え室に置く］(あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋1000)
'''


class W23_046( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "二人の未来環"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》', '《巫女》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードがアタックした時、あなたは自分の山札の上から1枚を公開する。そのカードが《魔法》のキャラなら、そのターン中、このカードのパワーを+2000。(公開したカードは元に戻す)
'''


class W23_046( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "それぞれの想いななか"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 4000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《音楽》', '《魔法》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】この能力は1ターンにつき1回まで発動する。あなたが【起】を使った時、あなたは自分のキャラを1枚選び、そのターン中、パワーを+2000。　
【自】◆ シフト レベル2 (あなたのメインフェイズの始めに、あなたは自分の手札の緑のカードを1枚とクロック置場のこのカードを選び、入れ替えてよい) 
'''


class W23_048( EVENT ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "姫乃の覚悟"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 2
        self.counter = False
        self.useCardLimit = None

    ''''''


class W23_049( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "かけがえのない家族"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None

    ''''''


class W23_050( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "また会えるよね"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('宝',)
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


class W23_051( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "二人の時間由夢"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《魔法》のキャラが3枚以上なら、このカードのパワーを＋1000。
【自】このカードのバトル相手がリバースした時、あなたは自分の山札の上から1枚を、控え室に置く。そのカードがクライマックスなら、あなたは自分の控え室の《魔法》のキャラを1枚選び、手札に戻してよい。
'''


class W23_052( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "溢れる気持ち音夢"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《魔法》', '《ドレス》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分のクロックの上から1枚を、控え室に置いてよい。
【自】［① 手札を1枚控え室に置く］あなたのクライマックス置場に「誓いのキス」が置かれた時、前列にこのカードがいるなら、あなたはコストを払ってよい。そうしたら、あなたは相手のコスト1以下のキャラを1枚選び、山札の上に起き、そのターン中、このカードのパワーを＋2000。
'''


class W23_053( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "あらたなる旅立ち美夏"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《メカ》', '《バナナ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】記憶 あなたの思い出置場に「ワン・オブ・サウザンド」か「バナナパフェ」があるなら、このカードは次の能力を得る。『【自】このカードがリバースした時、あなたはこのカードのバトル相手をリバースしてよい。』
'''


class W23_054( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "昔の思い出音夢"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》', '《風紀委員》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたのストックが2枚以下なら、このカードのレベルを＋1し、パワーを＋1000。
'''


class W23_055( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "恋人の証美春"
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

    '''【自】［あなたの山札の上から1枚をクロック置場に置き、このカードを手札に戻す］あなたのクライマックス置場に「美春の気持ち」が置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見てレベル0以下の《バナナ》のキャラを1枚まで選び、このカードがいた枠に置く。その山札をシャッフルする。
'''


class W23_056( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "優しいキス由夢"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分のストックの下から1枚を、控え室に置く。
'''


class W23_057( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "凛とした風格エリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《生徒会》', '《王族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【起】［あなたの【自】アンコール［手札のキャラを1枚控え室に置く］を持つキャラを1枚レストする］そのターン中、このカードは次の能力を得る。『【自】このカードのバトル相手がリバースした時、あなたはそのキャラを山札の上に置いてよい。』
'''


class W23_058( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "個人レッスンエリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《生徒会》', '《王族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】応援 このカードの前のあなたのキャラすべてに、パワーを+500。　
【自】アンコール[手札のキャラ1枚を控え室に置く](このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、このカードがいた枠にレストして置く。)
'''


class W23_059( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“友達”という宝物舞佳"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの前列のキャラがいないなら、このカードのパワーを+1500。　
【永】舞台にこのカードがいるなら、このカードは《鍋》を得る。
'''


class W23_060( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "手作りの紫陽花由夢"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚を公開する。そのカードが《魔法》のキャラなら、そのターン中、このカードは次の能力を得る。『【自】このカードがリバースした時、このカードのバトル相手のレベルが1以下なら、あなたはそのキャラをリバースしてよい。』(公開したカードは元に戻す)
'''


class W23_061( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "お慕いしています!忍"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《忍》', '《愛》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】相手のクライマックスがクライマックス置場に置かれた時、あなたはこのカードをストック置場に置いてよい。
'''


class W23_062( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "帰ってきた笑顔美夏"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 2500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《メカ》', '《バナナ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】［② あなたの舞台のキャラを1枚控え室に置く］あなたがこのカードの『助太刀』を使った時、あなたはコストを払ってよい。そうしたら、あなたは相手の、レベルが相手のレベルより高いキャラを1枚選び、控え室に置く。 　
【起】● 助太刀2500 レベル2［① 手札のこのカードを控え室に置く］(あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋2500)
'''

    def counterEffect(self, player1, player2, attacked_chara):
        print( "{} : カウンター(2500)。2コスト、自分の舞台のキャラを1枚控室に置くことで、相手の早出しキャラを1枚控室に送る"
               .format( self.name ) )
        player1.untilTurnEndEffect.adaptField( player1, player2, (player1, attacked_chara),
                                               [(player1, attacked_chara)], [lambda: True],
                                               [("increasePower", lambda: 2500)]
                                               )

        charaExistFlag = False
        costFlag = False
        levelOverCharaExist = False
        for i in range( 5 ):
            if player1.charaExistCheck( i ) is True:
                charaExistFlag = True
                break
        for i in range( 5 ):
            if player2.charaExistCheck( i ) and player2.MYFIELD["Stage"][i][0].level > player2.level:
                levelOverCharaExist = True
        if player1.MYFIELD["Stock"].costCheck( 2 ):
            costFlag = True
        if charaExistFlag and costFlag and levelOverCharaExist:
            confirmFlag = util.effectConfirm()
            if confirmFlag == 1:
                player1.useCost( 2 )

                # コストとして自分のキャラを控室に送る
                player1.MYFIELD["Stage"].showStage()
                while True:
                    select_chara = util.selectNumberChecker( 1, 5, "控室に置くカードを選んでください : " )
                    if player1.charaExistCheck( select_chara - 1 ):
                        print( "{} を控室に送ります".format( player1.MYFIELD["Stage"][select_chara - 1][0].name ) )
                        player1.MYFIELD["Stage"].leaveStageChara(
                            player1, player2, select_chara - 1, player1.MYFIELD["Waiting_Room"]
                        )
                        break
                    else:
                        print( "キャラがいません" )

                # 早出しキャラへの処理
                print( "相手の早出しキャラを控室に送ります" )
                player2.MYFIELD["Stage"].showStage()
                while True:
                    select_level_over_chara = util.selectNumberChecker( 1, 5, "カードを選んでください" )
                    if player2.charaExistCheck( select_level_over_chara - 1 ) and \
                            player2.MYFIELD["Stage"][select_level_over_chara - 1][0].level > player2.level:
                        print( "{} を控室に送ります".format( player2.MYFIELD["Stage"][select_level_over_chara - 1][0].name ) )
                        if player2.MYFIELD["Stage"][select_level_over_chara - 1][0].status == util.Status.STAND:
                            player2.standCount -= 1
                        player2.MYFIELD["Stage"].leaveStageChara(
                            player2, player1, select_level_over_chara - 1, player2.MYFIELD["Waiting_Room"]
                        )
                        break
                    else:
                        print( "このカードは選べません" )


class W23_063( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "世話焼きナース音夢"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 3000
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('《魔法》', '《ナース》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】応援このカードの前のあなたのキャラすべてに、パワーを＋Ｘ。Ｘはあなたの「応援」を持つキャラの枚数×1000に等しい。
'''


class W23_064( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“怪盗プリンセス”エリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《生徒会》', '《王族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】舞台にこのカードがいるなら、このカードは《怪盗》を得る。
'''


class W23_T12( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "先輩とバナナ美春"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《メカ》', '《バナナ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたのレベルが1以上なら、このカードはあなたのスタンドフェイズにスタンドしない。
'''


class W23_066( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ふたりだけの時間美夏"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《メカ》', '《バナナ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの前列の中央の枠のキャラに、パワーを+X。Xはそのキャラのコスト×1000に等しい。
'''


class W23_067( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "愛故の戦いななこ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《メガネ》', '《漫画》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【起】[①]そのターン中、このカードは次の能力を得る。『【自】このカードがリバースした時、このカードのバトル相手のレベルが1以下なら、あなたはそのキャラをリバースしてよい。』
'''


class W23_068( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "楽しい時間音夢"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》', '《ナース》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    ''''''


class W23_069( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "普段着はバニー！？美琴"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《新聞》', '《愛》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードのバトル相手がリバースした時、あなたのストックが3枚以下なら、あなたはそのキャラを山札の上に置いてよい。
'''


class W23_070( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "楽しいお買い物μ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 4500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《メカ》', '《メイド》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードがリバースした時、このカードのバトル相手のレベルが2以下なら、あなたはそのキャラをリバースしてよい。　
【自】バトル中のこのカードがリバースした時、あなたは自分のキャラを1枚選び、そのターン中、パワーを+1000。
'''


class W23_071( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ネコミミ由夢"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》', '《動物》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】この能力は1ターンにつき2回まで発動する。他のあなたの《魔法》のキャラが、手札から舞台に置かれた時、そのターン中、このカードのパワーを+1000。
'''


class W23_072( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "リオ&amp;フローラ&amp;ジェイミー"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《宇宙人》', '《王族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《王族》のキャラが2枚以上なら、このカードは『アンコール[手札のキャラを1枚控え室に置く]』を得る。
'''


class W23_073( EVENT ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ワン・オブ・サウザンド"
        self.color = util.Color.RED
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 1
        self.counter = False
        self.useCardLimit = None

    ''''''


class W23_052( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "誓いのキス"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('扉',)
        self.useCardLimit = None

    ''''''


class W23_075( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "美春の気持ち"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None

    ''''''


class W23_076( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "小さな神秘杏"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 3000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》', '《演劇》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】応援 このカードの前のあなたのキャラすべてに、パワーを＋Ｘ。Ｘはそのキャラのレベル×500に等しい。
【自】［②］このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見て《魔法》か《演劇》のキャラを1枚まで選んで相手に見せ、手札に加える。その山札をシャッフルする。
'''

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
        print( "{} 登場時2コストで魔法をサーチすることができる".format( self.name ) )
        if player1.MYFIELD["Stock"].costCheck( 2 ):
            flag = util.effectConfirm()
            if flag == 1:
                for i, card in enumerate( player1.MYFIELD["Deck"] ):
                    print( "{} : {}".format( i + 1, card.name ) )

                while True:
                    select_card = util.selectNumberChecker( 1, len( player1.MYFIELD["Deck"] ), "サーチするカードを選んでください" )
                    if "魔法" in player1.MYFIELD["Deck"][select_card - 1].feature:
                        player1.useCost( 2 )
                        print( "{} を手札に加えます".format( player1.MYFIELD["Deck"][select_card - 1].name ) )
                        player1.MYFIELD["Deck"].turnOver( player1, select_card - 1 )
                        player1.MYFIELD["Hand"].append( player1.MYFIELD["Event_Zone"].pop() )
                        player1.MYFIELD["Deck"].shuffle()
                        break
                    else:
                        print( "魔法を選んでください" )


class W23_077( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "夢のような夜葵"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《新聞》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】あなたのクライマックスがクライマックス置場に置かれた時、そのターン中、このカードのパワーを＋1500。
【自】あなたのクライマックス置場に「“お兄ちゃん”へ」が置かれた時、前列にこのカードがいるなら、あなたは自分の控え室の「“お兄ちゃん”へ」を1枚選び、山札に戻してよい。そうしたら、その山札をシャッフルする。
【自】このカードがフロントアタックされた時、あなたは自分の山札を上から1枚見て、山札の上か控え室に置く。
'''


class W23_078( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "アツアツな二人萌"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》', '《鍋》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《鍋》のキャラすべてに、パワーを＋500。
【起】［① このカードをレストする］あなたは2枚引き、自分の手札を2枚選び、控え室に置く。
'''


class W23_079( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "銀色の旋律眞子"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《音楽》', '《鍋》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードがアタックした時、クライマックス置場に「大切なフルート」があるなら、あなたは自分の《音楽》のキャラを1枚選び、そのターン中、パワーを＋2000。
'''


class W23_080( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "愛しの先輩まゆき"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《生徒会》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】他のあなたの《スポーツ》のキャラがアタックした時、そのターン中、このカードのパワーを＋1000。
【自】チェンジ［① 手札を1枚控え室に置き、このカードを思い出にする］あなたのアンコールステップの始めに、このカードがレストしているなら、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「さらなる高みへ まゆき」を1枚選び、このカードがいた枠に置く。
'''


class W23_081( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "笑顔のロボット麻耶"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《委員長》', '《メカ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】この能力は1ターンにつき2回まで発動する。他のあなたの《メカ》のキャラが、手札から舞台に置かれた時、そのターン中、このカードのパワーを＋1000。
【自】この能力は1ターンにつき2回まで発動する。他のあなたの《委員長》のキャラが、手札から舞台に置かれた時、そのターン中、このカードのパワーを＋1000。
'''


class W23_082( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ニコニコ笑顔葵"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《新聞》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】この能力は1ターンにつき1回まで発動する。あなたが【起】を使った時、そのターン中、このカードのパワーを＋1500。
【自】［あなたの山札の上から1枚をクロック置場に置く］このカードのバトル相手がリバースした時、あなたはコストを払ってもよい。そうしたら、あなたは1枚引く。
'''


class W23_083( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "照れ隠しまゆき"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《生徒会》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】相手のターン中、他のあなたの《生徒会》のキャラ1枚につき、このカードのパワーを+500。　
【自】他のあなたの《スポーツ》のキャラがアタックした時、そのターン中、このカードのパワーを+1000。
'''


class W23_084( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "Vサイン杏"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》', '《演劇》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】[①]相手のアタックフェイズの始めに、あなたはコストを払ってよい。そうしたら、そのターン中、このカードのパワーを+2000。
'''


class W23_085( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ゆったりとした時間莉乃"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《ドングリ》', '《美術》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】[② このカードを手札に戻す]相手のアタックフェイズの始めに、あなたはコストを払ってよい。そうしたら、あなたは他の自分のキャラを1枚選び、手札に戻す。
'''


class W23_086( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "彼女の手料理眞子"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《音楽》', '《鍋》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、そのターン中、このカードのパワーを-1500。
'''


class W23_087( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "仮説から真相へ杏"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8000
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('《演劇》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】あなたのキャラが手札から控え室に置かれた時、そのターン中、このカードは『アンコール[①]』を得る。
'''


class W23_088( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "新しい未来萌"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《音楽》', '《鍋》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《鍋》のキャラ1枚につき、このカードのパワーを＋500。
【自】このカードが手札から舞台に置かれた時、あなたは自分のクロックの上から1枚を、控え室に置いてよい。 
'''


class W23_089( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "帰ってきたSSP麻耶　"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《委員長》', '《パジャマ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】［このカードを控え室に置く］他のあなたのキャラが舞台から控え室に置かれた時、後列にこのカードがいるなら、あなたはコストを払ってよい。そうしたら、そのキャラをそのキャラがいた枠にレストして置く。 
'''


class W23_090( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“恋する<ruby><rb>10JQKAFL</rb><rp>(</rp><rt>ロイヤル☆ストレートフラッシュ</rt><rp>)</rp></ruby>”椎恋"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《動物》', '《ポーカー》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚を公開する。そのカードがクライマックスなら、次の相手のターンの終わりまで、このカードのパワーを+3000。(公開したカードは元に戻す)
'''


class W23_091( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "浜辺で水遊び葵　"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《新聞》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    ''''''


class W23_092( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "一番のドキドキアリス"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《人形》', '《かき氷》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】バトル中のこのカードがリバースした時、このカードを山札の下に置く。
'''


class W23_093( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "姉妹の“イノチ”香澄"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《霊》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】[① このカードを思い出にする]他のあなたのキャラが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、そのキャラを手札に戻す。
'''


class W23_094( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "毒舌メイドさん杏"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《演劇》', '《メイド》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたの手札が5枚以上なら、このカードのパワーを+1000。 
'''


class W23_095( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "夢の世界へ萌"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 7000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《音楽》', '《鍋》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    ''''''


class W23_096( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "さらなる高みへまゆき"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《生徒会》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】[あなたの山札の上から1枚をクロック置場に置く]このカードのバトル相手がリバースした時、あなたはコストを払ってよい。そうしたら、あなたは1枚引く。
'''


class W23_097( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "混ぜるな危険！杉並＆杉並"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《新聞》', '《オカルト》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたの手札が6枚以上なら、このカードのパワーを＋1500。 
'''


class W23_098( EVENT ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ずっと一緒に、ずっと笑顔で。"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 0
        self.counter = False
        self.useCardLimit = None

    ''''''


class W23_099( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“お兄ちゃん”へ"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('本',)
        self.useCardLimit = None

    ''''''


class W23_100( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "大切なフルート"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None

    ''''''
