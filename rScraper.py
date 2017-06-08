import requests
import re
from bs4 import BeautifulSoup
class rScraper(object):
    """Search a given URL page for a specific character"""
    #only for one character, and only for valid URLs
    def scrape(self, URL, char):
        
        #errors in URL input
        if type(URL)!=str: raise TypeError("Invalid URL input") #if the URL input is not a string
        elif requests.get(URL).status_code!=200: raise ValueError("Non-existent URL") #if the URL is not existent (if it's status code is not 200)
        
        #errors in char input
        elif type(char)!=str: raise TypeError("Invalid character input") #if the character input is not a string
        elif len(char)!=1 or re.search(r'[a-z,A-Z]',char)==None:  #if there's more than one character, or the character is not a-z
            raise ValueError("Must pass through one character")
        
        #At this point - must be that the inputs are valid, so continue
        
        page = requests.get(URL)  
        text = BeautifulSoup(page.text,"html.parser") #use beautiful soup to parse
        [s.extract() for s in text(['style','script','[document]','head','title'])]
        text = text.get_text()    #get the text content of the page
 
        print(text)
        count = 0 #will count occurences of the character
        for each in text:  #parse through text data
            if each == char.lower() or each == char.upper(): count +=1   #add to count for uppercase, or lowercase version of the character
            
        return count #number of times the given character appeared on the page
 
#write a main that takes an input and does its job!!!
def __main():
    URL = input("Please enter a valid URL:")
    char = input("Please enter a character (a-z):")
    scraper = rScraper()
    count = scraper.scrape(URL,char)
    print("Here's the count, of how many times this character appeared on this webpage:",str(count))
    ans = input("Would you like to try again? y/n")
    if ans == "y": __main()
if __name__=="__main__":
    __main()

    
     
        
            
        
        
        