from django.shortcuts import render
from django.http import HttpResponse

from hr_bot.settings import RASA_SERVER

# Create views for the bot

def index(request):
    rasa_server =  RASA_SERVER
    return render(request, "hrbot.html", {'rasa_server': rasa_server} )
