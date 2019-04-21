## Generated Story 255706069223404498
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_is_operational_city
    - slot{"location_supported": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "no"}
    - slot{"mail_preference" : "no"}
    - action_send_mail
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story 25570634587623404498
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - action_is_operational_city
    - slot{"location_supported": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price_range
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "no"}
    - slot{"mail_preference" : "no"}
    - action_send_mail
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story 2554587069223404435
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Durgapur"}
    - slot{"location": "Durgapur"}
    - action_is_operational_city
    - slot{"location_supported": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "no"}
    - slot{"mail_preference" : "no"}
    - action_send_mail
    - utter_goodbye
* affirm
    - utter_goodbye
    - export


## Generated Story 6722305456060677374
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_is_operational_city
    - slot{"location_supported": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "yes", "mail_id": "example@example.com"}
    - slot{"mail_preference" : "yes"}
    - slot{"mail_id": "example@example.com"}
    - action_send_mail
    - slot{"is_mail_id_provided" : false}
    - utter_ask_mail_id
* get_mail{"mail_id": "example@example.com"}
    - slot{"mail_id": "example@example.com"}
    - action_send_mail
    - slot{"is_mail_id_provided" : true}
    - utter_goodbye
* affirm
    - utter_goodbye
    - export


## Generated Story 672230578358777374
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}    
    - action_is_operational_city
    - slot{"location_supported": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "yes", "mail_id": "check@some.com"}
    - slot{"mail_preference" : "yes"}
    - slot{"mail_id": "check@some.com"}
    - action_send_mail
    - slot{"is_mail_id_provided" : true}
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story 1993277579540566202
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_is_operational_city
    - slot{"location_supported": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price_range
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "no"}
    - slot{"mail_preference" : "no"}
    - action_send_mail
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story 3320800183399695936
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "erode"}
    - slot{"location": "erode"}
    - action_is_operational_city
    - slot{"location_supported": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "yes", "mail_id": "example@example.com"}
    - slot{"mail_preference" : "yes"}
    - slot{"mail_id": "example@example.com"}
    - action_send_mail
    - slot{"is_mail_id_provided" : false}
    - utter_ask_mail_id
* get_mail{"mail_id": "check@somedomain.edu"}
    - slot{"mail_id": "check@somedomain.edu"}
    - action_send_mail
    - slot{"is_mail_id_provided" : true}
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story 3320800183399695936
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "erode"}
    - slot{"location": "erode"}
    - action_is_operational_city
    - slot{"location_supported": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "yes", "mail_id": "example@example.com"}
    - slot{"mail_preference" : "yes"}
    - slot{"mail_id": "example@example.com"}
    - action_send_mail
    - slot{"is_mail_id_provided" : true}
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story -3865090405359340534
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "perundurai"}
    - slot{"location": "perundurai"}
    - action_is_operational_city
    - slot{"location_supported": false}
    - utter_non_operating_area
    - utter_ask_different_location
* restaurant_search{"location": "erode"}
    - slot{"location": "erode"}
    - action_is_operational_city
    - slot{"location_supported": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "yes", "mail_id": "someperson@yahoo.in"}
    - slot{"mail_preference" : "yes"}
    - slot{"mail_id": "someperson@yahoo.in"}
    - action_send_mail
    - slot{"is_mail_id_provided" : false}
    - utter_ask_mail_id
* get_mail{"mail_id": "check@somedomain.edu"}
    - slot{"mail_id": "check@somedomain.edu"}
    - action_send_mail
    - slot{"is_mail_id_provided" : true}
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story -38654567405359340534
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "perundurai"}
    - slot{"location": "perundurai"}
    - action_is_operational_city
    - slot{"location_supported": false}
    - utter_non_operating_area
    - utter_ask_different_location
* restaurant_search{"location": "erode"}
    - slot{"location": "erode"}
    - action_is_operational_city
    - slot{"location_supported": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "yes", "mail_id": "someperson@yahoo.in"}
    - slot{"mail_preference" : "yes"}
    - slot{"mail_id": "someperson@yahoo.in"}
    - action_send_mail
    - slot{"is_mail_id_provided" : true}
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story -386509043458769340534
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "perundurai"}
    - slot{"location": "perundurai"}
    - action_is_operational_city
    - slot{"location_supported": false}
    - utter_non_operating_area
    - utter_ask_different_location
* restaurant_search{"location": "erode"}
    - slot{"location": "erode"}
    - action_is_operational_city
    - slot{"location_supported": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "yes"}
    - slot{"mail_preference" : "yes"}
    - utter_ask_mail_id
* get_mail{"mail_id": "someperson@yahoo.in"}
    - slot{"mail_id": "someperson@yahoo.in"}
    - action_send_mail
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story 5665090405359340534
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "annur"}
    - slot{"location": "annur"}
    - action_is_operational_city
    - slot{"location_supported": false}
    - utter_non_operating_area
    - utter_ask_different_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_is_operational_city
    - slot{"location_supported": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "no"}
    - slot{"mail_preference" : "no"}
    - action_send_mail
    - utter_goodbye
* affirm
    - utter_goodbye
    - export


