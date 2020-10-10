import logging

logger = logging.Logger(__name__)

def getName(soup, handle):
    try:
        filter_1 = soup.find('div', attrs={'class': 'main-info'})
        filter_2 = filter_1.findAll('div')
        filter_3 = filter_2[1].find('div')
        name = filter_3.text.split(',')[0]
        logger.info('getName() returned:' + name)
        return name
    except Exception as e:
        print('Error while getting name')
        print(str(e))
        return 'Not Found'

def getCurrentRatings(soup, handle):
    try:
        filter_1 = soup.find('div', attrs={'class': 'info'})
        filter_2 = filter_1.find('ul')
        filter_3 = filter_2.find('li')
        filter_4 = filter_3.find('span')
        current_ratings = filter_4.text
        logger.info('getCurrentRatings() returned:' + current_ratings)
        return current_ratings
    except Exception as e:
        print('Error while getting Ratings')
        print(str(e))
        return 'Not Found'

def getUniversity(soup, handle):
    filter_1 = soup.find('div', attrs={'class':'main-info'})
    filter_2 = filter_1.findAll('div')
    university = ''
    if len(filter_2) > 3:
        filter_3 = filter_2[3].find('a')
        university = filter_3.text
    logger.info('getUniversity() returned:' + university)
    return university

def getRank(soup, handle):
    filter_1 = soup.find('div', attrs={'class':'main-info'})
    filter_2 = filter_1.find('div')
    filter_3 = filter_2.find('span')
    rank = filter_3.text
    print(rank)
    logger.info('getRank() returned:' + rank)
    return rank

def getProfileURL(soup, handle):
    filter_1 = soup.find('div', attrs={'class': 'title-photo'})
    filter_2 = filter_1.find('div')
    filter_3 = filter_2.find('div')
    filter_4 = filter_3.find('div')
    filter_5 = filter_4.find('img')
    img_url = filter_5['src'][2:]
    img_url = 'https://'+img_url
    logger.info('getProfileURL() returned:' + img_url)
    return img_url

if __name__ == '__main__':
    from bs4 import BeautifulSoup
    import requests
    handle = 'razdeep'
    url = 'https://codeforces.com/profile/'
    url += handle
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html5lib')
    getCurrentRatings(soup, handle)