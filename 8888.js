const express = require('express');
const app = express();
const http = require('http');
const hostname = '127.0.0.1';
const port = 8888;

const server = http.createServer((req, res) =>{
	res.statusCode = 200;
	res.setHearder('Content-Type', 'text/plain');
	res.end('Hello World\n');
});

server.listen(port, hostname, () =>{
	console.log('Server running at http://${hostname}:${port}/');
});

//app.get('/', (req, res) => res.send('Hello World!'));

//app.listen(port, () => console.log('Example app listening on port ${port}!'));
