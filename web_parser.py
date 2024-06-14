import requests
from bs4 import BeautifulSoup
import re

from config import *

# Parser for steam
class WebParser:
    def __init__(self) -> None:
        self.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
        self.soup = None


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
    
    def is_excists_a(self, class_, name: str):
        resp = requests.get(SEARCH_LINK+"term="+name.replace(" ", "+"))
        self.soup = BeautifulSoup(resp.text, "lxml")
        res = self.soup.find("div", id="search_results").find("a", class_=class_)
        if res:
            return res
        else:
            return False
    
    def get_first_game_soup(self):
        # getting first game link from search page with results
        first_game = requests.get(self.soup.find("div", id="search_resultsRows")
                                 .find("a", onmouseout="HideGameHover( this, event, 'global_hover' )")
                                 .get("href"))
        
        soup = BeautifulSoup(first_game.text, "lxml")
        return soup
    
    def get_desc(self):
        
        soup = self.get_first_game_soup()
        res = soup.find("div", class_="game_description_snippet").text

        return res

    def get_price(self):
        soup = self.get_first_game_soup()
        return soup.find("div", class_="discount_final_price").text
    
    def get_devers(self):
        soup = self.get_first_game_soup()
        # right panel
        panel = soup.find("div", class_="glance_ctn_responsive_left")
        devs = panel.find_all("div", class_="dev_row")
        
        # getting developers and publisher
        dev = devs[0].find("div", class_="summary column").next_element.next_element
        pub = devs[1].find("div", class_="summary column").next_element.next_element
        
        #formating
        dev = "Developer: " + dev.text
        pub = "Publisher: " + pub.text

        return {"dev" : dev,
                "pub" : pub}
    
    def get_reviews(self):
        soup = self.get_first_game_soup()
        # right panel
        panel = soup.find("div", class_="glance_ctn_responsive_left").find("div", id="userReviews")
        revs = panel.find_all("div", class_="summary column")
        
        # getting values
        nearest_revs = revs[0].find_all("span")[0].text
        all_revs = revs[1].find_all("span")[0].text
        
        #formating
        all_revs = "All: " + all_revs
        nearest_revs = "Nearest: " + nearest_revs

        return {"all" : all_revs,
                "nrst" : nearest_revs}
    
    def get_date(self):
        soup = self.get_first_game_soup()
        # right panel
        panel = soup.find("div", class_="glance_ctn_responsive_left")
        date = panel.find("div", class_="date").text
        res = "Release date: " + date
        return res