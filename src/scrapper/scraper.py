import requests
from bs4 import BeautifulSoup
import pickle

def get_soup(url):
    """
        Takes url as input and returns beautiful soup of html parser
    """
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def main():
    greetings_url = "https://therightwording.com/best-new-years-messages-and-wishes-for-friends-and-family/"
    soup = get_soup(greetings_url)
    li_selector = "body section main article ul li"
    li_items = soup.select(li_selector)
    filter_li = list()
    for li in li_items:
        try:
            if li.findAll("a") or li.attrs['class']:
                continue
        except Exception as e:
            filter_li.append(li.text)

    with open('data/greetings_newyear.pickle', 'wb') as f:
        pickle.dump(filter_li,f)

if __name__ == "__main__":
    main()