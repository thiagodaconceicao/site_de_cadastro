import { Client } from 'pg';

const client = new Client({
  host: 'localhost',
  port: 5432,
  database: Users,
  user: thiago,
  password: tgc20059,
  application_name: postgres

})

await client.connect()


