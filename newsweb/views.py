from newsapi import NewsApiClient
from .models import Contact
import requests
import json
from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
    return render(request, 'contact.html')



def home(request):
 
    news_api_requests = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'home.html', {'api' : api})

def apple(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/everything?q=apple&from=2020-08-27&to=2020-08-27&sortBy=popularity&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'apple.html', {'api' : api})



    #entertainment news 


def argentina_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ar&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/argentina-entertainment.html', {'api' : api})

def australia_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=au&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/australia-entertainment.html', {'api' : api})

def austria_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=at&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/austria-entertainment.html', {'api' : api})
    
def belgium_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=be&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/belgium-entertainment.html', {'api' : api})

def brazil_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=br&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/brazil-entertainment.html', {'api' : api})


def bulgaria_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=bg&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/bulgaria-entertainment.html', {'api' : api})

def canada_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ca&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/canada-entertainment.html', {'api' : api})

def china_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cn&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/china-entertainment.html', {'api' : api})

def colombia_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=co&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/colombia-entertainment.html', {'api' : api})

def cuba_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cu&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/cuba-entertainment.html', {'api' : api})

def Czech_Republic_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cz&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/Czech-Republic-entertainment.html', {'api' : api})

def egypt_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=eg&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/egypt-entertainment.html', {'api' : api})

def france_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=fr&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/france-entertainment.html', {'api' : api})

def germany_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=de&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/germany-entertainment.html', {'api' : api})


def greece_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=de&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/greece-entertainment.html', {'api' : api})
    #Hong Kong
def HK_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=hk&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/HK-entertainment.html', {'api' : api})

def hungary_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=hu&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/hungary-entertainment.html', {'api' : api})

