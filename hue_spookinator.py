import requests
import random
import time

# I only have white lamps so hue and saturation don't work. If you have the full RGB version you can uncomment the parts if you want.

BRIDGE_IP = ''
USERNAME = ''  # Generate with curl -X POST -d '{"devicetype": "<USERNAME>"}' "http://<bridge ip>/api"
LIGHT_NUMBER = '' # See states of all connected lamps with curl "http://<bridge ip>/api/<USERNAME>/lights/"
LIGHT_URL = f'http://{BRIDGE_IP}/api/{USERNAME}/lights/{LIGHT_NUMBER}/state'

RANDOM_RANGE_START = 100
RANDOM_RANGE_END = 240
BASE_BRIGHTNESS = 100

def set_light(on, brightness=254, hue=None, saturation=None, color_temp=None):
    """Send a command to the Philips Hue light."""
    state = {'on': on, 'bri': brightness}
    if hue is not None:
        state['hue'] = hue
    if saturation is not None:
        state['sat'] = saturation
    if color_temp is not None:
        state['ct'] = color_temp
    
    response = requests.put(LIGHT_URL, json=state)
    #print(response.json())

def spooky_flicker():
    while True:
        next_flicker = random.randint(RANDOM_RANGE_START, RANDOM_RANGE_END)  
        
        print(f"Waiting for {next_flicker} seconds...")
        time.sleep(next_flicker)

        flicker_times = random.randint(5, 10)
        special_event = random.randint(0, 10)
	
        if special_event == 5:
            print("Special event 1")
            for _ in range(7):
                brightness = random.randint(1, 254)
                #hue = random.randint(0, 65535) 
                #saturation = random.randint(150, 254) 

                set_light(True, brightness=brightness) #, hue=hue, saturation=saturation)
                time.sleep(random.uniform(0.1, 0.7))
            
                set_light(False)
                time.sleep(random.uniform(0.1, 0.3))

            set_light(True, brightness=254) #, hue=hue, saturation=saturation)
            time.sleep(1.5)
            set_light(False)
            time.sleep(10)
            set_light(True, brightness=BASE_BRIGHTNESS)

        elif special_event == 10:
            print("Special Event 2: SOS")
            set_light(False)
            time.sleep(1)

            for _ in range(3):
                set_light(True, brightness=BASE_BRIGHTNESS)
                time.sleep(0.2)
                set_light(False)
                time.sleep(0.2)
            
            for _ in range(3):
                set_light(True, brightness=BASE_BRIGHTNESS)
                time.sleep(0.8)
                set_light(False)
                time.sleep(0.2)
            
            for _ in range(3):
                set_light(True, brightness=BASE_BRIGHTNESS)
                time.sleep(0.2)
                set_light(False)
                time.sleep(0.2)
            
            set_light(True, brightness=BASE_BRIGHTNESS)

                
        else:
            for _ in range(flicker_times):
                brightness = random.randint(1, 254)
                #hue = random.randint(0, 65535) 
                #saturation = random.randint(150, 254) 

                set_light(True, brightness=brightness) #, hue=hue, saturation=saturation)
                time.sleep(random.uniform(0.1, 0.7))
            
                set_light(False)
                time.sleep(random.uniform(0.1, 0.3))

            set_light(True, brightness=BASE_BRIGHTNESS) #, hue=8418, saturation=140, color_temp=366)

if __name__ == "__main__":
    try:
        spooky_flicker()
    except KeyboardInterrupt:
        set_light(True, brightness=BASE_BRIGHTNESS) #, hue=8418, saturation=140, color_temp=366)
        print()
