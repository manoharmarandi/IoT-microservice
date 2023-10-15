import plotly.graph_objects as go
import requests

def fetch_data_from_iot_edge(device_id):
    # Fetch data from the IoT Edge device
    url = f"http://{device_id}/data"
    response = requests.get(url)
    data = response.json()
    return data

def display_graph(data):
    # Extract x and y values from the data
    x = [item['timestamp'] for item in data]
    y = [item['value'] for item in data]

    # Create a line graph using Plotly
    fig = go.Figure(data=go.Scatter(x=x, y=y))
    fig.show()

def main():
    # Prompt the user to choose a data source
    data_source = input("Choose a data source (1. IoT Edge Device): ")

    if data_source == "1":
        device_id = input("Enter the IoT Edge device ID: ")
        data = fetch_data_from_iot_edge(device_id)
        display_graph(data)
    else:
        print("Invalid data source.")

if __name__ == "__main__":
    main()
