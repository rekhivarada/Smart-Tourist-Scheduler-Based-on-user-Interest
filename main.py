from calendar import SUNDAY
from pickletools import long1
import random
from flask import Blueprint, flash, redirect, render_template, session, url_for,  request
from numpy import double
from werkzeug.security import generate_password_hash
from flask_login import login_required, current_user
from .models import TripData, UserCategory, VenueData, UserCategoryTrip
from . import db
import requests
import string
import  pandas as pd
from flask import json
import math
import gmplot
from datetime import date
import math
import geopy.distance
from datetime import date
import math
import time
from twilio.rest import Client
import datetime
import geopy.distance


main = Blueprint('main', __name__)



@main.route('/')
def index():
    return render_template('root.html')


@main.route('/home')
@login_required
def home():
    return render_template('home.html', user_firstname=current_user.user_firstname, user_id = current_user.user_id)


@main.route('/budget', methods=['POST', 'GET'])
@login_required
def budget():
    return render_template('index.html')

# Adding a get_trip_data_postroute for Schedule page
@main.route('/get_trip_data')
@login_required
def get_trip_data():
    return render_template('get_trip_data.html')


# Adding a route for Schedule page
@main.route('/get_trip_data', methods=['POST'])
@login_required
def get_trip_data_post():

    while(True):
        new_trip_id = str(''.join(random.choices(string.ascii_lowercase + string.digits, k = 8)))
        
        if TripData.query.filter_by(trip_id=new_trip_id).first():
            continue
        else:
            break

    session["trip_id"] = new_trip_id


    df=pd.read_csv('/home/rushikesh/Projects/Flask/BE_project/fs_link/worldcities.csv')
    vals=df['city_ascii'].values
    city=vals.tolist()
    vals=df['lat'].values
    lattitude=vals.tolist()
    vals=df['lng'].values
    longitude=vals.tolist()

    l = request.form.get('city_name')
    ind=city.index(l)
    lattitude=lattitude[ind]
    longitude=longitude[ind]
    
    
    trip_instance = {
        "user_id" : current_user.user_id,
        "trip_id" : new_trip_id,    
        "city_name"  : request.form.get('city_name'),
        "start_date" : request.form.get('start_date'),
        "end_date" : request.form.get('end_date'),
        "lattitude" : str(lattitude),
        "longitude" : str(longitude)
    }

    #create new record in respective realtion
    trip_data_var = TripData(**trip_instance)
    db.session.add(trip_data_var)
    db.session.commit()



    return redirect(url_for('pref.trip_preferences'))


# # Adding a route for trip preferences page
# @main.route('/trip_preferences')
# @login_required
# def trip_preferences():
#     return render_template('trip_preferences.html')


