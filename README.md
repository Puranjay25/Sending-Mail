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

## Changes to be made in file

**1) db.py file**
    In line **#4** write your own **database name** and **password** of your database
 
**2) app.py file**
    In line **#11** and line **#34**(in assignment to *sender*) write your own email address through which you want to send the email
    In line **#12** write password for your mail

# Note
Gmail doesn't allow you to send mail from unknown apps. So you wan't be able to send mails until and unless **"Allow less secure apps"** is set to **ON** from your gmail account through which you are sending mail. This feature can be turned on from settings
