from .scraper import Scraper
from .utils.preprocessor import Preprocessor


class Ebay(Scraper):
    def __init__(self):
        super().__init__()
        self.cleaner = Preprocessor()

    
    def check_currency(self, currency):
        if currency != None:
            return currency
        else:
            price = self.get_price("span", {"class": "notranslate"})
            currency = self.cleaner.extract_currency(price)

            return currency


    def scrap_product(self, url):
        self.url = url
        self.product_page = self.open_url("html.parser", "div", {"id": "CenterPanel"})

        # Check product or page existence
        if self.product_page == None:
            return None
        
        # Extracts Product Information
        product_name = self.get_product_name("h1", {"id": "itemTitle"})
        product_name = self.cleaner.clean_product_name(product_name)
        price = self.get_price("span", {"class", "notranslate"})
        # Remove any currency and any text
        price = self.cleaner.clean_price(price)
        currency = self.get_currency("span", {"itemprop": "priceCurrency"})
        currency = self.check_currency(currency)
        image_url = self.get_image_url("img", {"id": "icImg"})

        # Product Details
        product = {
            'product_name': product_name,
            'price': price,
            'currency': currency,
            'product_image': image_url,
            'product_url': self.url
        }

        return product