from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == "POST":
        category = request.POST['Business']
        if category == "HEADLINES":
            try:
                api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=b2978c74ac7c4e69880b01358540a4ab")
                api_data = json.loads(api_request.content)
            except Exception as e:
                api_data = "Some error occured..."

            data = api_data.get("articles")
            
            return render(request,'home.html',{
                'api' : api_data,
                'data' : data
                })

        else:
            try:
                api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=" + category + "&apiKey=b2978c74ac7c4e69880b01358540a4ab")
                api_data = json.loads(api_request.content)
            except Exception as e:
                api_data = "Some error occured..."

            data = api_data.get("articles")
            
            return render(request,'home.html',{
                'api' : api_data,
                'data' : data
                })

    else:
        try:
            api_request = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=b2978c74ac7c4e69880b01358540a4ab")
            api_data = json.loads(api_request.content)
        except Exception as e:
            api_data = "Some error occured..."

        data = api_data.get("articles")
        
        return render(request,'home.html',{
            'api' : api_data,
            'data' : data
            })
