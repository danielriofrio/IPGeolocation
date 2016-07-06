# IPGeolocation
Using free IP2GEOLOCATION database to locate external IPs. 

This project was developed by Daniel Riofrio. You can use this material as is.

This project allows the use of the free IP2GEOLOCATION dabase DB11 (https://lite.ip2location.com), 
to enrich external IP addresses information with their geolocation. 

This project includes:

  dr_dbscript.sql -> a script to create the table ipgeolocationinfo into PostGreSQL.

  dr_uploadCSVtoDB.py -> a python script to upload the CSV database from IP2GEOLOCATION.

  dr_getIPInfo.py -> a simple python script to query any IP. 
  
  dr_dbconnection.py -> a postgresql python script for handling the data. 
