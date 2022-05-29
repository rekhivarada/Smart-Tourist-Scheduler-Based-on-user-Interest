# # import string
# # import random

# # print(str(''.join(random.choices(string.digits, k = 25))))




# # cat = {'Art & Entertainment': True, 'College & University': True, 'Event': False, 'Food': True, 'Nightlife Spot': True,
# #         'Outdoors & Recreation': False, 'Professional & Other Places': True, 'Residence': False, 'Shop & Service': False, 'Travel & Transport': True}

# # cat_list = ''

# # for key, value in cat.items():
# #     if value:
# #         cat_list = cat_list + key+'@%@'


# # print(cat_list)


# # from flask import Request


# # str1 = '411030,Mahārāshtra,India @%@ Above Vishal Megamart (Laxmi Road),Pune,Mahārāshtra,India @%@ Vasantrao Deshmukh Path, Shivaji Nagar,Pune,Mahārāshtra,India @%@ Near Sambhaji Park, JM Road,Pune 411004,Mahārāshtra,India @%@ Jangli Maharaj Road,Pune,Mahārāshtra,India @%@ 759/75, GoodLuck Chowk (Corner of FC Road and Bhandarkar Road),Pune,Mahārāshtra,India @%@ 638, Deccan Gymkhana, Shivajinagar,Pune India,Mahārāshtra,India @%@ 3rd Floor R Deccan Mall (Jangali Maharaj Road),Pune,Mahārāshtra,India @%@ India @%@ J M Rd, Shivaji Nagar,Pune,Mahārāshtra,India @%@ Survey No 12/27, Fergusson College Road (Sudhabhau Kelkar Road),Pune 411004,Mahārāshtra,India @%@ Opp To Sagar Arcade,Ranade Institute Lane (FC Road),Pune,Mahārāshtra,India @%@ F C Rd,Pune,Mahārāshtra,India @%@ Tulshibaug (Laxmi road),Pune,Mahārāshtra,India @%@ Maldhakka chowk,Pune,Mahārāshtra,India @%@ India @%@ 1206, Next to Shiv Sagar, Opposite Sambhaji Park, J.M. Road,Pune 411004,Mahārāshtra,India @%@ 6a 1195/C, Next To Tukaram Paduka Mandir, Opposite National Heart Institute (Fergusson College Road, Shivaji Nagar),Pune 411005,Mahārāshtra,India @%@ R Deccan Mall, Jangli Maharaj Road (Deccan Gymkhana),Pune 411004,Mahārāshtra,India @%@ '

# # print(len(str1))


