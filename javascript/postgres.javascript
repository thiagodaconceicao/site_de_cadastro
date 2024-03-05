const express = require('express');
const { Client } = require('pg');

const app = express();
const port = 3000;

const client = new Client({
  host: 'localhost',
  port: 5432,
  database: 'Users',
  user: 'test',
  password: '12345',
  application_name: 'postgres'
});