def india_entertainment(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/india-entertainment.html', {'api' : api})


def indonesia_entertainment(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=id&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/indonesia-entertainment.html', {'api' : api})

def ireland_entertainment(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ie&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/ireland-entertainment.html', {'api' : api})


def israel_entertainment(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=il&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/israel-entertainment.html', {'api' : api})

def italy_entertainment(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=it&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/italy-entertainment.html', {'api' : api})


def japan_entertainment(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=jp&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/japan-entertainment.html', {'api' : api})

def latvia_entertainment(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=lv&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/latvia-entertainment.html', {'api' : api})


def lithuania_entertainment(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=lt&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/lithuania-entertainment.html', {'api' : api})


def malaysia_entertainment(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=my&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/malaysia-entertainment.html', {'api' : api})



def mexico_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=mx&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/mexico-entertainment.html', {'api' : api})


def morocco_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ma&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/morocco-entertainment.html', {'api' : api})


def netherlands_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=nl&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/netherlands-entertainment.html', {'api' : api})


def nz_entertainment(request):
 
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=nz&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")

    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/nz-entertainment.html', {'api' : api})


def nigeria_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ng&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/nigeria-entertainment.html', {'api' : api})


def norway_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=no&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/norway-entertainment.html', {'api' : api})


def philippines_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ph&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/philippines-entertainment.html', {'api' : api})


def poland_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=pl&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/poland-entertainment.html', {'api' : api})


def portugal_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=pt&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/portugal-entertainment.html', {'api' : api})


def romania_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ro&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/romania-entertainment.html', {'api' : api})


def russia_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ru&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/russia-entertainment.html', {'api' : api})



def SA_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sa&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/saudi-arabia-entertainment.html', {'api' : api})



def serbia_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=rs&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/serbia-entertainment.html', {'api' : api})


def singapore_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sg&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/singapore-entertainment.html', {'api' : api})


def slovakia_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sk&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/slovakia-entertainment.html', {'api' : api})


def slovenia_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=si&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/slovenia-entertainment.html', {'api' : api})


def south_africa_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=za&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/south-africa-entertainment.html', {'api' : api})


def south_korea_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=kr&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/south-korea-entertainment.html', {'api' : api})


def sweden_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=se&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/sweden-entertainment.html', {'api' : api})


def switzerland_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ch&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/switzerland-entertainment.html', {'api' : api})


def taiwan_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=tw&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/taiwan-entertainment.html', {'api' : api})


def thailand_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=th&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/thailand-entertainment.html', {'api' : api})



def turkey_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=tr&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/turkey-entertainment.html', {'api' : api})


def UAE_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ae&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/UAE-entertainment.html', {'api' : api})


def ukraine_entertainment(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ua&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'entertainment/ukraine-entertainment.html', {'api' : api})


def uk_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=gb&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/uk-entertainment.html', {'api' : api})


def us_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/us-entertainment.html', {'api' : api})


def venuzuela_entertainment(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ve&category=entertainment&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'entertainment/venuzuela-entertainment.html', {'api' : api})


    #business news 


def argentina_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ar&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/argentina-business.html', {'api' : api})

def australia_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=au&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/australia-business.html', {'api' : api})

def austria_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=at&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/austria-business.html', {'api' : api})
    
def belgium_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=be&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/belgium-business.html', {'api' : api})

def brazil_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=br&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/brazil-business.html', {'api' : api})


def bulgaria_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=bg&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/bulgaria-business.html', {'api' : api})

def canada_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ca&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/canada-business.html', {'api' : api})

def china_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cn&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/china-business.html', {'api' : api})

def colombia_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=co&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/colombia-business.html', {'api' : api})

def cuba_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cu&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/cuba-business.html', {'api' : api})

def Czech_Republic_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cz&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/Czech-Republic-business.html', {'api' : api})

def egypt_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=eg&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/egypt-business.html', {'api' : api})

def france_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=fr&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/france-business.html', {'api' : api})

def germany_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=de&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/germany-business.html', {'api' : api})


def greece_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=de&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/greece-business.html', {'api' : api})
    #Hong Kong
def HK_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=hk&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/HK-business.html', {'api' : api})

def hungary_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=hu&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/hungary-business.html', {'api' : api})

def india_business(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/india-business.html', {'api' : api})


def indonesia_business(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=id&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/indonesia-business.html', {'api' : api})

def ireland_business(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ie&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/ireland-business.html', {'api' : api})


def israel_business(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=il&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/israel-business.html', {'api' : api})

def italy_business(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=it&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/italy-business.html', {'api' : api})


def japan_business(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=jp&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/japan-business.html', {'api' : api})

def latvia_business(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=lv&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/latvia-business.html', {'api' : api})


def lithuania_business(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=lt&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/lithuania-business.html', {'api' : api})


def malaysia_business(request):
 

    
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=my&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/malaysia-business.html', {'api' : api})



def mexico_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=mx&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/mexico-business.html', {'api' : api})


def morocco_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ma&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/morocco-business.html', {'api' : api})


def netherlands_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=nl&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/netherlands-business.html', {'api' : api})


def nz_business(request):
 
    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=nz&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")

    api = json.loads(news_api_requests.content)

    return render(request, 'business/nz-business.html', {'api' : api})


def nigeria_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ng&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/nigeria-business.html', {'api' : api})


def norway_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=no&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/norway-business.html', {'api' : api})


def philippines_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ph&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/philippines-business.html', {'api' : api})


def poland_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=pl&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/poland-business.html', {'api' : api})


def portugal_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=pt&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/portugal-business.html', {'api' : api})


def romania_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ro&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/romania-business.html', {'api' : api})


def russia_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ru&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/russia-business.html', {'api' : api})



def SA_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sa&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/saudi-arabia-business.html', {'api' : api})



def serbia_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=rs&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/serbia-business.html', {'api' : api})


def singapore_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sg&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/singapore-business.html', {'api' : api})


def slovakia_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sk&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/slovakia-business.html', {'api' : api})


def slovenia_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=si&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/slovenia-business.html', {'api' : api})


def south_africa_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=za&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/south-africa-business.html', {'api' : api})


def south_korea_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=kr&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/south-korea-business.html', {'api' : api})


def sweden_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=se&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/sweden-business.html', {'api' : api})


def switzerland_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ch&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/switzerland-business.html', {'api' : api})


def taiwan_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=tw&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/taiwan-business.html', {'api' : api})


def thailand_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=th&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/thailand-business.html', {'api' : api})



def turkey_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=tr&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/turkey-business.html', {'api' : api})


def UAE_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ae&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/UAE-business.html', {'api' : api})


def ukraine_business(request):

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ua&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)

    return render(request, 'business/ukraine-business.html', {'api' : api})


def uk_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=gb&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/uk-business.html', {'api' : api})


def us_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/us-business.html', {'api' : api})


def venuzuela_business(request):
 

    news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ve&category=business&apiKey=0e2f001f361849869d4271ff5efcf91f")
    api = json.loads(news_api_requests.content)
    return render(request, 'business/venuzuela-business.html', {'api' : api})



    #health news 


def argentina_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ar&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/argentina-health.html', {'api' : api})
    
def australia_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=au&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/australia-health.html', {'api' : api})
    
def austria_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=at&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/austria-health.html', {'api' : api})
        
def belgium_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=be&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/belgium-health.html', {'api' : api})
    
def brazil_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=br&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/brazil-health.html', {'api' : api})
    
    
def bulgaria_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=bg&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/bulgaria-health.html', {'api' : api})
    
def canada_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ca&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/canada-health.html', {'api' : api})
    
def china_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cn&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/china-health.html', {'api' : api})
    
def colombia_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=co&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/colombia-health.html', {'api' : api})
    
def cuba_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cu&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/cuba-health.html', {'api' : api})
    
def Czech_Republic_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cz&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/Czech-Republic-health.html', {'api' : api})
    
def egypt_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=eg&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/egypt-health.html', {'api' : api})
    
def france_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=fr&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/france-health.html', {'api' : api})
    
def germany_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=de&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/germany-health.html', {'api' : api})
    
    
def greece_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=de&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/greece-health.html', {'api' : api})
        #Hong Kong
def HK_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=hk&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/HK-health.html', {'api' : api})
    
def hungary_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=hu&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/hungary-health.html', {'api' : api})
    
def india_health(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/india-health.html', {'api' : api})
    
    
def indonesia_health(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=id&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/indonesia-health.html', {'api' : api})
    
def ireland_health(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ie&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/ireland-health.html', {'api' : api})
    
    
def israel_health(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=il&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/israel-health.html', {'api' : api})
    
def italy_health(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=it&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/italy-health.html', {'api' : api})
    
    
def japan_health(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=jp&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/japan-health.html', {'api' : api})
    
def latvia_health(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=lv&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/latvia-health.html', {'api' : api})
    
    
def lithuania_health(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=lt&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/lithuania-health.html', {'api' : api})
    
    
def malaysia_health(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=my&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/malaysia-health.html', {'api' : api})
    
    
    
def mexico_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=mx&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/mexico-health.html', {'api' : api})
    
    
def morocco_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ma&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/morocco-health.html', {'api' : api})
    
    
def netherlands_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=nl&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/netherlands-health.html', {'api' : api})
    
    
def nz_health(request):
     
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=nz&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
    
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/nz-health.html', {'api' : api})
    
    
def nigeria_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ng&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/nigeria-health.html', {'api' : api})
    
    
def norway_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=no&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/norway-health.html', {'api' : api})
    
    
def philippines_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ph&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/philippines-health.html', {'api' : api})
    
    
def poland_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=pl&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/poland-health.html', {'api' : api})
    
    
def portugal_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=pt&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/portugal-health.html', {'api' : api})
    
    
def romania_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ro&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/romania-health.html', {'api' : api})
    
    
def russia_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ru&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/russia-health.html', {'api' : api})
    
    
    
def SA_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sa&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/saudi-arabia-health.html', {'api' : api})
    
    
    
def serbia_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=rs&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/serbia-health.html', {'api' : api})
    
    
def singapore_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sg&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/singapore-health.html', {'api' : api})
    
    
def slovakia_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sk&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/slovakia-health.html', {'api' : api})
    
    
def slovenia_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=si&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/slovenia-health.html', {'api' : api})
    
    
def south_africa_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=za&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/south-africa-health.html', {'api' : api})
    
    
def south_korea_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=kr&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/south-korea-health.html', {'api' : api})
    
    
def sweden_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=se&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/sweden-health.html', {'api' : api})
    
    
def switzerland_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ch&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/switzerland-health.html', {'api' : api})
    
    
def taiwan_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=tw&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/taiwan-health.html', {'api' : api})
    
    
def thailand_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=th&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/thailand-health.html', {'api' : api})
    
    
    
def turkey_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=tr&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/turkey-health.html', {'api' : api})
    
    
def UAE_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ae&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/UAE-health.html', {'api' : api})
    
    
def ukraine_health(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ua&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'health/ukraine-health.html', {'api' : api})
    
    
def uk_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=gb&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/uk-health.html', {'api' : api})
    
    
def us_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/us-health.html', {'api' : api})
    
    
def venuzuela_health(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ve&category=health&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'health/venuzuela-health.html', {'api' : api})
    



    #science news 


def argentina_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ar&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/argentina-science.html', {'api' : api})
    
def australia_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=au&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/australia-science.html', {'api' : api})
    
def austria_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=at&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/austria-science.html', {'api' : api})
        
def belgium_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=be&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/belgium-science.html', {'api' : api})
    
def brazil_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=br&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/brazil-science.html', {'api' : api})
    
    
def bulgaria_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=bg&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/bulgaria-science.html', {'api' : api})
    
def canada_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ca&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/canada-science.html', {'api' : api})
    
def china_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cn&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/china-science.html', {'api' : api})
    
def colombia_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=co&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/colombia-science.html', {'api' : api})
    
def cuba_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cu&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/cuba-science.html', {'api' : api})
    
def Czech_Republic_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cz&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/Czech-Republic-science.html', {'api' : api})
    
def egypt_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=eg&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/egypt-science.html', {'api' : api})
    
def france_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=fr&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/france-science.html', {'api' : api})
    
def germany_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=de&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/germany-science.html', {'api' : api})
    
    
def greece_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=de&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/greece-science.html', {'api' : api})
        #Hong Kong
def HK_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=hk&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/HK-science.html', {'api' : api})
    
def hungary_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=hu&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/hungary-science.html', {'api' : api})
    
def india_science(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/india-science.html', {'api' : api})
    
    
def indonesia_science(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=id&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/indonesia-science.html', {'api' : api})
    
def ireland_science(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ie&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/ireland-science.html', {'api' : api})
    
    
def israel_science(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=il&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/israel-science.html', {'api' : api})
    
def italy_science(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=it&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/italy-science.html', {'api' : api})
    
    
def japan_science(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=jp&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/japan-science.html', {'api' : api})
    
def latvia_science(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=lv&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/latvia-science.html', {'api' : api})
    
    
def lithuania_science(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=lt&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/lithuania-science.html', {'api' : api})
    
    
def malaysia_science(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=my&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/malaysia-science.html', {'api' : api})
    
    
    
def mexico_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=mx&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/mexico-science.html', {'api' : api})
    
    
def morocco_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ma&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/morocco-science.html', {'api' : api})
    
    
def netherlands_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=nl&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/netherlands-science.html', {'api' : api})
    
    
def nz_science(request):
     
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=nz&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
    
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/nz-science.html', {'api' : api})
    
    
def nigeria_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ng&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/nigeria-science.html', {'api' : api})
    
    
def norway_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=no&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/norway-science.html', {'api' : api})
    
    
def philippines_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ph&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/philippines-science.html', {'api' : api})
    
    
def poland_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=pl&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/poland-science.html', {'api' : api})
    
    
def portugal_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=pt&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/portugal-science.html', {'api' : api})
    
    
def romania_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ro&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/romania-science.html', {'api' : api})
    
    
def russia_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ru&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/russia-science.html', {'api' : api})
    
    
    
def SA_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sa&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/saudi-arabia-science.html', {'api' : api})
    
    
    
def serbia_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=rs&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/serbia-science.html', {'api' : api})
    
    
def singapore_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sg&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/singapore-science.html', {'api' : api})
    
    
def slovakia_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sk&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/slovakia-science.html', {'api' : api})
    
    
def slovenia_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=si&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/slovenia-science.html', {'api' : api})
    
    
def south_africa_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=za&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/south-africa-science.html', {'api' : api})
    
    
def south_korea_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=kr&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/south-korea-science.html', {'api' : api})
    
    
def sweden_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=se&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/sweden-science.html', {'api' : api})
    
    
def switzerland_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ch&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/switzerland-science.html', {'api' : api})
    
    
def taiwan_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=tw&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/taiwan-science.html', {'api' : api})
    
    
def thailand_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=th&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/thailand-science.html', {'api' : api})
    
    
    
def turkey_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=tr&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/turkey-science.html', {'api' : api})
    
    
def UAE_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ae&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/UAE-science.html', {'api' : api})
    
    
def ukraine_science(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ua&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'science/ukraine-science.html', {'api' : api})
    
    
def uk_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=gb&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/uk-science.html', {'api' : api})
    
    
def us_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/us-science.html', {'api' : api})
    
    
def venuzuela_science(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ve&category=science&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'science/venuzuela-science.html', {'api' : api})
    



    #sports news 


def argentina_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ar&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/argentina-sports.html', {'api' : api})
    
def australia_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=au&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/australia-sports.html', {'api' : api})
    
def austria_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=at&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/austria-sports.html', {'api' : api})
        
def belgium_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=be&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/belgium-sports.html', {'api' : api})
    
def brazil_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=br&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/brazil-sports.html', {'api' : api})
    
    
def bulgaria_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=bg&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/bulgaria-sports.html', {'api' : api})
    
def canada_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ca&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/canada-sports.html', {'api' : api})
    
def china_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cn&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/china-sports.html', {'api' : api})
    
def colombia_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=co&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/colombia-sports.html', {'api' : api})
    
def cuba_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cu&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/cuba-sports.html', {'api' : api})
    
def Czech_Republic_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cz&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/Czech-Republic-sports.html', {'api' : api})
    
def egypt_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=eg&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/egypt-sports.html', {'api' : api})
    
def france_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=fr&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/france-sports.html', {'api' : api})
    
def germany_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=de&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/germany-sports.html', {'api' : api})
    
    
def greece_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=de&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/greece-sports.html', {'api' : api})
        #Hong Kong
def HK_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=hk&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/HK-sports.html', {'api' : api})
    
def hungary_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=hu&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/hungary-sports.html', {'api' : api})
    
def india_sports(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/india-sports.html', {'api' : api})
    
    
def indonesia_sports(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=id&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/indonesia-sports.html', {'api' : api})
    
def ireland_sports(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ie&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/ireland-sports.html', {'api' : api})
    
    
def israel_sports(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=il&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/israel-sports.html', {'api' : api})
    
def italy_sports(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=it&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/italy-sports.html', {'api' : api})
    
    
def japan_sports(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=jp&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/japan-sports.html', {'api' : api})
    
def latvia_sports(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=lv&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/latvia-sports.html', {'api' : api})
    
    
def lithuania_sports(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=lt&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/lithuania-sports.html', {'api' : api})
    
    
def malaysia_sports(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=my&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/malaysia-sports.html', {'api' : api})
    
    
    
def mexico_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=mx&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/mexico-sports.html', {'api' : api})
    
    
def morocco_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ma&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/morocco-sports.html', {'api' : api})
    
    
def netherlands_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=nl&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/netherlands-sports.html', {'api' : api})
    
    
def nz_sports(request):
     
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=nz&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
    
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/nz-sports.html', {'api' : api})
    
    
def nigeria_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ng&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/nigeria-sports.html', {'api' : api})
    
    
def norway_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=no&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/norway-sports.html', {'api' : api})
    
    
def philippines_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ph&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/philippines-sports.html', {'api' : api})
    
    
def poland_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=pl&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/poland-sports.html', {'api' : api})
    
    
def portugal_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=pt&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/portugal-sports.html', {'api' : api})
    
    
def romania_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ro&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/romania-sports.html', {'api' : api})
    
    
def russia_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ru&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/russia-sports.html', {'api' : api})
    
    
    
def SA_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sa&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/saudi-arabia-sports.html', {'api' : api})
    
    
    
def serbia_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=rs&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/serbia-sports.html', {'api' : api})
    
    
def singapore_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sg&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/singapore-sports.html', {'api' : api})
    
    
def slovakia_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sk&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/slovakia-sports.html', {'api' : api})
    
    
def slovenia_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=si&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/slovenia-sports.html', {'api' : api})
    
    
def south_africa_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=za&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/south-africa-sports.html', {'api' : api})
    
    
def south_korea_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=kr&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/south-korea-sports.html', {'api' : api})
    
    
def sweden_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=se&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/sweden-sports.html', {'api' : api})
    
    
def switzerland_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ch&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/switzerland-sports.html', {'api' : api})
    
    
def taiwan_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=tw&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/taiwan-sports.html', {'api' : api})
    
    
def thailand_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=th&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/thailand-sports.html', {'api' : api})
    
    
    
def turkey_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=tr&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/turkey-sports.html', {'api' : api})
    
    
def UAE_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ae&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/UAE-sports.html', {'api' : api})
    
    
def ukraine_sports(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ua&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'sports/ukraine-sports.html', {'api' : api})
    
    
def uk_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=gb&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/uk-sports.html', {'api' : api})
    
    
def us_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/us-sports.html', {'api' : api})
    
    
def venuzuela_sports(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ve&category=sports&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'sports/venuzuela-sports.html', {'api' : api})
    
    

    #technology news 


def argentina_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ar&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/argentina-technology.html', {'api' : api})
    
def australia_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=au&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/australia-technology.html', {'api' : api})
    
def austria_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=at&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/austria-technology.html', {'api' : api})
        
def belgium_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=be&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/belgium-technology.html', {'api' : api})
    
def brazil_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=br&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/brazil-technology.html', {'api' : api})
    
    
def bulgaria_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=bg&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/bulgaria-technology.html', {'api' : api})
    
def canada_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ca&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/canada-technology.html', {'api' : api})
    
def china_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cn&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/china-technology.html', {'api' : api})
    
def colombia_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=co&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/colombia-technology.html', {'api' : api})
    
def cuba_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cu&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/cuba-technology.html', {'api' : api})
    
def Czech_Republic_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=cz&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/Czech-Republic-technology.html', {'api' : api})
    
def egypt_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=eg&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/egypt-technology.html', {'api' : api})
    
def france_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=fr&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/france-technology.html', {'api' : api})
    
def germany_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=de&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/germany-technology.html', {'api' : api})
    
    
def greece_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=de&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/greece-technology.html', {'api' : api})
        #Hong Kong
def HK_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=hk&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/HK-technology.html', {'api' : api})
    
def hungary_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=hu&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/hungary-technology.html', {'api' : api})
    
def india_technology(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/india-technology.html', {'api' : api})
    
    
def indonesia_technology(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=id&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/indonesia-technology.html', {'api' : api})
    
def ireland_technology(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ie&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/ireland-technology.html', {'api' : api})
    
    
def israel_technology(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=il&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/israel-technology.html', {'api' : api})
    
def italy_technology(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=it&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/italy-technology.html', {'api' : api})
    
    
def japan_technology(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=jp&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/japan-technology.html', {'api' : api})
    
def latvia_technology(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=lv&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/latvia-technology.html', {'api' : api})
    
    
def lithuania_technology(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=lt&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/lithuania-technology.html', {'api' : api})
    
    
def malaysia_technology(request):
     
    
        
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=my&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/malaysia-technology.html', {'api' : api})
    
    
    
def mexico_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=mx&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/mexico-technology.html', {'api' : api})
    
    
def morocco_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ma&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/morocco-technology.html', {'api' : api})
    
    
def netherlands_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=nl&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/netherlands-technology.html', {'api' : api})
    
    
def nz_technology(request):
     
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=nz&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
    
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/nz-technology.html', {'api' : api})
    
    
def nigeria_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ng&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/nigeria-technology.html', {'api' : api})
    
    
def norway_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=no&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/norway-technology.html', {'api' : api})
    
    
def philippines_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ph&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/philippines-technology.html', {'api' : api})
    
    
def poland_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=pl&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/poland-technology.html', {'api' : api})
    
    
def portugal_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=pt&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/portugal-technology.html', {'api' : api})
    
    
def romania_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ro&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/romania-technology.html', {'api' : api})
    
    
def russia_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ru&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/russia-technology.html', {'api' : api})
    
    
    
def SA_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sa&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/saudi-arabia-technology.html', {'api' : api})
    
    
    
def serbia_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=rs&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/serbia-technology.html', {'api' : api})
    
    
def singapore_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sg&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/singapore-technology.html', {'api' : api})
    
    
def slovakia_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=sk&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/slovakia-technology.html', {'api' : api})
    
    
def slovenia_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=si&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/slovenia-technology.html', {'api' : api})
    
    
def south_africa_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=za&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/south-africa-technology.html', {'api' : api})
    
    
def south_korea_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=kr&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/south-korea-technology.html', {'api' : api})
    
    
def sweden_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=se&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/sweden-technology.html', {'api' : api})
    
    
def switzerland_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ch&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/switzerland-technology.html', {'api' : api})
    
    
def taiwan_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=tw&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/taiwan-technology.html', {'api' : api})
    
    
def thailand_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=th&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/thailand-technology.html', {'api' : api})
    
    
    
def turkey_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=tr&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/turkey-technology.html', {'api' : api})
    
    
def UAE_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ae&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/UAE-technology.html', {'api' : api})
    
    
def ukraine_technology(request):
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ua&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
    
        return render(request, 'technology/ukraine-technology.html', {'api' : api})
    
    
def uk_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=gb&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/uk-technology.html', {'api' : api})
    
    
def us_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/us-technology.html', {'api' : api})
    
    
def venuzuela_technology(request):
     
    
        news_api_requests = requests.get("http://newsapi.org/v2/top-headlines?country=ve&category=technology&apiKey=0e2f001f361849869d4271ff5efcf91f")
        api = json.loads(news_api_requests.content)
        return render(request, 'technology/venuzuela-technology.html', {'api' : api})
    
        