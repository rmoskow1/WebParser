import requests
from bs4 import BeautifulSoup

# scrape method: parses through the visible text of a website and returns the number of times
# a given letter appears in the text
# fails when: no string is given for the website or letter (int or None), the letter is more than one char
# the letter is a non-alphabetic char
def scrape(website, letter):

    # error if no letter input
    if letter == "" or website == "":
        raise TypeError("No input was given for one of the fields")

    # error if letter input is an int
    elif type(letter) != str or type(website) != str:
        raise TypeError("A non-string should not be given for either input")

    # otherwise if letter input isn't one character raise error
    elif len(letter) > 1:
        raise ValueError("Input must be one character")

    # or if letter input is a non-alphabetic character
    elif not (letter.isalpha()):
        raise ValueError("Only letters are accepted")


    # get website data
    r = requests.get(website)

    # get only the visible text using BeautifulSoup
    soup = BeautifulSoup(r.text, "html.parser")
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    text = soup.getText()

    # initialize counter
    counter = 0

    # loop through text, incrementing counter every time the letter (caps or lower) comes up
    for i in text:
        if i.lower() == letter.lower():
            counter += 1

    # return counter
    return counter

# main method
if __name__ == "__main__":

    # get input for website and letter and print the scrape result
    website = input("Give a website\n> ")
    letter = input("Give a letter\n> ")
    print(scrape(website,letter))
