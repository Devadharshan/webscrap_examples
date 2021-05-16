import requests
from bs4 import BeautifulSoup
import csv

headers = {'Accept-Language':'en-US'} # just to change the text to english
website = requests.get('https://www.imdb.com/title/tt0770828/',headers=headers)
soup = BeautifulSoup(website.text,'html.parser')

#print(soup.title)
title = soup.select_one('.title_wrapper>h1') # title_wrapper check the chrome inspector tool from the website
print(title.text.split('(')[0]) #split and [0] to remove the year
#title = soup.select_one('.title_wrapper>h1').contains 
#.contains prints the tags inside it
runtime = soup.select_one('time').text.strip()
plot = soup.select_one('.summary_text').text.strip() 
rating = soup.find(attrs={'itemprop':'ratingValue'}).text # we use find since its what it is designed in the imbd website
votes = soup.find(attrs={'itemprop':'ratingCount'}).text
print(votes)
print(rating)
print(runtime)
print(plot)

cast_list = soup.select('.cast_list tr')[1:5]
cast =''
for item in cast_list:
    cast+=item.select('td')[1].text.strip()+', '
print(cast[:-2])  # to get the first 4 actors

