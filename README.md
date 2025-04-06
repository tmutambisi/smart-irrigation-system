# smart-irrigation-system

This project implements a soil moisture monitoring system using a DHT22 sensor for temperature and humidity measurements, a potentiometer (simulating a soil moisture sensor), and an LED to simulate a water pump. The system also includes a pushbutton for manual control of the pump.

Components Used
DHT22 Sensor: Measures temperature and humidity.
Potentiometer (ADC): Simulates soil moisture sensor.
LED: Represents the water pump.
Pushbutton: Allows manual control of the pump.
Microcontroller: (e.g., Raspberry Pi Pico) for running the code.
Features
Automatically controls the water pump based on soil moisture levels.
Manual override via a pushbutton to turn the pump on or off.
Monitors and displays temperature, humidity, and soil moisture readings.
Code Overview

Installation
Clone the repository

git clone https://github.com/tmutambisi/smart-irrigation-system.git

cd soil-moisture-monitor

Upload the code to your microcontroller using a suitable IDE (e.g., Thonny for Raspberry Pi Pico).
Connect the components according to the specified pins in the code.

Usage
Run the script on your microcontroller.
The system will automatically turn on the pump when the soil moisture level falls below the threshold.
Press the pushbutton to manually control the pump.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Thanks to the contributors and the open-source community for their support and resources.
