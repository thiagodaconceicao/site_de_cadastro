//const express = require('express');
const { Client } = require('pg');

//const app = express();
//const port = 3000;

const client = new Client({
  host: 'localhost',
  port: 5432,
  database: 'Users',
  user: 'test',
  password: '12345',
  application_name: 'postgres'
});

client.connect()
console.log('Connected to postgres');

const UserGet = async (email, password) => {

  const query = {
    text: 'INSERT INTO users (email, password) values ($1, $2)',
    VALUES: [email, password],
  };

  const result = await pool.query(query);
  console.log("User added to database");
  return result;
};

