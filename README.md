# NLP2SQL

This project was built to help people use normal english to get what they want from the database. Our aim is qute high but 
frankly, our project needs a lot of improvement to reach this goal. We can use this application in railway services where the user may type in their question and it should be able to return the answer by interacting with database. This project currently supports English only. 

	python:- 3.7
	OS:- Ubuntu 16.04

	Libraries:-

	1. MySQLdb
	2. speech_recognition

Currently the databaseis fixed to school.sql in database_store folder. If you want to use a different SQL database, you can 
change it in the program or change the school.sql file. 


To run the program, you have 2 methods:- 

1. Through the Command line by running main.py

    	python3 main.py 
	
    	'-d', '--database'    - Path to SQL dump file
    
    	'-l', '--language'    - Path to language configuration file
    
    	'-j', '--json_output' - path to JSON output file
    
    	'-t', '--thesaurus'   - path to thesaurus file
    
    	'-s', '--stopwords'   - path to stopwords file
	
     	'-i', '--sentence'    - Input sentence to parse

2. Through the gui by running nlp2sql_with_gui.py using commandline when terminal/commandline is open in NLP2SQL Folder

   		python3 nlp2sql_with_gui.py 

   or running this file in your IDE.
   
   
## Reference -
   
Our inspiration, architecture and some part of the code base is from https://github.com/FerreroJeremy/ln2sql 
