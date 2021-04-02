import sqlite3
from contextlib import closing

if __name__ == '__main__':
    lead_sentence = """
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
        

    """
    chara_card = """

class {}(CHARA):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "{}"
        self.color = {}
        self.cardType = util.CardType.CHARA
        self.trigger = {}
        self.power = {}
        self.level = {}
        self.cost = {}
        self.soul = {}
        self.feature = {}
        self.status = util.Status.STAND
        self.counter = False
        self.attackLimit = False
        self.appendEffect = None
        self.useCardLimit = None
    \'\'\'{}\'\'\'
    """

    event_card = """
    
class {}(EVENT):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "{}"
        self.color = {}
        self.cardType = util.CardType.EVENT
        self.trigger = {}
        self.level = {}
        self.cost = {}
        self.counter = False
        self.useCardLimit = None
    \'\'\'{}\'\'\'
    """

    cx_card = """
    
class {}(CX):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.name = "{}"
        self.color = {}
        self.cardType = util.CardType.CX
        self.trigger = {}
        self.useCardLimit = None
    \'\'\'{}\'\'\'
    """

    dbname = "CardInformation.db"
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        pack_file = input("ID : ")
        card_data = c.execute("select * from card where id like '{}%'".format(pack_file))
        with open("{}.py".format(pack_file), "wt") as f:
            for data in card_data:
                print(data)
                color = None
                if data[3] == "黄":
                    color = "util.Color.YELLOW"
                elif data[3] == "緑":
                    color = "util.Color.GREEN"
                elif data[3] == "赤":
                    color = "util.Color.RED"
                elif data[3] == "青":
                    color = "util.Color.BLUE"
                else:
                    color = None

                trigger = None
                if data[6] == 0 or data[6] is None:
                    trigger = "()"
                elif data[6] == 1:
                    trigger = ("util.TriggerType.SOUL_ONE",)
                elif data[6] == 2:
                    trigger = ("util.TriggerType.SOUL_TWO",)
                elif data[6] is None:
                    trigger = None
                elif data[6].find("・"):
                    trigger = tuple(data[6].split("・"))

                feature = None
                if data[9] == "なし":
                    feature = ()
                elif data[10] == "なし":
                    feature = (data[9],)
                else:
                    feature = (data[9], data[10])

                f.write(lead_sentence)
                if data[2] == "キャラ" or data[2] == "キャラクター":
                    f.write(chara_card.format(
                        data[0][:7], data[1], color, trigger, data[7],
                        data[4], data[5], data[8], feature, data[11])
                    )
                elif data[2] == "イベント":
                    f.write(event_card.format(
                        data[0][:7], data[1], color, trigger, data[4], data[5], data[11])
                    )
                elif data[2] == "クライマックス":
                    f.write(cx_card.format(data[0][:7], data[1], color, trigger, data[11]))