#     # list = ['amphitheater                    =   db.Column(db.Boolean, default=False, nullable=False)
#     # aquarium                        =   db.Column(db.Boolean, default=False, nullable=False)
#     # arcade                          =   db.Column(db.Boolean, default=False, nullable=False)
#     # art_gallery                     =   db.Column(db.Boolean, default=False, nullable=False)
#     # bowling_alley                   =   db.Column(db.Boolean, default=False, nullable=False)
#     # casino                          =   db.Column(db.Boolean, default=False, nullable=False)
#     # circus                          =   db.Column(db.Boolean, default=False, nullable=False)
#     # comedy_club                     =   db.Column(db.Boolean, default=False, nullable=False)
#     # concert_hall                    =   db.Column(db.Boolean, default=False, nullable=False)
#     # country_dance_club              =   db.Column(db.Boolean, default=False, nullable=False)
#     # disc_golf                       =   db.Column(db.Boolean, default=False, nullable=False)
#     # escape_room                     =   db.Column(db.Boolean, default=False, nullable=False)
#     # exhibit                         =   db.Column(db.Boolean, default=False, nullable=False)
#     # general_entertainment           =   db.Column(db.Boolean, default=False, nullable=False)
#     # go_kart_track                   =   db.Column(db.Boolean, default=False, nullable=False)
#     # historic_site                   =   db.Column(db.Boolean, default=False, nullable=False)
#     # karaoke_box                     =   db.Column(db.Boolean, default=False, nullable=False)
#     # laser_tag                       =   db.Column(db.Boolean, default=False, nullable=False)
#     # memorial_site                   =   db.Column(db.Boolean, default=False, nullable=False)
#     # mini_golf                       =   db.Column(db.Boolean, default=False, nullable=False)
#     # movie_theater                   =   db.Column(db.Boolean, default=False, nullable=False)
#     # museum                          =   db.Column(db.Boolean, default=False, nullable=False)
#     # music_venue                     =   db.Column(db.Boolean, default=False, nullable=False)
#     # pachinko_parlor                 =   db.Column(db.Boolean, default=False, nullable=False)
#     # performing_arts_venue           =   db.Column(db.Boolean, default=False, nullable=False)
#     # pool_hall                       =   db.Column(db.Boolean, default=False, nullable=False)
#     # public_art                      =   db.Column(db.Boolean, default=False, nullable=False)
#     # racecourse                      =   db.Column(db.Boolean, default=False, nullable=False)
#     # racetrack                       =   db.Column(db.Boolean, default=False, nullable=False)
#     # roller_rink                     =   db.Column(db.Boolean, default=False, nullable=False)
#     # salsa_club                      =   db.Column(db.Boolean, default=False, nullable=False)
#     # samba_school                    =   db.Column(db.Boolean, default=False, nullable=False)
#     # stadium                         =   db.Column(db.Boolean, default=False, nullable=False)
#     # theme_park                      =   db.Column(db.Boolean, default=False, nullable=False)
#     # tour_provider                   =   db.Column(db.Boolean, default=False, nullable=False)
#     # vr_cafe                         =   db.Column(db.Boolean, default=False, nullable=False)
#     # water_park                      =   db.Column(db.Boolean, default=False, nullable=False)
#     # zoo']







# # lattitudeint=[]
# # for i in lattitude:
# #     lattitudeint.append(float(i))
# # langitudeint = []
# # for i in langitude:
# #     langitudeint.append(float(i))

# # gmapOne=gmplot.GoogleMapPlotter(19.0760,21.0418,19.9975)
# # gmapOne.scatter(lattitudeint,langitudeint,size=50,marker=False)
# # gmapOne.plot(lattitudeint,langitudeint,'blue',edge_width=2.5)
# # gmapOne.draw("map1.html")
# # distance=[]
# # n=len(lattitude)
# # for i in range(n):
# #     p=math.sqrt(pow(langitudeint[i],2)+pow(lattitudeint[i],2))
# #     distance.append(p)
# # #print(distance)
# # sorted_distance=sorted(distance)
# # #print(sorted_distance)
# # ans=[]
# # for i in sorted_distance:
# #     ind=distance.index(i)
# #     ans.append(lattitudeint[ind])
# # #print(ans)
# # lat1=[]
# # lang1=[]
# # for i in sorted_distance:
# #     ind=distance.index(i)
# #     lat1.append(lattitudeint[ind])
# #     lang1.append(langitudeint[ind])
# # gmapOne=gmplot.GoogleMapPlotter(19.0760,21.0418,19.9975)
# # gmapOne.scatter(lat1,lang1,size=50,marker=False)
# # gmapOne.plot(lat1,lang1,'blue',edge_width=2.5)
# # gmapOne.draw("map.html")




# # import random
# # from flask import Blueprint, flash, redirect, render_template, session, url_for,  request
# # from werkzeug.security import generate_password_hash
# # from flask_login import login_required, current_user
# # from .models import TripData, UserCategory, VenueData
# # from . import db
# # import requests
# # import string
# # import  pandas as pd


# # CLIENT_ID='AH5YKUWPNYWWQPAX2EEDEE0UUJSQGVIXZROW11HCTUURE0SG'
# # CLIENT_SECRET='0PGEM5WODIHNYPVJPXDDBV5FEBU0GD2D1RNYRQBKROCQEUPS'
# # VERSION=20202808
# # radius=10000
# # LIMIT=10000
# # lat=fetch_lattitude
# # lng=fetch_longitude

