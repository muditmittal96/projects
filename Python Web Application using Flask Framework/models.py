from forms import  HomePage, FirstQuestion, SecondQuestion, ChartFig, ThirdQuestion, FourthQuestion, FifthQuestion, SixthQuestion, SeventhQuestion, Consent
from flask import render_template, redirect, url_for, session, flash, Flask
import numpy as np
import mysql.connector
from mysql.connector import Error
import time
import sys
import datetime
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.permanent_session_lifetime = datetime.timedelta(days=365)


class Newuser:
    def __init__(self,participant_name,researcher_name,date,id,age,gender,education,applicants,start_time,end_time,a1,a2,a3,a4,a5,a6,a7):
        self.participant_name = participant_name
        self.researcher_name = researcher_name
        self.date = date
        self.id = id
        self.age = age
        self.gender = gender
        self.education = education
        self.applicants = applicants
        self.start_time = start_time
        self.end_time = end_time
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7

    def insertVariblesIntoTable(self):
        connection = mysql.connector.connect(host='us-cdbr-east-06.cleardb.net',
                                             database='heroku_0edf3357430bd25',
                                             user='b85cc0f47cd9bd',
                                             password='4281cb9f')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO user (Participant_Name, Researcher_Name, Date, Id, Age, Gender, Education, Applicants, Start_Time, End_Time, A1, A2, A3, A4, A5, A6, A7)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

        recordTuple = (self.participant_name, self.researcher_name, self.date, self.id, self.age, self.gender, self.education, self.applicants, self.start_time, self.end_time, self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        cursor.close()
        connection.close()



############################################

        # VIEWS WITH FORMS

#########################################

@app.route('/', methods=['GET', 'POST'])
def consent_form():
    session['index'] = 0
    form10 = Consent()
    if form10.validate_on_submit():
        session['id'] = random.randint(1,100000)
        session['participant_name'] = form10.participant_name.data
        session['researcher_name'] = form10.researcher_name.data
        t = datetime.datetime.now().date()
        session['date'] = t.strftime('%m/%d/%Y')
        return redirect(url_for('user_info'))
    return render_template('consent.html', form10=form10)

@app.route('/home', methods=['GET', 'POST'])
def user_info():
    # if session['id'] == None:
    #     session['id'] = 1
    form = HomePage()
    if form.validate_on_submit():
        session['Age'] = form.age.data
        session['Gender'] = form.gender.data
        session['Education'] = form.education.data

        return redirect(url_for('sample_fig'))
    return render_template('home.html',form=form)

@app.route('/test_simulation', methods=['GET', 'POST'])
def sample_fig():
    form11 = ChartFig()
    applicants = [10,7,5,4]
    if form11.submit11.data:
        return redirect(url_for('sample_question'))
    return render_template('sample_fig.html', form11=form11, applicants=applicants)


@app.route('/test_question', methods=['GET', 'POST'])
def sample_question():
    form12 = FirstQuestion()
    if form12.validate_on_submit():
        return redirect(url_for('preread'))
    return render_template('sample_question.html',form12=form12)

@app.route('/preread', methods=['GET', 'POST'])
def preread():
    form13 = ChartFig()
    if form13.submit13.data:
        return redirect(url_for('chart_fig'))
    return render_template('preread.html',form13=form13)

@app.route('/simulation', methods=['GET', 'POST'])
def chart_fig():
    form9 = ChartFig()
    now = datetime.datetime.now()
    session['Start_Time'] = now.strftime('%H:%M:%S')
    tasks = [[10,8,10,8],[10,7,5,4],[5,3,5,4],[5,4,10,5],[5,4,5,2],
    [10,7,5,1],[5,4,5,1],[10,1,5,4],[10,9,10,1],[10,1,10,0],
    [100,100,50,0],[50,40,100,80],[100,70,100,80],[50,30,50,40],
    [100,80,100,50],[50,40,100,40],[100,70,50,10],[50,40,50,10],
    [100,10,50,40],[100,90,100,10],[100,10,50,50],[100,100,50,0]]
    applicants = tasks[session['index']]
    session['applicants'] = applicants

    if form9.submit9.data:
        return redirect(url_for('first_answer'))
    return render_template('simulation.html', form9=form9, applicants=applicants)



@app.route('/Q1', methods=['GET', 'POST'])
def first_answer():
    now = datetime.datetime.now()
    session['End_Time'] = now.strftime('%H:%M:%S')
    form2 = FirstQuestion()
    if form2.validate_on_submit():
        session['A1'] = form2.q1.data
        return redirect(url_for('second_answer'))
    return render_template('Q1.html',form2=form2)



@app.route('/Q2', methods=['GET', 'POST'])
def second_answer():
    form3 = SecondQuestion()
    if form3.validate_on_submit():
        session['A2'] = form3.q2.data
        return redirect(url_for('third_answer'))
    return render_template('Q2.html',form3=form3)



@app.route('/Q3', methods=['GET', 'POST'])
def third_answer():
    form4 = ThirdQuestion()
    if form4.validate_on_submit():
        session['A3'] = form4.q3.data
        return redirect(url_for('fourth_answer'))
    return render_template('Q3.html',form4=form4)



@app.route('/Q4', methods=['GET', 'POST'])
def fourth_answer():
    form5 = FourthQuestion()
    if form5.validate_on_submit():
        session['A4'] = form5.q4.data
        return redirect(url_for('fifth_answer'))
    return render_template('Q4.html',form5=form5)



@app.route('/Q5', methods=['GET', 'POST'])
def fifth_answer():
    form6 = FifthQuestion()
    if form6.validate_on_submit():
        session['A5'] = form6.q5.data
        return redirect(url_for('sixth_answer'))
    return render_template('Q5.html',form6=form6)



@app.route('/Q6', methods=['GET', 'POST'])
def sixth_answer():
    form7 = SixthQuestion()
    if form7.validate_on_submit():
        session['A6'] = form7.q6.data
        return redirect(url_for('seventh_answer'))
    return render_template('Q6.html',form7=form7)



@app.route('/Q7', methods=['GET', 'POST'])
def seventh_answer():
    form8 = SeventhQuestion()
    if form8.validate_on_submit():
        session['A7'] = form8.q7.data
        new = Newuser(session['participant_name'], session['researcher_name'], session['date'], session['id'],session['Age'],session['Gender'],session['Education'],str(session['applicants']),session['Start_Time'],session['End_Time'],session['A1'],session['A2'],session['A3'],session['A4'],session['A5'],session['A6'],session['A7'])
        new.insertVariblesIntoTable()
        if session['index'] == 21:
            url = 'thankyou'
        else:
            url = 'chart_fig'
        session['index'] = session['index'] + 1
        return redirect(url_for(url))
    return render_template('Q7.html',form8=form8)



@app.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    # session['id'] = session['id'] + 1
    return render_template('thankyou.html')




if __name__ == '__main__':
    app.run(debug=True)
