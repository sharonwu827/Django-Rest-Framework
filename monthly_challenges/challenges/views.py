from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def monthly_challenge(request,month):
    challenge_text = None
    if month =='january':
        challenge_text = "No Carbs!"
    elif month =='february':
        challenge_text = "Drink more water"
    elif month =='march':
        challenge_text = "Smile and Be Happy"
    else:
        return HttpResponseNotFound("Not Supported")
    return HttpResponse(challenge_text)
