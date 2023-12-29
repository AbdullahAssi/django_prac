from django.http import HttpResponse 
from django.shortcuts import render

def index(request): 
    data = {
        'name': 'Muhammad Abdullah',
        'age': 20,
        'email': 'pakabdullah225@gmail.com',
        'phone': '0300-1234567',
        'address': 'Islamabad, Pakistan',
    }
    skills = [
        {'name': 'HTML', 'percent': 90},
        {'name': 'CSS', 'percent': 80},
        {'name': 'Bootstrap', 'percent': 70},
        {'name': 'JavaScript', 'percent': 60},
        {'name': 'Reactjs', 'percent': 80},
        {'name': 'Nextjs', 'percent': 70},
        {'name': 'ReactNative', 'percent': 40},
    ]
    page = { 'title': 'Home'}

    context = {'data': data, 'skills': skills , 'page': page}

    return render(request, 'home/index.html', context)


def about(request): 
    data= {
        'name': 'Muhammad Abdullah',
        'about': 'I am a student of BS AI in NUTECH. I am a web developer and I have a good command on HTML, CSS, Bootstrap, JavaScript, JQuery, Django, Python, C++, C#, Java, PHP, MySQL, SQL Server, Oracle Database, and WordPress. I have also a good command on Adobe Photoshop, Adobe Illustrator, Adobe XD, and Adobe Premiere Pro. I have also a good command on Microsoft Office. I have also a good command on Linux, Windows, and Mac OS. I have also a good command on SEO, SMM, and SEM. I have also a good command on Google Analytics, Google AdSense, Google AdWords, and Google Search Console. I have also a good command on Facebook, Twitter, Instagram, LinkedIn, and YouTube. I have also a good command on Google Maps, Google My Business, and Google Drive. I have also a good command on Google Docs, Google Sheets, and Google Slides. I have also a good command on Google Forms, Google Sites, and Google Calendar.',
    }
    page = { 'title': 'About'}
    context = {'data': data, 'page': page}
    return render(request, 'home/about.html' , context)
