# The Pup House Inn #

To run this application on your own machine:

1. Make sure Python 3 and virtualenv are installed on your computer. If you don't have Python 3, you are on a macOS, and have brew installed you can run: 

	```brew install pyton3``` 

	If you have none of the above installed you can download python 3 from [here](https://www.python.org/downloads/). I recommend installing [brew](https://brew.sh/) if you're on macOS to install python 3. 

	Once Python 3 is installed to get virtualenv installed run:

	```pip3 install virtualenv``` 


2. Create a virtual enviornment:

	```virtualenv -p python3 nameofenv```

3. Activate the virtualenv by changing into the directory that was just created by the virtualenv ```nameofenv``` and run:

	```source bin/activate```

4. Once the virutalenv is activated we need to install Django 2.0.4
 
 	```pip install Django==2.0.4```

5. Create a directory in the virutalenv called ```src``` - it can be named anything you want - and clone the repo into the created directory.

6. Change into the newly created directory and run:
	
	```./manage.py runserver```.

7. Navigate to ```localhost:8000``` in your web browser.