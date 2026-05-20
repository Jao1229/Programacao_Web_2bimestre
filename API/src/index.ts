import express from 'express'
import produtosRouter from './route/produtos.route.js'
import { drizzle } from 'drizzle-orm/better-sqlite3'
import { migrate } from 'drizzle-orm/better-sqlite3/migrator'
import Database from 'better-sqlite3'
import * as schema from './db/schema.js'
const sqlite = new Database('produtos.db')
export const db = drizzle({ client: sqlite, schema })
// Aplica migrations pendentes ao carregar o módulo
migrate(db, { migrationsFolder: './drizzle' })
const app = express()
const port = 3000
app.use(express.json())
// registro de rotas
app.use('/produtos', produtosRouter)
app.listen(port, () => {
console.log(`Servidor rodando em http://localhost:3000`)
})