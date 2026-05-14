const express = require("express");
const os = require("os");

const app = express();

app.get("/", (req, res) => {
  res.send(`
    <h1>Multi-Architecture Docker Demo</h1>
    <p>Node.js app successfully containerized using Docker Buildx</p>
    <p>Running on architecture: ${os.arch()}</p>
  `);
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});