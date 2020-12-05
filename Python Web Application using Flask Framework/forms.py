from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField, RadioField, SelectField, TextField, DateField
from wtforms.validators import DataRequired, InputRequired
from wtforms.validators import DataRequired
import random
import mysql.connector
from mysql.connector import Error

class Consent(FlaskForm):
    participant_name = TextField('', validators = [DataRequired()])
    researcher_name = TextField('', validators = [DataRequired()])
    response = RadioField('', choices=[('Agree','I agree to the above terms and conditions'),('Disagree','I disagree to the above terms and conditions')], validators=[DataRequired()])
    # date = DateField('')
    submit10 = SubmitField('Next')

class HomePage(FlaskForm):
    age = SelectField('Please select your age:', choices=[(str(i),i) for i in range(1,90)],validators=[DataRequired()])
    gender = RadioField('Please select your gender:', choices=[('male','Male'),('female','Female')],validators=[DataRequired()])
    education = RadioField('Please select your edcuation:', choices=[('high school','High School'),('bachelors','Bachelors'),('masters','Masters'),('phd','PhD')],validators=[DataRequired()])
    submit1 = SubmitField('Next')

class FirstQuestion(FlaskForm):

    q1 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    submit2 = SubmitField('Next')
    submit12 = SubmitField('Next')

class SecondQuestion(FlaskForm):

    q2 = RadioField('',choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    submit3 = SubmitField('Next')

class ChartFig(FlaskForm):

    submit9 = SubmitField('Next')
    submit11 = SubmitField('Next')
    submit13 = SubmitField('Next')

class ThirdQuestion(FlaskForm):

    q3 = RadioField('', choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    submit4 = SubmitField('Next')

class FourthQuestion(FlaskForm):

    q4 = RadioField('', choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    submit5 = SubmitField('Next')


class FifthQuestion(FlaskForm):

    q5 = RadioField('', choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    submit6 = SubmitField('Next')


class SixthQuestion(FlaskForm):

    q6 = RadioField('', choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    submit7 = SubmitField('Next')


class SeventhQuestion(FlaskForm):

    q7 = RadioField('', choices=[('Strongly Disagree','Strongly Disagree'),('Disagree','Disagree'),('Neither Agree nor Disagree','Neither Agree nor Disagree'),('Agree','Agree'),('Strongly Agree','Strongly Agree')], validators=[DataRequired()])
    submit8 = SubmitField('Next')
