-------------------------------------------------------------
V 0.1 SW MINIPROJECT -- 9/9/18
CASEY KUROSAWA
-------------------------------------------------------------

OVERVIEW

 - DESIGN SYSTEM THAT COLLECTS AND STORES TEMPERATURE AND HUMIDITY DATA

 - REQUIRED FEATURES:
 	- AUTHENTICATION
 	- CLOUD STORAGE
 	- MULTIPLE USERS (SIMULTANEOUS ACCESS?)
 	- MULTIPLE STATS PER USER

 - 5 MODULES
 	- MAIN INTERFACE
 	- AUTHENTICATION
 	- CLOUD DATABASE
 	- TEMPERATURE MODULE
 	- HUMIDITY MODULE

TEMP MODULE
-------------------------------------------------------------
TEMPERATURE CONSIDERATIONS
HIGHEST RECORDED AIR TEMPERATURE -> 134F
LOWEST RECORDED AIR TEMPERATURE -> -128.6F
-------------------------------------------------------------

HUMID MODULE
-------------------------------------------------------------
HUMIDITY DATA - ABSOLUTE, RELATIVE OR SPECIFIC
RELATIVE HUMIDITY : 0% - 100% (1% IS LOWEST RECORDED ON EARTH), OVERSATURATION POSSIBLE IN HIGH ATMOSPHERE

DEW POINT
HIGHEST RECORDED DEW POINT - 95F
LOWEST ???
-------------------------------------------------------------

TECH
-------------------------------------------------------------
CLOUD SERVICES : AMAZON WEB SERVICES, MICROSOFT AZURE, GOOGLE CLOUD, ?ORACLE DATABASES?
      -FIRST 3 OFFER FREE TRIALS
NETWORK COMMUNICATION : JSON (?BSON?), XML, PLAINTEXT
LOGIN SERVICES : GOOGLE, FACEBOOK, SSH, OTHER?
FRONTEND : TERMINAL?, PYTHON
-------------------------------------------------------------

METRICS
-------------------------------------------------------------
???
COMPARE DATA SENT W/ DATA OBSERVED?
-------------------------------------------------------------

SENSOR SIM
-------------------------------------------------------------
MININET W/ PERIODIC PINGS
UPLOAD RANDOM DATASHEET
-------------------------------------------------------------
