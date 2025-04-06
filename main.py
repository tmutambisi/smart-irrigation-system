from machine import Pin, ADC
import dht
import time

# Initialize DHT22 sensor
dht_sensor = dht.DHT22(Pin(15))

# Initialize potentiometer (simulating soil moisture sensor)
soil_moisture = ADC(Pin(26))

# Initialize LED (simulating water pump)
pump = Pin(14, Pin.OUT)

# Initialize pushbutton for manual control
button = Pin(16, Pin.IN, Pin.PULL_DOWN)

# Threshold for soil moisture
MOISTURE_THRESHOLD = 200

while True:
    # Read temperature and humidity from DHT22
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()

    # Read soil moisture level
    moisture_level = soil_moisture.read_u16()

    # Check if button is pressed
    manual_override = button.value()

    # Control pump based on moisture level or manual override
    if manual_override or moisture_level < MOISTURE_THRESHOLD:
        pump.value(1)  # Turn pump ON
        pump_status = "ON"
    else:
        pump.value(0)  # Turn pump OFF
        pump_status = "OFF"

    # Print sensor readings and pump status
    print(f"Temperature: {temperature:.1f}°C")
    print(f"Humidity: {humidity:.1f}%")
    print(f"Soil Moisture Level: {moisture_level}")
    print(f"Pump Status: {pump_status}")
    print("-" * 30)

    time.sleep(2)
