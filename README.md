# A simple api for cell data
This project is done with flask in python and takes the form of a simple rest api

## How to use this project
There's two mai nway of running this project, you can run it manually on your host machine :
1. run```pip install requirements.txt```
2. run ```python app.py```

Or you can run it contenarized in docker, to do so:
1. run ```docker build -t flask-project .```
2. run ```docker run --name flask-project-image -p 80:80 flask-project```

## Sample requests

A sample request would look like this :

```curl http://localhost/api\?q\=10%20rue%20du%20renard%20rouen```

And a sample response would look like that :

```
{
"SFR": {"2G": true, "3G": true, "4G": true},
"Orange": {"2G": true, "3G": true, "4G": true},
"Free": {"2G": false, "3G": true, "4G": true},
"Bouygue":{"2G": true, "3G": true, "4G": true}
}
```

## Values you can change

If you open [app.py](app.py)  you'll find a bunch of global variables you can modify to tweak the fonctionnalities of the API

precision value, which is set by default to 500, reducing that number will increment the precision of the results but may risk to certain query having no results

there's also path_to_csv which let's you easily swap the csv used for cell data