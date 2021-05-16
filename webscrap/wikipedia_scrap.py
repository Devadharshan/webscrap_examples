from os import write
from unicodedata import name
import requests
from bs4 import BeautifulSoup
import csv

#scraping table from wikipedia and stoing in a csv file

website = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')

soup = BeautifulSoup(website.text,'html.parser')

first_table = soup.select_one('.wikitable')
#print(first_table)

table_rows = first_table.select('tr')[1:-1] #select the rows and we use [1:] to ignore the table heading and -1 to get rid of last element
#print(table_rows[:3]) #we select just 3 items to verify the working state

csv_data = [['rank','name','population','percentage','data','source']]
for row in table_rows:
    rank = row.find('th').text.strip() # strip to get rid of the white space
    #print(rank)
    table_data = row.select('td')
    name = table_data[0].find('a').text #index since since its first element
    #print(name)
    population = table_data[1].text
    #print(population)
    percentage = table_data[2].text
    #print(percentage)
    date = table_data[3].text
    #print(date)
    source = table_data[4].text.strip().split('[')[0] #to remove the space and []
    #print(source)
    csv_data.append([rank,name,population,percentage,date,source])
#print(csv_data)
with open('wikipediacountries.csv','w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data) #multiple rows so rows
