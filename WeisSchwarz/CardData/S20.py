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


class S20_002(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《閃光》のアスナ"
        self.color = util.Color.YELLOW
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
    '''【永】あなたのターン中、このカードの正面のキャラのレベルが3以上なら、このカードのパワーを＋4000し、ソウルを＋1。 
【自】このカードのバトル相手がリバースした時、あなたはそのキャラをストック置場に置く。 
'''
    

class S20_003(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ソファに横たわるアスナ"
        self.color = util.Color.YELLOW
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
    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札から1枚を公開する。そのカードが《アバター》のキャラでないならクロック置場に置く。(そうでないなら元に戻す)
'''
    

class S20_004(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "囚われの女王 アスナ"
        self.color = util.Color.YELLOW
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
    '''【永】他のあなたのカード名に「キリト」を含むキャラがいるなら、このカードのパワーを＋1000し、このカードは『【自】アンコール［手札のキャラを1枚控え室に置く］』を得る。
'''
    

class S20_005(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "着替え中のアスナ"
        self.color = util.Color.YELLOW
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
    '''【自】他のあなたの、《アバター》か《ネット》のキャラがアタックした時、そのターン中、このカードのパワーを＋1000。
'''
    

class S20_007(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "凛とした強さ アスナ"
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
    '''【自】このカードが手札から舞台に置かれた時か「前線への復帰」の効果で舞台に置かれた時、あなたは自分のクロックの上から1枚を、控え室に置いてよい。 
【自】［① 手札を1枚控え室に置く］このカードがアタックした時、あなたはコストを払ってよい。そうしたら、あなたの《アバター》のキャラすべてに、そのターン中、パワーを＋500し、ソウルを＋1。 
'''
    

class S20_008(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "新婚生活 アスナ"
        self.color = util.Color.YELLOW
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
    '''【永】応援 このカードの前のあなたのキャラすべてに、パワーを＋500。
【自】あなたのクライマックスがクライマックス置場に置かれた時、あなたは自分のキャラを1枚選び、そのターン中、パワーを＋1000。
'''
    

class S20_010(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "副団長 アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】あなたがこのカードの『助太刀』を使った時、あなたの、《アバター》か《ネット》のキャラが2枚以上なら、あなたは自分のキャラを1枚選び、そのターン中、パワーを＋1000。
【起】●助太刀1000 レベル1［手札のこのカードを控え室に置く］(あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋1000)
'''
    

class S20_011(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "雨宿り アスナ"
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
    '''【永】このカードの下のマーカー1枚につき、このカードのレベルを＋1し、パワーを＋1500。
【自】このカードのバトル相手がリバースした時、あなたは自分の山札の上から1枚を、このカードの下にマーカーとして置いてよい。
'''
    

class S20_T04(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "プロポーズの返事 アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 3500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】応援 このカードの前のあなたのキャラすべてに、パワーを＋1000。
【自】 このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚を公開する。そのカードが《アバター》か《ネット》のキャラなら、あなたは自分のキャラを1枚選び、そのターン中、ソウルを＋1。(公開したカードは元に戻す)
'''
    

class S20_013(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "団長 ヒースクリフ"
        self.color = util.Color.YELLOW
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
    '''【自】このカードがアタックしたとき、クライマックス置場に「闘技場でのデュエル」があるなら、あなたは相手のコスト1以下のキャラを1枚選び、手札に戻し、そのターン中、このカードはリバースしない。
'''
    

class S20_014(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "強い絆 アスナ"
        self.color = util.Color.YELLOW
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
    '''【自】絆／「血盟騎士団への入団 キリト」［あなたの山札の上から1枚をクロック置場に置く］(このカードがプレイされて舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「血盟騎士団への入団 キリト」を1枚選び、手札に戻す)
【起】［①］あなたは自分の《アバター》のキャラを1枚選び、そのターン中、パワーを＋500。
'''
    

class S20_T01(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "早とちり アスナ"
        self.color = util.Color.YELLOW
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
    '''【永】あなたのターン中、このカードのパワーを＋1000。
'''
    

class S20_016(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "監視役 クラディール"
        self.color = util.Color.YELLOW
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
    '''【起】［①］あなたは相手の前列のレベル0以下のキャラを1枚選び、ストック置場に置く。
'''
    

class S20_T02(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "戦いのはじまり アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    

class S20_T03(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "隠された正体 ヒースクリフ"
        self.color = util.Color.YELLOW
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
    

class S20_T05(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "熟練の料理スキル アスナ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8500
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】あなたのターン中、他のあなたの《アバター》のキャラが2枚以上なら、このカードのレベルを＋1し、パワーを＋1500。
'''
    

class S20_008(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "新婚生活 アスナ"
        self.color = util.Color.YELLOW
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
    '''【永】応援 このカードの前のあなたのキャラすべてに、パワーを＋500。
【自】あなたのクライマックスがクライマックス置場に置かれた時、あなたは自分のキャラを1枚選び、そのターン中、パワーを＋1000。
'''
    
    
class S20_021(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "前線への復帰"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 1
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_022(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "身代わり"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 1
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_021(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "前線への復帰"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 1
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_022(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "身代わり"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 1
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_023(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "誓い合った約束"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
    
    
class S20_T06(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《スター・スプラッシュ》"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
    
    
class S20_025(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "闘技場でのデュエル"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
    

class S20_027(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "魔法剣士 リーファ"
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
    '''【自】［①］このカードがアタックした時、クライマックス置場に「スペル詠唱」があるなら、あなたはコストを払ってよい。そうしたら、そのターン中、このカードのパワーを＋1000し、このカードは次の能力を得る。『【自】このカードのバトル相手でレベル2以上のキャラがリバースした時、あなたはそのキャラをクロック置場に置いてよい。』
'''
    

class S20_027(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "純粋な願い リーファ"
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
    '''【永】あなたの山札が5枚以下なら、あなたの手札のこのカードのレベルを－1。
【永】他のあなたの、《アバター》か《ネット》のキャラすべてに、パワーを＋1500。
【起】［① 手札の、《アバター》か《ネット》のキャラを1枚控え室に置く］次の相手のターンの終わりまで、このカードのパワーを＋3000し、このカードは次の能力を得る。『【永】このカードは相手の効果に選ばれない。』
'''
    

class S20_028(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "頼りになる案内役 リーファ"
        self.color = util.Color.GREEN
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
    '''【自】このカードがアタックした時、あなたは他の自分のキャラを1枚選び、そのターン中、レベルを＋1し、パワーを＋1000。 
'''
    

class S20_029(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "揺れる気持ち 直葉"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】他のあなたのキャラすべてに、パワーを＋500。
【自】［①］あなたのクライマックス置場に「隠し続けた想い」が置かれた時、あなたはコストを払ってよい。そうしたら、あなたのキャラすべてに、そのターン中、パワーを＋1500。
'''
    

class S20_030(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《シルフ》の少女 リーファ"
        self.color = util.Color.GREEN
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
    '''【自】アンコール［手札のキャラを1枚控え室に置く］(このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、このカードがいた枠にレストして置く)
【起】［あなたの、《アバター》か《ネット》のキャラを2枚レストする］そのターン中、このカードのパワーを＋2500。
'''
    

class S20_031(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "制服の直葉"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《ネット》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】他のあなたの、《アバター》か《ネット》のキャラが3枚以上なら、このカードは『【自】アンコール［手札のキャラを1枚控え室に置く］』を得る。
【自】［①］このカードがアタックした時、あなたはコストを払ってよい。そうしたら、そのターン中、このカードのパワーを＋2500。
'''
    

class S20_032(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "自分に言い聞かせる直葉"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】このカードが手札から舞台に置かれた時、あなたは他の自分の、《アバター》か《ネット》のキャラを1枚選び、そのターン中、パワーを＋500。
【自】絆／「大切な人のために キリト」［①］(このカードがプレイされて舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「大切な人のために キリト」を1枚選び、手札に戻す)
'''
    

class S20_037(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "鋭い指摘 リーファ"
        self.color = util.Color.GREEN
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
    '''【永】あなたのストックが3枚以上なら、このカードのパワーを＋1000。
'''
    

class S20_038(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "お風呂上りの直葉"
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
    ''''''
    

class S20_039(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "慌てるリーファ"
        self.color = util.Color.GREEN
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
    
    
class S20_045(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "隠し続けた想い"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
    

class S20_046(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "探し続けたもの リズベット"
        self.color = util.Color.RED
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
    '''【自】［①］このカードがアタックした時、クライマックス置場に「求めていた温もり」があるなら、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室のキャラを2枚まで選び、手札に戻し、自分の手札を1枚選び、控え室に置き、そのターン中、このカードのパワーを＋1000。 
'''
    

class S20_048(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "親友を祝福するリズベット"
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
    '''【自】このカードがアタックした時、他のあなたのカード名に「アスナ」を含むキャラすべてに、そのターン中、パワーを＋500。
【自】絆／「パーティーの誘い アスナ」［①］(このカードがプレイされて舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「パーティーの誘い アスナ」を1枚選び、手札に戻す)
'''
    

class S20_049(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《フラワーガーデン》のシリカ"
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
    '''【自】［①］このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「《プネウマの花》」を1枚選び、手札に戻す。
'''
    

class S20_050(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "職人の矜持 リズベット"
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
    '''【自】このカードがリバースした時、このカードのバトル相手のレベルが0以下なら、あなたはそのキャラをリバースしてよい。
【自】加速［あなたの山札の上から1枚をクロック置場に置く］あなたのクライマックスフェイズの始めに、あなたはコストを払ってよい。そうしたら、あなたは他の自分の《武器》のキャラを1枚選び、そのターン中、パワーを＋2500。
'''
    

class S20_051(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "まっすぐな信頼 シリカ"
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
    '''【起】集中 ［① あなたのキャラを2枚レストする］あなたは自分の山札の上から4枚をめくり、控え室に置く。それらのカードのクライマックス1枚につき、あなたは自分の控え室の、《アバター》か《ネット》か《使い魔》のキャラを1枚まで選び、手札に戻す。
'''
    

class S20_052(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "着替え中のリズベット"
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
    '''【永】他のあなたの、《アバター》か《ネット》のキャラ1枚につき、このカードのパワーを＋500。
'''
    

class S20_053(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "決意の告白 リズベット"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 4000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】応援 このカードの前のあなたのキャラすべてに、パワーを＋Ｘ。Ｘはそのキャラのレベル×500に等しい。
【自】［②］このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室のキャラを1枚選び、手札に戻す。
'''
    

class S20_054(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "使い魔 ピナ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《使い魔》', '《竜》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】他のあなたのカード名に「シリカ」を含むキャラすべてに、パワーを＋500。
【自】［このカードを控え室に置く］他のあなたのカード名に「シリカ」を含むキャラが舞台から控え室に置かれた時、後列にこのカードがあるなら、あなたはコストを払ってよい。そうしたら、そのキャラをそのキャラがいた枠にレストして置く。
'''
    

class S20_055(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "デート気分 シリカ"
        self.color = util.Color.RED
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
    '''【自】あなたのクライマックスフェイズの始めに、あなたは自分の山札から1枚を公開する。そのカードがクライマックスなら、このカードをレストする。(公開したカードは元に戻す)
'''
    

class S20_056(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "メイスの使い手 リズベット"
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
    '''【自】［①］このカードがアタックした時、クライマックス置場に「気づいた本当の気持ち」があるなら、あなたはコストを払ってよい。そうしたら、あなたの《武器》のキャラすべてに、そのターン中、パワーを＋2500。
'''
    

class S20_057(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "冒険のはじまり シリカ"
        self.color = util.Color.RED
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
    '''【自】［①］このカードがアタックした時、クライマックス置場に「初めての冒険」があるなら、あなたはコストを払ってよい、そうしたら、あなたは自分の控え室の「使い魔 ピナ」を1枚選び、舞台の好きな枠にレストして置き、そのターン中、このカードのパワーを＋3500。
'''
    

class S20_058(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ダガー使い シリカ"
        self.color = util.Color.RED
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
    

class S20_59(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "かわいい悪戯 シリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】あなたのクライマックスフェイズの始めに、あなたは自分の山札の上から1枚を公開する。そのカードがクライマックスなら、あなたは他の自分のキャラを1枚選び、控え室に置く。(公開したカードは元に戻す)
'''
    

class S20_060(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "前向きな笑顔 リズベット"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚を公開する。そのカードがクライマックスなら、このカードをレストする。(公開したカードは元に戻す)
'''
    

class S20_061(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "鍛冶屋のリズベット"
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
    '''【永】応援このカードの前のあなたのキャラすべてに、パワーを＋500。
【自】［このカードをレストする］あなたが『加速』を使った時、このカードがスタンドしているなら、あなたはコストを払ってよい。そうしたら、あなたは自分のキャラを1枚選び、そのターン中、パワーを＋1500。
'''
    

class S20_062(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《ビーストテイマー》シリカ"
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
    '''【自】絆／「使い魔 ピナ」［①］(このカードがプレイされて舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「使い魔 ピナ」を1枚選び、手札に戻す)
'''
    

class S20_063(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "アイドル的存在 シリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    

class S20_064(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "パーティーの脱退 シリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【起】●助太刀1500 レベル1［手札のこのカードを控え室に置く］(あなたはフロントアタックされている自分のキャラを1枚選び、そのターン中、パワーを＋1500)
'''
    

class S20_066(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "窮地のシリカ"
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
    '''【永】前列の中央の枠にこのカードがいるなら、このカードのパワーを＋1000。
'''
    

class S20_067(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "背中を押すリズベット"
        self.color = util.Color.RED
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
    '''【自】チェンジ［② 手札を1枚控え室に置き、このカードを控え室に置く］あなたのクライマックスフェイズの始めに、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の 「前向きな笑顔 リズベット」を1枚選び、このカードがいた枠に置く。
'''
    

class S20_068(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ハプニング シリカ"
        self.color = util.Color.RED
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
    ''''''
    

class S20_069(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "感謝の気持ち シリカ"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8500
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【起】［あなたの、《アバター》か《ネット》か《使い魔》のキャラを2枚レストする］そのターン中、このカードのパワーを＋2500。
'''
    
    
class S20_070(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《プネウマの花》"
        self.color = util.Color.RED
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 0
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_071(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "白竜の洞窟"
        self.color = util.Color.RED
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 1
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_072(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "求めていた温もり"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
    
    
class S20_073(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "初めての冒険"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
    
    
class S20_074(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ピナの蘇生"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
    
    
class S20_075(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "気づいた本当の気持ち"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
    

class S20_077(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《黒の剣士》キリト"
        self.color = util.Color.BLUE
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
    '''【自】［③ 手札を1枚クロック置場に置く］あなたのクライマックス置場に「《二刀流》の使い手」が置かれた時、前列にこのカードがいるなら、あなたはコストを払ってよい。そうしたら、そのターン中、このカードのパワーを＋3500し、このカードは次の能力を得る。『【自】この能力は1ターンにつき1回まで発動する。このカードのバトル相手がリバースした時、あなたはこのカードをスタンドしてよい。』
【自】このカードがアタックした時、あなたは自分の山札の上から1枚を公開する。そのカードが《アバター》か《ネット》のキャラなら、手札に加える。(そうでないなら元に戻す)
'''
    

class S20_78(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "刀使い クライン"
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
    '''【自】このカードが手札から舞台に置かれた時、あなたは山札の上から1枚を公開する。そのカードが《アバター》か《ネット》のキャラなら、あなたは自分のキャラを1枚選び、そのターン中、パワーを＋1000。公開したカードは元に戻す
【起】集中［①］あなたは自分の山札から4枚をめくり、控え室に置く。それらのカードのクライマックス1枚につき、あなたは自分の、《アバター》か《ネット》のキャラを1枚選び、次の相手ターンの終わりまで、パワーを＋1000。
'''
    

class S20_079(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "戦場に身を置くキリト"
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
    '''【自】［① 手札を1枚控え室に置く］このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見て《アバター》のキャラを1枚まで選んで相手に見せ、手札に加える。その山札をシャッフルする。
'''
    

class S20_080(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "大切な人のために キリト"
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
    '''【自】［①］このカードがアタックした時、クライマックス置場に「世界の終焉」があるなら、あなたはコストを払ってよい。そうしたら、あなたは1枚引く。
【自】加速［あなたの山札の上から1枚をクロック置場に置く］あなたのクライマックスフェイズの始めに、あなたはコストを払ってよい。そうしたら、次の相手のターンの終わりまで、このカードのパワーを＋2500。
'''
    

class S20_081(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "人工知能 ユイ"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【自】［②］このカードがアタックした時、クライマックス置場に「突然の別れ」があるなら、あなたはコストを払ってよい。そうしたら、あなたは2枚まで引く。
'''
    

class S20_082(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ユニークスキルの発現 キリト"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7500
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】このカードの下のマーカー1枚につき、このカードのレベルを＋1し、パワーを＋1500。
【自】このカードのバトル相手がリバースした時、あなたは自分の山札の上から1枚を、このカードの下にマーカーとして置いてよい。
【自】［このカードの下のマーカーすべてを控え室に置く］他のあなたのキャラがアタックした時、このカードの下のマーカーが5枚以上なら、あなたはコストを払ってよい。そうしたら、このカードをスタンドし、そのターン中、このカードのパワーを＋6000。
'''
    

class S20_083(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ソロプレイヤー キリト"
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
    '''【永】他のあなたのキャラがいないなら、このカードのレベルを＋1し、パワーを＋1500。
'''
    

class S20_084(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "月夜の黒猫団 サチ"
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
    '''【永】相手のターン中、このカードのパワーを＋1000。
'''
    

class S20_085(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "強い絆 キリト"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    '''【永】他のあなたのカード名に「アスナ」を含むキャラすべてに、パワーを＋500。
【永】相手のターン中、他のあなたのキャラすべてに、パワーを＋500。
'''
    

class S20_086(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "品定めするキリト"
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
    '''【永】他のあなたのカード名に「アスナ」を含むキャラがいるなら、このカードのパワーを＋1000し、このカードは『【自】アンコール［手札のキャラを1枚控え室に置く］』を得る。
'''
    

class S20_087(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "さりげない優しさ キリト"
        self.color = util.Color.BLUE
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
    '''【自】チェンジ［② 手札を1枚控え室に置き、このカードを控え室に置く］あなたのクライマックスフェイズの始めに、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の 「ユニークスキルの発現 キリト」を1枚選び、このカードがいた枠に置く。
'''
    

class S20_089(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "穏やかな日常 キリト"
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
    '''【自】絆／「着替え中のアスナ」［①］(このカードがプレイされて舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「着替え中のアスナ」を1枚選び、手札に戻す)
'''
    

class S20_T07(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "戦いのはじまり キリト"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    

class S20_T09(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "愛らしい少女 ユイ"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《ネット》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    

class S20_T12(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "五十五層の雪山 キリト"
        self.color = util.Color.BLUE
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
    '''【起】●助太刀3000 レベル2［① 手札のこのカードを控え室に置く］(あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋3000)
'''
    

class S20_T10(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "血盟騎士団への入団 キリト"
        self.color = util.Color.BLUE
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
    '''【永】相手のターン中、このカードのパワーを＋1000。
'''
    

class S20_T11(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "斧戦士 エギル"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9000
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('《アバター》', '《武器》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    ''''''
    
    
class S20_096(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "プロポーズ"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 2
        self.cost = 2
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_097(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ありがとう、さよなら"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 1
        self.counter = False
        self.useCardLimit = None
    ''''''
    
    
class S20_T14(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "《二刀流》の使い手"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
    
    
class S20_T13(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "世界の終焉"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
    
    
class S20_100(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "突然の別れ"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('：',)
        self.useCardLimit = None
    ''''''
