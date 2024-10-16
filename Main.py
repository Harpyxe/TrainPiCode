import requests
import RPi.GPIO as GPIO
import time
from hx711 import HX711
import random2 as random

### GPIO setups
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(6, GPIO.OUT)

### HX711 setup
hx=HX711(dout_pin=5,pd_sck_pin=6)

### Functional arguments
train_name="RB69"
stations=["Shibuya Station", "Frankfurter HBF", "Manchester", "Cuba ost","Ditsch Plaza", "Lego Land", "Mittel Erde", "Hogwarts"]

seat_pins=[21]
timeout=0.5

reference_unit=1000
old_weight=int()




def update_api(weight_value, occupied_seats):

	station_name = stations[random.randint(0,len(stations))]
	
	url="http://192.168.188.24:8080/sensordata"
	myobj={
		"Zugname":train_name,
		"Gewicht":weight_value,
		"Sitzauslastung":occupied_seats,
		"Station":station_name
		}
		
	print(myobj)
	try:
		x=requests.post(url,json=myobj)
		print(x.status_code)
		print(x.test)
	except request.exception.RequestException as e:
		print(f"An error occurred: {e}")





### Run in loop
while True:
	
	val=hx.get_raw_data(times=3)
	current_value=sum(val)/3
	current_value_clean=current_value/reference_unit
	hx.power_down()
	hx.power_up()
	print(current_value)
	time.sleep(0.1)
	
	print(current_value-old_weight,"ddd")
	old_weight=current_value
	
	
	
	
	for seat_pin in seat_pins:
		if GPIO.input(seat_pin) == 0:
			print("dddddddddddddddddddd")
			time.sleep(0.1)