# Adding a route for trip preferences page
@main.route('/schedule_trip', methods=['POST', 'GET'])
@login_required
def schedule_trip():

    # if request.method == "POST":

        # if request.form['trip_preferences_default'] == 'default':
        #     user = UserCategory.query.filter_by(user_id = current_user.user_id).first()
        # else:
        user = UserCategoryTrip.query.filter_by(trip_id = session.get("trip_id")).first()


        

        user_preferences=[]
        venues=[]

        if user.user_id==current_user.user_id:
            if user.art_and_entertainment==True:
                user_preferences.append('Arts & Entertainment')
            if user.college_and_university==True:
                user_preferences.append('College & University')
            if user.event==True:
                user_preferences.append('Event')
            if user.food==True:
                user_preferences.append('Food')
            if user.nightlife_spot==True:
                user_preferences.append('Nightlife Spot')
            if user.outdoors_and_recreation==True:
                user_preferences.append('Outdoors & Recreation')
            if user.professional_and_other_places==True:
                user_preferences.append('Professional & Other Places')
            if user.residence==True:
                user_preferences.append('Residence')
            if user.shop_and_service==True:
                user_preferences.append('Shop & Service')
            if user.travel_and_transport==True:
                user_preferences.append('Travel & Transport')

            # Next code

        trip_id = session.get("trip_id")
        
        trip_record = TripData.query.filter_by(trip_id = trip_id).first()


        
        
        session['user_preferences'] = user_preferences

        # trip = TripData.query.filter_by(trip_id = new_trip_id).first()

        fetch_lattitude = trip_record.lattitude
        fetch_longitude = trip_record.longitude

            # print('Libraries imported.')

        CLIENT_ID='AH5YKUWPNYWWQPAX2EEDEE0UUJSQGVIXZROW11HCTUURE0SG'
        CLIENT_SECRET='0PGEM5WODIHNYPVJPXDDBV5FEBU0GD2D1RNYRQBKROCQEUPS'
        VERSION=20202808
        radius=10000
        LIMIT=10000
        lat=fetch_lattitude
        lng=fetch_longitude

        url5='https://api.foursquare.com/v2/venues/categories?client_id={}&client_secret={}&v={}'.format(CLIENT_ID,CLIENT_SECRET,VERSION)
        dictionary={}
        dictionary_id={}
        category=requests.get(url5).json()['response']['categories']
        for i in category:
            # print('category: \n', i['name'])
            if i['name'] in user_preferences:
                li=[]
                sub_category_id = []
                for j in i['categories']:
                    li.append(j['name'])
                    sub_category_id.append(j['id'])
                    #print('Subcategory: ', j['name'])
                dictionary_id[i['name']]=sub_category_id
                dictionary[i['name']]=li
        #print(dictionary)
        #print(dictionary_id)
        url1='https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&limit={}'.format(CLIENT_ID,CLIENT_SECRET,VERSION,lat,lng,LIMIT)
        nearbyLocation=requests.get(url1).json()['response']
        ans={}
        for i in dictionary_id:
            ans[i]=[]
        #print(ans)
    
        for i in nearbyLocation['groups']:
            for j in i['items']:
                id=j['venue']['id']
                d=j['venue']['categories']
                name_venue=j['venue']['name']
                
                idf=d[0]['id']
                ct=0
                for p in dictionary_id:
                    ct=ct+1
                    k=dictionary_id[p]
                    if idf in k:
                        name = d[0]['name']
                        cat_id=d[0]['id']
                        #print(id+" "+name+" "+cat_id+" "+str(ct)+" "+name_venue)
                        li=ans[p]
                        li.append(id)
                        ans[p]=li

        #print(ans)
        pages={}


        for i in ans:
            d=ans[i]
            print(i)
            for j in d:
                places=[]
                venue_id=j
                print(venue_id)
                urlv = 'https://api.foursquare.com/v2/venues/' + venue_id + '?&client_id={}&client_secret={}&v={}&radius={}&limit={}'.format(
                    CLIENT_ID, CLIENT_SECRET, VERSION, radius, LIMIT)
                
                venuedesc = requests.get(urlv).json()['response']['venue']
                
                location_list=venuedesc['location']
                # p = location_list['location']
                lattitude=str(location_list['lat'])
                longitude=str(location_list['lng'])
                
                venue_name=venuedesc['name']
                venue_location=venuedesc['location']
                venue_categories=venuedesc['categories']
                # print(venue_name)
                #print(venue_location['formattedAddress'])
                kl=venue_categories[0]['icon']
                photourl =kl['prefix']+'100'+kl['suffix']
                # print(photourl)
                address=""
                #print(venue_categories[0]['icon'])
                for add in venue_location['formattedAddress']:
                    address=address+add+","
                address=address[0:len(address)-1]
                # print(address)
                places.append(str(venue_id))
                places.append(str(venue_name))
                places.append(str(address))
                places.append((str(photourl)))
                places.append((str(lattitude)))
                places.append((str(longitude)))



                venues.append(places)


        
                # venues_copy = venues

        venue_list = []

        for place in venues:

            x = []

            x.append(str(place[0]))
            x.append(str(place[4]))
            x.append(str(place[5]))
            x.append(str(place[1]))
            x.append(str(place[2]))

            venue_list.append(x)

        session["venue_list"] = venue_list
        

        return render_template('venue_list.html', venues = venues, user_preferences=user_preferences)



