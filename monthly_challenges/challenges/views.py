from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


monthly_challenges = {
    "january":"No Carbs!",
    'february':"Drink more water",
    'march':"Smile and Be Happy"
}

# Create your views here.

def monthly_challenge_by_number(request,month):
    return HttpResponse(month)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Not Found")

