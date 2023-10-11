# app.py
from flask import Flask

app = Flask(__name__)

# Endpoint to generate a graph based on collected temperature data
@app.route('/graph')
def generate_graph():
  # Logic to generate a graph based on the collected temperature data
  # ...
  return 'Graph generated successfully'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
