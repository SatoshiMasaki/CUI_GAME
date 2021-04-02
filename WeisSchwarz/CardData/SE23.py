

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


class SE23_01(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "穏やかな時アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
        self.power = 8000
        self.level = 2
        self.cost = 1
        self.soul = 2
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 ［手札を1枚控え室に置く］ あなたのクライマックス置場に「《世界樹》の上で」が置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見て「希望の光 アスナ」を1枚と、《アバター》か《ネット》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''
    

class SE23_02(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "苦い記憶アスナ"
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
    '''【永】 他のあなたの、《アバター》か《ネット》のキャラすべてに、パワーを＋500。
【起】 ［このカードをレストする］ あなたは自分のカード名に「キリト」を含むキャラを1枚選び、そのターン中、パワーを＋500。
'''
    

class SE23_03(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《ALO》の日常アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたの、《アバター》か《ネット》のキャラすべてに、パワーを＋500。
【起】 集中 ［①］ あなたは自分の山札の上から4枚をめくり、控え室に置く。それらのカードのクライマックス1枚につき、あなたは自分の、《アバター》か《ネット》のキャラを1枚選び、そのターン中、パワーを＋2000。
'''
    

class SE23_04(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "秋の散策明日奈"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 他のあなたの、《ネット》か《アバター》のキャラがアタックした時、そのターン中、このカードのパワーを＋1000。
'''
    

class SE23_05(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "兄妹のひと時直葉"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
        self.power = 5000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《ネット》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】応援 このカードの前のあなたのキャラすべてに、パワーを＋X。Xはそのキャラのレベル×500に等しい。
【自】［② 手札を1枚控え室に置く］ あなたのクライマックス置場に「フェアリィ・ダンス」が置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の手札の「仮想と現実 リーファ＆直葉」を1枚選び、舞台の好きな枠に置く。
'''
    

class SE23_06(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "素材採集リーファ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''【自】 あなたがこのカードの『助太刀』を使った時、あなたは自分の山札の上から1枚を公開する。そのカードが《アバター》か《ネット》のキャラなら手札に加え、あなたは自分の手札を1枚選び、控え室に置く。(そうでないなら元に戻す)
【起】 ●助太刀2500 レベル2［① 手札のこのカードを控え室に置く］(あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋2500)
'''
    

class SE23_07(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "素材採集シリカ"
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
    '''【自】 このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚を公開する。そのカードが《アバター》か《ネット》のキャラなら手札に加え、あなたは自分の手札を1枚選び、控え室に置く。(そうでないなら元に戻す)
【自】 このカードがリバースした時、このカードのバトル相手のレベルが0以下なら、あなたはそのキャラをリバースしてよい。
'''
    

class SE23_08(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "新川昌一"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたの《武器》のキャラすべてに、パワーを＋500。
【永】 相手の前列のキャラすべてに、《標的》を与える。
'''
    

class SE23_09(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "<ruby><rb>Sterben</rb><rp>(</rp><rt>ステルベン</rt><rp>)</rp></ruby><ruby><rb>《死銃》</rb><rp>(</rp><rt>デス・ガン</rt><rp>)</rp></ruby>"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードがアタックした時、相手のキャラすべてが《標的》なら、あなたは相手に1ダメージを与えてよい。（ダメージキャンセルは発生する）
【自】 このカードがアタックした時、クライマックス置場に「因縁の刺剣使い」があるなら、次の相手のターンの終わりまで、このカードのパワーを＋2500し、このカードは次の能力を得る。『【自】 このカードのバトル相手がリバースした時、あなたはそのキャラを山札の上に置いてよい。』
'''
    

class SE23_10(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "みんなで観戦リズベット"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 相手のストックが3枚以下なら、このカードのパワーを＋1000。
'''
    

class SE23_11(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "レッドプレイヤー<ruby><rb>《死銃》</rb><rp>(</rp><rt>デス・ガン</rt><rp>)</rp></ruby>"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 あなたのドローフェイズの始めに、あなたに1ダメージを与える。(ダメージキャンセルは発生する)
'''
    

class SE23_12(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "現れた死神<ruby><rb>《死銃》</rb><rp>(</rp><rt>デス・ガン</rt><rp>)</rp></ruby>"
        self.color = util.Color.RED
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
    '''【自】 ［あなたの山札の上から1枚をクロック置場に置く］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは相手の前列のコスト1以下のキャラを1枚選ぶ。そのキャラは次の相手のスタンドフェイズにスタンドしない。
'''
    

class SE23_13(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "過剰な執着恭二"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
        self.power = 4000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたの《武器》のキャラすべてに、パワーを＋1000。
【永】 相手の後列のキャラすべてに、《標的》を与える。
'''
    

class SE23_14(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "みんなでMob狩りリズベット"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
        self.power = 7000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたの、《アバター》か《ネット》のキャラ1枚につき、このカードのパワーを＋500。
【自】 ［①］ このカードがフロントアタックした時、あなたはコストを払ってよい。そうしたら、あなたは相手のキャラを1枚選び、そのターン中、レベルを－1。
'''
    

class SE23_15(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "死に至る弾丸<ruby><rb>《死銃》</rb><rp>(</rp><rt>デス・ガン</rt><rp>)</rp></ruby>"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
        self.power = 7000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 相手のキャラすべてが《標的》なら、このカードのパワーを＋2000。
【自】 ［① あなたの山札の上から1枚をクロック置場に置く］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは相手の前列のレベル2以下の《標的》のキャラを1枚選び、控え室に置く。
'''
    

class SE23_16(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "いつものシリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''【永】 あなたのストックが6枚以上なら、このカードのパワーを＋500し、ソウルを＋1。
'''
    
    
class SE23_17(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "因縁の<ruby><rb>刺剣</rb><rp>(</rp><rt>エストック</rt><rp>)</rp></ruby>使い"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
    

class SE23_18(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "理想の自分シノン"
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
    '''【自】 ［① あなたの山札の上から1枚をクロック置場に置く］ このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見てレベル2以上のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''
    

class SE23_19(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "木漏れ日の中シノン"
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
    '''【永】 相手のターン中、他のあなたの前列の中央の枠のキャラに、パワーを＋1000。
【起】 集中 ［①］ あなたは自分の山札の上から4枚をめくり、控え室に置く。あなたは自分の山札を見て《アバター》か《ネット》のキャラをＸ枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。あなたは自分の手札をＸ枚選び、控え室に置く。Ｘはそれらのカードのクライマックスの枚数に等しい。
'''
    

class SE23_20(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "一時的な共闘キリト"
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
    '''【自】 このカードがアタックした時、あなたは他の自分のカード名に「シノン」を含むキャラを1枚選び、そのターン中、パワーを＋1000。
【自】 相手のアタックフェイズの始めに、あなたは自分の山札の上から1枚を控え室に置いてよい。そのカードが《アバター》か《ネット》のキャラなら、あなたはこのカードを前列のキャラのいない枠に動かしてよい。
'''
    

class SE23_21(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "一時的な共闘シノン"
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
【自】 アンコール ［あなたの山札の上から1枚をクロック置場に置く］（このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、このカードがいた枠にレストして置く）
'''
    

class SE23_22(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "強くあるべき存在シノン"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''【永】 他のあなたの、《アバター》か《ネット》のキャラすべてに、パワーを＋1000。
【自】 チェンジ ［② 手札を1枚控え室に置き、このカードを控え室に置く］ あなたのクライマックスフェイズの始めに、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「最後の一撃 シノン」を1枚選び、このカードがいた枠に置く。
'''
    

class SE23_23(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "因縁の果てキリト"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''【自】 このカードが手札から舞台に置かれた時、あなたは自分の山札を上から1枚見て、山札の上か下に置く。
【自】 このカードがアタックした時、クライマックス置場に「かつての名前」があるなら、あなたは自分のクロックの上から1枚までを、控え室に置き、そのターン中、このカードのパワーを＋3000。
【自】 ［①］ このカードがフロントアタックされた時、あなたはコストを払ってよい。そうしたら、そのターン中、このカードのパワーを＋1500。
'''
    

class SE23_24(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "最後の一撃シノン"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''【自】 このカードが手札から舞台に置かれた時か『チェンジ』で舞台に置かれた時、あなたは自分のクロック置場の上から1枚を、控え室に置いてよい。
【自】 ［② 手札を1枚控え室に置く］このカードがアタックした時、クライマックス置場に「幻影の一弾」があるなら、あなたはコストを払ってよい。そうしたら、相手に4ダメージを与える。このダメージがキャンセルされた時、次の相手のターンの終わりまで、このカードのパワーを＋3500。
【自】 バトル中のこのカードがリバースした時、このカードを思い出にする。
'''
    

class SE23_25(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "銃の基礎知識シノン"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたの前列のキャラがいないなら、このカードのパワーを＋1000し、このカードは『【自】アンコール［手札のキャラを1枚控え室に置く］』を得る。
'''
    

class SE23_26(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "潜行のキリト"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 このカードはサイドアタックできない。
'''
    

class SE23_27(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "秋の散策和人"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】 このカードが手札から舞台に置かれた時、あなたは1枚引き、自分の手札を1枚選び、控え室に置く。
【自】 ［このカードを控え室に置く］ 他のあなたのキャラが舞台から控え室に置かれた時、後列にこのカードがいるなら、あなたはコストを払ってよい。そうしたら、そのキャラをそのキャラがいた枠にレストして置く。
'''
    

class SE23_28(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "強くなりたい詩乃"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》', '《メガネ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 他のあなたの、《アバター》か《ネット》のキャラすべてに、パワーを＋500。
【自】 ［①］ あなたのクライマックス置場に「小さな一歩」が置かれた時、あなたはコストを払ってよい。そうしたら、あなたは他の自分のカード名に「シノン」を含むキャラを1枚選び、そのターン中、パワーを＋2000し、次の能力を与える。『【自】 このカードのバトル相手がリバースした時、あなたは1枚引いてよい。』
'''
    

class SE23_29(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "戦う選択キリト"
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
    '''【自】 このカードが手札から舞台に置かれた時、そのターン中、このカードのパワーを＋Ｘ。Ｘはあなたの、《アバター》か《ネット》のキャラの枚数×500に等しい。
'''
    

class SE23_30(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "麗しのアバターキリト"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''【永】 応援 このカードの前のあなたのキャラすべてに、パワーを＋Ｘ。Ｘはあなたの『応援』を持つキャラの枚数×500に等しい。
【自】 このカードが手札から舞台に置かれた時、あなたは1枚引き、自分の手札を1枚選び、控え室に置く。
'''
    

class SE23_31(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "お怒りシノン"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''【自】 あなたがこのカードの『助太刀』を使った時、あなたは自分の山札の上から3枚を、控え室に置く。
【起】 ●助太刀2000 レベル1［① 手札のこのカードを控え室に置く］(あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋2000)
'''
    

class SE23_32(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "“後ろに注意”(チェック・シックス)シノン"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
        self.power = 7000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】 このカードの正面のキャラのレベルが3以上なら、このカードのパワーを＋3000。
【起】 ［あなたの、《アバター》か《ネット》のキャラを2枚レストする］ そのターン中、このカードのパワーを＋2500。
'''
    

class SE23_33(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《死銃》(デス・ガン)との対峙キリト"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('util.Trigger.ONE',)
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
    '''【自】 ［①］ このカードがアタックした時、クライマックス置場に「かつての名前」があるなら、あなたはコストを払ってよい。そうしたら、あなたは1枚引き、そのターン中、このカードのパワーを＋3000。あなたのアンコールステップの始めに、このカードがレストしているなら、あなたはこのカードを控え室に置き、あなたは自分の手札の「因縁の果て キリト」を1枚まで選び、このカードがいた枠に置く。
'''
    
    
class SE23_34(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "かつての名前"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
    
    
class SE23_35(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "幻影の一弾(ファントム・バレット)"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
    
    
class SE23_36(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "小さな一歩"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
