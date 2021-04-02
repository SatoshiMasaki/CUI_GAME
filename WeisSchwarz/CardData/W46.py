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


class W46_001( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "朝のひとときひまり"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《帽子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードがアタックした時、他のあなたのキャラが1枚以下なら、あなたは自分の山札の上から1枚を、控え室に置いてよい。そのカードがレベル0以下のキャラなら、そのキャラを後列の好きな枠に置く。
【自】相手のアタックフェイズの始めに、あなたはこのカードを前列の中央のキャラのいない枠に動かしてよい。
'''


class W46_002( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ふたりの抱負ひまり"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《帽子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】あなたがこのカードの『助太刀』を使った時、あなたの《風南島》のキャラがいるなら、あなたは自分のバトル中のキャラを1枚選び、そのターン中、パワーを＋1000。
【起】●助太刀1000 レベル1［手札のこのカードを控え室に置く］(あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋1000)
'''


class W46_003( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "白い帽子の少女ひまり"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《帽子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】経験 あなたのレベル置場に「無邪気な水しぶき ひまり」があるなら、あなたの手札のこのカードのレベルを－1。
【自】あなたのクライマックス置場に「風のいたずら」が置かれた時、前列にこのカードがいるなら、あなたは自分の山札を見て《風南島》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''


class W46_004( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "漂泊の天使ひまり"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《風南島》', '《帽子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札から6枚まで見て、カードを3枚選び控え室に置く。残りのカードを山札の上に好きな順番で置く。
【自】この能力は1ターンにつき2回まで発動する。他のあなたの《風南島》のキャラが手札から舞台に置かれた時、そのターン中、このカードのパワーを＋1000。
【自】[②]このカードがアタックした時、あなたは自分の山札の上から1枚を公開する。そのカードが《風南島》のキャラならあなたはコストを払ってよい。そうしたら、あなたは自分のクロックの上から1枚を控え室に置く。(公開したカードは元に戻す)
'''


class W46_005( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "不思議な帽子の親友めです"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《帽子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】[①あなたの山札の上から1枚をクロック置場に置き、このカードを思い出にする]バトル中のこのカードがリバースした時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見て《帽子》のキャラを選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''


class W46_006( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "求め合う心ひまり"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《帽子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたのターン中、他のあなたの《風南島》のキャラすべてに、パワーを＋1000。
【起】[あなたのキャラを2枚レストする］ あなたは自分の山札を上から1枚見て、山札の上か下に置く。
'''


class W46_007( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "常夏の楽園ひまり"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 8500
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('《風南島》', '《帽子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《風南島》のキャラが2枚以上なら、このカードのパワーを＋2000し、このカードは「【自】アンコール[手札のキャラを1枚控え室に置く]」を得る。
【自】このカードが手札から舞台に置かれた時、あなたの思い出置場に「不思議な帽子の親友 めです」がないなら、相手は自分の控え室のカードを1枚選び、山札に戻してよい。そうしたら、その山札をシャッフルする。
'''


class W46_008( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "水着のひまり"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《帽子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】 他のあなたの《風南島》のキャラすべてに、パワーを＋500。
【自】[手札を1枚控え室に置く］ あなたのクライマックス置場に「始まりと始まり」が置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見て《風南島》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''


class W46_009( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "TABデビューひまり"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《帽子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から2枚まで見て、山札の上に好きな順番で置く。
【自】この能力は1ターンにつき2回まで発動する。他のあなたの《風南島》のキャラが手札から舞台に置かれた時、そのターン中、このカードのパワーを＋1000。
'''


class W46_010( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "温泉で一息ひまり"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《帽子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードがアタックした時、あなたは自分の山札の上から1枚を、控え室に置く。そのカードがクライマックスなら、あなたのキャラすべてに、そのターン中、ソウルを＋1。
【自】[①］ このカードの与えたダメージがキャンセルされた時、あなたはコストを払ってよい。そうしたら、あなたは1枚引く。
'''


class W46_011( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "無邪気な水しぶきひまり"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《帽子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚公開する。そのカードが《風南島》のキャラなら次の相手のターンの終わりまで、このカードのパワーを＋1500。(公開したカードは元に戻す)
'''


class W46_012( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "穏やかな目覚めひまり"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 7000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《帽子》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    ''''''


class W46_013( EVENT ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "楽園システム"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 1
        self.counter = False
        self.useCardLimit = None

    ''''''


class W46_014( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "風のいたずら"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.useCardLimit = None

    ''''''


class W46_015( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "始まりと始まり"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None

    ''''''


class W46_016( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "完全無欠なお嬢様遥月"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《風南島》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】記憶あなたの思い出が3枚以上なら、このカードのパワーを＋1500し、このカードは次の能力を得る。「【永】このカードのバトル中、相手は「助太刀」を手札からプレイできない。」
【自】このカードが手札から舞台に置かれた時、あなたは自分のクロックの上から1枚を、控え室に置いてよい。
'''


class W46_017( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "風南学園の生徒会長遥月"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたのストックが5枚以上なら、他のあなたのキャラすべてに、パワーを＋500。
【起】集中[①このカードをレストする]あなたは自分の山札を上から4枚をめくり、控え室に置く。それらのカードのクライマックス1枚につき、次の行動を行う。「あなたは自分のクロックを1枚選び、手札に戻し、自分の山札の上から1枚を、クロック置場に置く。」
'''


class W46_018( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "つながるこころ遥月"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードがリバースした時、このカードのバトル相手のレベルが0以下なら、あなたは相手のクロックの上から1枚を、控え室に置いてよい。そうしたら、あなたはそのキャラをクロック置場に置く。
【起】[①]あなたは自分の《風南島》のキャラを1枚選び、そのターン中、パワーを+1500。
'''


class W46_019( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ディフェンディングチャンピオン遥月"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】[手札を1枚控え室に置く]このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分のクロック置場の《風南島》のキャラを1枚選び、手札に戻し、自分の山札の上から1枚を、クロック置場に置く。
【起】[①このカードを思い出にする]あなたは自分の山札の上から4枚まで見て、《風南島》のキャラを1枚まで選んで相手に見せ、手札に加え、残りのカードを控え室に置く。
'''


class W46_020( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "一緒に衣装選び遥月"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】記憶あなたの思い出置場にカードがあるなら、このカードのパワーを＋2500し、このカードは『【自】アンコール［手札のキャラを1枚控え室に置く］』を得る。
'''


class W46_021( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "常夏の楽園遥月"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 5500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】応援このカードの前のあなたの《風南島》のキャラすべてに、パワーを＋1500。
【起】［②このカードをレストする］ あなたは自分のクロックを1枚選び、手札に戻し、自分の山札の上から1枚を、クロック置場に置く。
'''


class W46_022( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "一時の休息遥月"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】相手の控え室のクライマックスが3枚以下なら、あなたの手札のこのカードのレベルを－1。
【自】[②あなたの控え室の「つながるこころ 遥月」を1枚思い出にし、このカードを思い出にする]このカードがフロントアタックされた時、あなたはコストを払ってよい。そうしたら、あなたは手札の「完全無欠なお嬢様 遥月」を1枚まで選び、このカードがいた枠に防御キャラとして置く。
'''


class W46_023( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ドキドキハプニング遥月"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】バトル中のこのカードがリバースした時、あなたは自分の山札の上から1枚を公開する。そのカードがレベル0以下のキャラなら手札に加える。(そうでないなら元に戻す)
'''


class W46_024( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "言葉にならない気持ち遥月"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    ''''''


class W46_025( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "水着の遥月"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたのクライマックス置場に「春陽……」が置かれた時、前列にこのカードがいるなら、あなたは他の自分のキャラを1枚と、このカードを選び、そのターン中、次の能力を与える。『【自】このカードがアタックした時、あなたは自分の山札の上から1枚を公開する。そのカードのレベルが1以上ならストック置場に置く。』（クライマックスのレベルは0として扱う。そうでないなら元に戻す）
【自】チェンジ［このカードを控え室に置く］あなたのアンコールステップの始めに、このカードがレストしているなら、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の「10年目の真実 遥月」を1枚選び、このカードがいた枠に置く。
'''


class W46_026( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "10年目の真実遥月"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】相手のターン中、他のあなたの《風南島》のキャラ1枚につき、このカードのパワーを＋500。
【起】［あなたのキャラを2枚レストする］このカードをストック置場に置く。あなたは自分の控え室の「水着の遥月」を1枚選び、このカードがいた枠に置く。
'''


class W46_027( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "会長の演説遥月"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの「会長の演説 遥月」1枚につき、このカードのパワーを＋1000。
【自】あなたのクライマックス置場に「一緒にフォトクラ」が置かれた時、前列にこのカードがいるなら、あなたは自分の山札を見て「会長の演説 遥月」を1枚まで選び、舞台の好きな枠に置き、その山札をシャッフルする。
'''


class W46_028( EVENT ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "賑やかな歓迎会"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 0
        self.counter = False
        self.useCardLimit = None

    ''''''


class W46_029( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "春陽……"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('宝',)
        self.useCardLimit = None

    ''''''


class W46_030( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "一緒にフォトクラ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None

    ''''''


class W46_031( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "世話焼き系妹キャラ乃絵里"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《家族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】記憶このカードがアタックした時、あなたの思い出置場にカードがあるなら、そのターン中、このカードのパワーを＋1500。
【自】［①］このカードがアタックした時、クライマックス置場に「絶対に幸せになるための第一歩」があるなら、あなたはコストを払ってよい。そうしたら、あなたは他の自分のキャラを1枚と、このカードを選び、そのターン中、次の能力を与える。『【自】このカードのバトル相手がリバースした時、あなたは自分の控え室のキャラを1枚選び、手札に戻してよい。』
'''


class W46_032( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "水着の乃絵里"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《家族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から2枚を、控え室に置く。それらのカードにクライマックスがあるなら、あなたは相手の山札の上から1枚を、控え室に置いてよい。そうしたら、あなたは相手の控え室のカードを1枚選び、山札の上に置く。
【自】［①あなたの山札の上から1枚をクロック置場に置き、このカードを思い出にする］バトル中のこのカードがリバースした時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の《風南島》のキャラを1枚選び、手札に戻す。
'''


class W46_033( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "料理中の乃絵里"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《家族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《風南島》のキャラすべてに、パワーを＋500。
【起】［②このカードをレストする］あなたは自分の控え室のレベルＸ以下のキャラを1枚選び、手札に戻す。Ｘはあなたの思い出の枚数に等しい。
'''


class W46_034( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "背伸びしたいお年頃乃絵里"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《風南島》', '《家族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《風南島》のキャラ1枚につき、このカードのパワーを＋500。
【自】この能力は1ターンにつき1回まで発動する。このカードが手札から舞台に置かれたターン中、このカードのバトル相手がリバースした時、あなたは自分の山札の上から1枚を控え室に置く。そのカードのトリガーアイコンにソウルマークがあるなら、このカードをスタンドする。
'''


class W46_035( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "気持ちに向き合って乃絵里"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《家族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたのキャラが1枚以下なら、他のあなたのキャラすべてに、パワーを＋1500。
【自】バトル中のこのカードがリバースした時、あなたは自分の山札の上から1枚を公開する。そのカードのレベルが1以上なら、あなたはこのカードをストック置場に置いてよい。（クライマックスのレベルは0として扱う。公開したカードは元に戻す）
'''


class W46_036( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "水族館デート乃絵里"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 2000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《家族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】記憶あなたがこのカードの『助太刀』を使った時、あなたの思い出置場の《風南島》のキャラが2枚以上なら、あなたは自分のバトル中のキャラを1枚選び、そのターン中、パワーを＋1500。
【起】●助太刀1500 レベル1［①手札のこのカードを控え室に置く］(あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋1500）
'''


class W46_037( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "緊張しすぎな乃絵里"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 7000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《家族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《風南島》のキャラが2枚以上なら、このカードのパワーを＋500し、「【自】アンコール[手札のキャラを1枚控え室に置く]」を得る。
【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚を公開する。そのカードがクライマックスならこのカードをレストする。(公開したカードは元に戻す)
'''


class W46_038( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "最愛の妹鳴"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《家族》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードがアタックした時、あなたのクロック置場に「お兄さん想いの鳴」があるなら、そのターン中、このカードのパワーを＋4000。
【自】◆シフト レベル0(あなたのメインフェイズの始めに、あなたは自分の手札の赤のカードを1枚とクロック置場のこのカードを選び、入れ替えてよい)
'''


class W46_039( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "二人で迎える朝乃絵里"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《家族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    ''''''


class W46_040( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "お風呂場で乃絵里"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《家族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、このカードをレストする。
'''


class W46_041( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "お兄さん想いの鳴"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《家族》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードがアタックした時、あなたのクロック置場に「最愛の妹 鳴」があるなら、そのターン中、このカードのパワーを＋4000。
【自】◆シフト レベル1(あなたのメインフェイズの始めに、あなたは自分の手札の赤のカードを1枚とクロック置場のこのカードを選び、入れ替えてよい)
'''


class W46_042( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "従妹の乃絵里"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 4500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《家族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】アラーム このカードがクロックの1番上にあり、あなたの《風南島》のキャラが2枚以上なら、あなたのクライマックスフェイズの始めに、あなたは自分のキャラを1枚選び、スタンドし、そのターン中そのキャラのパワーを＋2000。
'''


class W46_043( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "初めてのデート乃絵里"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 5000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《家族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】あなたのクライマックス置場に「本当の家族に」が置かれた時、あなたは自分のキャラを1枚選び、そのターン中、次の能力を与える。『【自】このカードがリバースした時、このカードのバトル相手のレベルがこのカードのレベル以下なら、あなたはそのキャラをリバースしてよい。』
【自】他のあなたのバトル中の《風南島》のキャラがリバースした時、あなたは自分のキャラを1枚選び、そのターン中、パワーを＋3000。
'''


class W46_044( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "常夏の楽園乃絵里"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《家族》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】相手の控え室のクライマックスが5枚以上なら、あなたの手札のこのカードのレベルを－1。
【自】このカードが手札から舞台に置かれた時、他のあなたの《風南島》のキャラが4枚以上なら、あなたは自分の山札の上から1枚を、ストック置場に置いてよい。
'''


class W46_045( EVENT ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "あたしのお兄ちゃん…"
        self.color = util.Color.RED
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 3
        self.cost = 2
        self.counter = False
        self.useCardLimit = None

    ''''''


class W46_046( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "絶対に幸せになるための第一歩"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('扉',)
        self.useCardLimit = None

    ''''''


class W46_047( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "本当の家族に"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None

    ''''''


class W46_048( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "朝のハプニング依愛"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《風南島》', '《中二病》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】記憶あなたの思い出置場の《風南島》のキャラが2枚以上なら、このカードのパワーを＋1000。
【自】このカードが手札から舞台に置かれた時、あなたは2枚まで引き、自分の手札を1枚選び、控え室に置く。
【自】[①]あなたのクライマックス置場に「魔王の娘、立つ」が置かれた時、前列にこのカードがいるなら、あなたはコストを払ってよい。そうしたら、あなたは他の自分の《風南島》のキャラを1枚と、このカードを選び、そのターン中、パワーを＋2500し、次の能力を与える。「【自】このカードのバトル相手がリバースした時、あなたは自分の山札の上から3枚を、控え室に置き、あいてにXダメージを与える。Xはそれらのカードのクライマックスの枚数に等しい。」(ダメージキャンセルは発生する)
'''


class W46_049( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "楽園へようこそ天"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《風南島》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたの《風南島》のキャラが4枚以上なら、あなたの手札のこのカードのレベルを－1。
【自】このカードが手札から舞台に置かれた時、あなたは自分のクロックの上から1枚を、控え室に置いてよい。
【自】このカードがアタックした時、あなたは他の自分の《風南島》のキャラを1枚選び、そのターン中、パワーを＋X。Xは他のあなたの《風南島》のキャラの枚数×500に等しい。
'''


class W46_050( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "少女型人工知能天"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは他のあなたの《風南島》のキャラを1枚選び、そのターン中、パワーを＋1000。
【自】[このカードを手札に戻す]あなたのクライマックスがクライマックス置場に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分のキャラを1枚選び、そのターン中、パワーを＋2000。
'''


class W46_051( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "水着の天"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】あなたのクライマックスがクライマックス置場に置かれた時、あなたは自分のキャラを1枚選び、次の相手のターンの終わりまで、パワーを＋500。
【起】集中［①あなたのキャラを2枚レストする］あなたは自分の山札の上から4枚をめくり、控え室に置く。それらのカードのクライマックス1枚につき、あなたは自分の山札を見て《風南島》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''


class W46_052( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "夢見がちな少女依愛"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《中二病》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から2枚を、控え室に置き、そのターン中、このカードのパワーを＋X。Xはそれらのカードの《風南島》のキャラの枚数×1000に等しい。
'''


class W46_053( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "違和感の正体依愛"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《中二病》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたのキャラすべてが《風南島》なら、このカードのパワーを＋1000。
【自】バトル中のこのカードがリバースした時、相手はあなたの控え室のキャラを1枚選び、山札の上に置いてよい。
'''


class W46_054( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "主従関係依愛"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《中二病》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《風南島》のキャラ1枚につき、このカードのパワーを＋500。
【自】［①］このカードのバトル相手がリバースした時、あなたのクライマックス置場に「これからの二人を」があるなら、あなたはコストを払ってよい。そうしたら、あなたは相手のコスト0以下のキャラを1枚選び、山札の下に置く。
'''


class W46_055( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "お姫様の願い依愛"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《中二病》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時か「魔王の娘 依愛」の【起】の効果で舞台に置かれた時、あなたは他の自分のキャラを1枚選び、そのターン中、パワーを＋1500。
【起】[あなたのキャラを2枚レストする]このカードを控え室に置く。あなたは自分の控え室の「魔王の娘 依愛」を1枚選び、このカードがいた枠に置く。
'''


class W46_056( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "魔王の娘依愛"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《中二病》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時か「お姫様の願い 依愛」の【起】の効果で舞台に置かれた時、そのターン中、このカードのパワーを＋X。Xはあなたの《風南島》のキャラの枚数×500に等しい。
【起】[あなたのキャラを2枚レストする]このカードを控え室に置く。あなたは自分の控え室の「お姫様の願い 依愛」を1枚選び、このカードがいた枠に置く。
'''


class W46_057( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "本当の幸せ天"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】記憶 あなたの思い出置場にカードがあるなら、このカードのパワー＋1500。
【自】あなたのクライマックス置場に「願いを流れ星に…」が置かれた時、前列にこのカードがいるなら、あなたは他の自分のキャラ1枚と、このカードを選び、そのターン中、次の能力を与える。「【自】このカードがアタックした時、あなたは自分の山札の上から1枚を公開する。そのカードが《風南島》のキャラなら手札に加える。」(そうでないなら元に戻す)
'''


class W46_058( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "爛々とした笑顔天"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 2500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】［② あなたの舞台のキャラを1枚控え室に置く］あなたがこのカードの『助太刀』を使った時、あなたはコストを払ってよい。そうしたら、あなたは相手の、レベルが相手のレベルより高いキャラを1枚選び、控え室に置く。
【起】●助太刀2500 レベル2［① 手札のこのカードを控え室に置く］(あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋2500)
'''


class W46_059( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "告白の返事天"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】［①］このカードのバトル相手でレベル2以上のキャラがリバースした時、あなたはコストを払ってよい。そうしたら、あなたは1枚引く。
【自】記憶このカードがアタックした時、あなたの思い出置場の《風南島》のキャラが2枚以上なら、そのターン中、このカードのパワーを＋Ｘ。Ｘはこのカードの正面のキャラのレベル×2000に等しい。
'''


class W46_060( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "着替え中の依愛"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《中二病》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】応援このカードの前のあなたのキャラすべてに、パワーを＋500。
【起】集中［①］あなたは自分の山札の上から4枚をめくり、控え室に置く。それらのカードのクライマックス1枚につき、あなたは自分の《風南島》のキャラを1枚選び、そのターン中、パワーを＋2000。
'''


class W46_061( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "水族館デート天"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】他のあなたのキャラが1枚以下なら、このカードのレベルを＋1し、パワーを＋1000。
【自】[①手札を1枚控え室に置き、このカードを思い出にする]バトル中のこのカードがリバースした時、あなたはコストを払ってよい。そうしたら、あなたは自分の山札を見て《風南島》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''


class W46_062( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ふたりの放課後天"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 2000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札を上から1枚見て、山札の上か下に置く。
【自】あなたのクライマックス置場に「喪われた楽園の管理者」が置かれた時、前列にこのカードがいるなら、あなたは自分の山札の上から1枚を公開する。そのカードがコスト0以下のキャラなら、あなたはそのキャラを舞台の好きな枠に置いてよい。（そうしないなら元に戻す）
'''


class W46_063( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "心地良き施術依愛"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《中二病》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】バトル中のこのカードがリバースした時、あなたは自分の山札の上から1枚を公開する。そのカードが《風南島》のキャラなら、あなたはこのカードを思い出にしてよい。(公開したカードは元に戻す)
'''


class W46_064( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ありのままで…依愛"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《中二病》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】［あなたの山札の上から1枚をクロック置場に置く］バトル中のこのカードがリバースした時、あなたはコストを払ってよい。そうしたら、このカードをレストし、このカードは次のあなたのスタンドフェイズにスタンドしない。
'''


class W46_065( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "水着の依愛"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《中二病》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    ''''''


class W46_066( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ミスコン出場天"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】このカードの正面のキャラに、『【自】アンコール［手札のキャラを1枚控え室に置く］』を与える。
【永】他のあなたのキャラすべてに、次の能力を与える。『【永】このカードはサイドアタックできない。』
'''


class W46_067( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "はじめてのキス天"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分のキャラを1枚選び、次の相手のターンの終わりまで、パワーを＋Ｘ。Ｘはそのキャラのレベル×500に等しい。
【自】［このカードを手札に戻す］あなたのクライマックスがクライマックス置場に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分のキャラを1枚選び、次の相手のターンの終わりまで、パワーを＋1000。 
'''


class W46_068( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "常夏の楽園天"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】[手札を1枚控え室に置く]このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたの控え室の「楽園システム」を1枚選び、手札に戻す。
【自】記憶 このカードがアタックした時、あなたの思い出置場にカードがあるなら、そのターン中、このカードのパワーを＋X。Xはあなたの《風南島》のキャラの枚数×500に等しい。
'''


class W46_069( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "天の後任者奏"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《風南島》', '《科学》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    ''''''


class W46_070( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "常夏の楽園依愛"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 6000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《風南島》', '《中二病》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたの山札が5枚以下なら、あなたの手札のこのカードのレベルを－1。
【永】他のあなたの《風南島》のキャラすべてに、パワーを＋1000。
'''


class W46_071( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "装束の錬金術師依愛"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7500
        self.level = 2
        self.cost = 1
        self.soul = 2
        self.feature = ('《風南島》', '《中二病》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】記憶あなたの思い出置場の《風南島》のキャラが2枚以上なら、他のあなたの《風南島》のキャラ1枚につき、このカードのパワーを＋500。
【自】アンコール［手札の青のカードを1枚控え室に置く］（このカードが舞台から控え室に置かれた時、あなたはコストを払ってよい。そうしたら、このカードがいた枠にレストして置く）
'''


class W46_072( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "親友というもの大和"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ('：',)
        self.power = 9500
        self.level = 2
        self.cost = 2
        self.soul = 2
        self.feature = ('《風南島》', '《新聞》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】舞台のこのカードのレベルを－1。
【自】このカードが手札から舞台に置かれた時、他のあなたの、《風南島》か《新聞》のキャラが4枚以上なら、あなたは自分の山札の上から1枚を、ストック置場に置いてよい。
'''


class W46_073( EVENT ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "楽園システム"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 1
        self.counter = False
        self.useCardLimit = None

    ''''''


class W46_074( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "魔王の娘、立つ"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.useCardLimit = None

    ''''''


class W46_075( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "これからの二人を"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None

    ''''''


class W46_076( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "願いを流れ星に…"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('本',)
        self.useCardLimit = None

    ''''''


class W46_077( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "喪われた楽園の管理者"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None

    ''''''


class W46_078( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ふたつの世界の物語リッカ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《魔法》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、そのターン中、このカードのパワーを＋X。Xはあなたの《魔法》か《生徒会》のキャラの枚数×500に等しい。
【自】[③手札を1枚控え室に置く]この能力は1ターンにつき1回まで発動する。このカードが手札から舞台に置かれたターン中、このカードのバトル相手がリバースした時、あなたはコストを払ってよい。そうしたら、このカードをスタンドする。
'''


class W46_079( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "浜辺のお願いシャルル"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードのバトル相手がリバースした時、あなたは他の自分の《魔法》か《生徒会》のキャラを1枚選び、レストし、後列のキャラのいない枠に動かす。
'''


class W46_080( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "桜の研究リッカ"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードの正面のキャラのレベルがこのカードのレベルより高いなら、このカードはフロントアタックできない。
'''


class W46_081( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "エトが願ったことシャルル"
        self.color = util.Color.YELLOW
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 7500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】記憶このカードがアタックした時、あなたの思い出が2枚以上なら、そのターン中、このカードのパワーを＋Ｘ。Ｘはあなたの、《魔法》か《生徒会》のキャラの枚数×1000に等しい。
'''


class W46_082( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "あたたかな膝の上で四季"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》', '《人形》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《魔法》のキャラすべてに、パワーを＋500。
【起】集中[①あなたのキャラを2枚レストする]あなたは自分の山札の上から4枚をめくり、控え室に置く。それらのカードのクライマックス1枚につき、あなたは自分の山札を見て、《魔法》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''


class W46_083( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "まるでハネムーンのように姫乃"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 4500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》', '《和服》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《魔法》のキャラ1枚につき、このカードのパワーを＋500。
'''


class W46_084( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "表彰式姫乃"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《魔法》のキャラすべてに、パワーを＋500。
【自】このカードが手札から舞台に置かれた時、あなたのクロックの下から1枚と控え室の《魔法》のキャラを1枚選び、入れ替えてもよい。
'''


class W46_086( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "チョコレートバナナ四季"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 2000
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》', '《人形》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】あなたがこのカードの『助太刀』を使った時、あなたの《魔法》か《人形》のキャラがいるなら、あなたは自分のバトル中のキャラを1枚選び、そのターン中、パワーを＋1000。
【起】●助太刀2500 レベル2［手札のこのカードを控え室に置く］(あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋2500)
'''


class W46_087( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "図書館の中で四季"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《魔法》', '《人形》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他の自分のレベル3以上のキャラがいるなら、このカードのパワー+2000。
【自】相手のターン中、自分の受けたダメージがキャンセルされなかった時、前列にこのカードがいるなら、自分の山札を上から1枚見て、山札の上か控え室に置く。
'''


class W46_088( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "未来の花嫁さんサラ"
        self.color = util.Color.GREEN
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6000
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《魔法》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《魔法》か《スポーツ》のキャラ1枚につき、このカードのパワーを＋500。
'''


class W46_089( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "気持ちのゆらぎ美琴"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《新聞》', '《愛》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚を公開する。そのカードが《新聞》か《愛》のキャラなら手札に加え、あなたは手札を1枚選び、控え室に置く。(そうでないなら元に戻す)
【自】このカードがリバースした時、このカードのバトル相手のレベルが0以下なら、あなたはそのキャラをリバースしてよい。
'''


class W46_090( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "初夏の夢シャルル"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《新聞》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】応援このカードの前のあなたのキャラすべてに、パワーを＋500。
【起】集中［①あなたのキャラを2枚レストする］あなたは自分の山札の上から4枚をめくり、控え室に置く。それらのカードのクライマックス1枚につき、あなたは自分の控え室のキャラを1枚まで選び、手札に戻す。
'''


class W46_091( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "ふたつの世界の物語立夏"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《新聞》', '《生徒会》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】記憶 このカードがアタックした時、クライマックス置き場に「With You」があるなら、あなたは自分の控え室のレベルX以下の《新聞》か《生徒会》のキャラを1枚選び、手札に戻してよい。Xはあなたの思い出の枚数に等しい。
'''


class W46_092( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "もっと素直に美琴"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《新聞》', '《愛》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚を公開する。そのカードが《新聞》か《愛》のキャラなら、あなたは相手に1ダメージ与えてよい。(ダメージキャンセルは発生する。公開したカードは元に戻す)
【自】このカードがアタックした時、あなたは他の自分の《新聞》か《愛》のキャラを1枚選び、そのターン中、パワーを＋2000。
'''


class W46_093( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "潤んだ瞳立夏"
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

    '''【自】［手札のクライマックスを1枚控え室に置く］このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室の自分のレベル以下のレベルでコスト0以下の、《新聞》か《生徒会》のキャラを1枚選び、舞台の好きな枠に置く。
【起】［①このカードを思い出にする］あなたは自分の山札を上から4枚まで見て、《新聞》か《生徒会》のキャラを1枚まで選んで相手に見せ、手札に加え、残りのカードを控え室に置く。
'''


class W46_094( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "将来の夢美琴"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1000
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《新聞》', '《愛》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの《新聞》か《愛》のキャラすべてに、パワーを＋500。
【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から2枚を、控え室に置く。それらのカードにクライマックスがあるなら、あなたは自分のキャラを1枚選び、そのターン中、パワーを＋1500。
'''


class W46_095( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "はぐれる美琴"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 2000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《新聞》', '《愛》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】あなたがこのカードの『助太刀』を使った時、あなたの《新聞》か《愛》のキャラがいるなら、あなたは自分のバトル中のキャラを1枚選び、そのターン中、パワーを＋1000。
【起】●助太刀1000 レベル1［手札のこのカードを控え室に置く］(あなたは自分のフロントアタックされているキャラを1枚選び、そのターン中、パワーを＋1000)
'''


class W46_096( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "初夏の夢姫乃"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 3000
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《新聞》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードが手札から舞台に置かれた時、あなたは自分の山札の上から1枚見て、山札の上か控え室に置く。
【自】このカードがリバースした時、このカードのバトル相手のレベルが1以下なら、あなたはそのキャラをリバースしてよい。
'''


class W46_097( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "律儀な腹ペコ珍獣美琴"
        self.color = util.Color.RED
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 5500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《新聞》', '《愛》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】応援このカードの前のあなたのレベル3以上のキャラすべてに、パワーを＋2000。
【起】[このカードをレストする]あなたは自分の山札の上から1枚を公開する。そのカードが《新聞》か《愛》のキャラなら、あなたは自分のキャラを1枚選び、そのターン中、レベルを＋4。(公開したカードは元に戻す)
'''


class W46_098( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "WithYou"
        self.color = util.Color.RED
        self.cardType = util.CardType.CX
        self.trigger = ('util.Trigger.TWO',)
        self.useCardLimit = None

    ''''''


class W46_099( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "幸せな時間すもも"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 10000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《委員長》', '《演劇》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】舞台のこのカードのレベルを－3。このカードのパワーを＋Xし、このカードは相手の【自】の効果によってリバースされない。Xはこのカードの正面のキャラのレベル×1000に等しい。
【自】このカードが手札から舞台に置かれた時、あなたは自分のクロックの上から1枚を、控え室に置いてよい。
【自】[③手札の「守りたい笑顔 すもも」を1枚控え室に置く]この能力は1ターンにつき1回まで発動する。あなたの前列の中央の枠のキャラがアタックした時、クライマックス置場に「出会いの一冊」があるなら、あなたはコストを払ってよい。そうしたら、このカードをスタンドする。
'''

    def permanentEffect(self, player1, player2, position):
        """
        TODO : 効果リバース無効の実装
        舞台のこのカードのレベルを-3。効果リバース無効。正面のキャラのレベル×1000パンプ
        """

        def increasePower():
            oppositePosition = player1.MYFIELD["Stage"].oppositePosition( position + 1 )
            if player2.charaExistCheck( oppositePosition - 1 ):
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
        player1.cardEffect.CharaEffect.recovery( player1 )

    def selfAttackTrigger(self, player1, _, position):
        if isinstance( player1.MYFIELD["Stage"][position][0], type( self ) ):
            pass
        else:
            exist_SUMOMO = False
            costCheck = False
            if player1.MYFIELD["Stock"].costCheck( 0 ):
                costCheck = True
            for card in player1.MYFIELD["Hand"]:
                if card.name == "守りたい笑顔 すもも":
                    exist_SUMOMO = True
                    break

            if costCheck and exist_SUMOMO:
                print( "{} : 中央のキャラのアタック時3コストと手札の「守りたい笑顔 すもも」を控室に置くことで、このカードをスタンドする".format( self.name ) )
                flag = util.effectConfirm()
                if flag == 1:
                    player1.useCost( 0 )
                    for i, card in enumerate( player1.MYFIELD["Hand"] ):
                        if card.name == "守りたい笑顔 すもも":
                            player1.MYFIELD["Waiting_Room"].append( player1.MYFIELD["Hand"].pop( i ) )
                            break
                    for i in range( 5 ):
                        if player1.MYFIELD["Stage"][i][0].name == "幸せな時間 すもも":
                            player1.MYFIELD["Stage"][i][0].status = util.Status.STAND
                            player1.standCount += 1
                            print( "スタンドしました" )
                            break

    def CXcombo(self, player1, player2, position, useCard):
        def effect():
            return self.selfAttackTrigger

        if isinstance( useCard, W46_109 ):
            player1.untilTurnEndEffect.adaptField( player1, player2, (player1, position),
                                                   [(player1, 1)], [lambda: True],
                                                   [("appendEffect", effect, "selfAttackTrigger")] )


class W46_100( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "グニルックの練習葵"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《魔法》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】応援このカードの前のあなたのキャラすべてに、パワーを＋500。
【起】［②このカードをレストする］あなたは自分の山札を見て《魔法》か《ウェイトレス》のキャラを1枚まで選んで相手に見せ、手札に加え、その山札をシャッフルする。
'''


class W46_101( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "人間観察すもも"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 1500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《委員長》', '《演劇》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】他のあなたの前列の中央の枠のキャラに、次の能力を与える。「【永】このカードは相手のキャラの【自】の効果によってリバースされない。」
【自】[①]あなたのクライマックスがクライマックス置場に置かれた時、あなたはコストを払ってよい。あなたは自分の山札の上から4枚まで見て、青のキャラを1枚まで選んで相手に見せ、手札に加え、残りのカードを控え室に置く。
'''


class W46_102( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "聖夜の輝きさら"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9000
        self.level = 3
        self.cost = 2
        self.soul = 2
        self.feature = ('《新聞》', '《スポーツ》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】あなたの控え室のクライマックスが2枚以下なら、あなたの手札のこのカードのレベルを－1。
【永】他のあなたの《新聞》か《スポーツ》のキャラ1枚につき、このカードのパワーを＋500。
【自】このカードが手札から舞台に置かれた時、あなたは2枚まで引き、自分の手札を1枚選び、控え室に置く。
'''


class W46_103( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "一つ傘の下すもも"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 500
        self.level = 0
        self.cost = 0
        self.soul = 1
        self.feature = ('《委員長》', '《演劇》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】応援このカードの前のあなたのレベル0以下のキャラすべてに、パワーを＋1000。
【起】［②あなたのキャラを2枚レストする］あなたは自分の山札を上から2枚まで見て、カードを1枚まで選び、手札に加え、残りのカードを控え室に置く。
'''


class W46_104( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "新しい一年の始まり葵"
        self.color = util.Color.BLUE
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

    '''【自】［①手札のクライマックスを1枚控え室に置く］このカードが手札から舞台に置かれた時、あなたはコストを払ってよい。そうしたら、あなたは自分の控え室のクライマックスを1枚選び、手札に戻す。
'''

    def cipEffect(self, player1, _, __):
        if len( player1.MYFIELD["Stock"] ) >= 1:
            print( "{} : 登場時1コスト、手札のCXを一枚控室に置くことで、控室のCXを回収する".format( self.name ) )
            flag = util.effectConfirm()
            if flag == 1:
                player1.useCost( 1 )
                player1.MYFIELD["Hand"].showHand()
                while True:
                    select_card = util.selectNumberChecker( 1, len( player1.MYFIELD["Hand"] ), "カードを選んでください" )
                    if player1.MYFIELD["Hand"][select_card - 1].cardType == util.CardType.CX:
                        print( "控室のCXを回収します" )
                        print( "----------" )
                        player1.MYFIELD["Waiting_Room"].showWaitingRoom()
                        while True:
                            select_salvage_card = util.selectNumberChecker(
                                1, len( player1.MYFIELD["Waiting_Room"] ), "カードを選んでください"
                            )
                            if player1.MYFIELD["Waiting_Room"][select_salvage_card - 1].cardType == util.CardType.CX:
                                player1.MYFIELD["Hand"].append(
                                    player1.MYFIELD["Waiting_Room"].pop( select_salvage_card - 1 )
                                )
                                break
                            else:
                                print( "CXカードを選んでください" )
                        break
                    else:
                        print( "CXカードを選んでください" )


class W46_105( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "初夏の夢葵"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 6500
        self.level = 1
        self.cost = 1
        self.soul = 1
        self.feature = ('《新聞》',)
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【自】このカードのバトル相手がリバースした時、あなたのクライマックス置場に「夢だけど……」があるなら、あなたは自分の山札の上から4枚まで見て、 《新聞》か《ウェイトレス》のキャラを1枚まで選んで相手に見せ、手札に加え、残りのカードを控え室に置き、自分のキャラを1枚選び、次の相手のターンの終わりまで、パワーを＋1000。
'''


class W46_106( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "守りたい笑顔すもも"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = ()
        self.power = 5500
        self.level = 1
        self.cost = 0
        self.soul = 1
        self.feature = ('《委員長》', '《演劇》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】舞台のこのカードのレベルを－1。
【永】他のあなたのレベル0以下のキャラ1枚につき、このカードのパワーを＋500。
'''

    def permanentEffect(self, player1, player2, position):
        def limit():
            return True

        def increaseEffect():
            return player1.MYFIELD["Stage"].countLevel( player1, (0,) ) * 500

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


class W46_107( CHARA ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "砂糖のような甘い恋すもも"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CHARA
        self.trigger = (util.TriggerType.SOUL_ONE,)
        self.power = 9500
        self.level = 2
        self.cost = 1
        self.soul = 1
        self.feature = ('《委員長》', '《演劇》')
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None

    '''【永】舞台のこのカードのレベルを－2。このカードは相手のキャラの【自】の効果によってリバースされない。
'''


class W46_108( EVENT ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "すももの絵本"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.EVENT
        self.trigger = ()
        self.level = 1
        self.cost = 1
        self.counter = False
        self.useCardLimit = None

    ''''''


class W46_109( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "出会いの一冊"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = (util.TriggerType.SOUL_TWO,)
        self.useCardLimit = None

    ''''''

    def permanentEffect(self, player):
        color_flag = False
        for card in player.MYFIELD["Waiting_Room"]:
            if card.color == util.Color.BLUE:
                color_flag = True
                break
        if color_flag is True:
            print( "{} : 控室の青のカードを1枚ストックに置く".format( self.name ) )
            flag = util.effectConfirm()
            if flag == 1:
                player.MYFIELD["Waiting_Room"].showWaitingRoom()
                while True:
                    select_card = util.selectNumberChecker( 1, len( player.MYFIELD["Waiting_Room"] ), "カードを選んでください : " )
                    if player.MYFIELD["Waiting_Room"][select_card - 1].color == util.Color.BLUE:
                        player.MYFIELD["Stock"].append( player.MYFIELD["Waiting_Room"].pop( select_card - 1 ) )
                        break
                    else:
                        print( "青のカードを選んで下さい" )

        print( "{} : 自分のキャラすべてのソウルを+1".format( self.name ) )
        for i in range( 5 ):
            if len( player.MYFIELD["Stage"][i] ) != 0:
                player.MYFIELD["Stage"][i][0].soul += 1
                print( "{} に効果を使いました".format( player.MYFIELD["Stage"][i][0].name ) )
                print( "パワー : {}".format( player.MYFIELD["Stage"][i][0].power ) )
                print( "ソウル : {}".format( player.MYFIELD["Stage"][i][0].soul ) )
        return [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]


class W46_110( CX ):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "夢だけど……"
        self.color = util.Color.BLUE
        self.cardType = util.CardType.CX
        self.trigger = ('本',)
        self.useCardLimit = None

    ''''''
