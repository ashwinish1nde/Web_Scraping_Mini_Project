
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

Names = []
Prices = []
Availabilities = []


# print(soup.prettify())

#Scrapes all the html code of page
# for i in soup.find_all("code"):
#     print(i.text)
    # We can also do it like this
    # print(i.get_text())

# title = soup.title
# print(title)

titleContent = soup.find_all('h3')
for title in titleContent:
    a_tag = title.find('a')
    titleName = a_tag['title']
    Names.append(titleName)

prices = soup.find_all(class_='price_color')
for price in prices:
    Prices.append(price.text)

availTags = soup.find_all('p', class_='instock availability')
for availTag in availTags:
    availStatus = availTag.get_text(strip=True)
    Availabilities.append(availStatus)

data = pd.DataFrame({'Name': Names, 'Price':Prices, 'Availability':Availabilities})
data.to_excel('data/data.xlsx', index=False)