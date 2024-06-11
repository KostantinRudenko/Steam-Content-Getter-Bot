import requests
from bs4 import BeautifulSoup

class Parser:
    def __init__(self) -> None:
        self.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
        }
    
    def get_fifty_objects(link):
        req = requests.get("https://store.steampowered.com/search/results/?query&start=0&count=50&dynamic_data=&sort_by=Released_DESC&snr=1_7_7_230_7&supportedlang=russian&os=win&infinite=1")

        res = {}
        count = 0

        soup = BeautifulSoup(req.text, "lxml")
        games = soup.find_all("a", onmouseout="HideGameHover( this, event, 'global_hover' )")
        for game in games:

            name = game.find("span", class_ = "title").text
            price = game.find("div", class_="discount_final_price").text
            date = game.find("div", class_="col search_released responsive_secondrow").text.strip()
            link = game.get("href")

            res[count] = {
                "name" : name,
                "price" : price,
                "date" : date,
                "link" : link
                }
        
        return res