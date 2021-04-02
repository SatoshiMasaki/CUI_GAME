import requests
from requests import HTTPError
from bs4 import BeautifulSoup
import time
import manageDatabase
import re


def pack_page(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
                    }
        pack_page = requests.get(url=url, headers=headers)
        bsobj_ = BeautifulSoup(pack_page.text, "html.parser")
        card_page_list = bsobj_.table.find_all("a")
        # card_page_list = bsobj_.find_all("table")
        # card_page_list = card_page_list[2].find_all("a")
        for i in card_page_list:
            print(i)
            print("-----")
        for i, card_page in enumerate(card_page_list):
            if card_page.text == "レアリティ":
                print("レアリティのリンクをスキップします")
                continue
            elif card_page["title"] == "作成されていません":
                print("特徴ページのリンクをスキップします")
                continue

            time.sleep(3)
            card_page_html = requests.get(url="https:" + card_page["href"], headers=headers)
            print("https:"+card_page["href"])
            card_page_bsobj = BeautifulSoup(card_page_html.text, "html.parser")
            information_block = str(card_page_bsobj.find("blockquote")).split("<br/>")

            information_block[0] = information_block[0].replace("\n", "").replace(" ", "")
            card_id_index = information_block[0].find("/")
            card_id = information_block[0][card_id_index + 1:].replace("-", "_").replace(" ", "")
            card_name_index = information_block[1].find("：")
            card_name = information_block[1][card_name_index + 1:].replace("\n", "").replace(" ", "")
            card_type_index = information_block[2].find("：")
            card_type = information_block[2][card_type_index + 1:].replace("\n", "").replace(" ", "")
            color = information_block[3][3:-1]

            trigger = None
            level = None
            cost = None
            soul = None
            power = None
            feature_list = None
            if card_type == "キャラ" or card_type == "キャラクター":
                level = information_block[4][5]
                cost = information_block[4][11]
                soul_index = information_block[5].replace("\n", "").find("ソウル")
                power = 0
                if soul_index == 8:
                    power = information_block[5][5:8]
                elif soul_index == 9:
                    power = information_block[5][5:9]
                elif soul_index == 10:
                    power = information_block[5][5:10]
                soul = information_block[5][soul_index + 5]
                trigger = information_block[4][18]
                feature_list = re.findall("《.{1,4}》", information_block[6])
            elif card_type == "イベント":
                level = information_block[4][5]
                cost = information_block[4][11]
                trigger = information_block[4][18]
                power = ""
                soul = ""
                feature_list = []
            elif card_type == "クライマックス" or card_type == "CX":
                level = ""
                cost = ""
                power = ""
                soul = ""
                feature_list = []
                trigger = information_block[4][6]

            effect_list = []
            for i, data_string in enumerate(information_block):
                if i <= 6:
                    continue
                if "【" in data_string:
                    effect_list.append(data_string.replace("<div>", "").replace("</div>", "").replace("\n", ""))
                else:
                    break

            has_two_tag = re.compile("<.*>.*<.*>")
            for i, effect_sentence in enumerate(effect_list):
                while True:
                    if re.search(has_two_tag, effect_sentence):
                        start_tag = effect_sentence.find("<")
                        end_tag = effect_sentence.find(">")
                        effect_sentence = effect_sentence.replace(effect_sentence[start_tag:end_tag + 1], "", 1)
                    else:
                        start_tag = effect_sentence.find("<")
                        end_tag = effect_sentence.find(">")
                        effect_sentence = effect_sentence.replace(effect_sentence[start_tag:end_tag + 1], "",
                                                                   1).replace("?", "")
                        effect_list[i] = effect_sentence
                        break

            feature1 = "なし"
            feature2 = "なし"
            if feature_list is None:
                print("feature_listはNoneです")
            elif len(feature_list) == 2:
                feature1 = feature_list[0]
                feature2 = feature_list[1]
            elif "《特徴なし》" in feature_list or len(feature_list) == 0:
                pass
            else:
                feature1 = feature_list[0]
            insert_effect = ""
            if len(effect_list) != 0:
                for sentence in effect_list:
                    insert_effect += sentence
                    insert_effect += "\n"
            print("card_id : ", card_id)
            print("card_name : ", card_name)
            print("card_type : ", card_type)
            print("color : ", color)
            print("level : ", level)
            print("cost : ", cost)
            print("trigger : ", trigger)
            print("power : ", power)
            print("soul : ", soul)
            print("feature1 : ", feature1)
            print("feature2 : ", feature2)
            print("insert_effect : ", insert_effect)

            insert_data = (
                card_id, card_name, card_type, color, level, cost,
                trigger, power, soul, feature1, feature2, insert_effect
            )
            manageDatabase.insertDatabase(insert_data)
    except requests.HTTPError as err:
        print(err)


if __name__ == '__main__':
    url = input("URL : ")
    pack_page(url)
