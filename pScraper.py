import requests

def scrape(website, letter):

    try:
        r = requests.get(website)
    except:
        raise ValueError("This website does not exist")

    if letter == "":
        raise TypeError("No input was given")

    counter = 0

    if letter.isalpha() and len(letter) == 1:
        for i in r.text:
            if i.lower() == letter.lower():
                counter += 1

    elif len(letter) > 1:
        raise ValueError("Input must be one character")
    elif letter.isnumeric():
        raise TypeError("A number should not be given")
    elif not (letter.isalpha()):
        raise ValueError("Only letters are accepted")

    return counter

if __name__ == "__main__":
    website = input("Give a website\n> ")
    letter = input("Give a letter\n> ")
    scrape(website,letter)