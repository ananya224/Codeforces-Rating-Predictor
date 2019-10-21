from app import app
from flask import render_template, request
from app import scrapers
from app import predictor
import requests
from bs4 import BeautifulSoup

@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'POST'):
        handle = request.form.get('handle')
        # soup = 0
        try:
            url = 'https://codeforces.com/profile/'
            url += handle
            html_page = requests.get(url)
            soup = BeautifulSoup(html_page.content, 'html5lib')
            img_url = scrapers.getProfileURL(soup, handle)
            predicted = predictor.predict(handle)
            university=scrapers.getUniversity(soup, handle)
            rank=scrapers.getRank(soup, handle)

            return render_template('result.html', handle=handle, university=university, rank=rank,
                                                    predicted=predicted, img_url=img_url)
        except:
            print("Error fetching the soup")
            return render_template('404.html')
      
    return render_template('index.html')