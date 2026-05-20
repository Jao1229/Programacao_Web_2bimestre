import { sqliteTable, integer, text, real } from 'drizzle-orm/sqlite-core'
export const produtos = sqliteTable('produtos', {
id: integer('id').primaryKey({ autoIncrement: true }),
nome: text('nome').notNull(),
preco: real('preco').notNull(),
})
export type Produto = typeof produtos.$inferSelect 
export type NovoProduto = typeof produtos.$inferInsert 