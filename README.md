## Log Analysis, the third project in Udacity Full Stack Development Environment
1st Project in Udacity NanoDegree Program


## Project Overview 
Your task is to create a reporting tool that prints out reports (in plain text) 
based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.


## Steps to Run the Program

1. If you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.
2. Next, download the data from [this](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). 
   You will need to unzip this file after downloading it. The file inside is called 
   newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
3. To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
4. Run python log-results.py

#Log Output is: 

        Candidate is jerk, alleges rival - 338647 views for Question above
        Bears love berries, alleges bear - 253801 views for Question above
        Bad things gone, say good people - 170098 views for Question above

#The most popular article authors of all time:

        Ursula La Multa - 507594 views for Question above
        Rudolf von Treppenwitz - 423457 views for Question above
        Anonymous Contributor - 170098 views for Question above
        Markoff Chaney - 84557 views for Question above

#Days with more than 1% of requests lead to errors:

        2016-07-17 - 2 views for Question above
