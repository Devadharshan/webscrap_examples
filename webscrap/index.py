import requests
from bs4 import BeautifulSoup
#uncomment this 
#website = requests.get('https://quotes.toscrape.com/')
#soup = BeautifulSoup(website.text,'html.parser')

#title = soup.find('title') #to find title of the site
#print(title.text) #.text to remove the <title></title> tag

#link = soup.find('a') #to find any link <a> tag
#print(link)


#quote = soup.find(class_='text')  #class_ to differentiate from class
#print(quote)

#links = soup.find_all('a') #extract all the links 
#for link in links:
 #   print(link.text) # we use for loop since the link.text will raise error

#print("quotes")
#quotes = soup.find_all(class_='text') # to extract all the quotes
#print(quotes)

#login_link = soup.find(href='/login') #to extract from an href
#print(login_link)
'''
quote = soup.find(class_='quote')
quote_text = quote.find(class_='text')
quote_author = quote.find(class_='author')
print(quote_text.text)
print(quote_author.text)
'''


# using css selectors

#quotes = soup.select('.text')
#print(quotes)

# extracing from next page
page = 1
next_button = True
while next_button:
    website = requests.get('https://quotes.toscrape.com/page/'+str(page))
    soup = BeautifulSoup(website.text,'html.parser')

    next_button = soup.select_one('.next > a')
    quotes = soup.select('.quote')
    for quote in quotes:
        text = quote.select_one('.text')
        author = quote.select_one('.author')
        tags = quote.select('.tag')
        print(text.text)
        print(author.text)
        for tag in tags:
            print(tag.text)
        print("*******************")
    print('scraped page'+str(page))
    page+=1