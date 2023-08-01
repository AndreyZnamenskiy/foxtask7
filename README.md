# Task 7 - Report of Monaco 2018 Racing

## Package info
Web version of Monaco Race Report.  Based on Flask framework 

DEMO available here https://azn-foxtask7.onrender.com/

##  TASK TEXT:
### Task 7 - Web report of Monaco 2018 Racing
Write a web application using Flask framework and your previous report package.

The application has to have a few routes. E.g.

http://localhost:5000/report shows common statistics

http://localhost:5000/report/drivers/  shows a list of driver's names and codes. 

The code should be a link to info about drivers

http://localhost:5000/report/drivers/?driver_id=SVF shows info about a driver

Also, each route could get the order parameter

http://localhost:5000/report/drivers/?order=desc

Use jinja2 package for html template.

Write tests using Unittest module or py.test. Test status code and key components on the page

Add requierements.txt with a list of required packages. (Edited 07.11.2022)
Resources:

* Flask https://flask.palletsprojects.com/en/1.1.x/
* Jinja https://jinja.palletsprojects.com/en/2.11.x/
* The Python Requirements File and How to Create it  https://learnpython.com/blog/python-requirements-file/
* Beautiful Soup https://beautiful-soup-4.readthedocs.io/en/latest/
