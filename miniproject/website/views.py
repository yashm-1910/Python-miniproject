from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html', {'title':'About'})

def biological(request):
    return render(request, 'website/biological.html', {'title':'Biological Disasters'})

def chemical(request):
    return render(request, 'website/chemical.html', {'title':'Chemical Disasters'})

def cyclone(request):
    return render(request, 'website/cyclone.html', {'title':'Cyclone'})

def earthquake(request):
    return render(request, 'website/earthquake.html', {'title':'Earthquake'})

def floods(request):
    return render(request, 'website/floods.html', {'title':'Floods'})

def heatwave(request):
    return render(request, 'website/heatwave.html', {'title':'Heat Wave'})

def nuclear(request):
    return render(request, 'website/nuclear.html', {'title':'Nuclear and Radiological Emergency'})

def tsunami(request):
    return render(request, 'website/tsunami.html', {'title':'Tsunami'})

def urbanfloods(request):
    return render(request, 'website/urbanfloods.html', {'title':'Urban Floods'})

def satellite(request):
    return render(request, 'website/satellite.html', {'title':'Satellite Images'})