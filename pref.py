from flask import Blueprint, redirect, render_template, url_for,  request, session
from flask_login import login_required, current_user
from sqlalchemy import delete

from .models import ArtAndEntertainment, CollegeAndUniversity, Event, Food, NightlifeSpot, OutdoorsAndRecreation, ProfessionalAndOtherPlaces, Residence, ShopAndService, TravelAndTransport, User, UserCategory, UserCategoryTrip
from . import db
# from .main import new_trip_id



pref = Blueprint('pref', __name__)


#set a route for rendering template of set preferences
@pref.route('/set_preferences')
@login_required
def set_preferences():
    return render_template('preferences.html')

#set a route to fetch & store data in set preferences
@pref.route('/set_preferences', methods=['POST', 'GET'])
@login_required
def set_preferences_post():

    # A dictionary to store respective category
    user_category_status = {
        "user_id": current_user.user_id,
        "art_and_entertainment": bool(request.form.get('art_and_entertainment')),
        "college_and_university": bool(request.form.get('college_and_university')),
        "event": bool(request.form.get('event')),
        "food": bool(request.form.get('food')),
        "nightlife_spot": bool(request.form.get('nightlife_spot')),
        "outdoors_and_recreation": bool(request.form.get('outdoors_and_recreation')),
        "professional_and_other_places": bool(request.form.get('professional_and_other_places')),
        "residence": bool(request.form.get('residence')),
        "shop_and_service": bool(request.form.get('shop_and_service')),
        "travel_and_transport": bool(request.form.get('travel_and_transport'))
    }

    #check if record exists in respective relation, if yes then remove it
    if UserCategory.query.filter_by(user_id = current_user.user_id).first():
        db.session.execute(delete(UserCategory).where(UserCategory.user_id == current_user.user_id))

    #create new record in respective realtion
    user_category_var = UserCategory(**user_category_status)
    db.session.add(user_category_var)
    db.session.commit()
    
    # A dictionary to store respective category
    if user_category_status["art_and_entertainment"]:

        art_and_entertainment_status = {
            "user_id": current_user.user_id,
            "amphitheater":  bool(request.form.get('amphitheater')),
            "aquarium":  bool(request.form.get('aquarium')),
            "arcade":  bool(request.form.get('arcade')),
            "art_gallery":  bool(request.form.get('art_gallery')),
            "bowling_alley":  bool(request.form.get('bowling_alley')),
            "casino":  bool(request.form.get('casino')),
            "circus":  bool(request.form.get('circus')),
            "comedy_club":  bool(request.form.get('comedy_club')),
            "concert_hall":  bool(request.form.get('concert_hall')),
            "country_dance_club":  bool(request.form.get('country_dance_club')),
            "disc_golf":  bool(request.form.get('disc_golf')),
            "escape_room":  bool(request.form.get('escape_room')),
            "exhibit":  bool(request.form.get('exhibit')),
            "general_entertainment":  bool(request.form.get('general_entertainment')),
            "go_kart_track":  bool(request.form.get('go_kart_track')),
            "historic_site":  bool(request.form.get('historic_site')),
            "karaoke_box":  bool(request.form.get('karaoke_boxs')),
            "laser_tag":  bool(request.form.get('laser_tag')),
            "memorial_site":  bool(request.form.get('memorial_site')),
            "mini_golf":  bool(request.form.get('mini_golf')),
            "movie_theater":  bool(request.form.get('movie_theater')),
            "museum":  bool(request.form.get('museum')),
            "music_venue":  bool(request.form.get('music_venue')),
            "pachinko_parlor":  bool(request.form.get('pachinko_parlor')),
            "performing_arts_venue":  bool(request.form.get('performing_arts_venue')),
            "pool_hall":  bool(request.form.get('pool_hall')),
            "public_art":  bool(request.form.get('public_art')),
            "racecourse":  bool(request.form.get('racecourse')),
            "racetrack":  bool(request.form.get('racetrack')),
            "roller_rink":  bool(request.form.get('roller_rink')),
            "salsa_club":  bool(request.form.get('salsa_club')),
            "samba_school":  bool(request.form.get('samba_school')),
            "stadium":  bool(request.form.get('stadium')),
            "theme_park":  bool(request.form.get('theme_park')),
            "tour_provider":  bool(request.form.get('tour_provider')),
            "vr_cafe":  bool(request.form.get('vr_cafe')),
            "water_park":  bool(request.form.get('water_park')),
            "zoo":  bool(request.form.get('zoo')),

        }


        #check if record exists in respective relation, if yes then remove it
        if ArtAndEntertainment.query.filter_by(user_id = current_user.user_id).first():
            db.session.execute(delete(ArtAndEntertainment).where(ArtAndEntertainment.user_id == current_user.user_id))
        
        #create new record in respective realtion
        db.session.add(ArtAndEntertainment(**art_and_entertainment_status))
        db.session.commit()

    if user_category_status["college_and_university"]:

        # A dictionary to store respective category
        college_and_university_status = {

            "user_id": current_user.user_id,
            "college_academic_building":  bool(request.form.get('college_academic_building')),
            "college_administrative_building":  bool(request.form.get('college_administrative_building')),
            "college_auditorium":  bool(request.form.get('college_auditorium')),
            "college_bookstore":  bool(request.form.get('college_bookstore')),
            "college_cafeteria":  bool(request.form.get('college_cafeteria')),
            "college_classroom":  bool(request.form.get('college_classroom')),
            "college_gym":  bool(request.form.get('college_gym')),
            "college_lab":  bool(request.form.get('college_lab')),
            "college_library":  bool(request.form.get('college_library')),
            "college_quad":  bool(request.form.get('college_quad')),
            "college_rec_center":  bool(request.form.get('college_rec_center')),
            "college_residence_hall":  bool(request.form.get('college_residence_hall')),
            "college_stadium":  bool(request.form.get('college_stadium')),
            "college_theater":  bool(request.form.get('college_theater')),
            "community_college":  bool(request.form.get('community_college')),
            "fraternity_house":  bool(request.form.get('fraternity_house')),
            "general_college_and_university":  bool(request.form.get('general_college_and_university')),
            "law_school":  bool(request.form.get('law_school')),
            "medical_school":  bool(request.form.get('medical_school')),
            "sorority_house":  bool(request.form.get('sorority_house')),
            "student_center":  bool(request.form.get('student_center')),
            "trade_school":  bool(request.form.get('trade_school')),
            "university":  bool(request.form.get('university'))
        }


        #check if record exists in respective relation, if yes then remove it
        if CollegeAndUniversity.query.filter_by(user_id = current_user.user_id).first():
            db.session.execute(delete(CollegeAndUniversity).where(CollegeAndUniversity.user_id == current_user.user_id))
        
        #create new record in respective realtion
        db.session.add(CollegeAndUniversity(**college_and_university_status))
        db.session.commit()


    if user_category_status["event"]:

        # A dictionary to store respective category
        event_status = {
            "user_id": current_user.user_id,
            "christmas_market":  bool(request.form.get('christmas_market')),
            "conference":  bool(request.form.get('conference')),
            "convention":  bool(request.form.get('convention')),
            "festival":  bool(request.form.get('festival')),
            "line_or_queue":  bool(request.form.get('line_or_queue')),
            "music_festival":  bool(request.form.get('music_festival')),
            "other_event":  bool(request.form.get('other_event')),
            "parade":  bool(request.form.get('parade')),
            "sporting_event":  bool(request.form.get('sporting_event')),
            "stoop_sale":  bool(request.form.get('stoop_sale')),
            "street_fair":  bool(request.form.get('street_fair')),
            "trade_fair":  bool(request.form.get('trade_fair'))

        }

        #check if record exists in respective relation, if yes then remove it
        if Event.query.filter_by(user_id = current_user.user_id).first():
            db.session.execute(delete(Event).where(Event.user_id == current_user.user_id))
        
        #create new record in respective realtion
        db.session.add(Event(**event_status))
        db.session.commit()

    if user_category_status["food"]:

        # A dictionary to store respective category
        food_status = {
            "user_id": current_user.user_id,
            "afghan_restaurant":  bool(request.form.get('afghan_restaurant')),
            "african_restaurant":  bool(request.form.get('african_restaurant')),
            "american_restaurant":  bool(request.form.get('american_restaurant')),
            "armenian_restaurant":  bool(request.form.get('armenian_restaurant')),
            "asian_restaurant":  bool(request.form.get('asian_restaurant')),
            "australian_restaurant":  bool(request.form.get('australian_restaurant')),
            "austrian_restaurant":  bool(request.form.get('austrian_restaurant')),
            "bbq_joint":  bool(request.form.get('bbq_joint')),
            "bagel_shop":  bool(request.form.get('bagel_shop')),
            "bakery":  bool(request.form.get('bakery')),
            "bangladeshi_restaurant":  bool(request.form.get('bangladeshi_restaurant')),
            "belgian_restaurant":  bool(request.form.get('belgian_restaurant')),
            "bistro":  bool(request.form.get('bistro')),
            "breakfast_spot":  bool(request.form.get('breakfast_spot')),
            "bubble_tea_shop":  bool(request.form.get('bubble_tea_shop')),
            "buffet":  bool(request.form.get('buffet')),
            "burger_joint":  bool(request.form.get('burger_joint')),
            "cafeteria":  bool(request.form.get('cafeteria')),
            "café":  bool(request.form.get('café')),
            "cajun_or_creole_restaurant":  bool(request.form.get('cajun_or_creole_restaurant')),
            "caribbean_restaurant":  bool(request.form.get('caribbean_restaurant')),
            "caucasian_restaurant":  bool(request.form.get('caucasian_restaurant')),
            "coffee_shop":  bool(request.form.get('coffee_shop')),
            "comfort_food_restaurant":  bool(request.form.get('comfort_food_restaurant')),
            "creperie":  bool(request.form.get('creperie')),
            "czech_restaurant":  bool(request.form.get('czech_restaurant')),
            "deli_or_bodega":  bool(request.form.get('deli_or_bodega')),
            "dessert_shop":  bool(request.form.get('dessert_shop')),
            "diner":  bool(request.form.get('diner')),
            "donut_shop":  bool(request.form.get('donut_shop')),
            "dumpling_restaurant":  bool(request.form.get('dumpling_restaurant')),
            "dutch_restaurant":  bool(request.form.get('dutch_restaurant')),
            "eastern_european_restaurant":  bool(request.form.get('eastern_european_restaurant')),
            "english_restaurant":  bool(request.form.get('english_restaurant')),
            "falafel_restaurant":  bool(request.form.get('falafel_restaurant')),
            "fast_food_restaurant":  bool(request.form.get('fast_food_restaurant')),
            "fish_and_chips_shop":  bool(request.form.get('fish_and_chips_shop')),
            "fondue_restaurant":  bool(request.form.get('fondue_restaurant')),
            "food_court":  bool(request.form.get('food_court')),
            "food_stand":  bool(request.form.get('food_stand')),
            "food_truck":  bool(request.form.get('food_truck')),
            "french_restaurant":  bool(request.form.get('french_restaurant')),
            "fried_chicken_joint":  bool(request.form.get('fried_chicken_joint')),
            "friterie":  bool(request.form.get('friterie')),
            "gastropub":  bool(request.form.get('gastropub')),
            "german_restaurant":  bool(request.form.get('german_restaurant')),
            "greek_restaurant":  bool(request.form.get('greek_restaurant')),
            "halal_restaurant":  bool(request.form.get('halal_restaurant')),
            "hawaiian_restaurant":  bool(request.form.get('hawaiian_restaurant')),
            "hot_dog_joint":  bool(request.form.get('hot_dog_joint')),
            "hungarian_restaurant":  bool(request.form.get('hungarian_restaurant')),
            "indian_restaurant":  bool(request.form.get('indian_restaurant')),
            "irish_pub":  bool(request.form.get('irish_pub')),
            "italian_restaurant":  bool(request.form.get('italian_restaurant')),
            "jewish_restaurant":  bool(request.form.get('jewish_restaurant')),
            "juice_bar":  bool(request.form.get('juice_bar')),
            "kebab_restaurant":  bool(request.form.get('kebab_restaurant')),
            "latin_american_restaurant":  bool(request.form.get('latin_american_restaurant')),
            "mac_and_cheese_joint":  bool(request.form.get('mac_and_cheese_joint')),
            "mediterranean_restaurant":  bool(request.form.get('mediterranean_restaurant')),
            "mexican_restaurant":  bool(request.form.get('mexican_restaurant')),
            "middle_eastern_restaurant":  bool(request.form.get('middle_eastern_restaurant')),
            "modern_european_restaurant":  bool(request.form.get('modern_european_restaurant')),
            "molecular_gastronomy_restaurant":  bool(request.form.get('molecular_gastronomy_restaurant')),
            "pakistani_restaurant":  bool(request.form.get('pakistani_restaurant')),
            "pet_café":  bool(request.form.get('pet_café')),
            "pizza_place":  bool(request.form.get('pizza_place')),
            "polish_restaurant":  bool(request.form.get('polish_restaurant')),
            "portuguese_restaurant":  bool(request.form.get('portuguese_restaurant')),
            "poutine_place":  bool(request.form.get('poutine_place')),
            "restaurant":  bool(request.form.get('restaurant')),
            "russian_restaurant":  bool(request.form.get('russian_restaurant')),
            "salad_place":  bool(request.form.get('salad_place')),
            "sandwich_place":  bool(request.form.get('sandwich_place')),
            "scandinavian_restaurant":  bool(request.form.get('scandinavian_restaurant')),
            "scottish_restaurant":  bool(request.form.get('scottish_restaurant')),
            "seafood_restaurant":  bool(request.form.get('seafood_restaurant')),
            "slovak_restaurant":  bool(request.form.get('slovak_restaurant')),
            "snack_place":  bool(request.form.get('snack_place')),
            "soup_place":  bool(request.form.get('snack_place')),
            "southern_or_soul_food_restaurant":  bool(request.form.get('southern_or_soul_food_restaurant')),
            "spanish_restaurant":  bool(request.form.get('spanish_restaurant')),
            "sri_lankan_restaurant":  bool(request.form.get('sri_lankan_restaurant')),
            "steakhouse":  bool(request.form.get('steakhouse')),
            "swiss_restaurant":  bool(request.form.get('swiss_restaurant')),
            "tea_room":  bool(request.form.get('tea_room')),
            "theme_restaurant":  bool(request.form.get('theme_restaurant')),
            "turkish_restaurant":  bool(request.form.get('turkish_restaurant')),
            "ukrainian_restaurant":  bool(request.form.get('ukrainian_restaurant')),
            "vegetarian_or_vegan_restaurant":  bool(request.form.get('vegetarian_or_vegan_restaurant')),
            "wings_joint":  bool(request.form.get('wings_joint'))

        }

        #check if record exists in respective relation, if yes then remove it
        if Food.query.filter_by(user_id = current_user.user_id).first():
            db.session.execute(delete(Food).where(Food.user_id == current_user.user_id))
        
        #create new record in respective realtion
        db.session.add(Food(**food_status))
        db.session.commit()

    if user_category_status["nightlife_spot"]:

        # A dictionary to store respective category
        nightlife_spot_status = {
            "user_id": current_user.user_id,
            "bar":  bool(request.form.get('bar')),
            "brewery":  bool(request.form.get('brewery')),
            "lounge":  bool(request.form.get('lounge')),
            "night_market":  bool(request.form.get('night_market')),
            "nightclub":  bool(request.form.get('nightclub')),
            "other_nightlife":  bool(request.form.get('other_nightlife')),
            "strip_club":  bool(request.form.get('strip_club'))

        }

        #check if record exists in respective relation, if yes then remove it
        if NightlifeSpot.query.filter_by(user_id=current_user.user_id).first():
            db.session.execute(delete(NightlifeSpot).where(
                NightlifeSpot.user_id == current_user.user_id))

        #create new record in respective realtion
        db.session.add(NightlifeSpot(**nightlife_spot_status))
        db.session.commit()

    if user_category_status["outdoors_and_recreation"]:

        # A dictionary to store respective category
        outdoors_and_recreation_status = {
            "user_id": current_user.user_id,
            "athletics_and_sports":  bool(request.form.get('athletics_and_sports')),
            "bathing_area":  bool(request.form.get('bathing_area')),
            "bay":  bool(request.form.get('bay')),
            "beach":  bool(request.form.get('beach')),
            "bike_trail":  bool(request.form.get('bike_trail')),
            "boat_launch":  bool(request.form.get('boat_launch')),
            "botanical_garden":  bool(request.form.get('botanical_garden')),
            "bridge":  bool(request.form.get('bridge')),
            "campground":  bool(request.form.get('campground')),
            "canal_lock":  bool(request.form.get('canal_lock')),
            "canal":  bool(request.form.get('canal')),
            "castle":  bool(request.form.get('castle')),
            "cave":  bool(request.form.get('cave')),
            "cemetery":  bool(request.form.get('cemetery')),
            "dam":  bool(request.form.get('dam')),
            "dive_spot":  bool(request.form.get('dive_spot')),
            "dog_run":  bool(request.form.get('dog_run')),
            "farm":  bool(request.form.get('farm')),
            "field":  bool(request.form.get('field')),
            "fishing_spot":  bool(request.form.get('fishing_spot')),
            "forest":  bool(request.form.get('forest')),
            "fountain":  bool(request.form.get('fountain')),
            "garden":  bool(request.form.get('garden')),
            "gun_range":  bool(request.form.get('gun_range')),
            "harbor_or_marina":  bool(request.form.get('harbor_or_marina')),
            "hill":  bool(request.form.get('hill')),
            "hot_spring":  bool(request.form.get('hot_spring')),
            "indoor_play_area":  bool(request.form.get('indoor_play_area')),
            "island":  bool(request.form.get('island')),
            "lake":  bool(request.form.get('lake')),
            "lighthouse":  bool(request.form.get('lighthouse')),
            "mountain_hut":  bool(request.form.get('mountain_hut')),
            "mountain":  bool(request.form.get('mountain')),
            "national_park":  bool(request.form.get('national_park')),
            "nature_preserve":  bool(request.form.get('nature_preserve')),
            "other_great_outdoors":  bool(request.form.get('other_great_outdoors')),
            "palace":  bool(request.form.get('palace')),
            "park":  bool(request.form.get('park')),
            "pedestrian_plaza":  bool(request.form.get('pedestrian_plaza')),
            "picnic_area":  bool(request.form.get('picnic_area')),
            "picnic_shelter":  bool(request.form.get('picnic_shelter')),
            "playground":  bool(request.form.get('playground')),
            "plaza":  bool(request.form.get('plaza')),
            "pool":  bool(request.form.get('pool')),
            "rafting":  bool(request.form.get('rafting')),
            "recreation_center":  bool(request.form.get('recreation_center')),
            "reservoir":  bool(request.form.get('reservoir')),
            "river":  bool(request.form.get('river')),
            "rock_climbing_spot":  bool(request.form.get('rock_climbing_spot')),
            "roof_deck":  bool(request.form.get('roof_deck')),
            "scenic_lookout":  bool(request.form.get('scenic_lookout')),
            "sculpture_garden":  bool(request.form.get('sculpture_garden')),
            "ski_area":  bool(request.form.get('ski_area')),
            "skydiving_drop_zone":  bool(request.form.get('skydiving_drop_zone')),
            "stables":  bool(request.form.get('stables')),
            "state_or_provincial_park":  bool(request.form.get('state_or_provincial_park')),
            "states_and_municipalities":  bool(request.form.get('states_and_municipalities')),
            "summer_camp":  bool(request.form.get('summer_camp')),
            "trail":  bool(request.form.get('trail')),
            "tree":  bool(request.form.get('tree')),
            "vineyard":  bool(request.form.get('vineyard')),
            "volcano":  bool(request.form.get('volcano')),
            "waterfall":  bool(request.form.get('waterfall')),
            "waterfront":  bool(request.form.get('waterfront')),
            "well":  bool(request.form.get('well')),
            "windmill":  bool(request.form.get('windmill'))

        }


        #check if record exists in respective relation, if yes then remove it
        if OutdoorsAndRecreation.query.filter_by(user_id = current_user.user_id).first():
            db.session.execute(delete(OutdoorsAndRecreation).where(OutdoorsAndRecreation.user_id == current_user.user_id))
        
        #create new record in respective realtion
        db.session.add(OutdoorsAndRecreation(**outdoors_and_recreation_status))
        db.session.commit()

    if user_category_status["professional_and_other_places"]:

        # A dictionary to store respective category
        professional_and_other_places_status = {
            "user_id": current_user.user_id,
            "animal_shelter":  bool(request.form.get('animal_shelter')),
            "architecture_firm":  bool(request.form.get('architecture_firm')),
            "art_studio":  bool(request.form.get('art_studio')),
            "auditorium":  bool(request.form.get('auditorium')),
            "ballroom":  bool(request.form.get('ballroom')),
            "building":  bool(request.form.get('building')),
            "business_center":  bool(request.form.get('business_center')),
            "cidery":  bool(request.form.get('cidery')),
            "club_house":  bool(request.form.get('club_house')),
            "community_center":  bool(request.form.get('community_center')),
            "convention_center":  bool(request.form.get('convention_cente')),
            "cultural_center":  bool(request.form.get('cultural_center')),
            "distillery":  bool(request.form.get('distillery')),
            "distribution_center":  bool(request.form.get('distribution_center')),
            "event_space":  bool(request.form.get('event_space')),
            "factory":  bool(request.form.get('factory')),
            "fair":  bool(request.form.get('fair')),
            "funeral_home":  bool(request.form.get('funeral_home')),
            "government_building":  bool(request.form.get('government_building')),
            "industrial_estate":  bool(request.form.get('industrial_estate')),
            "library":  bool(request.form.get('library')),
            "meadery":  bool(request.form.get('meadery')),
            "medical_center":  bool(request.form.get('medical_center')),
            "military_base":  bool(request.form.get('military_base')),
            "non_profit":  bool(request.form.get('non_profit')),
            "observatory":  bool(request.form.get('observatory')),
            "office":  bool(request.form.get('office')),
            "parking":  bool(request.form.get('parking')),
            "post_office":  bool(request.form.get('post_office')),
            "power_plant":  bool(request.form.get('power_plant')),
            "prison":  bool(request.form.get('prison')),
            "radio_station":  bool(request.form.get('radio_station')),
            "recruiting_agency":  bool(request.form.get('recruiting_agency')),
            "research_laboratory":  bool(request.form.get('research_laboratory')),
            "research_station":  bool(request.form.get('research_station')),
            "school":  bool(request.form.get('school')),
            "social_club":  bool(request.form.get('social_club')),
            "spiritual_center":  bool(request.form.get('spiritual_center')),
            "tv_station":  bool(request.form.get('tv_station')),
            "voting_booth":  bool(request.form.get('voting_booth')),
            "warehouse":  bool(request.form.get('warehouse')),
            "waste_facility":  bool(request.form.get('waste_facility')),
            "wedding_hall":  bool(request.form.get('wedding_hall')),
            "winery":  bool(request.form.get('winery'))

        }

        #check if record exists in respective relation, if yes then remove it
        if ProfessionalAndOtherPlaces.query.filter_by(user_id = current_user.user_id).first():
            db.session.execute(delete(ProfessionalAndOtherPlaces).where(ProfessionalAndOtherPlaces.user_id == current_user.user_id))
        
        #create new record in respective realtion
        db.session.add(ProfessionalAndOtherPlaces(**professional_and_other_places_status))
        db.session.commit()


    if user_category_status["residence"]:
        
        # A dictionary to store respective category
        residence_status = {
            "user_id" : current_user.user_id,
            "assisted_living"  :    bool(request.form.get('assisted_living')),
            "home_private"  :    bool(request.form.get('home_private')),
            "housing_development"  :    bool(request.form.get('housing_development')),
            "residential_building_apartment_or_condo"  :    bool(request.form.get('residential_building_apartment_or_condo')),
            "trailer_park"  :    bool(request.form.get('trailer_park'))

        }

        #check if record exists in respective relation, if yes then remove it
        if Residence.query.filter_by(user_id = current_user.user_id).first():
            db.session.execute(delete(Residence).where(Residence.user_id == current_user.user_id))
        
        #create new record in respective realtion
        db.session.add(Residence(**residence_status))
        db.session.commit()

    if user_category_status["shop_and_service"]:

        # A dictionary to store respective category
        shop_and_service_status = {
            "user_id": current_user.user_id,
            "atm":    bool(request.form.get('atm')),
            "adult_boutique":    bool(request.form.get('adult_boutique')),
            "antique_shop":    bool(request.form.get('antique_shop')),
            "arts_and_crafts_store":    bool(request.form.get('arts_and_crafts_store')),
            "astrologer":    bool(request.form.get('astrologer')),
            "auto_dealership":    bool(request.form.get('auto_dealership')),
            "auto_garage":    bool(request.form.get('auto_garage')),
            "auto_workshop":    bool(request.form.get('auto_workshop')),
            "automotive_shop":    bool(request.form.get('automotive_shop')),
            "baby_store":    bool(request.form.get('baby_store')),
            "bank":    bool(request.form.get('bank')),
            "bath_house":    bool(request.form.get('bath_house')),
            "batik_shop":    bool(request.form.get('batik_shop')),
            "betting_shop":    bool(request.form.get('betting_shop')),
            "big_box_store":    bool(request.form.get('big_box_store')),
            "bike_shop":    bool(request.form.get('bike_shop')),
            "board_shop":    bool(request.form.get('board_shop')),
            "bookstore":    bool(request.form.get('bookstore')),
            "bridal_shop":    bool(request.form.get('bridal_shop')),
            "business_service":    bool(request.form.get('business_service')),
            "camera_store":    bool(request.form.get('camera_store')),
            "candy_store":    bool(request.form.get('candy_store')),
            "car_wash":    bool(request.form.get('car_wash')),
            "carpet_store":    bool(request.form.get('carpet_store')),
            "check_cashing_service":    bool(request.form.get('check_cashing_service')),
            "child_care_service":    bool(request.form.get('child_care_service')),
            "chocolate_shop":    bool(request.form.get('chocolate_shop')),
            "clothing_store":    bool(request.form.get('clothing_store')),
            "comic_shop":    bool(request.form.get('comic_shop')),
            "construction_and_landscaping":    bool(request.form.get('construction_and_landscaping')),
            "convenience_store":    bool(request.form.get('convenience_store')),
            "cosmetics_shop":    bool(request.form.get('cosmetics_shop')),
            "costume_shop":    bool(request.form.get('costume_shop')),
            "credit_union":    bool(request.form.get('credit_union')),
            "currency_exchange":    bool(request.form.get('currency_exchange')),
            "department_store":    bool(request.form.get('department_store')),
            "design_studio":    bool(request.form.get('design_studio')),
            "discount_store":    bool(request.form.get('discount_store')),
            "dive_shop":    bool(request.form.get('dive_shop')),
            "drugstore":    bool(request.form.get('drugstore')),
            "dry_cleaner":    bool(request.form.get('dry_cleaner')),
            "ev_charging_station":    bool(request.form.get('ev_charging_station')),
            "electronics_store":    bool(request.form.get('electronics_store')),
            "entertainment_service":    bool(request.form.get('entertainment_service')),
            "event_service":    bool(request.form.get('event_service')),
            "fabric_shop":    bool(request.form.get('fabric_shop')),
            "film_studio":    bool(request.form.get('film_studio')),
            "financial_or_legal_service":    bool(request.form.get('financial_or_legal_service')),
            "fireworks_store":    bool(request.form.get('fireworks_store')),
            "fishing_store":    bool(request.form.get('fishing_store')),
            "flea_market":    bool(request.form.get('flea_market')),
            "floating_market":    bool(request.form.get('floating_market')),
            "flower_shop":    bool(request.form.get('flower_shop')),
            "food_and_drink_shop":    bool(request.form.get('food_and_drink_shop')),
            "frame_store":    bool(request.form.get('frame_store')),
            "fruit_and_vegetable_store":    bool(request.form.get('fruit_and_vegetable_store')),
            "furniture_or_home_store":    bool(request.form.get('furniture_or_home_store')),
            "gaming_cafe":    bool(request.form.get('gaming_cafe')),
            "garden_center":    bool(request.form.get('garden_center')),
            "gas_station":    bool(request.form.get('gas_station')),
            "gift_shop":    bool(request.form.get('gift_shop')),
            "gun_shop":    bool(request.form.get('gun_shop')),
            "hardware_store":    bool(request.form.get('hardware_store')),
            "health_and_beauty_service":    bool(request.form.get('health_and_beauty_service')),
            "herbs_and_spices_store":    bool(request.form.get('herbs_and_spices_store')),
            "hobby_shop":    bool(request.form.get('hobby_shop')),
            "home_service":    bool(request.form.get('home_service')),
            "hunting_supply":    bool(request.form.get('hunting_supply')),
            "it_services":    bool(request.form.get('it_services')),
            "insurance_office":    bool(request.form.get('insurance_office')),
            "internet_cafe":    bool(request.form.get('internet_cafe')),
            "jewelry_store":    bool(request.form.get('jewelry_store')),
            "kitchen_supply_store":    bool(request.form.get('kitchen_supply_store')),
            "knitting_store":    bool(request.form.get('knitting_store')),
            "laundromat":    bool(request.form.get('laundromat')),
            "laundry_service":    bool(request.form.get('laundry_service')),
            "lawyer":    bool(request.form.get('lawyer')),
            "leather_goods_store":    bool(request.form.get('leather_goods_store')),
            "locksmith":    bool(request.form.get('locksmith')),
            "lottery_retailer":    bool(request.form.get('lottery_retailer')),
            "luggage_store":    bool(request.form.get('luggage_store')),
            "marijuana_dispensary":    bool(request.form.get('marijuana_dispensary')),
            "market":    bool(request.form.get('market')),
            "massage_studio":    bool(request.form.get('massage_studio')),
            "mattress_store":    bool(request.form.get('mattress_store')),
            "medical_supply_store":    bool(request.form.get('medical_supply_store')),
            "miscellaneous_shop":    bool(request.form.get('miscellaneous_shop')),
            "mobile_phone_shop":    bool(request.form.get('mobile_phone_shop')),
            "mobility_store":    bool(request.form.get('mobility_store')),
            "motorcycle_shop":    bool(request.form.get('motorcycle_shop')),
            "motorsports_shop":    bool(request.form.get('motorsports_shop')),
            "music_store":    bool(request.form.get('music_store')),
            "nail_salon":    bool(request.form.get('nail_salon')),
            "newsagent":    bool(request.form.get('newsagent')),
            "newsstand":    bool(request.form.get('newsstand')),
            "notary":    bool(request.form.get('notary')),
            "optical_shop":    bool(request.form.get('optical_shop')),
            "other_repair_shop":    bool(request.form.get('other_repair_shop')),
            "outdoor_supply_store":    bool(request.form.get('outdoor_supply_store')),
            "outlet_mall":    bool(request.form.get('outlet_mall')),
            "outlet_store":    bool(request.form.get('outlet_store')),
            "paper_or_office_supplies_store":    bool(request.form.get('paper_or_office_supplies_store')),
            "pawn_shop":    bool(request.form.get('pawn_shop')),
            "perfume_shop":    bool(request.form.get('perfume_shop')),
            "pet_service":    bool(request.form.get('pet_service')),
            "pet_store":    bool(request.form.get('pet_store')),
            "pharmacy":    bool(request.form.get('pharmacy')),
            "photography_lab":    bool(request.form.get('photography_lab')),
            "photography_studio":    bool(request.form.get('photography_studio')),
            "piercing_parlor":    bool(request.form.get('piercing_parlor')),
            "pop_up_shop":    bool(request.form.get('pop_up_shop')),
            "print_shop":    bool(request.form.get('print_shop')),
            "public_bathroom":    bool(request.form.get('public_bathroom')),
            "real_estate_office":    bool(request.form.get('real_estate_office')),
            "record_shop":    bool(request.form.get('record_shop')),
            "recording_studio":    bool(request.form.get('recording_studio')),
            "recycling_facility":    bool(request.form.get('recycling_facility')),
            "rental_service":    bool(request.form.get('rental_service')),
            "salon_or_barbershop":    bool(request.form.get('salon_or_barbershop')),
            "sauna_or_steam_room":    bool(request.form.get('sauna_or_steam_room')),
            "shipping_store":    bool(request.form.get('shipping_store')),
            "shoe_repair":    bool(request.form.get('shoe_repair')),
            "shopping_mall":    bool(request.form.get('shopping_mall')),
            "shopping_plaza":    bool(request.form.get('shopping_plaza')),
            "skate_shop":    bool(request.form.get('skate_shop')),
            "ski_shop":    bool(request.form.get('ski_shop')),
            "smoke_shop":    bool(request.form.get('smoke_shop')),
            "smoothie_shop":    bool(request.form.get('smoothie_shop')),
            "souvenir_shop":    bool(request.form.get('souvenir_shop')),
            "spa":    bool(request.form.get('spa')),
            "sporting_goods_shop":    bool(request.form.get('sporting_goods_shop')),
            "stationery_store":    bool(request.form.get('stationery_store')),
            "storage_facility":    bool(request.form.get('storage_facility')),
            "supplement_shop":    bool(request.form.get('supplement_shop')),
            "tailor_shop":    bool(request.form.get('tailor_shop')),
            "tanning_salon":    bool(request.form.get('tanning_salon')),
            "tattoo_parlor":    bool(request.form.get('tattoo_parlor')),
            "thrift_or_vintage_store":    bool(request.form.get('thrift_or_vintage_store')),
            "toy_or_game_store":    bool(request.form.get('toy_or_game_store')),
            "travel_agency":    bool(request.form.get('travel_agency')),
            "used_bookstore":    bool(request.form.get('used_bookstore')),
            "vape_store":    bool(request.form.get('vape_store')),
            "vehicle_inspection_station":    bool(request.form.get('vehicle_inspection_station')),
            "video_game_store":    bool(request.form.get('video_game_store')),
            "video_store":    bool(request.form.get('video_store')),
            "warehouse_store":    bool(request.form.get('warehouse_store')),
            "watch_shop":    bool(request.form.get('watch_shop'))

        }

        #check if record exists in respective relation, if yes then remove it
        if ShopAndService.query.filter_by(user_id = current_user.user_id).first():
            db.session.execute(delete(ShopAndService).where(ShopAndService.user_id == current_user.user_id))
        
        #create new record in respective realtion
        db.session.add(ShopAndService(**shop_and_service_status))
        db.session.commit()

    if user_category_status["travel_and_transport"]:

        # A dictionary to store respective category
        travel_and_transport_status = {
            "user_id": current_user.user_id,
            "airport":    bool(request.form.get('airport')),
            "baggage_locker":    bool(request.form.get('baggage_locker')),
            "bike_rental_or_bike_share":    bool(request.form.get('bike_rental_or_bike_share')),
            "boat_rental":    bool(request.form.get('boat_rental')),
            "boat_or_ferry":    bool(request.form.get('boat_or_ferry')),
            "border_crossing":    bool(request.form.get('border_crossing')),
            "bus_station":    bool(request.form.get('bus_station')),
            "bus_stop":    bool(request.form.get('bus_stop')),
            "cable_car":    bool(request.form.get('cable_car')),
            "cruise_ship":    bool(request.form.get('cruise_ship')),
            "duty_free_shop":    bool(request.form.get('duty_free_shop')),
            "general_travel":    bool(request.form.get('general_travel')),
            "heliport":    bool(request.form.get('heliport')),
            "hotel":    bool(request.form.get('hotel')),
            "intersection":    bool(request.form.get('intersection')),
            "light_rail_station":    bool(request.form.get('light_rail_station')),
            "marine_terminal":    bool(request.form.get('marine_terminal')),
            "metro_station":    bool(request.form.get('metro_station')),
            "moving_target":    bool(request.form.get('moving_target')),
            "pier":    bool(request.form.get('pier')),
            "port":    bool(request.form.get('port')),
            "rv_park":    bool(request.form.get('rv_park')),
            "rental_car_location":    bool(request.form.get('rental_car_location')),
            "rest_area":    bool(request.form.get('rest_area')),
            "road":    bool(request.form.get('road')),
            "taxi_stand":    bool(request.form.get('taxi_stand')),
            "taxi":    bool(request.form.get('taxi')),
            "toll_booth":    bool(request.form.get('toll_booth')),
            "toll_plaza":    bool(request.form.get('toll_plaza')),
            "tourist_information_center":    bool(request.form.get('tourist_information_center')),
            "train_station":    bool(request.form.get('train_station')),
            "tram_station":    bool(request.form.get('tram_station')),
            "transportation_service":    bool(request.form.get('transportation_service')),
            "travel_lounge":    bool(request.form.get('travel_lounge')),
            "truck_stop":    bool(request.form.get('truck_stop')),
            "tunnel":    bool(request.form.get('tunnel'))

        }


        #check if record exists in respective relation, if yes then remove it
        if TravelAndTransport.query.filter_by(user_id = current_user.user_id).first():
            db.session.execute(delete(TravelAndTransport).where(TravelAndTransport.user_id == current_user.user_id))
        
        #create new record in respective realtion
        db.session.add(TravelAndTransport(**travel_and_transport_status))
        db.session.commit()

    return redirect(url_for('main.profile'))






