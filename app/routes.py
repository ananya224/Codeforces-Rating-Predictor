from app import app
from flask import render_template, request
from app import scrapers
from app import predictor

@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'POST'):
        handle = request.form.get('handle')
        img_url = scrapers.getProfileURL('handle')
        predicted = predictor.predict('handle')
        return render_template('result.html', handle=handle, university=scrapers.getUniversity(handle), rank=scrapers.getRank(handle),
                                                predicted=predicted, img_url=img_url)
    return render_template('index.html')