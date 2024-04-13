<h1>COMP 3005 - Final Project V2</h1>
<hr/>
<h2>Setup:</h2>

Use the provided ddl.sql and dml.sql found in the SQL folder to populate the database.
It will create all the tables needed for the project and populate them with base data

The database must be created manually first.

The following python packages will need to be installed:

```pip install psycopg```
```pip install "psycopg[binary,pool]"```

Once installed the global variables for DBNAME, USER, PASSWORD, HOST, PORT will need to be edited in database_connection.py.
These variables are located at the top of the script.
Replace variables with the appropriate values for your setup.

Once all of this is done the python script should be ready to run

<hr/>
<h2>Running:</h2>
You can simply run the python script using the following command

```
python3 main.py
```

You'll be greeted with a menu providing the following 5 option:
```
Health and Fitness Club login

1 - Authenticate as User
2 - Authenticate as Trainer
3 - Authenticate as Admin
4 - Register for User account
q - Quit
```
You can select any of these options and then follow the prompts. 

You can use these accounts to login:
<ul>
<li>USER ACCOUNTS</li>
<li>Email: "jane@gmail.com" Password: "jane"</li>
<li>Email: "jim@gmail.com" Password: "jim"</li>
<li>Email: "john@gmail.com" Password: "john</li>
<li>Email: "sarah@gmail.com" Password "sarah"</li>
</ul>
<ul>
<li>TRAINER ACCOUNTS</li>
<li>Email: "tim@fitness.com" Password: "tim"</li>
<li>Email: "kyle@fitness.com" Password: "kyle"</li>
<li>Email: "abby@fitness.com" Password: "abby"</li>
<li>Email: "sam@fitness.com" Password "sam"</li>
</ul>
<ul>
<li>ADMIN ACCOUNTS</li>
<li>Email: "justin@fitness.com" Password: "justin"</li>
<li>Email: "paul@fitness.com" Password: "paul"</li>
<li>Email: "hailey@fitness.com" Password: "hailey"</li>
</ul>

<hr/>
Youtube Link: https://youtu.be/JqqtIvBXp4s