from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd


executable_path = {'executable_path': 'C:\Windows\chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


@app.route('/scrape')
def scrape():

    mars_data = scrape_mars.scrape_info()





ir __name__ == "__main__":
    app.run(debug=True)


