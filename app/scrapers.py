import requests
from bs4 import BeautifulSoup

def getUniversity(handle):
    url = 'https://codeforces.com/profile/'
    url += handle
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html5lib')
    filter_1 = soup.find('div', attrs={'class':'main-info'})
    filter_2 = filter_1.findAll('div')
    university = ''
    if len(filter_2) > 3:
        filter_3 = filter_2[3].find('a')
        university = filter_3.text
    # print(university)
    return university

def getRank(handle):
    try:
        url = 'https://codeforces.com/profile/'
        url += handle
        html_page = requests.get(url)
        soup = BeautifulSoup(html_page.content, 'html5lib')
        filter_1 = soup.find('div', attrs={'class':'main-info'})
        filter_2 = filter_1.find('div')
        filter_3 = filter_2.find('span')
        rank = filter_3.text
        print(rank)
        return rank
    except:
        return 'Not Found'

def getProfileURL(handle):
    url = 'https://codeforces.com/profile/'
    url += handle
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html5lib')
    filter_1 = soup.find('div', attrs={'class': 'title-photo'})
    filter_2 = filter_1.find('div')
    filter_3 = filter_2.find('div')
    filter_4 = filter_3.find('div')
    filter_5 = filter_4.find('img')
    img_url = filter_5['src'][2:]
    img_url = 'https://'+img_url
    return img_url

if __name__ == '__main__':
    getProfileURL('razdeep')