## Generated Story 566509034976359340534
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mettur"}
    - slot{"location": "mettur"}
    - action_is_operational_city
    - slot{"location_supported": false}
    - utter_non_operating_area
    - utter_ask_different_location
* restaurant_search{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - action_is_operational_city
    - slot{"location_supported": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "yes", "mail_id": "check@somedomain.edu"}
    - slot{"mail_preference" : "yes"}
    - slot{"mail_id": "check@somedomain.edu"}
    - action_send_mail
    - slot{"is_mail_id_provided" : false}
    - utter_ask_mail_id
* get_mail{"mail_id": "check@somedomain.edu"}
    - slot{"mail_id": "check@somedomain.edu"}
    - action_send_mail
    - slot{"is_mail_id_provided" : true}
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story 566509034976359340534
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mettur"}
    - slot{"location": "mettur"}
    - action_is_operational_city
    - slot{"location_supported": false}
    - utter_non_operating_area
    - utter_ask_different_location
* restaurant_search{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - action_is_operational_city
    - slot{"location_supported": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "yes", "mail_id": "check@somedomain.edu"}
    - slot{"mail_preference" : "yes"}
    - slot{"mail_id": "check@somedomain.edu"}
    - action_send_mail
    - slot{"is_mail_id_provided" : true}
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story 566509034976359340534
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mettur"}
    - slot{"location": "mettur"}
    - action_is_operational_city
    - slot{"location_supported": false}
    - utter_non_operating_area
    - utter_ask_different_location
* restaurant_search{"location": "jodhpur"}
    - slot{"location": "jodhpur"}
    - action_is_operational_city
    - slot{"location_supported": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "yes"}
    - slot{"mail_preference" : "yes"}
    - utter_ask_mail_id
* get_mail{"mail_id": "check@somedomain.edu"}
    - slot{"mail_id": "check@somedomain.edu"}
    - action_send_mail
    - slot{"is_mail_id_provided" : false}
    - utter_ask_mail_id
* get_mail{"mail_id": "check@somedomain.edu"}
    - slot{"mail_id": "check@somedomain.edu"}
    - action_send_mail
    - slot{"is_mail_id_provided" : true}
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story 93725090405359340534
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "nasik"}
    - slot{"location": "nasik"}
    - action_is_operational_city
    - slot{"location_supported": false}
    - utter_non_operating_area
    - utter_ask_different_location
* restaurant_search{"location": "mettupalayam"}
    - slot{"location": "mettupalayam"}
    - action_is_operational_city
    - slot{"location_supported": false}
    - utter_non_operating_area
    - utter_ask_different_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_is_operational_city
    - slot{"location_supported": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "no"}
    - slot{"mail_preference" : "no"}
    - action_send_mail
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story 61865090405359340534
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "baroda"}
    - slot{"location": "baroda"}
    - action_is_operational_city
    - slot{"location_supported": false}
    - utter_non_operating_area
    - utter_ask_different_location
* restaurant_search{"location": "bellari"}
    - slot{"location": "bellari"}
    - action_is_operational_city
    - slot{"location_supported": false}
    - utter_non_operating_area
    - utter_ask_different_location
* restaurant_search{"location": "srinagar"}
    - slot{"location": "srinagar"}
    - action_is_operational_city
    - slot{"location_supported": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "yes", "mail_id": "something@example.au"}
    - slot{"mail_preference" : "yes"}
    - slot{"mail_id": "something@example.au"}
    - action_send_mail
    - slot{"is_mail_id_provided" : false}
    - utter_ask_mail_id
* get_mail{"mail_id": "check@somedomain.edu"}
    - slot{"mail_id": "check@somedomain.edu"}
    - action_send_mail
    - slot{"is_mail_id_provided" : true}
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story 61865090405359340534
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "baroda"}
    - slot{"location": "baroda"}
    - action_is_operational_city
    - slot{"location_supported": false}
    - utter_non_operating_area
    - utter_ask_different_location
* restaurant_search{"location": "bellari"}
    - slot{"location": "bellari"}
    - action_is_operational_city
    - slot{"location_supported": false}
    - utter_non_operating_area
    - utter_ask_different_location
* restaurant_search{"location": "srinagar"}
    - slot{"location": "srinagar"}
    - action_is_operational_city
    - slot{"location_supported": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "yes"}
    - slot{"mail_preference" : "yes"}
    - utter_ask_mail_id
* get_mail{"mail_id": "something@example.au"}
    - slot{"mail_id": "something@example.au"}
    - action_send_mail
    - utter_goodbye
* affirm
    - utter_goodbye
    - export

## Generated Story 67865090405359340534
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chenganur"}
    - slot{"location": "chenganur"}
    - action_is_operational_city
    - slot{"location_supported": false}
    - utter_non_operating_area
    - utter_ask_different_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_is_operational_city
    - slot{"location_supported": true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price_range
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"can_ask_send_mail": true}
    - utter_details_on_mail
* get_mail{"mail_preference" : "no"}
    - slot{"mail_preference" : "no"}
    - action_send_mail
    - utter_goodbye
* affirm
    - utter_goodbye
    - export