import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/nader/OneDrive/Documents/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
result = []
other_result = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
driver.quit()
for a in soup.findAll(attrs='css-kmdwe8_e1nywbhn0'):
    name = a.find('h2')
    if name not in result:
        result.append(name.text)

for b in soup.findAll(attrs='blog-card__date-wrapper'):
    date = b.find('h2')
    if date not in result:
        other_result.append(date.text)

df = pd.DataFrame({'Names':result, 'Dates': other_result})
df.to_csv('names.csv', encoding='utf-8', index=False)