# # url5='https://api.foursquare.com/v2/venues/categories?client_id={}&client_secret={}&v={}'.format(CLIENT_ID,CLIENT_SECRET,VERSION)
# # dictionary={}
# # dictionary_id={}
# # category=requests.get(url5).json()['response']['categories']
# # for i in category:
# #             # print('category: \n', i['name'])
# #     if i['name'] in user_preferences:
# #         li=[]
# #         sub_category_id = []
# #         for j in i['categories']:
# #                     li.append(j['name'])
# #                     sub_category_id.append(j['id'])
# #                     #print('Subcategory: ', j['name'])
# #                 dictionary_id[i['name']]=sub_category_id
# #                 dictionary[i['name']]=li
# #         #print(dictionary)
# #         #print(dictionary_id)
# #         url1='https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&limit={}'.format(CLIENT_ID,CLIENT_SECRET,VERSION,lat,lng,LIMIT)
# #         nearbyLocation=Request.get(url1).json()['response']
# #         ans={}
# #         for i in dictionary_id:
# #             ans[i]=[]
# #         #print(ans)
    
# #         for i in nearbyLocation['groups']:
# #             for j in i['items']:
# #                 id=j['venue']['id']
# #                 d=j['venue']['categories']
# #                 name_venue=j['venue']['name']
# #                 location_list=j['venue']
# #                 p = location_list['location']
# #                 lattitude=str(p['lat'])
# #                 longitude=str(p['lng'])
# #                 idf=d[0]['id']
# #                 ct=0
# #                 for p in dictionary_id:
# #                     ct=ct+1
# #                     k=dictionary_id[p]
# #                     if idf in k:
# #                         name = d[0]['name']
# #                         cat_id=d[0]['id']
# #                         #print(id+" "+name+" "+cat_id+" "+str(ct)+" "+name_venue)
# #                         li=ans[p]
# #                         li.append(id)
# #                         ans[p]=li

# #         #print(ans)
# #         pages={}


# #         for i in ans:
# #             d=ans[i]
# #             print(i)
# #             for j in d:
# #                 places=[]
# #                 venue_id=j
# #                 print(venue_id)
# #                 urlv = 'https://api.foursquare.com/v2/venues/' + venue_id + '?&client_id={}&client_secret={}&v={}&radius={}&limit={}'.format(
# #                     CLIENT_ID, CLIENT_SECRET, VERSION, radius, LIMIT)
# #                 venuedesc = requests.get(urlv).json()['response']['venue']
# #                 venue_name=venuedesc['name']
# #                 venue_location=venuedesc['location']
# #                 venue_categories=venuedesc['categories']
# #                 # print(venue_name)
# #                 #print(venue_location['formattedAddress'])
# #                 kl=venue_categories[0]['icon']
# #                 photourl =kl['prefix']+'100'+kl['suffix']
# #                 # print(photourl)
# #                 address=""
# #                 #print(venue_categories[0]['icon'])
# #                 for add in venue_location['formattedAddress']:
# #                     address=address+add+","
# #                 address=address[0:len(address)-1]
# #                 # print(address)
# #                 places.append(str(venue_id))
# #                 places.append(str(venue_name))
# #                 places.append(str(address))
# #                 places.append((str(photourl)))
# #                 places.append((str(lattitude)))
# #                 places.append((str(longitude)))



# #                 venues.append(places)


        
# #                 # venues_copy = venues

# #         venue_id_list = []
# #         for place in venues:

# #             x =[]
# #             x.append(str(place[0]))
# #             x.append(str(place[4]))
# #             x.append(str(place[5]))
# #             venue_id_list.append(x)

# # import geocoder
# # g = geocoder.ip('me')
# # print(g.latlng)


# from datetime import date
# import math
# import geopy.distance


