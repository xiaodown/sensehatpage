def get_sensor_data():
    from sense_hat import SenseHat

    sense = SenseHat()
    temperature_c = sense.get_temperature()
    temperature_f = round((temperature_c * 9/5) + 32, 1)
    humidity = round(sense.get_humidity(), 1)
    
    return {
        'temperature': temperature_f,
        'humidity': humidity
    }