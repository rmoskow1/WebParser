import requests
from bs4 import BeautifulSoup

def scrape(website, letter):


    r = requests.get(website)

    soup = BeautifulSoup(r.text, "html.parser")
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    text = soup.getText()

    if letter == "":
        raise TypeError("No input was given")
    elif type(letter) == int:
        raise TypeError("A number should not be given")

    counter = 0

    if letter.isalpha() and len(letter) == 1:
        for i in text:
            if i.lower() == letter.lower():
                counter += 1

    elif len(letter) > 1:
        raise ValueError("Input must be one character")
    elif not (letter.isalpha()):
        raise ValueError("Only letters are accepted")

    return counter

if __name__ == "__main__":
    website = input("Give a website\n> ")
    letter = input("Give a letter\n> ")
    print(scrape(website,letter))