###########################################################################################################################################################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
###########################################################################################################################################################







# Adding a route for trip preferences page
@pref.route('/trip_preferences', methods=['POST', 'GET'])
@login_required
def trip_preferences():

    if request.method == "POST":
        # if session['trip_id']:
        #     trip_id = session['trip_id']
        # else:
        trip_id = session.get("trip_id")

        # A dictionary to store respective category
        user_category_trip_status = {
            "user_id": current_user.user_id,
            "trip_id": trip_id,
            "art_and_entertainment": bool(request.form.get('art_and_entertainment')),
            "college_and_university": bool(request.form.get('college_and_university')),
            "event": bool(request.form.get('event')),
            "food": bool(request.form.get('food')),
            "nightlife_spot": bool(request.form.get('nightlife_spot')),
            "outdoors_and_recreation": bool(request.form.get('outdoors_and_recreation')),
            "professional_and_other_places": bool(request.form.get('professional_and_other_places')),
            "residence": bool(request.form.get('residence')),
            "shop_and_service": bool(request.form.get('shop_and_service')),
            "travel_and_transport": bool(request.form.get('travel_and_transport'))
        }

        #check if record exists in respective relation, if yes then remove it
        if UserCategoryTrip.query.filter_by(trip_id = trip_id).first():
            db.session.execute(delete(UserCategoryTrip).where(UserCategoryTrip.trip_id == trip_id))

        #create new record in respective realtion
        user_category_trip_var = UserCategoryTrip(**user_category_trip_status)
        db.session.add(user_category_trip_var)
        db.session.commit()
        
        # A dictionary to store respective category
        if user_category_trip_status["art_and_entertainment"]:

            art_and_entertainment_trip_status = {
                "user_id": current_user.user_id,
                "amphitheater":  bool(request.form.get('amphitheater')),
                "aquarium":  bool(request.form.get('aquarium')),
                "arcade":  bool(request.form.get('arcade')),
                "art_gallery":  bool(request.form.get('art_gallery')),
                "bowling_alley":  bool(request.form.get('bowling_alley')),
                "casino":  bool(request.form.get('casino')),
                "circus":  bool(request.form.get('circus')),
                "comedy_club":  bool(request.form.get('comedy_club')),
                "concert_hall":  bool(request.form.get('concert_hall')),
                "country_dance_club":  bool(request.form.get('country_dance_club')),
                "disc_golf":  bool(request.form.get('disc_golf')),
                "escape_room":  bool(request.form.get('escape_room')),
                "exhibit":  bool(request.form.get('exhibit')),
                "general_entertainment":  bool(request.form.get('general_entertainment')),
                "go_kart_track":  bool(request.form.get('go_kart_track')),
                "historic_site":  bool(request.form.get('historic_site')),
                "karaoke_box":  bool(request.form.get('karaoke_boxs')),
                "laser_tag":  bool(request.form.get('laser_tag')),
                "memorial_site":  bool(request.form.get('memorial_site')),
                "mini_golf":  bool(request.form.get('mini_golf')),
                "movie_theater":  bool(request.form.get('movie_theater')),
                "museum":  bool(request.form.get('museum')),
                "music_venue":  bool(request.form.get('music_venue')),
                "pachinko_parlor":  bool(request.form.get('pachinko_parlor')),
                "performing_arts_venue":  bool(request.form.get('performing_arts_venue')),
                "pool_hall":  bool(request.form.get('pool_hall')),
                "public_art":  bool(request.form.get('public_art')),
                "racecourse":  bool(request.form.get('racecourse')),
                "racetrack":  bool(request.form.get('racetrack')),
                "roller_rink":  bool(request.form.get('roller_rink')),
                "salsa_club":  bool(request.form.get('salsa_club')),
                "samba_school":  bool(request.form.get('samba_school')),
                "stadium":  bool(request.form.get('stadium')),
                "theme_park":  bool(request.form.get('theme_park')),
                "tour_provider":  bool(request.form.get('tour_provider')),
                "vr_cafe":  bool(request.form.get('vr_cafe')),
                "water_park":  bool(request.form.get('water_park')),
                "zoo":  bool(request.form.get('zoo')),

            }


            #check if record exists in respective relation, if yes then remove it
            # if ArtAndEntertainment.query.filter_by(user_id = current_user.user_id).first():
            #     db.session.execute(delete(ArtAndEntertainment).where(ArtAndEntertainment.user_id == current_user.user_id))
            
            # #create new record in respective realtion
            # db.session.add(ArtAndEntertainment(**art_and_entertainment_status))
            # db.session.commit()

        if user_category_trip_status["college_and_university"]:

            # A dictionary to store respective category
            college_and_university_trip_status = {

                "user_id": current_user.user_id,
                "college_academic_building":  bool(request.form.get('college_academic_building')),
                "college_administrative_building":  bool(request.form.get('college_administrative_building')),
                "college_auditorium":  bool(request.form.get('college_auditorium')),
                "college_bookstore":  bool(request.form.get('college_bookstore')),
                "college_cafeteria":  bool(request.form.get('college_cafeteria')),
                "college_classroom":  bool(request.form.get('college_classroom')),
                "college_gym":  bool(request.form.get('college_gym')),
                "college_lab":  bool(request.form.get('college_lab')),
                "college_library":  bool(request.form.get('college_library')),
                "college_quad":  bool(request.form.get('college_quad')),
                "college_rec_center":  bool(request.form.get('college_rec_center')),
                "college_residence_hall":  bool(request.form.get('college_residence_hall')),
                "college_stadium":  bool(request.form.get('college_stadium')),
                "college_theater":  bool(request.form.get('college_theater')),
                "community_college":  bool(request.form.get('community_college')),
                "fraternity_house":  bool(request.form.get('fraternity_house')),
                "general_college_and_university":  bool(request.form.get('general_college_and_university')),
                "law_school":  bool(request.form.get('law_school')),
                "medical_school":  bool(request.form.get('medical_school')),
                "sorority_house":  bool(request.form.get('sorority_house')),
                "student_center":  bool(request.form.get('student_center')),
                "trade_school":  bool(request.form.get('trade_school')),
                "university":  bool(request.form.get('university'))
            }


            # #check if record exists in respective relation, if yes then remove it
            # if CollegeAndUniversity.query.filter_by(user_id = current_user.user_id).first():
            #     db.session.execute(delete(CollegeAndUniversity).where(CollegeAndUniversity.user_id == current_user.user_id))
            
            # #create new record in respective realtion
            # db.session.add(CollegeAndUniversity(**college_and_university_status))
            # db.session.commit()


        if user_category_trip_status["event"]:

            # A dictionary to store respective category
            event_trip_status = {
                "user_id": current_user.user_id,
                "christmas_market":  bool(request.form.get('christmas_market')),
                "conference":  bool(request.form.get('conference')),
                "convention":  bool(request.form.get('convention')),
                "festival":  bool(request.form.get('festival')),
                "line_or_queue":  bool(request.form.get('line_or_queue')),
                "music_festival":  bool(request.form.get('music_festival')),
                "other_event":  bool(request.form.get('other_event')),
                "parade":  bool(request.form.get('parade')),
                "sporting_event":  bool(request.form.get('sporting_event')),
                "stoop_sale":  bool(request.form.get('stoop_sale')),
                "street_fair":  bool(request.form.get('street_fair')),
                "trade_fair":  bool(request.form.get('trade_fair'))

            }

            # #check if record exists in respective relation, if yes then remove it
            # if Event.query.filter_by(user_id = current_user.user_id).first():
            #     db.session.execute(delete(Event).where(Event.user_id == current_user.user_id))
            
            # #create new record in respective realtion
            # db.session.add(Event(**event_status))
            # db.session.commit()

        if user_category_trip_status["food"]:

            # A dictionary to store respective category
            food_trip_status = {
                "user_id": current_user.user_id,
                "afghan_restaurant":  bool(request.form.get('afghan_restaurant')),
                "african_restaurant":  bool(request.form.get('african_restaurant')),
                "american_restaurant":  bool(request.form.get('american_restaurant')),
                "armenian_restaurant":  bool(request.form.get('armenian_restaurant')),
                "asian_restaurant":  bool(request.form.get('asian_restaurant')),
                "australian_restaurant":  bool(request.form.get('australian_restaurant')),
                "austrian_restaurant":  bool(request.form.get('austrian_restaurant')),
                "bbq_joint":  bool(request.form.get('bbq_joint')),
                "bagel_shop":  bool(request.form.get('bagel_shop')),
                "bakery":  bool(request.form.get('bakery')),
                "bangladeshi_restaurant":  bool(request.form.get('bangladeshi_restaurant')),
                "belgian_restaurant":  bool(request.form.get('belgian_restaurant')),
                "bistro":  bool(request.form.get('bistro')),
                "breakfast_spot":  bool(request.form.get('breakfast_spot')),
                "bubble_tea_shop":  bool(request.form.get('bubble_tea_shop')),
                "buffet":  bool(request.form.get('buffet')),
                "burger_joint":  bool(request.form.get('burger_joint')),
                "cafeteria":  bool(request.form.get('cafeteria')),
                "café":  bool(request.form.get('café')),
                "cajun_or_creole_restaurant":  bool(request.form.get('cajun_or_creole_restaurant')),
                "caribbean_restaurant":  bool(request.form.get('caribbean_restaurant')),
                "caucasian_restaurant":  bool(request.form.get('caucasian_restaurant')),
                "coffee_shop":  bool(request.form.get('coffee_shop')),
                "comfort_food_restaurant":  bool(request.form.get('comfort_food_restaurant')),
                "creperie":  bool(request.form.get('creperie')),
                "czech_restaurant":  bool(request.form.get('czech_restaurant')),
                "deli_or_bodega":  bool(request.form.get('deli_or_bodega')),
                "dessert_shop":  bool(request.form.get('dessert_shop')),
                "diner":  bool(request.form.get('diner')),
                "donut_shop":  bool(request.form.get('donut_shop')),
                "dumpling_restaurant":  bool(request.form.get('dumpling_restaurant')),
                "dutch_restaurant":  bool(request.form.get('dutch_restaurant')),
                "eastern_european_restaurant":  bool(request.form.get('eastern_european_restaurant')),
                "english_restaurant":  bool(request.form.get('english_restaurant')),
                "falafel_restaurant":  bool(request.form.get('falafel_restaurant')),
                "fast_food_restaurant":  bool(request.form.get('fast_food_restaurant')),
                "fish_and_chips_shop":  bool(request.form.get('fish_and_chips_shop')),
                "fondue_restaurant":  bool(request.form.get('fondue_restaurant')),
                "food_court":  bool(request.form.get('food_court')),
                "food_stand":  bool(request.form.get('food_stand')),
                "food_truck":  bool(request.form.get('food_truck')),
                "french_restaurant":  bool(request.form.get('french_restaurant')),
                "fried_chicken_joint":  bool(request.form.get('fried_chicken_joint')),
                "friterie":  bool(request.form.get('friterie')),
                "gastropub":  bool(request.form.get('gastropub')),
                "german_restaurant":  bool(request.form.get('german_restaurant')),
                "greek_restaurant":  bool(request.form.get('greek_restaurant')),
                "halal_restaurant":  bool(request.form.get('halal_restaurant')),
                "hawaiian_restaurant":  bool(request.form.get('hawaiian_restaurant')),
                "hot_dog_joint":  bool(request.form.get('hot_dog_joint')),
                "hungarian_restaurant":  bool(request.form.get('hungarian_restaurant')),
                "indian_restaurant":  bool(request.form.get('indian_restaurant')),
                "irish_pub":  bool(request.form.get('irish_pub')),
                "italian_restaurant":  bool(request.form.get('italian_restaurant')),
                "jewish_restaurant":  bool(request.form.get('jewish_restaurant')),
                "juice_bar":  bool(request.form.get('juice_bar')),
                "kebab_restaurant":  bool(request.form.get('kebab_restaurant')),
                "latin_american_restaurant":  bool(request.form.get('latin_american_restaurant')),
                "mac_and_cheese_joint":  bool(request.form.get('mac_and_cheese_joint')),
                "mediterranean_restaurant":  bool(request.form.get('mediterranean_restaurant')),
                "mexican_restaurant":  bool(request.form.get('mexican_restaurant')),
                "middle_eastern_restaurant":  bool(request.form.get('middle_eastern_restaurant')),
                "modern_european_restaurant":  bool(request.form.get('modern_european_restaurant')),
                "molecular_gastronomy_restaurant":  bool(request.form.get('molecular_gastronomy_restaurant')),
                "pakistani_restaurant":  bool(request.form.get('pakistani_restaurant')),
                "pet_café":  bool(request.form.get('pet_café')),
                "pizza_place":  bool(request.form.get('pizza_place')),
                "polish_restaurant":  bool(request.form.get('polish_restaurant')),
                "portuguese_restaurant":  bool(request.form.get('portuguese_restaurant')),
                "poutine_place":  bool(request.form.get('poutine_place')),
                "restaurant":  bool(request.form.get('restaurant')),
                "russian_restaurant":  bool(request.form.get('russian_restaurant')),
                "salad_place":  bool(request.form.get('salad_place')),
                "sandwich_place":  bool(request.form.get('sandwich_place')),
                "scandinavian_restaurant":  bool(request.form.get('scandinavian_restaurant')),
                "scottish_restaurant":  bool(request.form.get('scottish_restaurant')),
                "seafood_restaurant":  bool(request.form.get('seafood_restaurant')),
                "slovak_restaurant":  bool(request.form.get('slovak_restaurant')),
                "snack_place":  bool(request.form.get('snack_place')),
                "soup_place":  bool(request.form.get('snack_place')),
                "southern_or_soul_food_restaurant":  bool(request.form.get('southern_or_soul_food_restaurant')),
                "spanish_restaurant":  bool(request.form.get('spanish_restaurant')),
                "sri_lankan_restaurant":  bool(request.form.get('sri_lankan_restaurant')),
                "steakhouse":  bool(request.form.get('steakhouse')),
                "swiss_restaurant":  bool(request.form.get('swiss_restaurant')),
                "tea_room":  bool(request.form.get('tea_room')),
                "theme_restaurant":  bool(request.form.get('theme_restaurant')),
                "turkish_restaurant":  bool(request.form.get('turkish_restaurant')),
                "ukrainian_restaurant":  bool(request.form.get('ukrainian_restaurant')),
                "vegetarian_or_vegan_restaurant":  bool(request.form.get('vegetarian_or_vegan_restaurant')),
                "wings_joint":  bool(request.form.get('wings_joint'))

            }

            # #check if record exists in respective relation, if yes then remove it
            # if Food.query.filter_by(user_id = current_user.user_id).first():
            #     db.session.execute(delete(Food).where(Food.user_id == current_user.user_id))
            
            # #create new record in respective realtion
            # db.session.add(Food(**food_status))
            # db.session.commit()

        if user_category_trip_status["nightlife_spot"]:

            # A dictionary to store respective category
            nightlife_spot_trip_status = {
                "user_id": current_user.user_id,
                "bar":  bool(request.form.get('bar')),
                "brewery":  bool(request.form.get('brewery')),
                "lounge":  bool(request.form.get('lounge')),
                "night_market":  bool(request.form.get('night_market')),
                "nightclub":  bool(request.form.get('nightclub')),
                "other_nightlife":  bool(request.form.get('other_nightlife')),
                "strip_club":  bool(request.form.get('strip_club'))

            }

            # #check if record exists in respective relation, if yes then remove it
            # if NightlifeSpot.query.filter_by(user_id=current_user.user_id).first():
            #     db.session.execute(delete(NightlifeSpot).where(
            #         NightlifeSpot.user_id == current_user.user_id))

            # #create new record in respective realtion
            # db.session.add(NightlifeSpot(**nightlife_spot_status))
            # db.session.commit()

        if user_category_trip_status["outdoors_and_recreation"]:

            # A dictionary to store respective category
            outdoors_and_recreation_trip_status = {
                "user_id": current_user.user_id,
                "athletics_and_sports":  bool(request.form.get('athletics_and_sports')),
                "bathing_area":  bool(request.form.get('bathing_area')),
                "bay":  bool(request.form.get('bay')),
                "beach":  bool(request.form.get('beach')),
                "bike_trail":  bool(request.form.get('bike_trail')),
                "boat_launch":  bool(request.form.get('boat_launch')),
                "botanical_garden":  bool(request.form.get('botanical_garden')),
                "bridge":  bool(request.form.get('bridge')),
                "campground":  bool(request.form.get('campground')),
                "canal_lock":  bool(request.form.get('canal_lock')),
                "canal":  bool(request.form.get('canal')),
                "castle":  bool(request.form.get('castle')),
                "cave":  bool(request.form.get('cave')),
                "cemetery":  bool(request.form.get('cemetery')),
                "dam":  bool(request.form.get('dam')),
                "dive_spot":  bool(request.form.get('dive_spot')),
                "dog_run":  bool(request.form.get('dog_run')),
                "farm":  bool(request.form.get('farm')),
                "field":  bool(request.form.get('field')),
                "fishing_spot":  bool(request.form.get('fishing_spot')),
                "forest":  bool(request.form.get('forest')),
                "fountain":  bool(request.form.get('fountain')),
                "garden":  bool(request.form.get('garden')),
                "gun_range":  bool(request.form.get('gun_range')),
                "harbor_or_marina":  bool(request.form.get('harbor_or_marina')),
                "hill":  bool(request.form.get('hill')),
                "hot_spring":  bool(request.form.get('hot_spring')),
                "indoor_play_area":  bool(request.form.get('indoor_play_area')),
                "island":  bool(request.form.get('island')),
                "lake":  bool(request.form.get('lake')),
                "lighthouse":  bool(request.form.get('lighthouse')),
                "mountain_hut":  bool(request.form.get('mountain_hut')),
                "mountain":  bool(request.form.get('mountain')),
                "national_park":  bool(request.form.get('national_park')),
                "nature_preserve":  bool(request.form.get('nature_preserve')),
                "other_great_outdoors":  bool(request.form.get('other_great_outdoors')),
                "palace":  bool(request.form.get('palace')),
                "park":  bool(request.form.get('park')),
                "pedestrian_plaza":  bool(request.form.get('pedestrian_plaza')),
                "picnic_area":  bool(request.form.get('picnic_area')),
                "picnic_shelter":  bool(request.form.get('picnic_shelter')),
                "playground":  bool(request.form.get('playground')),
                "plaza":  bool(request.form.get('plaza')),
                "pool":  bool(request.form.get('pool')),
                "rafting":  bool(request.form.get('rafting')),
                "recreation_center":  bool(request.form.get('recreation_center')),
                "reservoir":  bool(request.form.get('reservoir')),
                "river":  bool(request.form.get('river')),
                "rock_climbing_spot":  bool(request.form.get('rock_climbing_spot')),
                "roof_deck":  bool(request.form.get('roof_deck')),
                "scenic_lookout":  bool(request.form.get('scenic_lookout')),
                "sculpture_garden":  bool(request.form.get('sculpture_garden')),
                "ski_area":  bool(request.form.get('ski_area')),
                "skydiving_drop_zone":  bool(request.form.get('skydiving_drop_zone')),
                "stables":  bool(request.form.get('stables')),
                "state_or_provincial_park":  bool(request.form.get('state_or_provincial_park')),
                "states_and_municipalities":  bool(request.form.get('states_and_municipalities')),
                "summer_camp":  bool(request.form.get('summer_camp')),
                "trail":  bool(request.form.get('trail')),
                "tree":  bool(request.form.get('tree')),
                "vineyard":  bool(request.form.get('vineyard')),
                "volcano":  bool(request.form.get('volcano')),
                "waterfall":  bool(request.form.get('waterfall')),
                "waterfront":  bool(request.form.get('waterfront')),
                "well":  bool(request.form.get('well')),
                "windmill":  bool(request.form.get('windmill'))

            }


            #check if record exists in respective relation, if yes then remove it
            # if OutdoorsAndRecreation.query.filter_by(user_id = current_user.user_id).first():
            #     db.session.execute(delete(OutdoorsAndRecreation).where(OutdoorsAndRecreation.user_id == current_user.user_id))
            
            # #create new record in respective realtion
            # db.session.add(OutdoorsAndRecreation(**outdoors_and_recreation_status))
            # db.session.commit()

        if user_category_trip_status["professional_and_other_places"]:

            # A dictionary to store respective category
            professional_and_other_places_status = {
                "user_id": current_user.user_id,
                "animal_shelter":  bool(request.form.get('animal_shelter')),
                "architecture_firm":  bool(request.form.get('architecture_firm')),
                "art_studio":  bool(request.form.get('art_studio')),
                "auditorium":  bool(request.form.get('auditorium')),
                "ballroom":  bool(request.form.get('ballroom')),
                "building":  bool(request.form.get('building')),
                "business_center":  bool(request.form.get('business_center')),
                "cidery":  bool(request.form.get('cidery')),
                "club_house":  bool(request.form.get('club_house')),
                "community_center":  bool(request.form.get('community_center')),
                "convention_center":  bool(request.form.get('convention_cente')),
                "cultural_center":  bool(request.form.get('cultural_center')),
                "distillery":  bool(request.form.get('distillery')),
                "distribution_center":  bool(request.form.get('distribution_center')),
                "event_space":  bool(request.form.get('event_space')),
                "factory":  bool(request.form.get('factory')),
                "fair":  bool(request.form.get('fair')),
                "funeral_home":  bool(request.form.get('funeral_home')),
                "government_building":  bool(request.form.get('government_building')),
                "industrial_estate":  bool(request.form.get('industrial_estate')),
                "library":  bool(request.form.get('library')),
                "meadery":  bool(request.form.get('meadery')),
                "medical_center":  bool(request.form.get('medical_center')),
                "military_base":  bool(request.form.get('military_base')),
                "non_profit":  bool(request.form.get('non_profit')),
                "observatory":  bool(request.form.get('observatory')),
                "office":  bool(request.form.get('office')),
                "parking":  bool(request.form.get('parking')),
                "post_office":  bool(request.form.get('post_office')),
                "power_plant":  bool(request.form.get('power_plant')),
                "prison":  bool(request.form.get('prison')),
                "radio_station":  bool(request.form.get('radio_station')),
                "recruiting_agency":  bool(request.form.get('recruiting_agency')),
                "research_laboratory":  bool(request.form.get('research_laboratory')),
                "research_station":  bool(request.form.get('research_station')),
                "school":  bool(request.form.get('school')),
                "social_club":  bool(request.form.get('social_club')),
                "spiritual_center":  bool(request.form.get('spiritual_center')),
                "tv_station":  bool(request.form.get('tv_station')),
                "voting_booth":  bool(request.form.get('voting_booth')),
                "warehouse":  bool(request.form.get('warehouse')),
                "waste_facility":  bool(request.form.get('waste_facility')),
                "wedding_hall":  bool(request.form.get('wedding_hall')),
                "winery":  bool(request.form.get('winery'))

            }

            #check if record exists in respective relation, if yes then remove it
            # if ProfessionalAndOtherPlaces.query.filter_by(user_id = current_user.user_id).first():
            #     db.session.execute(delete(ProfessionalAndOtherPlaces).where(ProfessionalAndOtherPlaces.user_id == current_user.user_id))
            
            # #create new record in respective realtion
            # db.session.add(ProfessionalAndOtherPlaces(**professional_and_other_places_status))
            # db.session.commit()


        if user_category_trip_status["residence"]:
            
            # A dictionary to store respective category
            residence_status = {
                "user_id" : current_user.user_id,
                "assisted_living"  :    bool(request.form.get('assisted_living')),
                "home_private"  :    bool(request.form.get('home_private')),
                "housing_development"  :    bool(request.form.get('housing_development')),
                "residential_building_apartment_or_condo"  :    bool(request.form.get('residential_building_apartment_or_condo')),
                "trailer_park"  :    bool(request.form.get('trailer_park'))

            }

            #check if record exists in respective relation, if yes then remove it
            # if Residence.query.filter_by(user_id = current_user.user_id).first():
            #     db.session.execute(delete(Residence).where(Residence.user_id == current_user.user_id))
            
            # #create new record in respective realtion
            # db.session.add(Residence(**residence_status))
            # db.session.commit()

        if user_category_trip_status["shop_and_service"]:

            # A dictionary to store respective category
            shop_and_service_status = {
                "user_id": current_user.user_id,
                "atm":    bool(request.form.get('atm')),
                "adult_boutique":    bool(request.form.get('adult_boutique')),
                "antique_shop":    bool(request.form.get('antique_shop')),
                "arts_and_crafts_store":    bool(request.form.get('arts_and_crafts_store')),
                "astrologer":    bool(request.form.get('astrologer')),
                "auto_dealership":    bool(request.form.get('auto_dealership')),
                "auto_garage":    bool(request.form.get('auto_garage')),
                "auto_workshop":    bool(request.form.get('auto_workshop')),
                "automotive_shop":    bool(request.form.get('automotive_shop')),
                "baby_store":    bool(request.form.get('baby_store')),
                "bank":    bool(request.form.get('bank')),
                "bath_house":    bool(request.form.get('bath_house')),
                "batik_shop":    bool(request.form.get('batik_shop')),
                "betting_shop":    bool(request.form.get('betting_shop')),
                "big_box_store":    bool(request.form.get('big_box_store')),
                "bike_shop":    bool(request.form.get('bike_shop')),
                "board_shop":    bool(request.form.get('board_shop')),
                "bookstore":    bool(request.form.get('bookstore')),
                "bridal_shop":    bool(request.form.get('bridal_shop')),
                "business_service":    bool(request.form.get('business_service')),
                "camera_store":    bool(request.form.get('camera_store')),
                "candy_store":    bool(request.form.get('candy_store')),
                "car_wash":    bool(request.form.get('car_wash')),
                "carpet_store":    bool(request.form.get('carpet_store')),
                "check_cashing_service":    bool(request.form.get('check_cashing_service')),
                "child_care_service":    bool(request.form.get('child_care_service')),
                "chocolate_shop":    bool(request.form.get('chocolate_shop')),
                "clothing_store":    bool(request.form.get('clothing_store')),
                "comic_shop":    bool(request.form.get('comic_shop')),
                "construction_and_landscaping":    bool(request.form.get('construction_and_landscaping')),
                "convenience_store":    bool(request.form.get('convenience_store')),
                "cosmetics_shop":    bool(request.form.get('cosmetics_shop')),
                "costume_shop":    bool(request.form.get('costume_shop')),
                "credit_union":    bool(request.form.get('credit_union')),
                "currency_exchange":    bool(request.form.get('currency_exchange')),
                "department_store":    bool(request.form.get('department_store')),
                "design_studio":    bool(request.form.get('design_studio')),
                "discount_store":    bool(request.form.get('discount_store')),
                "dive_shop":    bool(request.form.get('dive_shop')),
                "drugstore":    bool(request.form.get('drugstore')),
                "dry_cleaner":    bool(request.form.get('dry_cleaner')),
                "ev_charging_station":    bool(request.form.get('ev_charging_station')),
                "electronics_store":    bool(request.form.get('electronics_store')),
                "entertainment_service":    bool(request.form.get('entertainment_service')),
                "event_service":    bool(request.form.get('event_service')),
                "fabric_shop":    bool(request.form.get('fabric_shop')),
                "film_studio":    bool(request.form.get('film_studio')),
                "financial_or_legal_service":    bool(request.form.get('financial_or_legal_service')),
                "fireworks_store":    bool(request.form.get('fireworks_store')),
                "fishing_store":    bool(request.form.get('fishing_store')),
                "flea_market":    bool(request.form.get('flea_market')),
                "floating_market":    bool(request.form.get('floating_market')),
                "flower_shop":    bool(request.form.get('flower_shop')),
                "food_and_drink_shop":    bool(request.form.get('food_and_drink_shop')),
                "frame_store":    bool(request.form.get('frame_store')),
                "fruit_and_vegetable_store":    bool(request.form.get('fruit_and_vegetable_store')),
                "furniture_or_home_store":    bool(request.form.get('furniture_or_home_store')),
                "gaming_cafe":    bool(request.form.get('gaming_cafe')),
                "garden_center":    bool(request.form.get('garden_center')),
                "gas_station":    bool(request.form.get('gas_station')),
                "gift_shop":    bool(request.form.get('gift_shop')),
                "gun_shop":    bool(request.form.get('gun_shop')),
                "hardware_store":    bool(request.form.get('hardware_store')),
                "health_and_beauty_service":    bool(request.form.get('health_and_beauty_service')),
                "herbs_and_spices_store":    bool(request.form.get('herbs_and_spices_store')),
                "hobby_shop":    bool(request.form.get('hobby_shop')),
                "home_service":    bool(request.form.get('home_service')),
                "hunting_supply":    bool(request.form.get('hunting_supply')),
                "it_services":    bool(request.form.get('it_services')),
                "insurance_office":    bool(request.form.get('insurance_office')),
                "internet_cafe":    bool(request.form.get('internet_cafe')),
                "jewelry_store":    bool(request.form.get('jewelry_store')),
                "kitchen_supply_store":    bool(request.form.get('kitchen_supply_store')),
                "knitting_store":    bool(request.form.get('knitting_store')),
                "laundromat":    bool(request.form.get('laundromat')),
                "laundry_service":    bool(request.form.get('laundry_service')),
                "lawyer":    bool(request.form.get('lawyer')),
                "leather_goods_store":    bool(request.form.get('leather_goods_store')),
                "locksmith":    bool(request.form.get('locksmith')),
                "lottery_retailer":    bool(request.form.get('lottery_retailer')),
                "luggage_store":    bool(request.form.get('luggage_store')),
                "marijuana_dispensary":    bool(request.form.get('marijuana_dispensary')),
                "market":    bool(request.form.get('market')),
                "massage_studio":    bool(request.form.get('massage_studio')),
                "mattress_store":    bool(request.form.get('mattress_store')),
                "medical_supply_store":    bool(request.form.get('medical_supply_store')),
                "miscellaneous_shop":    bool(request.form.get('miscellaneous_shop')),
                "mobile_phone_shop":    bool(request.form.get('mobile_phone_shop')),
                "mobility_store":    bool(request.form.get('mobility_store')),
                "motorcycle_shop":    bool(request.form.get('motorcycle_shop')),
                "motorsports_shop":    bool(request.form.get('motorsports_shop')),
                "music_store":    bool(request.form.get('music_store')),
                "nail_salon":    bool(request.form.get('nail_salon')),
                "newsagent":    bool(request.form.get('newsagent')),
                "newsstand":    bool(request.form.get('newsstand')),
                "notary":    bool(request.form.get('notary')),
                "optical_shop":    bool(request.form.get('optical_shop')),
                "other_repair_shop":    bool(request.form.get('other_repair_shop')),
                "outdoor_supply_store":    bool(request.form.get('outdoor_supply_store')),
                "outlet_mall":    bool(request.form.get('outlet_mall')),
                "outlet_store":    bool(request.form.get('outlet_store')),
                "paper_or_office_supplies_store":    bool(request.form.get('paper_or_office_supplies_store')),
                "pawn_shop":    bool(request.form.get('pawn_shop')),
                "perfume_shop":    bool(request.form.get('perfume_shop')),
                "pet_service":    bool(request.form.get('pet_service')),
                "pet_store":    bool(request.form.get('pet_store')),
                "pharmacy":    bool(request.form.get('pharmacy')),
                "photography_lab":    bool(request.form.get('photography_lab')),
                "photography_studio":    bool(request.form.get('photography_studio')),
                "piercing_parlor":    bool(request.form.get('piercing_parlor')),
                "pop_up_shop":    bool(request.form.get('pop_up_shop')),
                "print_shop":    bool(request.form.get('print_shop')),
                "public_bathroom":    bool(request.form.get('public_bathroom')),
                "real_estate_office":    bool(request.form.get('real_estate_office')),
                "record_shop":    bool(request.form.get('record_shop')),
                "recording_studio":    bool(request.form.get('recording_studio')),
                "recycling_facility":    bool(request.form.get('recycling_facility')),
                "rental_service":    bool(request.form.get('rental_service')),
                "salon_or_barbershop":    bool(request.form.get('salon_or_barbershop')),
                "sauna_or_steam_room":    bool(request.form.get('sauna_or_steam_room')),
                "shipping_store":    bool(request.form.get('shipping_store')),
                "shoe_repair":    bool(request.form.get('shoe_repair')),
                "shopping_mall":    bool(request.form.get('shopping_mall')),
                "shopping_plaza":    bool(request.form.get('shopping_plaza')),
                "skate_shop":    bool(request.form.get('skate_shop')),
                "ski_shop":    bool(request.form.get('ski_shop')),
                "smoke_shop":    bool(request.form.get('smoke_shop')),
                "smoothie_shop":    bool(request.form.get('smoothie_shop')),
                "souvenir_shop":    bool(request.form.get('souvenir_shop')),
                "spa":    bool(request.form.get('spa')),
                "sporting_goods_shop":    bool(request.form.get('sporting_goods_shop')),
                "stationery_store":    bool(request.form.get('stationery_store')),
                "storage_facility":    bool(request.form.get('storage_facility')),
                "supplement_shop":    bool(request.form.get('supplement_shop')),
                "tailor_shop":    bool(request.form.get('tailor_shop')),
                "tanning_salon":    bool(request.form.get('tanning_salon')),
                "tattoo_parlor":    bool(request.form.get('tattoo_parlor')),
                "thrift_or_vintage_store":    bool(request.form.get('thrift_or_vintage_store')),
                "toy_or_game_store":    bool(request.form.get('toy_or_game_store')),
                "travel_agency":    bool(request.form.get('travel_agency')),
                "used_bookstore":    bool(request.form.get('used_bookstore')),
                "vape_store":    bool(request.form.get('vape_store')),
                "vehicle_inspection_station":    bool(request.form.get('vehicle_inspection_station')),
                "video_game_store":    bool(request.form.get('video_game_store')),
                "video_store":    bool(request.form.get('video_store')),
                "warehouse_store":    bool(request.form.get('warehouse_store')),
                "watch_shop":    bool(request.form.get('watch_shop'))

            }

            #check if record exists in respective relation, if yes then remove it
            # if ShopAndService.query.filter_by(user_id = current_user.user_id).first():
            #     db.session.execute(delete(ShopAndService).where(ShopAndService.user_id == current_user.user_id))
            
            # #create new record in respective realtion
            # db.session.add(ShopAndService(**shop_and_service_status))
            # db.session.commit()

        if user_category_trip_status["travel_and_transport"]:

            # A dictionary to store respective category
            travel_and_transport_status = {
                "user_id": current_user.user_id,
                "airport":    bool(request.form.get('airport')),
                "baggage_locker":    bool(request.form.get('baggage_locker')),
                "bike_rental_or_bike_share":    bool(request.form.get('bike_rental_or_bike_share')),
                "boat_rental":    bool(request.form.get('boat_rental')),
                "boat_or_ferry":    bool(request.form.get('boat_or_ferry')),
                "border_crossing":    bool(request.form.get('border_crossing')),
                "bus_station":    bool(request.form.get('bus_station')),
                "bus_stop":    bool(request.form.get('bus_stop')),
                "cable_car":    bool(request.form.get('cable_car')),
                "cruise_ship":    bool(request.form.get('cruise_ship')),
                "duty_free_shop":    bool(request.form.get('duty_free_shop')),
                "general_travel":    bool(request.form.get('general_travel')),
                "heliport":    bool(request.form.get('heliport')),
                "hotel":    bool(request.form.get('hotel')),
                "intersection":    bool(request.form.get('intersection')),
                "light_rail_station":    bool(request.form.get('light_rail_station')),
                "marine_terminal":    bool(request.form.get('marine_terminal')),
                "metro_station":    bool(request.form.get('metro_station')),
                "moving_target":    bool(request.form.get('moving_target')),
                "pier":    bool(request.form.get('pier')),
                "port":    bool(request.form.get('port')),
                "rv_park":    bool(request.form.get('rv_park')),
                "rental_car_location":    bool(request.form.get('rental_car_location')),
                "rest_area":    bool(request.form.get('rest_area')),
                "road":    bool(request.form.get('road')),
                "taxi_stand":    bool(request.form.get('taxi_stand')),
                "taxi":    bool(request.form.get('taxi')),
                "toll_booth":    bool(request.form.get('toll_booth')),
                "toll_plaza":    bool(request.form.get('toll_plaza')),
                "tourist_information_center":    bool(request.form.get('tourist_information_center')),
                "train_station":    bool(request.form.get('train_station')),
                "tram_station":    bool(request.form.get('tram_station')),
                "transportation_service":    bool(request.form.get('transportation_service')),
                "travel_lounge":    bool(request.form.get('travel_lounge')),
                "truck_stop":    bool(request.form.get('truck_stop')),
                "tunnel":    bool(request.form.get('tunnel'))

            }


            #check if record exists in respective relation, if yes then remove it
            # if TravelAndTransport.query.filter_by(user_id = current_user.user_id).first():
            #     db.session.execute(delete(TravelAndTransport).where(TravelAndTransport.user_id == current_user.user_id))
            
            # #create new record in respective realtion
            # db.session.add(TravelAndTransport(**travel_and_transport_status))
            # db.session.commit()

        return redirect(url_for('main.schedule_trip'))

    return render_template('trip_preferences.html')
