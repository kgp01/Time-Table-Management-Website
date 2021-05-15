from django.shortcuts import render,redirect
from .models import events
from django.contrib import messages
from django.contrib.auth.models import User, auth
from datetime import datetime
from django.db import connection

from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request, 'home.html')

def deleteall(request):
    events.objects.filter(user = request.user).delete()
    return redirect('addevent')


def deleteone(request,cid):
    events.objects.get(pk=cid).delete()
    evs = events.objects.filter(user = request.user)
    data = {'event1':evs}
    # return render(request, 'addevent.html', data)
    return redirect('addevent')

def addevent(request):
    if request.method == 'POST':
        starttime =request.POST['starttime']
        endtime=request.POST['endtime']
        print(starttime)
        name = request.POST['name']
        starttime = starttime+":00"
        endtime = endtime + ":00"
        st =datetime.strptime(starttime, '%H:%M:%S').time()
        et =datetime.strptime(endtime, '%H:%M:%S').time()
        if request.user.is_authenticated:
            event = events(user = request.user,name = name, starttime = st,endtime = et)
            event.save();
            print("event created")
            # event.query
            event1 = events.objects.filter(user = request.user)
            data = {'event1':event1}
            # print(type(event1))
            # for obj in event1:
            #     print(obj.name)
            #     print(obj.starttime)

            return render(request, 'addevent.html', data)
        else:
            messages.info(request, 'Please login to creat events')
            
            return redirect('login.html')
    else:
        event1 = events.objects.filter(user = request.user)
        data = {'event1':event1}
        return render(request, 'addevent.html',data)
    


def showtimetable(request):
    event = events.objects.filter(user = request.user)
    # write your code here:
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    dict_1 = {}
    for i in event:
        
        et = str(i.endtime)
        et = int(et[0 : 2]) + float(et[3 : 5])/60.0
       
        temp_list = []
        temp_list.append(i.name)
        temp_list.append(str(i.starttime))
        temp_list.append(str(i.endtime))
        print(temp_list[0], temp_list[1], temp_list[2])
        
        dict_1[et] = temp_list
    
    for i in dict_1.keys():
        print(dict_1[i])
        print(end = " ")

    
    for i in sorted(dict_1.keys()) :
        list_1.append(dict_1[i])
    
    for i in list_1:
        print(i[0], i[1], i[2])
        list_2.append(i[0])
        list_3.append(i[1])
        list_4.append(i[2])
        print(end = " ")


        # i.name
        # i.starttime
        # i.endtime
    
    
    data = {"list_2": list_2, "list_3": list_3, "list_4": list_4, 'range': range(len(list_2))}

    return render(request, 'showtimetable.html', data)

    


