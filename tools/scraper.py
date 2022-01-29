import requests
import warnings
from xml.dom.minidom import Element
from bs4 import BeautifulSoup



class Scraper():
    def __init__(self):
        self.url = None
        self.product_page = None

    def open_url(self, parser: str, element: str, attribute: dict, headers :dict = None) -> Element:
        """Open given e-commerce url (Ebay, Amazon)

        Args:
            parser (str): BS4 supported parser example: 'html.parser'
            element (str): Html element contains content
            attribute (dict): Specific html attribute that includes content
                example: {"id": "myID"}

        Returns:
            Element: Element of content
        """

        if headers != None:
            req = requests.get(self.url, headers=headers)
        else:
            req = requests.get(self.url)

        soup = BeautifulSoup(req.content, parser)
        self.product_page = soup.find(element, attribute)

        # Check if page is empty
        if self.product_page == None:
            warnings.warn("Product unavailable or Page not found... skipping")

        return self.product_page

    
    def get_product_name(self, element: str, attribute: dict) -> str:
        """Extracts product name from page elements

        Args:
            element (str): Html element that contains product name
            attribute (dict): Specific attribute that contains element
                example: {"id": "myID"}

        Returns:
            str: Product title
        """

        product_name_element = self.product_page.find(element, attribute)
        if product_name_element != None:
            product_name = product_name_element.get_text()
            
            return product_name

    def get_price(self, element: str, attribute: dict) -> str:
        """Extracts product price from page elements

        Args:
            element (str): Html element that contains product name
            attribute (dict): Specific attribute that contains element
                example: {"id": "myID"}

        Returns:
            str: Product price
        """

        # Converted Price
        # price_element = self.product_page.find("span", {"id": "convbidPrice"})

        # Unconverted Price
        price_element = self.product_page.find(element, attribute) 
        if price_element != None:
            price = price_element.get_text()
            
            return price

    
    def get_image_url(self, element: str, attribute: dict) -> str:
        """Extracts product Image URL in src attribute

        Args:
            element (str): Html element that contains product name
            attribute (dict): Specific attribute that contains element
                example: {"id": "myID"}

        Returns:
            int: Product Image URL
        """
        image_element = self.product_page.find(element, attribute)
        if image_element != None:
            product_img = image_element['src']
            
            return product_img

    def get_currency(self, element: str, attribute: dict) -> str:
        """Extract price currency from html element

        Args:
            element (str): Html element that contains product name
            attribute (dict): Specific attribute that contains element
                example: {"id": "myID"}

        Returns:
            int: Product Image URL
        """
        currency_element = self.product_page.find(element, attribute)
        if currency_element != None:
            currency = currency_element["content"]

            return currency

            