# venue_count=25
# date1=date(2019,1,13)
# date2=date(2019,1,14)
# # month=[31,28,31,30,31,30,31,31,30,31,30,31]
# def numOfDays(date1,date2):
#     return (date2-date1).days
# def sujject_by_train(days_in_hours,dis,mo,day,year):
#     ans=(dis/55)+venue_count
#     if ans>days_in_hours:
#         p=math.ceil((ans-days_in_hours)/24)
#         print(ans)
#         print(p)
#         return "Please Extend Your End Date & the days: "+str(p)+" & "+str(day+p)+"/"+str(mo)+"/"+str(year)
#     else:
#         return "Enjoy Your Journey"
# def sujject_by_bus(days_in_hours,dis,month,day,year):
#     ans = (dis / 40) + venue_count
#     if ans > days_in_hours:
#         p = math.ceil((ans - days_in_hours) / 24)
#         print(ans)
#         print(p)
#         return "Please Extend Your End Date & the days: "+str(p)+" & "+str(day+p)+"/"+str(mo)+"/"+str(year)
#     else:
#         return "Enjoy Your Journey"
# def sujject_by_car(days_in_hours,dis,month,day,year):
#     ans = (dis / 48.88) + venue_count
#     if ans > days_in_hours:
#         p = math.ceil((ans - days_in_hours) / 24)
#         print(ans)
#         print(p)
#         return "Please Extend Your End Date & the days: "+str(p)+" & "+str(day+p)+"/"+str(mo)+"/"+str(year)
#     else:
#         return "Enjoy Your Journey"

# print("Days: ",numOfDays(date1,date2))
# days_In_Hours=numOfDays(date1,date2)*(24-13)
# print("Days in hours: ",days_In_Hours)
# myList=[19.0760,72.8777,21.0418,75.7876,19.9975,73.7898]
# cords1=(myList[0],myList[1])
# cords2=(myList[2],myList[3])
# distance=geopy.distance.geodesic(cords1,cords2).km
# for i in range(2,len(myList)-2,2):
#     cords1 = (myList[i], myList[i+1])
#     cords2 = (myList[i+2], myList[i+3])
#     distance += geopy.distance.geodesic(cords1, cords2).km
# print("Distance: ",distance)
# Sujjetion='train'
# if Sujjetion=='train':
#     print(sujject_by_train(days_In_Hours,distance,date2.month,date2.day,date2.year))
# elif Sujjetion=='bus':
#     print(sujject_by_bus(days_In_Hours,distance,date2.month,date2.day,date2.year))
# elif Sujjetion=='car':
#     print(sujject_by_car(days_In_Hours,distance,date2.month,date2.day,date2.year))




from datetime import date
import math
import time
from twilio.rest import Client
import datetime
import geopy.distance
venue_count=0
date1=date(2019,1,12)
date2=date(2019,1,13)
client = Client("AC55b49e0375a2402ca28ab2dcb257a394", "f4dec6229835e621e81e875c7f04eaa5")
venue_List=['mumbai','nashik','Bhusawal','sangamner','slajdlj','dsklhfks','lskdjfk']
def numOfDays(date1,date2):
    return (date2-date1).days
def sujject_by_train(days_in_hours,dis,mo,day,year,mo1,day1,year1,myList):
    ans=(dis/55)+venue_count
    if ans>days_in_hours:
        p=math.ceil((ans-days_in_hours)/24)
        print(ans)
        print(p)
        return "Please Extend Your End Date & the days: "+str(p)+" & "+str(day+p)+"/"+str(mo)+"/"+str(year)
    else:
        Final_List.append("10:00:00")

        return "Enjoy Your Journey"
def sujject_by_bus(days_in_hours,dis,mo,day,year):
    ans = (dis / 40) + venue_count
    if ans > days_in_hours:
        p = math.ceil((ans - days_in_hours) / 24)
        print(ans)
        print(p)
        return "Please Extend Your End Date & the days: "+str(p)+" & "+str(day+p)+"/"+str(mo)+"/"+str(year)
    else:
        return "Enjoy Your Journey"
def sujject_by_car(days_in_hours,dis,mo,day,year):
    ans = (dis / 48.88) + venue_count
    if ans > days_in_hours:
        p = math.ceil((ans - days_in_hours) / 24)
        print(ans)
        print(p)
        return "Please Extend Your End Date & the days: "+str(p)+" & "+str(day+p)+"/"+str(mo)+"/"+str(year)
    else:
        return "Enjoy Your Journey"

