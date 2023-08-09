from email import message
from showstatic.models import saveforms
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render, redirect
import sqlite3

# from .models import ShowStaticSaveforms

def layout(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "layout.html")

def contact(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "contact.html")

def index(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "index.html")

def photos(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "photos.html")

def mywork(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "mywork.html")

def saveform(request):
    if request.method == 'POST':
        contactName = request.POST.get('contactName')
        contactEmail = request.POST.get('contactEmail')
        contactSubject = request.POST.get('contactSubject')
        contactMessage = request.POST.get('contactMessage')
        
        data = saveforms(
            contactName=contactName, 
            contactEmail=contactEmail,
            contactSubject=contactSubject, 
            contactMessage=contactMessage)
        data.save()

        messages.success(request, 'Form submitted successfully!')
        return render(request, "index.html")

import sqlite3
from django.shortcuts import render

def admin(request):
    if request.method == "GET":
        return render(request, "login.html")
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        valid_usernames = ["kamalsoni"]
        valid_passwords = ["9426827891#Ks"]

        if username in valid_usernames and password in valid_passwords:
            connection = sqlite3.connect('db.sqlite3')
            cursor = connection.cursor()

            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()

            selected_table = request.POST.get("selected_table")
            rows = []

            if selected_table:
                cursor.execute(f"SELECT * FROM {selected_table};")
                rows = cursor.fetchall()
            
            connection.close()

            return render(request, 'db.html', {'tables': tables, 'selected_table': selected_table, 'rows': rows})
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})

def table_contents(request, table_name):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()

    connection.close()

    return render(request, 'table_contents.html', {'table_name': table_name, 'rows': rows})