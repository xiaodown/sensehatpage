def get_cpu_temperature():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp_str = f.read()
    return float(temp_str) / 1000.0

def get_sensor_data():
    from sense_hat import SenseHat

    sense = SenseHat()
    raw_temp_c = sense.get_temperature()
    cpu_temp_c = get_cpu_temperature()
    # Adjust temperature reading
    corrected_temp_c = raw_temp_c - ((cpu_temp_c - raw_temp_c) / 1.5)
    temperature_f = round((corrected_temp_c * 9/5) + 32, 1)
    humidity = round(sense.get_humidity(), 1)
    
    return {
        'temperature': temperature_f,
        'humidity': humidity
    }