@main.route('/store_venue', methods=['POST', 'GET'])
@login_required
def store_venue():

        venue_list = session.get("venue_list")
    
    # if request.method == "POST":

        # venue_status = {}
        venue_id_string = ''
        lattitude_string = ''
        longitude_string = ''
        name_string = ''
        addr_string = ''

        for venue in venue_list:
            if request.form.get(str(venue[0])):
                venue_id_string = venue_id_string + venue[0] + ' @%@ '
                lattitude_string = lattitude_string + venue[1] + ' @%@ '
                longitude_string = longitude_string + venue[2] + ' @%@ '
                name_string = name_string + venue[3] + ' @%@ '
                addr_string = addr_string + venue[4] + ' @%@ '
                

        


        venue = VenueData(trip_id = session.get("trip_id"), venue_id = str(venue_id_string), lattitude = str(lattitude_string), longitude = str(longitude_string), name = str(name_string), address = str(addr_string))

        db.session.add(venue)
        db.session.commit()

        return redirect(url_for('main.route'))

    


@main.route('/route', methods=['POST', 'GET'])
@login_required
def route():

    trip = VenueData.query.filter_by(trip_id= session.get("trip_id")).first()

    # venue_id_list_string = trip.venue_id
    # venue_id_list = list(venue_id_list_string.split(' @%@ '))

    lattitude_list_string = str(trip.lattitude)
    lattitude = list(lattitude_list_string.split(' @%@ '))
    lattitude.pop()

    longitude_list_string = str(trip.longitude)
    longitude = list(longitude_list_string.split(' @%@ '))
    longitude.pop()

    name_list_string = str(trip.name)
    name = list(name_list_string.split(' @%@ '))
    name.pop()


    addr_list_string = str(trip.address)
    addr = list(addr_list_string.split(' @%@ '))
    addr.pop()

    name_addr_list = [sub[item] for item in range(len(addr))
                      for sub in [name, addr]]
    
    
    lattitudeint=[]
    for i in lattitude:
        lattitudeint.append(double(i))
    longitudeint = []
    for i in longitude:
        longitudeint.append(double(i))

    # gmapOne=gmplot.GoogleMapPlotter(19.0760,21.0418,19.9975)
    # gmapOne.scatter(lattitudeint,longitudeint,size=50,marker=False)
    # gmapOne.plot(lattitudeint,longitudeint,'blue',edge_width=2.5)
    # gmapOne.draw("map1.html")
    distance=[]
    n=len(lattitude)
    for i in range(n):
        p=math.sqrt(pow(longitudeint[i],2)+pow(lattitudeint[i],2))
        distance.append(p)
    #print(distance)
    sorted_distance=sorted(distance)
    #print(sorted_distance)
    ans=[]
    for i in sorted_distance:
        ind=distance.index(i)
        ans.append(lattitudeint[ind])
    #print(ans)
    lat1=[]
    long1=[]
    for i in sorted_distance:
        ind=distance.index(i)
        lat1.append(lattitudeint[ind])
        long1.append(longitudeint[ind])



    myTrip = [sub[item] for item in range(len(long1))
                      for sub in [lat1, long1]]

    venue_count = len(myTrip)/2

    session['venue_count'] = venue_count


    user = TripData.query.filter_by(trip_id= session.get("trip_id")).first()


    start_date = user.start_date
    end_date = user.end_date

    syear = int(start_date[0:4])
    smonth = int(start_date[5:7])
    sday = int(start_date[8:10])

    eyear = int(end_date[0:4])
    emonth = int(end_date[5:7])
    eday = int(end_date[8:10])

    date1=date(syear,smonth,sday)
    date2=date(eyear,emonth,eday)


    
    # def suggest_by_train(days_in_hours,dis,mo,day,year):
    #     ans=(dis/55)+venue_count
    #     if ans>days_in_hours:
    #         p=math.ceil((ans-days_in_hours)/24)
    #         print(ans)
    #         print(p)
    #         return "Please Extend Your End Date & the days: "+str(p)+" & "+str(day+p)+"/"+str(mo)+"/"+str(year)
    #     else:
    #         return "Enjoy Your Journey"
    # def suggest_by_bus(days_in_hours,dis,mo,day,year):
    #     ans = (dis / 40) + venue_count
    #     if ans > days_in_hours:
    #         p = math.ceil((ans - days_in_hours) / 24)
    #         print(ans)
    #         print(p)
    #         return "Please Extend Your End Date & the days: "+str(p)+" & "+str(day+p)+"/"+str(mo)+"/"+str(year)
    #     else:
    #         return "Enjoy Your Journey"
    
    


    # print("Days: ",numOfDays(date1,date2))
    days_In_Hours=((date2-date1).days)*(24-13)
    # print("Days in hours: ",days_In_Hours)
    myList = myTrip

    
    cords1=(myList[0],myList[1])
    cords2=(myList[2],myList[3])
    distance=geopy.distance.geodesic(cords1,cords2).km
    for i in range(2,len(myList)-2,2):
        cords1 = (myList[i], myList[i+1])
        cords2 = (myList[i+2], myList[i+3])
        distance += geopy.distance.geodesic(cords1, cords2).km
    # print("Distance: ",distance)
    Sujjetion='car'

    # if Sujjetion=='train':
    #     print(suggest_by_train(days_In_Hours,distance,date2.month,date2.day,date2.year))
    # elif Sujjetion=='bus':
    #     print(suggest_by_bus(days_In_Hours,distance,date2.month,date2.day,date2.year))
    # el

    dis = []

    if Sujjetion=='car':
        # suggest_by_car(days_In_Hours,distance,date2.month,date2.day,date2.year)
        ans = (distance / 48.88) + session.get('venue_count')
        if ans > days_In_Hours:

            p = math.ceil((ans - days_In_Hours) / 24)
            flash("Please Extend Your End Date & the days: "+str(p)+" & "+str(date2.day+p)+"/"+str(date2.month)+"/"+str(date2.year))
            
            return redirect(url_for('main.get_trip_data'))

        else:
            flash("Enjoy your trip !")

            venue_List = name
            print(venue_List)
            client = Client("AC55b49e0375a2402ca28ab2dcb257a394", "f4dec6229835e621e81e875c7f04eaa5")

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
                # li.append("16:00:00")
                Final_hour_list.append(li)
            print("Venuw list : " ,venue_List)
            print("Final_hour_list : " ,Final_hour_list)
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
                # li = []
                for j in range(0,len(i)-1):
                    print(j)
                    li.append(venue_List[k])
                    k=k+1
                Final_venue_list.append(li)
            
            print("Final vinue list : ",Final_venue_list)
            print(Final_hour_list)

            print("final date list : ", Final_date_list)
            for i in range(0,len(Final_date_list)-(numOfDays(date1, date2)-len(Final_hour_list))):
                message=message+"Date: "+str(Final_date_list[i])+"\n"
                time_list=Final_hour_list[i]
                shedule=Final_venue_list[i]
                print(time_list)
                print(shedule)
                for j in range(0,len(time_list)):
                    message=message+"Time: "+str(time_list[j])+" Action: "+str(shedule[j])+"\n"

            print("msg : ",message)

            
            # mob = current_user.user_mob
            # user = User.query.filter_by(user_email=form_email).first()


            client.messages.create(to="+917620695744",
                                from_="+19853317974",
                                body=message)
            #print(curent_date)
            #print(current_time)
            flash("Enjoy Your Journey")    



    # myTrip = [sub[item] for item in range(len(longitude))
    #                   for sub in [lattitude, longitude]]

    # gmapOne=gmplot.GoogleMapPlotter(19.0760,21.0418,19.9975)
    # gmapOne.scatter(lat1,long1,size=50,marker=False)
    # gmapOne.plot(lat1,long1,'blue',edge_width=2.5)
    # gmapOne.draw("map.html")


    # for i in lattitude:
    #     lattitudeint.append(float(i))
    # longitudeint = []
    # for i in longitude:
    #     longitudeint.append(float(i))

    # gmapOne=gmplot.GoogleMapPlotter(19.0760,21.0418,19.9975)
    # gmapOne.scatter(lattitudeint,longitudeint,size=50,marker=False)
    # gmapOne.plot(lattitudeint,longitudeint,'blue',edge_width=2.5)
    # gmapOne.draw("{{url_for('templates', filename = 'map.html')}}")
    # distance=[]
    # n=len(lattitude)
    # for i in range(n):
    #     p=math.sqrt(pow(longitudeint[i],2)+pow(lattitudeint[i],2))
    #     distance.append(p)
    # #print(distance)
    # sorted_distance=sorted(distance)
    # #print(sorted_distance)
    # ans=[]
    # for i in sorted_distance:
    #     ind=distance.index(i)
    #     ans.append(lattitudeint[ind])
    # #print(ans)
    # lat1=[]
    # long1=[]
    # for i in sorted_distance:
    #     ind=distance.index(i)
    #     lat1.append(lattitudeint[ind])
    #     long1.append(longitudeint[ind])
    # gmapOne=gmplot.GoogleMapPlotter(19.0760,21.0418,19.9975)
    # gmapOne.scatter(lat1,long1,size=50,marker=False)
    # gmapOne.plot(lat1,long1,'blue',edge_width=2.5)
    # gmapOne.draw("{{url_for('templates', filename = 'map.html')}}")


    return render_template('map.html', myTrip = myTrip, name_addr_list = name_addr_list)

