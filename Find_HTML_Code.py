import requests
import warnings
from bs4 import BeautifulSoup
from bs4 import GuessedAtParserWarning

def all():
    warnings.filterwarnings('ignore', category=GuessedAtParserWarning)

    text_html = requests.get("https://towardsdatascience.com", "lxml")



    soup = BeautifulSoup(text_html.text)
    perviy_post_na_stranice = soup.find("div", class_="col u-xs-size12of12 js-trackPostPresentation u-paddingLeft12 "
                                          "u-marginBottom15 u-paddingRight12 u-size6of12" ).find("a")

    id_posta = soup.find("div", class_="col u-xs-size12of12 js-trackPostPresentation u-paddingLeft12 u-marginBottom15"
                                       " u-paddingRight12 u-size6of12").get("data-post-id")
    cartinka_2 = soup.find("div", class_="u-lineHeightBase postItem").find("a").get("style").split('"')[1]


    new_text_html = requests.get(perviy_post_na_stranice.get("href"))
    soup = BeautifulSoup(new_text_html.text)

    #cartinka = soup.find("source").get("srcset").split(",")[0]
    shapka_posta = soup.find("h1", {"data-testid":"storyTitle"}).text
    text_posta = soup.find_all("p",{"data-selectable-paragraph":""})[10].text


    return [id_posta, cartinka_2,shapka_posta,text_posta]

print(all())
