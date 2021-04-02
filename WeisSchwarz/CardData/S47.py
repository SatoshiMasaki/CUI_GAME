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


class S47_101(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "継がれる剣技アスナ"
        self.color = util.Color.YELLOW
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
    '''【自】 このカードが手札から舞台に置かれた時、そのターン中、このカードのパワーを＋1500。
【自】 このカードのバトル相手が【リバース】した時、あなたのクライマックス置場に「《絶剣》の最期」があり、他のあなたの、《アバター》か《ネット》のキャラが3枚以上なら、あなたは自分の山札を上から3枚まで見て、カードを1枚まで選び、手札に加え、残りのカードを控え室に置く。
'''
    

class S47_102(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "波状攻撃アスナ	"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 5000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 応援 このカードの前のあなたの、《アバター》か《ネット》のキャラすべてに、パワーを＋2000し、次の能力を与える。『【自】 このカードのバトル相手がリバースした時、あなたはそのキャラを思い出にしてよい。』
【自】 このカードが手札から舞台に置かれた時、あなたは自分の山札を見て《アバター》か《ネット》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
【自】［② 手札を1枚控え室に置く］ 他のあなたのキャラがアタックした時、クライマックス置場に「《エクスキャリバー》獲得クエスト」があり、他のあなたの、《アバター》か《ネット》のキャラが4枚以上なら、あなたはコストを払ってよい。そうしたら、あなたは自分の「波状攻撃 キリト」を1枚とこのカードを選び、入れ替える。（カードの向きは変わらない）
'''
    

class S47_103(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "安らぎのひと時アスナ"
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
    '''【自】［あなたの控え室のキャラを2枚山札に戻し、その山札をシャッフルする］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、そのターン中、このカードのソウルを＋1。
【自】 バトル中のこのカードが【リバース】した時、あなたは自分の山札の上から1枚を公開する。そのカードのレベルが1以上なら、あなたはこのカードをストック置場に置いてよい。（クライマックスのレベルは0として扱う。公開したカードは元に戻す）
'''
    def cipEffect(self, player1, _, __):
        flag = util.effectConfirm()
        if flag == 1:
            player1.MYFIELD["Waiting_Room"].showWaitingRoom()
            for _ in range(2):
                pass

    def loseBattle(self, player1, player2, selfPosition, oppositePosition):
        pass
    

class S47_104(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "俊敏な始動アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 8000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 このカードの正面のキャラのレベルがこのカードのレベルより高いなら、このカードはフロントアタックできない。
'''
    

class S47_106(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "夏祭り直葉	"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 あなたのクライマックスがクライマックス置場に置かれた時、あなたは自分の山札の上から1枚を公開する。そのカードが《アバター》か《ネット》のキャラなら、あなたは自分のキャラを1枚選び、そのターン中、ソウルを＋1。（公開したカードは元に戻す）
【自】 相手がレベルアップした時、あなたのクライマックス置場に「フェアリィ・ダンス」があるなら、あなたは自分の山札を上から4枚まで見て、《アバター》か《ネット》のキャラを1枚まで選んで相手に見せ、手札に加え、残りのカードを控え室に置く。
【起】［このカードを【レスト】する］ あなたは自分のキャラを1枚選び、そのターン中、パワーを＋1000。
'''
    

class S47_107(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "みんなで冒険リーファ	"
        self.color = util.Color.GREEN
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
    '''【永】 他のあなたの、《アバター》か《ネット》のキャラ1枚につき、このカードのパワーを＋500。
【自】 このカードが手札から舞台に置かれた時、あなたは自分の山札を上からＸ枚まで見て、カードを1枚まで選び、手札に加え、残りのカードを控え室に置く。Ｘはあなたの、《アバター》か《ネット》のキャラの枚数に等しい。
【自】［手札のキャラを2枚控え室に置く］ このカードのバトル相手が【リバース】した時、あなたはコストを払ってよい。そうしたら、あなたはそのバトル相手をクロック置場に置く。
'''
    

class S47_108(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "みんなで冒険リズベット"
        self.color = util.Color.RED
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
    '''【永】 あなたの控え室のクライマックスが2枚以下なら、あなたの手札のこのカードのレベルを－1。
【永】 他のあなたの、《アバター》か《ネット》のキャラ1枚につき、このカードのパワーを＋500。
【自】［手札を1枚控え室に置く］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分のクロックの上から1枚を、ストック置場に置く。
'''
    

class S47_109(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "みんなで冒険シリカ"
        self.color = util.Color.RED
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
    '''【自】 このカードが手札から舞台に置かれた時、あなたは自分の山札を上から1枚見て、山札の上か控え室に置く。
【自】 このカードがアタックした時、他のあなたのキャラが1枚以下なら、あなたは自分の山札の上から1枚を、控え室に置いてよい。そのカードがレベル0以下のキャラなら、そのキャラを後列の好きな枠に置く。
'''
    

class S47_110(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "打ち上げパーティー珪子"
        self.color = None
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】［手札のクライマックスを1枚控え室に置く］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の、《アバター》か《ネット》のキャラを1枚選び、手札に戻す。
【自】 このカードが【リバース】した時、このカードのバトル相手のレベルが1以下なら、あなたはそのキャラを【リバース】してよい。
'''
    

class S47_111(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "出会いを喜ぶ里香"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 1500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 あなたがこのカードの『助太刀』を使った時、あなたの、《アバター》か《ネット》のキャラがいるなら、あなたは自分のバトル中のキャラを1枚選び、そのターン中、パワーを＋1000。
【起】●助太刀1500 レベル1［(1) 手札のこのカードを控え室に置く］ （あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋1500）
'''
    

class S47_112(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "波状攻撃キリト"
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
    '''【永】 手札のこのカードをプレイするにあたり、あなたは自分の「戦いの後 キリト」を1枚選び、控え室に置いてよい。そうしたら、このカードをコスト0でプレイできる。
【永】 他のあなたの、《アバター》か《ネット》のキャラが3枚以上なら、このカードのパワーを＋1500し、このカードは次の能力を得る。『【自】 このカードのバトル相手がリバースした時、あなたは他の自分の、《アバター》か《ネット》のキャラを1枚選び、レストし、後列のキャラのいない枠に動かす。』
【自】 このカードが手札から舞台に置かれた時、あなたは自分のクロックの上から1枚を、控え室に置いてよい。
'''
    

class S47_113(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "戦いの後キリト"
        self.color = util.Color.BLUE
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
    '''【自】 この能力は1ターンにつき1回まで発動する。あなたが【起】を使った時、あなたは自分のキャラを1枚選び、そのターン中、パワーを＋500。
【起】 集中 ［① あなたのキャラを2枚レストする］ あなたは自分の山札の上から4枚をめくり、控え室に置く。それらのカードのクライマックス1枚につき、次の行動を行う。『あなたは2枚まで引き、自分の手札を1枚選び、控え室に置く。』
'''
    

class S47_114(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "命がけの本気キリト	"
        self.color = util.Color.BLUE
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
    '''【自】 このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚を公開する。そのカードが《アバター》か《ネット》のキャラなら、そのターン中、このカードのパワーを＋2000。（公開したカードは元に戻す）
【自】 このカードが舞台から控え室に置かれた時、あなたは自分の山札の上から3枚までを、公開してよい。1枚以上公開したなら、あなたはそれらのカードの《アバター》か《ネット》のキャラを1枚まで選び、手札に加え、残りのカードを控え室に置き、自分の手札を1枚選び、控え室に置く。
'''
    

class S47_115(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "みんなで冒険ユイ	"
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
    '''【自】 このカードが手札から舞台に置かれた時、あなたは自分の山札を上から2枚まで見て、山札の上に好きな順番で置く。
【自】［(1) このカードを手札に戻す］ あなたのクライマックスがクライマックス置場に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分のキャラを1枚選び、次の相手のターンの終わりまで、パワーを＋2500。
'''
    

class S47_116(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "怯える瞳シノン"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 0
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
    

class S47_117(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "強烈な気迫クライン"
        self.color = util.Color.BLUE
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
    '''【自】 この能力は1ターンにつき1回まで発動する。あなたが【起】を使った時、そのターン中、このカードのパワーを＋1500。
【自】 あなたのクライマックスがクライマックス置場に置かれた時、そのターン中、このカードのパワーを＋1500。
'''
    

class S47_118(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“DiceyCaf?”ギルバート"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 0
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】［(2) 手札の、《アバター》か《ネット》のキャラを1枚控え室に置く］ あなたがこのカードの『助太刀』を使った時、あなたはコストを払ってよい。そうしたら、あなたは相手の、レベルが相手のレベルより高いキャラを1枚選び、山札の下に置く。
【起】●助太刀2500 レベル1［(1) 手札のこのカードを控え室に置く］ （あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋2500）
'''
    

class S47_119(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "みんなで冒険シノン	"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】［(1) 手札のクライマックスを1枚控え室に置く］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室のクライマックスを1枚選び、手札に戻す。
【自】 このカードがアタックした時、このカードの正面のキャラのレベルが3以上なら、そのターン中、このカードのパワーを＋Ｘ。Ｘはあなたの、《アバター》か《ネット》のキャラの枚数×1000に等しい。
'''
