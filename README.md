# Notes

## Basic
to run python code from command line just run
>>python
or 
>>python3 
then you will be able to run commands

otherwise python comes with idle which you can run commands from too

other data structures:

## Tuples:
- tuples like list but u cant change items in it
- you could use it to return multiple items of different types from a function
- the items in it dont need to be the same type

## Sets:
- can be mutated 
- dont maintain order you set for them (it orders items itself)
- cant have duplicates (if there is duplicates in it, it deletes them)
- can also do set theory on them eg intersection, union, difference (set 1 minus the items that are in set 2 that are also in set1)
- can also create a set out of a list

## Dictionaries:
- Kinda like maps
- Also ordered
- can be mutates
- labelled data (keys)
- Cant have duplicate keys (can have duplicate values)
- can add to update etc
- Values can be of diff types but key same type
- uses - imagine where you would want coums or something or key values that you might want to access by name

## Complex functions
- you can have nestes functions which have accessto all variabels inside prent function
- you can assign params default valuesto make them optional
- you can pass in args to accept moore args
- you can pass in kwargs to accept key value args and you caqn chek if they were passed in in the function

## Classes
- use snake case to define functions and variables and camal case for classes
- init methos is called a dundar method &  it has the underscores cus u dont normally call it directly ()when u instantiate class)
- prperty decorator makes the method not callable - you just referewnce like variable

## Managing venvs
- using pipenve
> pip install pipenv
navigate to project where you want the venv in
> pipenv --help
 will gie you command to run to create venv - also creates pipfile in venv which shows python version and packages and pipfile.lock which is for pipenv to know whether things are up to date & dependnencies
> pipenv --python3.7 eg
# install to this venv
> pipenv install flask
Then you have to activate the python venv and this is where you un your commands from eg running the program eg if you run python you should see the version your on
> pipenv shell
uninstall lib plus all dependencies
> pipenv uninstall package_name
get out of venv
> exit 

## Data analysis 
free data sets: https://github.com/mwaskom/seaborn-data
flask docs: http://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application
command to run flask app: $ flask --app hello run
databases:
- SQLite: test file goo or quick db development but not to be used in pro
- PostgreSQL and MySQL: open source good for prod
- various noSQL
with flask use SQLAlchemy which is orm library (write db code in python)
deployment options for python: PythonAnywhere and Heroku
