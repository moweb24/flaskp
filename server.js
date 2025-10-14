const express = require("express");
const axios = require("axios");
const app = express();
app.use(express.json());

app.get("/", (req, res) => {
  res.send(`<form method="post" action="/submit">
              <input name="name" placeholder="Name"/>
              <input name="desc" placeholder="Description"/>
              <button type="submit">Send</button>
            </form>`);
});

app.post("/submit", async (req, res) => {
  const data = { item: "Sample item", desc: "Sample desc" };
  try {
    const r = await axios.post("http://localhost:5000/submit", data);
    res.json(r.data);
  } catch (err) {
    res.status(500).send(err.toString());
  }
});

app.listen(3000, () => console.log("Frontend on 3000"));
