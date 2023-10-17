from sense_hat import SenseHat
import time
import requests
from azure.iot.device import IoTHubDeviceClient, Message

sense = SenseHat()

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

def show_t():
    sense.show_letter("T", back_colour=red)
    time.sleep(.5)

def show_p():
    sense.show_letter("P", back_colour=green)
    time.sleep(.5)

def show_h():
    sense.show_letter("H", back_colour=blue)
    time.sleep(.5)

def update_screen(mode, show_letter=False):
    if mode == "temp":
        if show_letter:
            show_t()
        temp = sense.temp
        temp_value = temp / 2.5 + 16
        pixels = [red if i < temp_value else white for i in range(64)]
    elif mode == "pressure":
        if show_letter:
            show_p()
        pressure = sense.pressure
        pressure_value = pressure / 20
        pixels = [green if i < pressure_value else white for i in range(64)]
    elif mode == "humidity":
        if show_letter:
            show_h()
        humidity = sense.humidity
        humidity_value = 64 * humidity / 100
        pixels = [blue if i < humidity_value else white for i in range(64)]
    sense.set_pixels(pixels)

show_t()
show_p()
show_h()

update_screen("temp")

index = 0
sensors = ["temp", "pressure", "humidity"]

connection_string = "[Your IoT Hub Edge device connection string]"
application_url = "https://kits-test-1.azurewebsites.net/"

def send_data_to_application(data):
    try:
        response = requests.post(application_url, json=data)
        if response.status_code == 200:
            print("Data sent to application")
        else:
            print("Failed to send data to application")
    except Exception as e:
        print("Failed to send data to application:", str(e))

def send_data_to_iot_hub(data):
    try:
        client = IoTHubDeviceClient.create_from_connection_string(connection_string)
        message = Message(data)
        client.send_message(message)
        print("Message sent to Azure IoT Hub")
    except Exception as e:
        print("Failed to send message to Azure IoT Hub:", str(e))

while True:
    selection = False
    events = sense.stick.get_events()
    for event in events:
        if event.action != "released":
            if event.direction == "left":
                index -= 1
                selection = True
            elif event.direction == "right":
                index += 1
                selection = True

    if selection:
        current_mode = sensors[index % 3]
        update_screen(current_mode, show_letter=True)
        data = {"mode": current_mode}
        send_data_to_application(data)
        send_data_to_iot_hub(data)
    else:
        current_mode = sensors[index % 3]
        update_screen(current_mode)
        data = {"mode": current_mode}
        send_data_to_application(data)
        send_data_to_iot_hub(data)
