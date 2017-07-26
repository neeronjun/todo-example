import serial, time, requests
arduino = serial.Serial('/dev/ttyACM0',9600, timeout=2.0)

clock=time.time()

'''while True:

    ask for temperature
    text = "[TEMP]\n"
    bytes= text.encode("latin-1")
    arduino.write(bytes)

    #read the value
    bytes = arduino.readline()
    if bytes:
        text = bytes.decode("utf-8").strip()
        #print(text)

    
    #ask for humidity
    text = "[humidity]\n"
    bytes= text.encode("latin-1")
    arduino.write(bytes)

    #read the value
    bytes = arduino.readline()
    if bytes:
        text = bytes.decode("utf-8").strip()
       # print(text)
    #time.sleep(2) '''
def post_to_stream(userid, city, state, lat, long, temp, humidity, light, outdoors):
       
    url = "http:\\drdelozier.pythonanywhere.com/stream/store"
    payload = {'userid': str(userid),
                'city': str(city),
                'state': str(state),    
                'lat': str(lat),
                'long': str(long),
                'temp': str(temp),
                'humidity': str(humidity),
                'light': str(light),
                'outdoors': str(outdoors),
            }
    response = requests.get(url+ stream, params = payload)
    print(response.status_code)
    print(response.url)
    print(response.text)

while True:
    text = "[temp]\n"
    bytes= text.encode("latin-1")
    arduino.write(bytes)

    #read the value
    bytes = arduino.readline()
    if bytes:
        temperature = bytes.decode("utf-8").strip()

    
    text = "[humidity]\n"
    bytes= text.encode("latin-1")
    arduino.write(bytes)

    #read the value
    bytes = arduino.readline()
    if bytes:
        humidity = bytes.decode("utf-8").strip()
    post_to_stream('nrai', 'Kent', 'OH', 11, 12, temperature, humidity, 45, 1)
    #while(time.time() < clock + 15)