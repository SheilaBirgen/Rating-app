# Awwards
## Description
Awwards is an app where users can upload their site links and can be rated on the basis of usability,design and appearance

##### Download any text editor of your choice, either Sublime, Visual-Studio-Code or Atom.
##### Install your preferred version of python
  - ```sudo apt-get install python3.7```.
  - ```python --version``` to confirm that python has been installed.
##### Open the command-line and run the following command to open a directory:
  - ```cd your preferred directory``` => ```cd Desktop```
##### Git clone the project on your current directory by:
  - ```https://github.com/SheilaBirgen/Django-2```.
##### Move to your project directory:
- ```cd Django-2```.
##### Open the project on your terminal:
  - ```atom . or code .``` , according to the type of your text editor.
##### Install virtual environment using python:
  - ```python3.7 -m venv virtual```, check your project to confirm you have a folder called virtual,
  - then activate it by running ```source virtual/bin/activate```
##### To install the packages in the ```requirements.txt file```,
  - ```pip install -r requirements.txt```  That will install all packages including Django.
##### To open python shell:
  - ```python3.7``` ,
  - ```import django```
  - And lastly ```django.get_version()``` to see and confirm the version of django installed.
  - You can then ```ctrl z``` to get out of the shell,
##### After ensuring you have all the above
  - ```python3 manage.py runserver``` to run the project.
  - Then click the local host link given to open the project on a browser ```http://127.0.0.1:8000/```.

### BDD

| Behaviour | Input | Output |
| --------- | ------| ------ |
|On loading the app you see the landing page with a navbar at the top and a sign up form| Click `register if its a new user` and `login`if registered | You are redirected to the landing page if you had left the page or just loads the landing page again if you are still on the landing page.|
|Clicking the `submit project` link on the navbar | Mouse click |You are redirected to a page where various posts are displayed.|
|Clicking the `Logout`| Mouse click | Displays the `Home` and `logout` links you are logged in`login`.|

## Technologies Used

- dj-database-url==0.5.0
- Django==1.11
- django-bootstrap3==12.0.3
- django-heroku==0.3.1
- Pillow==7.0.0
- psycopg2==2.8.4
- python-decouple==3.3
- whitenoise==5.0.1
## Database Screenshot
![](media/db-screenshot.png)

## Known Bugs
update of profile pictures isn't working currently

## Support and contact Details
You can reach out to me through the github account SheilaBirgen
or on my email as jeronobergen@gmail.com

## CodeBeat Badge

## License
@2019 Sheila Birgen 
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)