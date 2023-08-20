import time
import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


def get_posts(url):
    browser_options = ChromeOptions()
    browser_options.headless = True
    
    driver = Chrome(options=browser_options)
    driver.get(url)
    time.sleep(1)

    news_list = driver.find_elements(By.CSS_SELECTOR, ".list-item")
    posts = []
    for news in news_list:
        title = news.find_element(By.CSS_SELECTOR, "h3 > a")
        date = news.find_element(By.CSS_SELECTOR, ".published")
        resume = news.find_element(By.CSS_SELECTOR, "p")
        news_items = [title.text, date.text, resume.text]

        posts.append(news_items)

    df = pd.DataFrame(posts, columns=['titulo', 'data', 'resumo'])
    df.to_csv('posts.csv')   

    driver.quit()


def main():
    get_posts("https://gizmodo.uol.com.br/")


if __name__ == '__main__':
    main()
