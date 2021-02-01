from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def init_browser():
    executable_path = {'executable_path': 'C:\Windows\chromedriver'}
    return Browser('chrome', **executable_path, headless=False)



def scraped_news():
    mars_data = {}

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
    

    mars_data["news_title"] = news_title
    mars_data["news_p"] = news_p

    browser.quit()

    #return dictionary results
    return mars_data


def scraped_facts():
    mars_data = {}
     

    url = "https://space-facts.com/mars/"
    
    #scrape url with pandas
    facts_df = pd.read_html(url)

    df = facts_df[0]
    df.columns=["Fact", ""]
    df.set_index("Fact", inplace=True)

    # html_table.replace("\n", "")

    mars_facts = df.to_html('table.html')

    mars_data['facts_df'] = mars_facts

    return mars_data


def scraped_hemispheres():
    mars_data = {}

    #initialize browser
    browser = init_browser()

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    time.sleep(1)

    #html object, parse with beautiful soup
    html = browser.html
    soup = bs(html, "html.parser")

    hemispheres = []

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
    
        hemispheres.append({'Title': title, 'Image_URL': image_url})

        mars_data["hemispheres"] = hemispheres


    browser.quit()

    return mars_data


