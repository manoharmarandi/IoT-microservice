// App.js
import React, { useEffect, useState } from 'react';

function App() {
  const [graphData, setGraphData] = useState('');

  useEffect(() => {
    // Fetch the graph data from the Graph Generator Microservice
    fetch('/graph')
      .then(response => response.text())
      .then(data => setGraphData(data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1>Temperature Data Graph</h1>
      <div>{graphData}</div>
    </div>
  );
}

export default App;
