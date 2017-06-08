import unittest
from unittest import mock
from pScraper import scrape
import re

text1 = "Call me Ishmael. Some years ago- never mind how long precisely- having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people's hats off- then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me."
text2 = ""

#will create a mock get method, which will return a mock response object with a status code and text
def mocked_requests_get(*args,**kwargs):
    class MockResponse():
        def __init__(self,status_code,text):
            self.text = text
            self.status_code = status_code
        #use 200 as status_code for the real URL, and an arbitrary number as status_code for a fake URL 
    if args[0] == "realURL":return MockResponse(200,text1)
    if args[0] == "fakeURL":return MockResponse(100,text1)

#will mock the BeautifulSoup parser, and return a text
#class MockBeautifulSoup():
    #def __init__(self, text):
        #self.textPage = text
    #def get_text(textType):
        #if textType == "text1": return text1
        #elif se == "text2":return emptyText
            

@mock.patch('requests.get',side_effect = mocked_requests_get)
#@mock.patch('BeautifulSoup',side_effect = MockBeautifulSoup)
class rWebParser_test(unittest.TestCase):
    #tests that the program will respond properly to various possible inputs
    def test_Char(self, mock_requests_get):
        #should throw an exception if not in a-z:
        self.assertRaises(TypeError, scrape,"realURL",7) #if the input is  an int
        self.assertRaises(ValueError, scrape,"realURL","") #if the input is an empty space
        self.assertRaises(ValueError,scrape,"realURL","addfd") #if the input is more than one character

    #tests if the correct number is given- looking at known answers
    def test_Result(self, mock_requests_get):
        self.assertEqual(scrape("realURL","e"),107) #check known answers
        self.assertEqual(scrape("realURL","q"),2)
        self.assertEqual(scrape("realURL","r"),56)

    #tests that this scraper is not case sensitive
    def test_Capitals(self,mock_requests_get):
        self.assertEqual(scrape("realURL","l"),scrape("realURL","L"))  #check on same page for uppercase and lowercase (results should be the same)
        self.assertEqual(scrape("realURL","p"),scrape("realURL","P"))

    #check that scraper functions when the character is NOT on the page
    def test_Zero(self,mock_requests_get):
        self.assertEqual(scrape("realURL","J"),0)

    #check that errors will be raised if an invalid URL link is passed through the parameter   
    def test_URL(self,mock_requests_get):
        self.assertRaises(ValueError, scrape,"fakeURL","y")#test for an invalid url link
          #THIS NEEDS TO CHANGE = LEARN HOW TO MOCK
        self.assertRaises(TypeError, scrape, 4 ,"y") #when URL input is not a string
   
        
if __name__ == "__main__":
    unittest.main()
