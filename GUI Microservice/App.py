from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    graph_data = fetch_graph_data()
    return render_template('index.html', graph_data=graph_data)

def fetch_graph_data():
    try:
        response = requests.get('http://graph-generator-service/graph')
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f'Error fetching graph data: {e}')
        return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
