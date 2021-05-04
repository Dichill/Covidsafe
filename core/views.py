import os
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# CovidSafeCore
from .covidsafecore import generateqrcode
from .covidsafecore import generatesqlcode

# So user goes to generatecode first to get
# his/her own code, so that he/she can have permission
# to generate a code. This is used to protect against
# SQL Injections, Spammers, and etc.a

PATH_TO_DIRECTORY = os.getcwd() + "/core/generated/"


def getqrimage(request):
    code = request.GET.get('c')

    try:
        image_data = open(PATH_TO_DIRECTORY + code + '.png', mode='rb').read()
        return HttpResponse(image_data, content_type="image/png")
    except:
        return HttpResponse('Method "GET" not allowed')


def generatecode(request):
    token = request.GET.get('t')
    name = request.GET.get('n')
    location = request.GET.get('l')

    try:
        # Verify if Token Matches
        sqlcode = generatesqlcode.generatesqlcode(token, name)
        return redirect('http://127.0.0.1:8000/api/generate/qr/' + "?t=" + str(token) + "&n=" + str(name) + "&l=" + str(location) + "&c=" + str(sqlcode))
    except Exception as e:
        print(str(e))
        return HttpResponse('Method "GET" not allowed.')


def generateqr(request):
    token = request.GET.get('t')
    name = request.GET.get('n')
    location = request.GET.get('l')
    code = request.GET.get('c')

    # Verify Token and Code Here

    data = generateqrcode.GenerateQRCode(name, location)

    try:
        return redirect("http://127.0.0.1:8000/api/qrcode/?c=" + data)
    except Exception as e:
        print(str(e))
        return HttpResponse('Method "GET" not allowed.')


def home(request):
    return render(request, "index.html")
