from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def init_browser():
    executable_path = {'executable_path': 'C:\Windows\chromedriver'}
    return Browser('chrome', **executable_path, headless=False)



def scraped_news():
    
    browser = init_browser()
    
    url = "https://mars.nasa.gov/news/"

    browser.visit(url)

    time.sleep(1)

    #html object, parse with beautiful soup
    html = browser.html
    soup = bs(html, "html.parser")

    #get article title
    news_title = soup.find("div", class_="list_text").find("div", class_="content_title").find("a").text

    #get the news paragraph
    news_p = soup.find("div", class_="list_text").find("div", class_="article_teaser_body").text
    
    mars_news = {"news_title": news_title, "news_p": news_p}

    browser.quit()

    #return dictionary results
    return mars_news


def scraped_facts():
    
    url = "https://space-facts.com/mars/"
    
    #scrape url with pandas
    facts = pd.read_html(url)

    df = facts[0]
    df.columns=["Fact", ""]
    df.set_index("Fact", inplace=True)

    mars_facts = df.to_html()

    return mars_facts


def scraped_hemispheres():

    #initialize browser
    browser = init_browser()

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    time.sleep(1)

    #html object, parse with beautiful soup
    html = browser.html
    soup = bs(html, "html.parser")

    mars_hemispheres = []

    results = soup.find('div', class_='result-list')
    items = results.find_all('div', class_='item')

    for item in items:
    
        title = item.find('h3').text
    
        partial_url = item.find('a')['href']
    
        image_url = "https://astrogeology.usgs.gov/" + partial_url
    
        browser.visit(image_url)
    
        html = browser.html
    
        soup = bs(html, 'html.parser')
    
        new_url = url + image_url
    
        mars_hemispheres.append({'Title': title, 'Image_URL': image_url})

    browser.quit()

    return mars_hemispheres

def scrape():
    mars_info = {}
    mars_news = scraped_news()
    mars_info["mars_title"] = mars_news["news_title"]
    mars_info["mars_paragraph"] = mars_news["news_p"]
    mars_info["mars_facts"] = scraped_facts()
    mars_info["mars_hemispheres"] = scraped_hemispheres()

    return mars_info
