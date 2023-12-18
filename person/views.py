from django.shortcuts import render, HttpResponse

users = ['parsa', 'amir', 'alireza', 'mansor']
def profile(request,username):
    if username in users:
        return render(request, "person/parsa.html",{'username': username})
    else:
        return  HttpResponse("user not regesterd")