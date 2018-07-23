# Sending-Mail

## Pre Requisites

**1) Python**

  Install python on your machine by following the intructions [from here](https://www.python.org/getit/)
  
**2) Python flask**

   For installing flask module simply open the command promot/terminal and run 
    
    > pip install flask
  
**3) Flask-Mail**
    Flask-Mail is python module for sending mails. Open your terminal/command prompt and simply run
    
    > pip install Flask-Mail
    
**4) MySQL**
  If you are on ubuntu platform just type the folowing commands
  
    > sudo apt-get update
  
    > sudo apt-get install mysql-server

For any other platform [visit here](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/)

Also install MySQLdb by running

    > apt-get install python-mysqldb
    
Run mysql on your machine and follow these steps:

1) Create a database
2) Use that database
3) Run the following two commands-

        > create table users(username varchar(50), email varchar(40));
        
        > create table userinformation(firstname varchar(20), lastname varchar(20), email varchar(40), username varchar(50), password varchar(50), confirmpassword varchar(50));

## Changes to be made in file

**1) db.py file**

    In line **#4** write your own **database name** and **password** of your database
 
**2) app.py file**

    In line #11 and line #34(in assignment to sender) write your own email address through which you want to send the email
    
    In line #12 write password for your mail
    
## Intructions to run the file

1) Go to the directory of the project.
2) Type the following command in terminal/command prompt
  
         python app.py 

# Note
Gmail doesn't allow you to send mail from unknown apps. So you wan't be able to send mails until and unless **"Allow less secure apps"** is set to **ON** from your gmail account through which you are sending mail. This feature can be turned on from settings
