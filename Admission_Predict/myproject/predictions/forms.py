from django import forms

class ScoreForm(forms.Form):
    korean_score = forms.FloatField(label='국어 점수')
    english_score = forms.FloatField(label='영어 점수')
    math_score = forms.FloatField(label='수학 점수')
    korean_grade = forms.IntegerField(label='국어 등급')
    english_grade = forms.IntegerField(label='영어 등급')
    math_grade = forms.IntegerField(label='수학 등급')
    university = forms.CharField(label='지원한 대학교 이름')