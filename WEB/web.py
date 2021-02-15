from flask import Flask, render_template, request, redirect
import pickle
import pandas as pd
import calendar


app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def hm():
    return render_template('index.html')

@app.route('/abstract.html', methods=['GET', 'POST'])
def abstract():
    return render_template('abstract.html')

@app.route('/dataset.html', methods=['GET', 'POST'])
def dataset():
    return render_template('dataset.html')

@app.route('/description.html', methods=['GET', 'POST'])
def description():
    return render_template('description.html')

@app.route('/TSA.html', methods=['GET', 'POST'])
def TSA():
    return render_template('TSA.html')

@app.route('/visualisation.html', methods=['GET', 'POST'])
def visualisation():
    return render_template('visualisation.html')

@app.route('/prediction.html', methods=['GET','POST'])
def prediction():
    return render_template('prediction.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    year=request.values['year']
    month=request.values['month']
    date_1=year+'-'+month+'-1'
    test_date=pd.to_datetime(date_1)
    last_date=pd.to_datetime('2020-12-31')
    diff=(test_date-last_date).days
    future_dates=model.make_future_dataframe(periods=diff)
    output=model.predict(future_dates)
    output1=round(output.yhat.iloc[-1])
    output1=int(output1.item())
    mt=calendar.month_name[int(month)]
    return render_template('result.html',prediction_text="The expected no.of collisons in {}-{} is {}".format(mt,year,output1))

@app.route('/EDA_age.html', methods=['GET', 'POST'])
def age():
    return render_template('EDA_age.html')

@app.route('/EDA_area.html', methods=['GET', 'POST'])
def area():
    return render_template('EDA_area.html')

@app.route('/EDA_descent.html', methods=['GET', 'POST'])
def descent():
    return render_template('EDA_descent.html')

@app.route('/EDA_Hour.html', methods=['GET', 'POST'])
def Hour():
    return render_template('EDA_Hour.html')

@app.route('/EDA_Month.html', methods=['GET', 'POST'])
def Month():
    return render_template('EDA_Month.html')

@app.route('/EDA_Week.html', methods=['GET', 'POST'])
def Week():
    return render_template('EDA_Week.html')

@app.route('/EDA_Year.html', methods=['GET', 'POST'])
def Year():
    return render_template('EDA_Year.html')

if __name__=="__main__":
    app.run()


