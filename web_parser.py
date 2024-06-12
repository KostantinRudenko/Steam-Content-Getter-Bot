import requests
from bs4 import BeautifulSoup

from config import *

# Parser for steam
class WebParser:
    def __init__(self) -> None:
        self.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
    
    def get_new(self, count):
        response = requests.get(NEW_GAMES_LINK.format(count=count))

        res = []

        s = BeautifulSoup(response.text, "lxml")
        # Getting all game links
        games = s.find_all("a", onmouseout="HideGameHover( this, event, 'global_hover' )")
        for game in games:

            name = game.find("span", class_ = "title").text
            price = game.find("div", class_="discount_final_price").text
            date = game.find("div", class_="col search_released responsive_secondrow").text.strip()
            link = game.get("href")

            # Saving
            res.append({
                "Name" : name,
                "Price" : price,
                "Date" : date,
                "Link" : link
                })
        
        return res

if __name__ == "__main__":
    wp = WebParser()
    print(wp.get_new())