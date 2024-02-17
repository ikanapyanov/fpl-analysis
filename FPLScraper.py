import unittest
from selenium import webdriver
import time
from bs4 import BeautifulSoup

# Initiates the Selenium driver to web scrape from the FPL website
driver = webdriver.Chrome()
url= "https://fantasy.premierleague.com/statistics"
driver.maximize_window()
driver.get(url)

time.sleep(10)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content,"html.parser")

# Parses through the FPL website and prints out the player names on all pages
players = soup.findAll('div', class_='ElementInTable__Name-y9xi40-1 heNyFi')

players_length = len(players)

for p in range(28):

    for player in players:
        print(str(player.get_text()))

    if players_length % 30 == 0:
        driver.find_elements_by_class_name('PaginatorButton__Button-xqlaki-0 cDdTXr').click()
    
    else: break

if __name__ == "__main__":
    unittest.main()

driver.quit()

# <button type="button" class="PaginatorButton__Button-xqlaki-0 cDdTXr"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="Chevrons__ChevronRight-ifqxdy-1 hBRSDO"><path fill-rule="evenodd" d="M17.0003375,23.99975 C16.7018422,23.99975 16.4063468,23.8872518 16.1783503,23.6592553 L5.34101967,12.8204247 C4.88652678,12.3674318 4.88652678,11.6324432 5.34101967,11.1794503 L16.1783503,0.340619674 C16.6328432,-0.113873225 17.3663318,-0.113873225 17.8208247,0.340619674 C18.2753176,0.793612596 18.2753176,1.52860111 17.8208247,1.98309401 L7.80248121,11.9999375 L17.8208247,22.018281 C18.2753176,22.4697739 18.2753176,23.2062624 17.8208247,23.6592553 C17.5943282,23.8872518 17.2973329,23.99975 17.0003375,23.99975" transform="rotate(-180 11.58 12)" fill="currentColor"></path></svg><span class="PaginatorButton__HiddenLabel-xqlaki-1 diymPy">Next</span></button>