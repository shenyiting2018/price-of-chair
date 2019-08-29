
import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-partners-miami-garden-dining-chair-grey/p3711083")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price price--large"})
string_price = (element.text.strip()) # "40"

price_without_symbol = string_price[1:] # copy string

price = float(price_without_symbol)

if price < 200:
    print("Buy it!")
    print("The currnet price is {}.".format(price_without_symbol))
else:
    print("Do not buy!")
# https://www.johnlewis.com/john-lewis-partners-miami-garden-dining-chair-grey/p3711083
# <p class="price price--large">£40.00</p>
#print(request.content)