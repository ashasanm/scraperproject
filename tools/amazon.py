import re

from .scraper import Scraper
from .utils.preprocessor import Preprocessor

class Amazon(Scraper):
    def __init__(self):
        super().__init__()
        self.HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36',
                        'Accept-Language': 'en-US, en;q=0.5'})
        self.cleaner = Preprocessor()

    
    def check_price(self, price: any) -> str:
        """Check if current extracted price is empty

        Args:
            price (any): Extracted price

        Returns:
            str: Product price
        """
        if price != None:
            return price
            
        return self.get_price("span", {"id": "priceblock_ourprice"})

    
    def scrap_product(self, url):
        self.url = url
        self.product_page = self.open_url("lxml", "div", {"id": "dp"}, headers=self.HEADERS)

        # Check product or page existence
        if self.product_page == None:
            return None

        # Extract Product Information
        product_name = self.get_product_name("span", {"id": "productTitle"})
        product_name = self.cleaner.clean_product_name(product_name)
        price = self.get_price("span", {"data-a-color": "price"})
        price = self.check_price(price)
        currency = self.cleaner.extract_currency(price)
        price = self.cleaner.clean_price(price)
        image_url = self.get_image_url("img", {"class": "a-dynamic-image"})

        product = {
            "product_name": product_name,
            "price": price,
            "currency": currency,
            "image_url": image_url
        }

        return product
