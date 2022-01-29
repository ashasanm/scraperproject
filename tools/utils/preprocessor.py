import re


class Preprocessor():
    def clean_product_name(self, product_name: str) -> str:
        """Cleaning product name from unrelated text

        Args:
            product_name (str): Raw product name

        Returns:
            str: Processed product name
        """
        
        product_name = product_name.replace("Details about  \xa0", "")
        product_name = product_name.replace("Details about  ", "")
        product_name = product_name.replace("\n", "").strip().lower()
        
        return product_name

    def clean_price(self, price: str) -> str:
        """Extract price with regex (0-9, "," , ".")

        Args:
            price (str): Price that may contains currency

        Returns:
            str: Processed price text
        """

        match = re.findall(r"[0-9,.]+", price)
        price = match[0]

        return price


    def extract_currency(self, price: str) -> str:
        """Extract currency from price text with regex

        Args:
            price (str): Price that may contains currency

        Returns:
            str: extracted and reformatted currency text
        """

        currency = re.findall('([a-zA-Z ]*)\d*.*', price)
        currency = str(currency[0]).replace(" ", "")
        if "$" in price and currency != '':
            return currency + "D"
        elif "$" in price and currency == '':
            currency = "USD"
            return currency

        return currency