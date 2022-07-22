const express = require('express')
const cors = require('cors')
const bodyParser = require('body-parser')
const app = express()
const PORT = 3000

const db = require("./queries")

app.use(bodyParser.json())
app.use(
    bodyParser.urlencoded({ extended: true })
)

app.use(cors())

app.get('/', (req, res) => {
    res.json({info: "API is running"})
})

app.get('/users', db.getUsers)
app.get('/projects', db.getProjects)
app.post('/projects', db.createProject)
app.delete('/projects/:id', db.deleteProject)

app.listen(PORT, () => {
    console.log(`API is running on port ${PORT}`)
})