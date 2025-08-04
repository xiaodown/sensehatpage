def get_sensor_data():
    from sense_hat import SenseHat
    import time

    sense = SenseHat()
    
    # Read temperature and humidity, rounded to 1 decimal place
    temperature = round(sense.get_temperature(), 1)
    humidity = round(sense.get_humidity(), 1)
    
    return {
        'temperature': temperature,
        'humidity': humidity
    }