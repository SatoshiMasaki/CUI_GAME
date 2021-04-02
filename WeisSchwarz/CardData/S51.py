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


class S51_001(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "オン・ステージアスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 あなたのターン中、他のあなたのキャラすべてに、パワーを＋500。
【起】 集中 ［① あなたのキャラを2枚レストする］ あなたは自分の山札の上から4枚をめくり、控え室に置く。それらのカードのクライマックス1枚につき、あなたは自分の山札を見て《アバター》か《ネット》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''
    def permanentEffect(self, player1, player2, position):
        if player1.turnPlayer is True:
            pass

    def startUpEffect(self, player1, player2, position):
        player1.useCost(1)
        self.status = util.Status.REST
        search_count = player1.cardEffect.CharaEffect.concentration( player1, player2, position )
        if search_count != 0:
            pass # TODO サーチ


class S51_002(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "流星の約束アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、あなたは自分の山札の上から2枚を、控え室に置く。それらのカードにクライマックスがあるなら、そのターン中、このカードのソウルを＋2。
【自】［あなたのストックの上から1枚をクロック置場に置き、このカードを思い出にする］ バトル中のこのカードがリバースした時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室のカード名に「キリト」か「アスナ」か「ユイ」を含むキャラを1枚選び、手札に戻す。
'''
    

class S51_003(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "恐怖の克服アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、あなたは自分のクロックの上から1枚を、控え室に置いてよい。
【自】CXコンボ［手札を2枚控え室に置く］ このカードがアタックした時、クライマックス置場に「《マザーズ・ロザリオ》」があるなら、あなたはコストを払ってよい。そうしたら、あなたは自分の山札の上から11枚を、控え室に置き、相手にＸダメージを与え、そのターン中、このカードのパワーを＋3000。Ｘはそれらのカードのトリガーアイコンのソウルマークの合計に等しい。（ダメージキャンセルは発生する）
'''
    

class S51_004(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "公園デート明日奈"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、あなたは自分の、《アバター》か《ネット》のキャラを1枚選び、そのターン中、パワーを＋1500。
【自】 絆／「“連携攻撃”キリト」 ［手札を1枚控え室に置く］ （このカードがプレイされて舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「“連携攻撃”キリト」を1枚選び、手札に戻す）
'''
    

class S51_005(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "キリトの恋人アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】このカードはサイドアタックできない。
【自】CXコンボ［このカードのバトル相手がリバースした時、あなたのクライマックス置場に「変わらない気持ち」があるなら、あなたは自分の山札を見て《アバター》か《ネット》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''
    

class S51_006(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "おやつタイム明日奈"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 3500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 応援 このカードの前のあなたのキャラすべてに、パワーを＋Ｘ。Ｘはそのキャラのレベル×500に等しい。
【自】 このカードが手札から舞台に置かれた時、あなたは自分のキャラを1枚選び、そのターン中、パワーを＋1500し、次の能力を与える。『【永】 このカードは相手の効果に選ばれない。』
'''
    

class S51_007(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《閃光》アスナ&amp;《黒の剣士》キリト"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 あなたのクロック置場に「“本気になる時”キリト」があるなら、あなたの手札のこのカードのレベルを－1。
【永】 他のあなたの、《アバター》か《ネット》のキャラ1枚につき、このカードのパワーを＋500。
【自】 このカードが手札から舞台に置かれた時、あなたは1枚まで引き、自分の手札のコスト1以下のキャラを1枚まで選び、舞台の好きな枠に置く。
'''
    

class S51_008(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“連携攻撃”アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードがアタックした時、あなたは自分の、《アバター》か《ネット》のキャラを1枚選び、そのターン中、パワーを＋1500。
【自】 このカードが「“連携攻撃”キリト」の【自】の効果で舞台に置かれた時、あなたは自分の控え室の、《アバター》か《ネット》のキャラを1枚選び、ストック置場に置いてよい。
'''
    

class S51_009(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "待ち遠しい約束の日アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 舞台のこのカードのレベルを－1。
【自】 バトル中のこのカードがリバースした時、このカードを山札の下に置く。
'''
    

class S51_010(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "約束を胸にアスナ&amp;キリト"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 4500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 記憶 あなたの思い出置場に「流星の約束 アスナ」があるなら、このカードのパワーを＋5000し、ソウルを＋1。
'''
    

class S51_011(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "今日のMVPアスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 5000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、あなたは1枚引き、自分の手札を1枚選び、控え室に置く。
【自】 このカードがリバースした時、このカードのバトル相手のレベルが相手のレベルより高いなら、あなたはそのキャラをストック置場に置いてよい。そうしたら、あなたは相手のストックの下から1枚を、控え室に置く。
'''
    

class S51_012(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "魅惑の渚アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】［手札の《アバター》か《ネット》のキャラを1枚控え室に置く］あなたのキャラのトリガーチェックでクライマックスがでた時、そのカードのトリガーアイコンがソウル×2なら、コストを払ってよい。そうしたら、あなたは自分の山札を上から2枚まで見て、カードを1枚まで選び、手札に加え、残りのカードを控え室に置く。
【起】［①このカードをレストする］あなたは自分の山札の上から1枚を公開する。そのカードが《アバター》か《ネット》のキャラなら手札に加える。（そうでないなら元に戻す）
'''
    

class S51_013(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ボスバトルに挑戦アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたの「柔らかな表情 キリト」すべてに、パワーを＋1000し、ソウルを＋1。
'''
    

class S51_014(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "大切な習慣明日奈"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 記憶 あなたの思い出置場に「流星の約束 アスナ」があるなら、このカードのパワーを＋1000し、ソウルを＋1。
【自】 アンコール ［手札のキャラを1枚控え室に置く］ （このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、このカードがいた枠にレストして置く）
'''
    

class S51_016(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "戦闘準備アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 1000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 あなたがこのカードの『助太刀』を使った時、あなたのキャラすべてが《アバター》か《ネット》なら、あなたは自分の山札の上から1枚を、ストック置場に置いてよい。
【起】● 助太刀2000 レベル1 ［① 手札のこのカードを控え室に置く］ （あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋2000）
'''
    

class S51_017(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“天才ゲームデザイナー”茅場"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 2
        self.cost = 3
        self.soul = 3
        self.feature = ('《ネット》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 バトル中のこのカードがリバースした時、あなたは自分の山札の上から1枚を、クロック置場に置き、このカードをレストする。
'''
    
    
class S51_018(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "不意の呟き"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 0
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S51_019(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《マザーズ・ロザリオ》(S51)"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None
    ''''''
    
    
class S51_020(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "変わらない気持ち"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None
    ''''''
    

class S51_021(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "兄想いな妹リーファ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 0
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 この能力は1ターンにつき1回まで発動する。あなたが【起】を使った時、あなたは自分のキャラを1枚選び、そのターン中、パワーを＋1000。
【自】［①］ あなたのクライマックスがクライマックス置場に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を上から4枚まで見て、《アバター》か《ネット》のキャラを1枚まで選んで相手に見せ、手札に加え、残りのカードを控え室に置く。
'''
    

class S51_022(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《歌姫》ユナ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《ネット》', '《音楽》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】自分の控え室のクライマックスが2枚以下なら、手札のこのカードのレベルを-1。
【自】このカードが手札から舞台に置かれた時、あなたは自分のクロックの上から1枚を、控え室に置いてよい。
【自】このカードがアタックした時、あなたは他の自分の、《アバター》か《ネット》のキャラを1枚選び、そのターン中、パワーを+X。Xは他のあなたの、《アバター》か《ネット》のキャラの枚数×500に等しい。
'''
    

class S51_023(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "剣道合宿直葉"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたのキャラすべてに、次の能力を与える。『【永】 このカードはサイドアタックできない。』
【自】［① 手札を1枚控え室に置く］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見て《アバター》か《ネット》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''


class S51_024(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "水着の直葉"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、あなたは相手の前列のキャラを1枚選び、そのターン中、パワーを＋1000。
【自】 この能力は1ターンにつき1回まで発動する。あなたが【起】を使った時、そのターン中、このカードのパワーを＋1500。
'''
    

class S51_025(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“ARアイドル”ユナ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》', '《音楽》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 このカードの正面のキャラのレベルがこのカードのレベルより高いなら、このカードはフロントアタックできない。
【自】CXコンボ このカードがアタックした時、クライマックス置場に「夢だった大舞台」があるなら、あなたは自分のストックの上から1枚を、手札に戻してよい。
'''
    

class S51_026(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "意味深な言動ユナ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 6000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《ネット》', '《音楽》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 記憶 あなたの思い出置場の、《アバター》か《ネット》のキャラが2枚以上なら、このカードのパワーを＋4000。
【自】 アンコール ［手札の、《アバター》か《ネット》のキャラを1枚控え室に置く］ （このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、このカードがいた枠にレストして置く）
'''
    

class S51_027(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "誘いの挑発エイジ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】CXコンボ［あなたのクライマックス置場の「オーディナル・ナンバー2」を1枚クロック置場に置く］ このカードがアタックした時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の、《アバター》か《ネット》のキャラを4枚まで選び、ストック置場に好きな順番で置き、そのターン中、このカードのソウルを＋1。
【自】 バトル中のこのカードがリバースした時、このカードを思い出にする。
'''
    

class S51_028(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "不在の歯がゆさリーファ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードがアタックした時、そのターン中、このカードのパワーを＋Ｘ。Ｘは他のあなたの、《アバター》か《ネット》のキャラの枚数×1000に等しい。
【自】 この能力は1ターンにつき1回まで発動する。このカードが手札から舞台に置かれたターン中、このカードのバトル相手がリバースした時、あなたは自分の山札の上から1枚を、控え室に置く。そのカードのトリガーアイコンにソウルマークがあるなら、このカードをスタンドする。
'''
    

class S51_029(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "瞬刻の身ごなしエイジ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、あなたは相手のストックの上から1枚を、控え室に置いてよい。そうしたら、あなたは相手の控え室のカードを1枚選び、ストック置場に置く。
【自】［①］ 相手のターン中、バトル中のこのカードがリバースした時、あなたはコストを払ってよい。そうしたら、このカードをレストし、次のあなたのアンコールステップの始めに、このカードを控え室に置く。
'''
    

class S51_030(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "記憶の欠片ユナ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》', '《音楽》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 あなたがこのカードの『助太刀』を使った時、あなたは自分のクロックの「守りたかった笑顔 ユナ」を1枚選び、ストック置場に置いてよい。
【起】●助太刀1000 レベル1 ［手札のこのカードを控え室に置く］ （あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋1000）
'''
    

class S51_031(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "自信に満ちた横顔エイジ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、あなたは相手の思い出置場の表向きのカードを1枚選び、裏向きにしてよい。そうしたら、あなたのターンの終わりに、そのカードを表向きにする。
【自】［②］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは相手のキャラを1枚選び、相手の舞台のキャラのいない他の枠に動かす。
'''
    

class S51_032(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《血盟騎士団》ノーチラス"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 あなたはイベントと『助太刀』を手札からプレイできない。
'''
    

class S51_033(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《オーグマー》開発者重村"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《ネット》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 応援 このカードの前のあなたの、《アバター》か《ネット》のキャラすべてに、パワーを＋Ｘ。Ｘはそのキャラのレベル×500に等しい。
【起】［このカードをレストする］ あなたは自分の控え室の「大歓声の中 ユナ」を1枚選び、思い出にする。
【起】［② あなたの舞台の「自信に満ちた横顔 エイジ」を1枚思い出にする］ あなたは自分の山札を見てレベルＸ以下のカード名に「ユナ」を含むキャラを2枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。Ｘはあなたの思い出置場の「大歓声の中 ユナ」の枚数に等しい。
'''
    

class S51_034(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "スペシャルステージユナ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 5000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《ネット》', '《音楽》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたの、《アバター》か《ネット》のキャラすべてに、パワーを＋1000。
【自】 このカードが手札から舞台に置かれた時、あなたは自分のキャラを1枚選び、そのターン中、次の能力を与える。『【自】［①］ このカードのバトル相手がリバースした時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見て《アバター》か《ネット》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。』
'''
    

class S51_035(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《AnIncarnateoftheRadius》"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《エネミー》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、あなたは2枚まで引き、自分の手札を1枚選び、控え室に置く。
【自】CXコンボ［② 手札を4枚控え室に置き、あなたのクライマックス置場の「白の聖大樹」を1枚このカードの下にマーカーとして裏向きに置く］ あなたのアンコールステップの始めに、前列にこのカードがいるなら、あなたはコストを払ってよい。そうしたら、あなたは自分のクロックすべてを、控え室に置く。
【自】CXコンボ［⑥ 手札を3枚控え室に置き、このカードの下のマーカーを1枚控え室に置く］ 相手のアンコールステップの始めに、あなたはコストを払ってよい。そうしたら、次の行動を2回行う。『相手に3ダメージを与える。』（ダメージキャンセルは発生する）
'''
    

class S51_036(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "謎の青年剣士エイジ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】他のあなたのカード名に「ユナ」を含むキャラがいるなら、このカードのパワーを+3000。
【自】［このカードを控え室に置く］他のあなたのカード名に「ユナ」を含むキャラがフロントアタックされた時、あなたはコストを払ってよい。そうしたら、あなたは自分のバトル中のキャラを1枚選び、そのターン中、パワー+1000。
'''
    

class S51_037(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "一人の乾杯鋭二"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、相手の前列のキャラが1枚以下なら、あなたは相手の前列のキャラを1枚選び、そのターン中、パワーを－3000。
'''
    

class S51_038(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "歌が大好きユナ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》', '《音楽》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【起】［このカードをレストする］ あなたは自分の、《アバター》か《ネット》のキャラを1枚選び、そのターン中、パワーを＋1500。
'''
    

class S51_039(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "大歓声の中ユナ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》', '《音楽》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】［あなたのストックの上から1枚をクロック置場に置く］ このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分のクロックを1枚選び、手札に戻し、自分の山札の上から1枚を、クロック置場に置く。
'''
    

class S51_040(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "東都工業大学教授重村"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】［手札を1枚クロック置場に置く］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見てカード名に「ユナ」か「エイジ」を含むキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''
    

class S51_041(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "守りたかった笑顔ユナ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《音楽》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    

class S51_042(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "魔法攻撃リーファ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】CXコンボ このカードのバトル相手がリバースした時、あなたのクライマックス置場に「妖精たちの援護」があるなら、あなたは自分の控え室の、《アバター》か《ネット》のキャラを1枚まで選び、ストック置場に置き、自分の山札の上から1枚を公開する。そのカードのレベルが1以上なら手札に加える。（クライマックスのレベルは0として扱う。そうでないなら元に戻す）
'''
    

class S51_043(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "しっかり者の妹リーファ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたのキャラすべてに、次の能力を与える。『【永】 このカードはサイドアタックできない。』
【自】 この能力は1ターンにつき1回まで発動する。あなたが【起】を使った時、そのターン中、このカードのパワーを＋Ｘ。Ｘは他のあなたの、《アバター》か《ネット》のキャラの枚数×500に等しい。
'''
    
    
class S51_044(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "盾による対抗"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 3
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S51_045(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "オーディナル・スケール"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 0
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S51_046(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "SAO事件記録全集"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 0
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S51_047(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "夢だった大舞台"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None
    ''''''
    
    
class S51_048(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "オーディナル・ナンバー2"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None
    ''''''
    
    
class S51_049(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "白の聖大樹"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('宝',)
        self.useCardLimit = None
    ''''''
    
    
class S51_050(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "妖精たちの援護"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('宝',)
        self.useCardLimit = None
    ''''''
    

class S51_051(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "折れない意思リズベット"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 あなたの後列のキャラが1枚以下なら、このカードはアタックできない。
【自】CXコンボ［①］ このカードがアタックした時、クライマックス置場に「年季入りのパーティプレイ」があるなら、あなたはコストを払ってよい。そうしたら、あなたは他の自分のキャラを1枚と、このカードを選び、そのターン中、次の能力を与える。『【自】 このカードのバトル相手がリバースした時、あなたは自分の控え室のキャラを1枚選び、手札に戻してよい。』
'''
    

class S51_052(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“連携攻撃”シリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 あなたのキャラすべてが《アバター》か《ネット》なら、このカードのパワーを＋1500し、このカードは次の能力を得る。『【永】 このカードのバトル中、相手は『助太刀』を手札からプレイできない。』
【自】 このカードが手札から舞台に置かれた時か「“連携攻撃”キリト」の【自】の効果で舞台に置かれた時、あなたは自分のクロックの上から1枚を、控え室に置いてよい。
'''
    

class S51_053(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "オン・ステージシリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 応援 このカードの前のあなたのキャラすべてに、パワーを＋500。
【起】［① このカードをレストする］ あなたは自分の、《アバター》か《ネット》のキャラを1枚選び、そのターン中、次の能力を与える。『【自】 このカードのバトル相手がリバースした時、あなたは自分の控え室のキャラを1枚選び、手札に戻してよい。』
'''
    

class S51_054(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "さっぱりとした性格リズベット"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 他のあなたのバトル中のキャラがリバースした時、あなたは自分の、《アバター》か《ネット》のキャラを1枚選び、そのターン中、パワーを＋1500。
【自】［①］ あなたのキャラのトリガーチェックでクライマックスがでた時、そのカードのトリガーアイコンがソウルマーク×2なら、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室のキャラを1枚選び、手札に戻し、自分の手札を1枚選び、控え室に置く。
'''
    

class S51_055(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "にぎやかな放課後里香"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、あなたは自分の山札の上から2枚を、控え室に置き、そのターン中、このカードのパワーを＋Ｘ。Ｘはそれらのカードの、《アバター》か《ネット》のキャラの枚数×1000に等しい。
'''
    

class S51_056(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "身構えるシリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたの、《アバター》か《ネット》のキャラが2枚以上なら、このカードのパワーを＋1500し、このカードは『【自】 アンコール ［手札のキャラを1枚控え室に置く］』を得る。
'''
    

class S51_057(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“連携攻撃”リズベット"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時か「“連携攻撃”キリト」の【自】の効果で舞台に置かれた時、あなたは自分の控え室の、《アバター》か《ネット》のキャラを1枚選び、手札に戻してよい。
【自】［手札を2枚控え室に置く］ このカードがアタックした時、あなたはコストを払ってよい。そうしたら、相手に1ダメージを与える。（ダメージキャンセルは発生する）
'''
    

class S51_058(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "危機一髪シリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚を見て、山札の上か控え室に置く。
【自】CXコンボ［このカードを手札に戻す］あなたのクライマックス置場に「非道な罠」が置かれた時、コストを払ってよい。そうしたら、あなたは自分の山札の上から1枚を公開する。そのカードが《アバター》か《ネット》のキャラなら手札に加える。（そうでないなら元に戻す）
'''
    

class S51_0(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "反撃の狼煙リズベット"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードがアタックした時、他のあなたの、《アバター》か《ネット》のキャラが2枚以上なら、そのターン中、このカードのパワーを＋2000。
【自】 この能力は1ターンにつき1回まで発動する。バトル中のこのカードがリバースした時、あなたは自分の山札の上から1枚を公開する。そのカードのレベルが2以上なら、あなたはこのカードをレストしてよい。（クライマックスのレベルは0として扱う。公開したカードは元に戻す）
'''
    

class S51_060(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "弾む切込みシリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 5500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたの前列の中央の枠のキャラに、『【自】 アンコール ［手札のキャラを1枚控え室に置く］』を与える。
【永】 他のあなたの、《アバター》か《ネット》のキャラすべてに、パワーを＋1000。
'''
    

class S51_061(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ボスバトルに挑戦リズベット"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 あなたのターン中、他のあなたの「ボスバトルに挑戦 シリカ」すべてに、パワーを＋2000。
【自】 絆／「ボスバトルに挑戦 シリカ」 ［あなたの山札の上から1枚をクロック置場に置く］ （このカードがプレイされて舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「ボスバトルに挑戦 シリカ」を1枚選び、手札に戻す）
'''
    

class S51_062(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "あきれ顔の珪子"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 バトル中のこのカードがリバースした時、あなたは自分の山札の上から1枚を公開する。そのカードがレベル0以下のキャラなら手札に加える。（そうでないなら元に戻す）
'''
    

class S51_063(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "嬉し気な仕草シリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 あなたのストックが3枚以下なら、このカードのパワーを＋1500。
【永】 このカードの正面のキャラに、『【自】 アンコール ［あなたの山札の上から1枚をクロック置場に置く］』を与える。
'''
    

class S51_064(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ボスバトルに挑戦シリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    

class S51_065(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "あきれ顔の里香"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 2500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【起】● 助太刀3000 レベル2 ［① 手札のこのカードを控え室に置く］ （あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋3000）
'''
    

class S51_066(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "乗り気なリズベット"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 6500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたの、《アバター》か《ネット》のキャラ1枚につき、このカードのパワーを＋1000。
【自】［①］ アンコールステップの始めに、他のあなたの前列のレストしているキャラがいないなら、あなたはコストを払ってよい。そうしたら、このカードをレストする。
'''
    
    
class S51_067(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "歌ってご機嫌"
        self.color = util.Color.RED
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 0
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S51_068(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "かつての強敵"
        self.color = util.Color.RED
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 3
        self.cost = 3
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S51_069(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "年季入りのパーティプレイ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = (util.TriggerType.SOUL_ONE, util.TriggerType.GATE)
        self.useCardLimit = None
    ''''''

    def permanentEffect(self, player):
        for i in range(5):
            if len(player.MYFIELD["Stage"][i]) != 0:
                player.MYFIELD["Stage"][i][0].power += 1000
                player.MYFIELD["Stage"][i][0].soul += 1
                print("{} に効果を使いました".format(player.MYFIELD["Stage"][i][0].name))
                print("パワー : {}".format(player.MYFIELD["Stage"][i][0].power))
                print("ソウル : {}".format(player.MYFIELD["Stage"][i][0].soul))
        return [[1000, 1000, 1000, 1000, 1000], [1, 1, 1, 1, 1]]

    
class S51_070(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "非道な罠"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = (util.TriggerType.SOUL_ONE, util.TriggerType.STANDBY)
        self.useCardLimit = None
    ''''''

    def permanentEffect(self, player): # TODO 電源
        pass


class S51_071(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“本気になる時”キリト"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、そのターン中、このカードのパワーを＋1500。
【自】 このカードのバトル相手がリバースした時、あなたは他の自分の、《アバター》か《ネット》のキャラを1枚選び、レストし、後列のキャラのいない枠に動かす。
'''
    

class S51_072(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“連携攻撃”シノン"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 あなたの、《アバター》か《ネット》のキャラが4枚以上なら、あなたの手札のこのカードのレベルを－1。
【自】 このカードが手札から舞台に置かれた時か「“連携攻撃”キリト」の【自】の効果で舞台に置かれた時、あなたは1枚まで引き、そのターン中、このカードのパワーを＋2000。
【自】［① 手札を2枚控え室に置く］ この能力は1ターンにつき1回まで発動する。あなたの前列の中央の枠のキャラがアタックした時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札の上から3枚を、控え室に置く。それらのカードにクライマックスがあるなら、このカードをスタンドする。
'''
    

class S51_073(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“連携攻撃”キリト"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、あなたは自分の山札を上からＸ枚まで見て、カードを1枚まで選び、手札に加え、残りのカードを控え室に置く。Ｘはあなたの、《アバター》か《ネット》のキャラの枚数に等しい。
【自】CXコンボ［③ 手札を2枚控え室に置き、このカードを控え室に置く］ 他のあなたのキャラがアタックした時、クライマックス置場に「《黒の剣士》再び」があるなら、あなたはコストを払ってよい。そうしたら、あなたは「“連携攻撃”キリト」以外の自分の控え室のカード名に「連携攻撃」を含むキャラを1枚選び、このカードがいた枠に置く。
'''
    

class S51_074(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "半信半疑シノン"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 あなたのストックが2枚以下なら、このカードのパワーを＋1500。
【自】 アンコール ［あなたの舞台の、《アバター》か《ネット》のキャラを1枚クロック置場に置く］ （このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、このカードがいた枠にレストして置く）
'''
    

class S51_075(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《SAO生還者》明日奈＆和人"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 相手のターン中、他のあなたの、《アバター》か《ネット》のキャラすべてに、パワーを＋1000。
【自】 このカードが手札から舞台に置かれた時、あなたは自分の山札を上から2枚まで見て、カードを1枚まで選び、手札に加え、残りのカードを控え室に置き、自分の手札を1枚選び、控え室に置く。
'''
    

class S51_076(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "頼れる助っ人シノン"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたの、《アバター》か《ネット》のキャラ1枚につき、このカードのパワーを＋500。
【自】CXコンボ このカードがアタックした時、クライマックス置場に「信頼の射撃」があるなら、あなたは自分の山札の上から1枚を公開する。そのカードが《アバター》か《ネット》のキャラなら手札に加える。（そうでないなら元に戻す）
'''
    

class S51_077(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ARでの戦いキリト"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードがアタックした時、あなたは他の自分の、《アバター》か《ネット》のキャラを1枚選び、そのターン中、パワーを＋Ｘ。Ｘは他のあなたの、《アバター》か《ネット》のキャラの枚数×500に等しい。
'''
    

class S51_078(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "願ってもない援護ユイ"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 7500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 このカードの正面のキャラのレベルがこのカードのレベルより高いなら、このカードはフロントアタックできない。
【自】CXコンボ［手札を1枚ストック置場に置く］ このカードがアタックした時、あなたはコストを払ってよい。そうしたら、あなたは自分のクライマックス置場の「お待たせしました！」を1枚選び、手札に戻す。
'''
    

class S51_079(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "元気いっぱいユイ"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、そのターン中、このカードのパワーを＋Ｘ。Ｘはあなたの、《アバター》か《ネット》のキャラの枚数×500に等しい。
【自】［手札を2枚控え室に置く］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは相手のストックすべてを、控え室に置き、相手は自分の山札の上から同じ枚数をストック置場に置く。
【自】 相手のターン中、あなたの受けたダメージがキャンセルされなかった時、前列にこのカードがいるなら、あなたは自分の山札を上から1枚見て、山札の上か控え室に置く。
'''
    

class S51_080(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "アスナの恋人キリト"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】応援 このカードの前のあなたのレベル0以下のキャラすべてに、パワーを＋1000。
【自】CXコンボ［②］ あなたのアタックフェイズの始めに、あなたのクライマックス置場にクライマックスがないなら、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見て「約束の続き」を1枚まで選び、クライマックス置場に置き、その山札をシャッフルする。
'''
    

class S51_081(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ＡＲに馴染めない和人"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 絆／「波状攻撃 アスナ」 ［手札を1枚控え室に置く］ （このカードがプレイされて舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「波状攻撃 アスナ」を1枚選び、手札に戻す）
【起】［① このカードを控え室に置く］ あなたは自分の山札を上から4枚まで見て、《アバター》か《ネット》のキャラを1枚まで選んで相手に見せ、手札に加え、残りのカードを控え室に置く。
'''
    

class S51_082(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "デレデレなクライン"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚を公開する。そのカードが《アバター》か《ネット》のキャラなら、そのターン中、このカードのパワーを＋2000。（公開したカードは元に戻す）
【自】 このカードがアタックした時、他のあなたのキャラが1枚以下なら、あなたは自分の山札の上から1枚を、控え室に置いてよい。そのカードがレベル0以下のキャラなら、そのキャラを後列の好きな枠に置く。
'''
    

class S51_083(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "おやつタイムユイ"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、そのターン中、このカードのパワーを＋Ｘ。Ｘはあなたの、《アバター》か《ネット》のキャラの枚数×500に等しい。
【自】［手札を1枚控え室に置く］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「調査の報告」を1枚選び、手札に戻す。
'''
    

class S51_084(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“連携攻撃”エギル"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、あなたは相手の前列のキャラを1枚選び、そのターン中、パワーを＋3000。
【自】［あなたの控え室のキャラを2枚山札に戻し、その山札をシャッフルする］ このカードがアタックした時、あなたはコストを払ってよい。そうしたら、そのターン中、このカードのソウルを＋1。
'''
    

class S51_085(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "データ収集ユイ"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 6000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 応援 このカードの前のあなたのレベル3以上のキャラすべてに、パワーを＋2000。
【自】［① 手札を2枚控え室に置く］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見てカード名に「連携攻撃」を含むキャラを2枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''
    

class S51_086(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "寄り添う二人和人＆明日奈"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7500
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 相手のターン中、他のあなたの、《アバター》か《ネット》のキャラ1枚につき、このカードのパワーを＋1500。
'''
    

class S51_087(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "苦戦に滲む汗エギル"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 相手のターン中、他のあなたのキャラすべてに、パワーを＋500。
【自】［このカードを控え室に置く］ 他のあなたのキャラが舞台から控え室に置かれた時、後列にこのカードがいるなら、あなたはコストを払ってよい。そうしたら、そのキャラをそのキャラがいた枠にレストして置く。
'''
    

class S51_088(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "怒りの対面キリト"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたの「疾風の刺突 アスナ」すべてに、パワーを＋2000。
'''
    

class S51_089(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "鬼神の気迫キリト"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 このカードの下のマーカー1枚につき、このカードのレベルを＋1し、パワーを＋1500。
【自】 このカードのバトル相手がリバースした時、あなたは自分の山札を上から1枚見てよい。そうしたら、あなたはそのカードをこのカードの下にマーカーとして裏向きに置く。
'''
    

class S51_090(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "手掛かりを求めるキリト"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 あなたの手札が5枚以上なら、このカードのパワーを＋2500し、このカードは『【自】 アンコール ［手札のキャラを1枚控え室に置く］』を得る。
'''
    

class S51_091(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "柔らかな表情キリト"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 7000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    

class S51_092(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "クールに論駁シノン"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 2000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 あなたがこのカードの『助太刀』を使った時、あなたの、《アバター》か《ネット》のキャラがいるなら、あなたは自分のバトル中のキャラを1枚選び、そのターン中、パワーを＋1000。
【起】● 助太刀2500 レベル2 ［① 手札のこのカードを控え室に置く］ （あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋2500）
'''
    

class S51_093(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "緊急参戦クライン"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 6500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 あなたの、《アバター》か《ネット》のキャラが4枚以上なら、あなたの手札のこのカードのレベルを－1。
【永】 他のあなたのレベル0以下のキャラ1枚につき、このカードのパワーを＋1000。
'''
    

class S51_094(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "どこか寂しげ和人"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 舞台のこのカードのレベルを－2。
【自】 あなたのクライマックスがクライマックス置場に置かれた時、そのターン中、このカードのパワーを＋Ｘ。Ｘはあなたの、《アバター》か《ネット》のキャラの枚数×500に等しい。
'''
    
    
class S51_096(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "オーディナル・ナンバー1"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 1
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S51_097(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《黒の剣士》再び"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.useCardLimit = None
    ''''''
    
    
class S51_099(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "お待たせしました！"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None
    ''''''
    
    
class S51_100(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "約束の続き"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('本',)
        self.useCardLimit = None
    ''''''
