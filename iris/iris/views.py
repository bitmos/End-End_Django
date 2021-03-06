from django.shortcuts import render
from django.http import HttpResponse, response
import pickle
import json
import numpy as np
def initialize():
    global target
    global model
    with open('iris/columns.json','r') as f:
        target=json.load(f)["data_columns"]
    
    with open("iris/iris.pickle",'rb') as f:
        model=pickle.load(f)
    return model,target


# def index(request):
#     location=initialize()
#     data={
#         'locations':__locations
#     }
#     return render(request,'houseprice.html',{'data':data})
def estimate_iris(request):
    initialize()
    if request.method=="GET":
        return render(request,'iris/houseprice.html',{})
    else:
        slength=float(request.POST.get('slength'))
        swidth=float(request.POST.get('swidth'))
        plength=float(request.POST.get('plength'))
        pwidth=float(request.POST.get('pwidth'))

        x = np.zeros(4)
        x[0] = slength
        x[1] = swidth
        x[2] = plength
        x[3]=pwidth
        price=target[model.predict([x])[0]]
        data = {
              'price':price,
              'slength':slength,
              'swidth':swidth,
              'plength':plength,
              'pwidth':pwidth,

         }
        return render(request,'iris/houseprice.html',{'data':data})
         
    