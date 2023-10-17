const express = require('express');
const { createCanvas } = require('canvas');
const Chart = require('chart.js');

const app = express();
const port = 3000;

// Define the route to serve the index.html file
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

// Create a chart instance
const canvas = createCanvas(400, 200);
const ctx = canvas.getContext('2d');
const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [],
    datasets: [
      {
        label: 'Temperature',
        data: [],
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1,
      },
      {
        label: 'Humidity',
        data: [],
        backgroundColor: 'rgba(192, 75, 192, 0.2)',
        borderColor: 'rgba(192, 75, 192, 1)',
        borderWidth: 1,
      },
    ],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
  },
});

// Update the chart with new data
function updateChart(temperature, humidity) {
  chart.data.labels.push(new Date().toLocaleTimeString());
  chart.data.datasets[0].data.push(temperature);
  chart.data.datasets[1].data.push(humidity);

  // Limit the number of data points shown on the chart
  const maxDataPoints = 10;
  if (chart.data.labels.length > maxDataPoints) {
    chart.data.labels.shift();
    chart.data.datasets[0].data.shift();
    chart.data.datasets[1].data.shift();
  }

  // Update the chart
  chart.update();
}

// Route to receive data from the IoT device
app.post('/', (req, res) => {
  const { temperature, humidity } = req.body;
  updateChart(temperature, humidity);
  res.sendStatus(200);
});
