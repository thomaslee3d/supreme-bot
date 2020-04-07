import requests
import bs4
from splinter import Browser
from selenium import webdriver

class SupremeBot:
    def __init__(self, **info):
        self.base = 'https://www.supremenewyork.com/'
        self.shop_ext = "shop/all/"
        self.checkout_ext = "checkout/"
        self.info = info


    def init_browser(self):
        chrome_path = '/Downloads/chromedriver'
        driver = webdriver.chrome(chrome_path)
        self.b = Browser(driver)

    def find_product(self):
        r = requests.get("{}{}{}".format(self.base, self.shop_ext, self.info["category"])).text
        soup = bs4.BeautifulSoup(r, "lxml")
        temp_tuple = []
        temp_link = []
        print(r)

        for link in soup.find_all("a", href=True):
            temp_tuple.append((link["href"], link.text))

        for i in temp_tuple:
            if i[1] == self.info["product"] or i[1] == self.info["color"]:
                temp_link.append(i[0])

        self.final_link = list(set([x for x in temp_link if temp_link.count(x) == 2]))[0]
        print(self.final_link)


# link should look like this at these settings shop/tops-sweaters/vi9zu0emv/l1whbfsz0


if __name__ == "__main__":
    INFO = {
        "product": "Studded L/S Top",
        "color": "Black",
        "Size": "Medium",
        "category": "tops_sweaters",
        "namefield": "example",
        "emailfield": "example@example.com",
        "phonefield": "XXXXXXXXXX",
        "addressfield": "example road",
        "city": "example",
        "zip": "XXXXX",
        "country": "USA",
        "card": "visa",
        "number": "XXXXXXXXXXXX",
        "month": "XX",
        "year": "XXXXX",
        "ccv": "XXXX"
    }

    bot = SupremeBot(**INFO)
    bot.find_product()
