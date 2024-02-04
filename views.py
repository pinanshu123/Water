from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import requests
import pandas as pd
from .models import YourModel
from django.core.serializers import serialize
def index(request):
    return render(request, "Index.html")

def your_view(request):
    # Your logic here

    # Make the GET request to ThingSpeak API
    api_key = "UY5WT17S8CWQ6VLH"
    url = f"https://api.thingspeak.com/apps/thinghttp/send_request?api_key={api_key}"

    response = requests.get(url)

    # Check the response status
    if response.status_code == 200:
        # Success
        print(response.text)
        return HttpResponse("Success")
    else:
        # Handle error
        return HttpResponse("Failed")

def reg(request): 
    return render(request, "regulatory.html")

def who(request): 
    return render(request, "who.html")

def ind(request): 
    return render(request, "indian.html")

def clarity(request): 
    return render(request, "dive.html")

def project(request):
    return render(request, "about.html")

def Graph(request):
    return render(request, "vis.html")

def uploadcsv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        df = pd.read_csv(csv_file)
        for index, row in df.iterrows(): 
            instance = YourModel(timestamp = row['created_at'], turbidity = row['field1'], temperature = row['field2'], pH = row['field3'])
            instance.save()
        return HttpResponse("Success")
    
def getsensordata(request):
    alldata = YourModel.objects.all()
    jsondata = serialize('json', alldata)
    return JsonResponse({'data': jsondata}, safe=False)
