import os
import json
from azure.iot.device import IoTHubDeviceClient

# Create an instance of the IoT Hub device client
device_client = IoTHubDeviceClient.create_from_connection_string(os.getenv("IOT_HUB_CONNECTION_STRING"))

def fetch_temperature_data():
    try:
        # Send a message to the Temperature Data Collector Microservice
        message = {
            "command": "fetch_temperature_data"
        }
        device_client.send_message_to_output(json.dumps(message), "temperatureDataOutput")

        # Wait for the response from the Temperature Data Collector Microservice
        response = device_client.receive_message_on_input("temperatureDataInput")
        if response:
            return response.data.decode("utf-8")
        else:
            return "Error: No response received"
    except Exception as e:
        print(f"Error fetching temperature data: {e}")
        return "Error: Failed to fetch temperature data"

if __name__ == "__main__":
    device_client.connect()

    app.run(host="0.0.0.0", port=5000)
