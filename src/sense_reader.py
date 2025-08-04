def get_sensor_data():
    from sense_hat import SenseHat
    import time

    sense = SenseHat()
    
    # Read temperature and humidity
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    
    return {
        'temperature': temperature,
        'humidity': humidity
    }