print("Days: ",numOfDays(date1,date2))
days_In_Hours=numOfDays(date1,date2)*(24-13)
print("Days in hours: ",days_In_Hours)
myList=[19.0760,72.8777,21.0418,75.7876,19.9975,73.7898,19.9976,73.9898,20.0000,74.0000,20.0001,74.0001,20.0004,74.0006]
cords1=(myList[0],myList[1])
cords2=(myList[2],myList[3])
distance=geopy.distance.geodesic(cords1,cords2).km
for i in range(2,len(myList)-2,2):
    cords1 = (myList[i], myList[i+1])
    cords2 = (myList[i+2], myList[i+3])
    distance += geopy.distance.geodesic(cords1, cords2).km
print("Distance: ",distance)
'''Sujjetion='train'
if Sujjetion=='train':
    print(sujject_by_train(days_In_Hours,distance,date2.month,date2.day,date2.year,date1.month,date1.day,date1.year,myList))
elif Sujjetion=='bus':
    print(sujject_by_bus(days_In_Hours,distance,date2.month,date2.day,date2.year))
elif Sujjetion=='car':
    print(sujject_by_car(days_In_Hours,distance,date2.month,date2.day,date2.year))'''

ans = (distance / 48.88) + venue_count
print(distance/48.88)
dis=[]
if ans > days_In_Hours:
    p = math.ceil((ans - days_In_Hours) / 24)
    print(ans)
    print(p)
    print("Please Extend Your End Date & the days: " + str(p) + " & " + str(date2.day + p) + "/" + str(date2.month) + "/" + str(date2.year))
else:
    for i in range(0,len(myList)-2,2):
        cords1 = (myList[i], myList[i + 1])
        cords2 = (myList[i + 2], myList[i + 3])
        kl = geopy.distance.geodesic(cords1, cords2).km
        dis.append(kl)
    print(dis)
    hour_list=[]
    for i in dis:
        hour=math.ceil(i/48.88)
        hour_list.append(hour)
    Final_List=[]
    sum=10
    i=0
    f=1
    li=[10]
    print(hour_list)
    while i<len(hour_list):
        if (sum+hour_list[i])>21:
            Final_List.append(li)
            li=[10]
            f=0
            sum=10

        else:
            li.append(sum+hour_list[i])
            sum=sum+hour_list[i]+1
            i=i+1
            f=0
        if i==len(hour_list):
            Final_List.append(li)

    print(Final_List)
    Final_hour_list=[]
    for i in Final_List:
        li=[]
        for j in i:
            li.append(str(j)+":00:00")
        Final_hour_list.append(li)
    print(Final_hour_list)
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    curent_date=date.today()
    Final_date_list=[]
    vi=0
    for i in range(0,numOfDays(date1, date2)):
        if i==0:
            Final_date_list.append(date1)
            vi=date1.day
        else:
            da=date(date1.year,date1.month,(vi+1))
            Final_date_list.append(da)
            vi=vi+1
    message=''
    k=0
    Final_venue_list=[]
    for i in Final_hour_list:
        li=['started You journey']
        for j in range(1,len(i)):
            print(j)
            li.append(venue_List[k])
            k=k+1
        Final_venue_list.append(li)
    print(Final_venue_list)

    print(Final_date_list)
    for i in range(0,len(Final_date_list)):
        message=message+"Date: "+str(Final_date_list[i])+"\n"
        time_list=Final_hour_list[i]
        shedule=Final_venue_list[i]
        print(time_list)
        print(shedule)
        for j in range(0,len(time_list)):
            message=message+"Time: "+str(time_list[j])+" Action: "+str(shedule[j])+"\n"

    print(message)
    client.messages.create(to="+917620695744",
                           from_="+19853317974",
                           body=message)
    #print(curent_date)
    #print(current_time)
    print("Enjoy Your Journey")







################################################################




<!--  {% for i,place in enumerate(name_addr_list) %} -->

          <!-- <div class="outset places">
            <h4>{{i}}</h4>
            <h3>{{place[i]}}</h3>
            <p>{{place[i+1]}}</p>
            <img src={{place[3]}}>
             <p>latt - {{place[4]}}</p>
            <p>long - {{place[5]}}</p> 
          </div> -->



<!-- {% endfor %} -->
