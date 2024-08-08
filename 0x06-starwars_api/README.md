0x06. Star Wars API
Description
This project is about fetching and displaying information about Star Wars characters based on a given movie ID. The task requires interacting with the Star Wars API to retrieve character names and print them in the same order as they appear in the "characters" list of the /films/ endpoint.

Learning Objectives
By completing this project, you will gain familiarity with:

Making HTTP requests in JavaScript using the request module.
Working with APIs and parsing JSON data.
Handling asynchronous operations in JavaScript using callbacks, promises, and async/await.
Using command-line arguments in Node.js.
Manipulating arrays and iterating through them in JavaScript.
Requirements
All code should be interpreted on Ubuntu 20.04 LTS using Node.js (version 10.14.x).
All files should be executable and end with a new line.
The first line of all files should be #!/usr/bin/node.
Code should adhere to semistandard compliance (AirBnB style with semicolons).
Use of var is not allowed.
Installation
Install Node.js 10
bash
Copy code
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
Install semistandard
bash
Copy code
$ sudo npm install semistandard --global
Install the request module
bash
Copy code
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
Usage
To run the script, use the following command:

bash
Copy code
./0-starwars_characters.js <Movie ID>
For example, to fetch characters from "Return of the Jedi" (Movie ID = 3):

bash
Copy code
./0-starwars_characters.js 3
This will output:

python
Copy code
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
...
Repository
GitHub repository: alx-interview
Directory: 0x06-starwars_api
File: 0-starwars_characters.js