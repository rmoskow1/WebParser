import rScraper
import unittest

class ScraperTest(unittest.TestCase):
    def test_Scraper(self):
        self.assertEqual(rScraper.scrape("http://now.httpbin.org/", 'f'), 2) #test the basic case
        self.assertEqual(rScraper.scrape("http://now.httpbin.org/", 'A'), 9) #test to see if it interprets caps and lowercase as the same
        self.assertEqual(rScraper.scrape("http://now.httpbin.org/", 'w'), 4) #test to see if it catches letters that have both caps and lowers
        self.assertEqual(rScraper.scrape("http://now.httpbin.org/", 'W'), 4) #same test just reverse
        self.assertNotEqual(rScraper.scrape("http://now.httpbin.org/", '"'), 34) #test that non-alpha chars don't return their number
        self.assertRaises(rScraper.scrape("http://now.httpbin.org/", '"'), TypeError) #test that non-alpha chars return an error
        self.assertRaises(rScraper.scrape("http://now.httpbin.org/", 'ab'), TypeError) #test that multi-char return an error
        self.assertRaises(rScraper.scrape("www.pinchasteitzrocks.org", 'a'), ValueError) #test that non-websites return an error
        self.assertRaises(rScraper.scrape("http://now.httpbin.org/", 6), ValueError) #test that numbers chars return an error
        self.assertRaises(rScraper.scrape("http://now.httpbin.org/", ''), ValueError) #test that empty strings return an error

if __name__ == "__main__":
    unittest.main()
