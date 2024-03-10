const { Client } = require('pg');

const client = new Client({
  host: 'localhost',
  port: 5432,
  database: 'Users',
  user: 'teste',
  password: '12345',
});

client.connect();

