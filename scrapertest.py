import pScraper
import rScraper
import unittest
from unittest import mock

# class temp(object):
#     # pass
#     def __init__(self):
#         self.text = None

class ScraperTest(unittest.TestCase):

    @mock.patch('pScraper.requests.get')
    def test_Scraper(self, mock_req):

        mock_req.return_value.text = "l l l l"
        self.assertEqual(pScraper.scrape("www.cheating.com", 'l'), 4) # check standard letter test
        self.assertEqual(pScraper.scrape("www.cheating.com", 'L'), 4) # check that caps or lowers is irrelevant
        self.assertRaises(TypeError, pScraper.scrape, "www.cheating.com", 6) # check that numbers fail
        self.assertRaises(ValueError, pScraper.scrape, "www.cheating.com", 'Ll') # check that multi-char inputs fail
        self.assertEqual(pScraper.scrape("www.cheating.com", 'M'), 0) # check that it doesn't fail for 0
        self.assertRaises(TypeError, pScraper.scrape, "www.cheating.com", '') # check that no input fails

        mock_req.return_value.text = "M m M m"
        self.assertEqual(pScraper.scrape("www.cheating.com", 'm'), 4) # check that it properly interprets line with caps and lowers
        self.assertEqual(pScraper.scrape("www.cheating.com", 'M'), 4) # same

        mock_req.return_value.text = "L @ L @"
        self.assertRaises(ValueError, pScraper.scrape, "www.cheating.com", '@') # check that it fails for a non-alpha char

        self.assertRaises(TypeError, pScraper.scrape, "", 'L')  # check that no input fails for website
        self.assertRaises(TypeError, pScraper.scrape, 6, 'L')  # check that numbers fail for website

if __name__ == "__main__":
    unittest.main()
