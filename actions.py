from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import collections
import smtplib
from email.message import EmailMessage

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"f75a7c69770eb245bc3634a238239520"}
		zomato = zomatopy.initialize_app(config)
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		loc = tracker.get_slot('location')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american' : 1, 'chinese':25, 'italian':55, 'mexican':73, 'north indian':50,'south indian':85}
		results=zomato.restaurant_search("&sort=rating&order=desc", lat, lon, str(cuisines_dict.get(cuisine)))
		d = json.loads(results)
		price_dict = {'low' : range(0,300), 'mid' : range(301,700), 'high' : range(701,10000)}
		price_range = price_dict[price]

		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			response = response + "Showing you top rated restaurants: \n"
			response = response+"-----------------------------------------------------------------------------------------------------------------------\n"
			for restaurant in d['restaurants']:
				try:
					if restaurant['restaurant']['average_cost_for_two'] in price_range:
						response=response+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address'] + " has been rated " + str(restaurant['restaurant']['user_rating']['aggregate_rating']) + "\n"
				except Exception as e:
					response = response+str(e)

		dispatcher.utter_message(response)
		return [SlotSet('can_ask_send_mail', True)]



class ActionIsOperationalCity(Action):
	def name(self):
		return 'action_is_operational_city'

	def run(self, dispatcher, tracker, domain):
		supported_locs = ['bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'ahmedabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bokaro steel city', 'chandigarh', 'coimbatore', 'nagpur', 'cuttack', 'dehradun', 'dhanbad', 'durg-bhilai nagar', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gurgaon', 'guwahati', 'gwalior', 'hubli-dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kannur', 'Kanpur', 'Kakinada', 'Kochi', 'Kottayam', 'Kolhapur', 'Kollam', 'Kota', 'Kozhikode', 'Kurnool', 'Lucknow', 'Ludhiana', 'Madurai', 'Malappuram', 'Mathura', 'Goa', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Palakkad', 'Patna', 'Pondicherry', 'Prayagraj', 'PuneRaipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Siliguri', 'Solapur', 'Srinagar', 'Sultanpur', 'Surat', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirunelveli', 'Tiruppur', 'Tiruvannamalai', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Visakhapatnam', 'Vellore', 'Warangal']
		supported_locs = [x.lower() for x in supported_locs]

		loc = tracker.get_slot('location')
		if loc.lower() not in supported_locs:
			return [SlotSet('location_supported', False)]
		else:
			return [SlotSet('location_supported', True)]


class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		mail_preference = tracker.get_slot('mail_preference')
		if mail_preference.lower() == 'no':
			return [SlotSet('location', ''), SlotSet('cuisine', ''), SlotSet('price', ''), SlotSet('mail_preference', 'no'), SlotSet('can_ask_send_mail', False)]

		mail_id = tracker.get_slot('mail_id')
		if mail_id == None:
			return [SlotSet('is_mail_id_provided', False)]

		config={ "user_key":"f75a7c69770eb245bc3634a238239520"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')

		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american' : 1, 'chinese':25, 'italian':55, 'mexican':73, 'north indian':50,'south indian':85}
		results=zomato.restaurant_search("&sort=rating&order=desc", lat, lon, str(cuisines_dict.get(cuisine)))
		d = json.loads(results)
		price_dict = {'low' : range(0,300), 'mid' : range(301,700), 'high' : range(701,10000)}
		price_range = price_dict[price]

		response = ""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				try:
					if restaurant['restaurant']['average_cost_for_two'] in price_range:
						response=response+ 'Restaurant Name: ' + restaurant['restaurant']['name']+ '\nRestaurant locality address: ' + restaurant['restaurant']['location']['address'] + "\nAverage budget for two people: " + str(restaurant['restaurant']['average_cost_for_two']) + '\nZomato user rating: ' + str(restaurant['restaurant']['user_rating']['aggregate_rating']) + "\n"
				except Exception as e:
					response = response+str(e)

		msg = EmailMessage()
		msg.set_content(response)
		msg['Subject'] = 'Restaurants Detail:'
		msg['From'] = 'foodiebots@gmail.com'
		msg['To'] = mail_id

		try:
			s = smtplib.SMTP("smtp.gmail.com", 587)
			s.starttls()
			s.login('foodiebots@gmail.com', 'foodie123')
			s.send_message(msg)
			s.quit()
		except Exception as e:
			return str(e)

		return [SlotSet('is_mail_id_provided', True), SlotSet('location', ''), SlotSet('cuisine', ''), SlotSet('price', ''), SlotSet('mail_preference', 'no'), SlotSet('can_ask_send_mail', False)]