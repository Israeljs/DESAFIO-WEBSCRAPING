import time
import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def fetch_posts(news):
    title = news.find_element(By.CSS_SELECTOR, "h3 > a")
    date = news.find_element(By.CSS_SELECTOR, ".published")
    resume = news.find_element(By.CSS_SELECTOR, "p")
    items = [title.text, date.text, resume.text]
    return items

def create_csv(posts):
    df = pd.DataFrame(posts, columns=['titulo', 'data', 'resumo'])
    df.to_csv('posts.csv')

def get_onlY_news(driver, posts):
    news_list = driver.find_elements(By.CSS_SELECTOR, ".list-item")
    for news in news_list:
        post_category = news.find_element(By.CSS_SELECTOR, ".postCategory").text.find('OFERTAS')
        if  post_category == -1:
            news_items = fetch_posts(news)
            posts.append(news_items)

def get_posts(url):
    browser_options = ChromeOptions()
    browser_options.headless = True
    
    driver = Chrome(options=browser_options)
    driver.get(url)
    time.sleep(1)

    posts = []

    get_onlY_news(driver, posts)

    time.sleep(0.5)

    link_proximo = driver.find_element(By.CLASS_NAME, "next") 
    link_proximo.send_keys(Keys.ENTER)

    time.sleep(0.5)

    get_onlY_news(driver, posts)

    create_csv(posts)

    driver.quit()

def main():
    get_posts("https://gizmodo.uol.com.br/")

if __name__ == '__main__':
    main()
