const Pool = require('pg').Pool
const pool = new Pool({
    host: process.env.POSTGRES_HOST,
    user: process.env.POSTGRES_USER,
    password: process.env.POSTGRES_PWD,
    port: process.env.POSTGRES_PORT,
    database: process.env.POSTGRES_DB_NAME
})

const getUsers = (req, res) => {
    let str = 'SELECT * FROM users'
    pool.query(str, (err, results) => {
       res.status(200).json(results.rows) 
    })
}

const getProjects = (req, res) => {

    let str = 'SELECT * FROM projects INNER JOIN users ON assigned_to = user_id'
    if (req.query.category && req.query.assigned_to) {
        str+= ` WHERE category = '${req.query.category}' AND assigned_to = '${req.query.assigned_to}'`
    } else if (req.query.category) {
        str+= ` WHERE category = '${req.query.category}'`
    } else if (req.query.assigned_to) {
        str+= ` WHERE assigned_to = '${req.query.assigned_to}'`
    }

    pool.query(str, (err, results) => {
        if (err) throw err
        res.status(200).json(results.rows)
    })
}

const createProject = (req, res) => {
    const { title, category, assigned_to } = req.body

    pool.query("INSERT INTO projects(title, category, assigned_to) VALUES($1, $2, $3)",
        [title, category, assigned_to], (err, result) => {
            if (err) throw err
            res.status(201).send(`Project added`)
    })
}

const deleteProject = (req, res) => {
    const id = parseInt(req.params.id)

    pool.query('DELETE FROM projects WHERE project_id = $1', [id], (err, result) => {
        if (err) throw err
        res.status(200).send(`Project deleted with ID: ${id}`)
    })
}

module.exports = {
    getUsers,
    getProjects,
    createProject,
    deleteProject
}