from time import sleep
from sense_hat import SenseHat
import logging 
from datetime import datetime

sense = SenseHat()
temperature_list = []
humidity_list = []
logging.basicConfig(filename="sh.log", filemode="a")

time = 0

def log():
    logging.info('Humidity' + str(temperature) + datetime.now().strftime("%H:%M:%S"))
    logging.info('Temperature' + str(temperature) + datetime.now().strftime("%H:%M:%S"))

def asString(temp):
    return str(temp)

while time <= 120:

    temperature = round(sense.get_temperature(), 1)
    humidity = round(sense.get_humidity(), 1)
    time += 1
    temperature_list.append(temperature)
    humidity_list.append(humidity)
    log()
    sleep(1)

    if time == 20 or time == 40 or time == 60 or time == 80 or time ==  100 or time ==  120:
        sense.show_message(str(temperature))

        if time == 120:
            print("Min temperature is " + asString(min(temperature_list)))
            print("Mid temperature is " + asString(max(temperature_list)))
            print("Max temperature is " + asString(round(sum(temperature_list) / len(temperature_list), 1)))
        
            print("Min humidity is " + asString(min(humidity_list)))
            print("Mid humidity is " + asString(max(humidity_list)))
            print("Max humidity is " + asString(round(sum(humidity_list) / len(humidity_list), 1)))

