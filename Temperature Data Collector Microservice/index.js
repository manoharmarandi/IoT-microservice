// index.js
const express = require('express');
const app = express();
const port = 3000;

// Endpoint to collect temperature data
app.post('/temperature', (req, res) => {
  // Logic to collect temperature data from Azure IoT and store it in a database
  // ...
  res.send('Temperature data collected successfully');
});

app.listen(port, () => {
  console.log(`Temperature Data Collector Microservice listening at http://localhost:${port}`);
});