def numOfDays(date1,date2):
        return (date2-date1).days

def suggest_by_car(days_in_hours,dis,mo,day,year):
        ans = (dis / 48.88) + session.get('venue_count')
        if ans > days_in_hours:
            p = math.ceil((ans - days_in_hours) / 24)
            print(ans)
            print(p)

            flash("Please Extend Your End Date & the days: "+str(p)+" & "+str(day+p)+"/"+str(mo)+"/"+str(year))
            
            return redirect(url_for('main.get_trip_data'))
        else:
            flash("Enjoy your trip !")




# Adding a route for booking page
@main.route('/booking', methods=['POST', 'GET'])
@login_required
def booking():
    return render_template('booking.html')


# Adding a route for profile page
@main.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    return render_template('profile.html', user_firstname=current_user.user_firstname, user_lastname=current_user.user_lastname, user_email=current_user.user_email, user_mob=current_user.user_mob, user_sex=current_user.user_sex)


# Adding a route for update profile page
@main.route('/update_profile')
@login_required
def update_profile():
    return render_template('update_profile.html', user_firstname=current_user.user_firstname, user_lastname=current_user.user_lastname, user_email=current_user.user_email, user_mob=current_user.user_mob)


@main.route('/update_profile', methods=['POST'])
@login_required
def update_profile_post():

    # code collect user data and add it to database goes here
    current_user.user_firstname = request.form.get('input_firstname')
    db.session.commit()
    current_user.user_lastname = request.form.get('input_lastname')
    db.session.commit()
    current_user.user_email = request.form.get('input_email')
    db.session.commit()
    current_user.user_mob = request.form.get('input_mob')
    db.session.commit()
    current_user.user_sex = request.form.get('input_sex')
    db.session.commit()
    return redirect(url_for('main.profile'))


# update password
@main.route('/update_password')
@login_required
def update_password():
    return render_template('update_password.html')


@main.route('/update_password', methods=['POST'])
@login_required
def update_password_post():
    form_new_password = request.form.get('new_password')
    form_confirm_new_password = request.form.get('confirm_new_password')

    if form_new_password == form_confirm_new_password:
        hashed_password = generate_password_hash(
            form_new_password, method='sha256')
        current_user.user_password = hashed_password
        db.session.commit()
        return redirect(url_for('main.profile'))
    else:
        flash("New passwords don't match")
        return redirect(url_for('main.update_password'))

# Adding a route for about us page


@main.route('/about_us', methods=['POST', 'GET'])
@login_required
def about_us():
    return render_template('aboutus.html')

# Adding a route for test page

@main.route('/test')
def test():
    return render_template('test.html')


# Adding a route for 404 page, any unreachable page, will end up redirecting here
@main.errorhandler(404)
def invalid_route():
    return render_template('404.html')
