import unittest
from pScraper import scrape  #scrape()
import re

class rWebParser_test(unittest.main()):
    #tests that the program will respond properly to various possible inputs
    def testChar(self):
        #should throw an exception if not in a-z:
        self.assertRaises(NameError, scrape("https://www.google.com/",7)) #if the input is  an int
        self.assertRaises(NameError, scrape("https://www.google.com/","")) #if the input is an empty space
        self.assertRaises(NameError, scrape("https://www.google.com/","addfd")) #if the input is more than one character
    
    #tests if the correct number is given- looking at known answers
    #PROBLEM - if the checked sites were to change, the results may not be the same
    def testResult(self):
        self.assertEqual(scrape("http://httpbin.org/anything","l"),15) #check known answers
        self.assertEqual(scrape("http://httpbin.org/get","q"),9)
        self.assertEqual(scrape("http://httpbin.org/html","e"),329)
    
    #tests that this scraper is not case sensitive
    def testCapitals(self):
        self.assertEqual(scrape("https://www.google.com/","l"),scrape("https://www.google.com/","L"))  #check on same page for uppercase and lowercase (results should be the same)
        self.assertEqual(scrape("https://www.facebook.com/","p"),scrape("https://www.facebook.com/","P"))
    
    #check that scraper functions when the character is NOT on the page
    def testZero(self):
        self.assertEqual(scrape("http://httpbin.org/html","z"),0)
     
    #check that errors will be raised if an invalid URL link is passed through the parameter   
    def testURL(self):
        self.assertRaises(NameError, scrape("http://brulrnbfajkdnajbakjs.org/","y"))
        self.assertRaises(NameError, scrape(4,"y"))
        self.assertRaises(NameError, scrape("akfhkjaslfkl","z"))
        