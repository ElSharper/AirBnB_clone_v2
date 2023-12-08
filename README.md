# 0x02. AirBnB clone v2
  - MySQL
    > *Group project* *Python* *OOP* *Back-end* *SQL* *MySQL* *ORM* *SQLAlchemy*
  - Web Framework
    > *Python* *Back-end* *Webserver* *Flask*

## Usage
- First clone this repository.

- To run it:
  - Using `DBStorage`, Locate the "console.py" file and run it as follows:
  ```
  $ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
  ```
  - Using `FileStorage`, Locate the "console.py" file and run it as follows:
  ```
  $ ./console.py
  ```
- When this command is run the following prompt should appear:
```
(hbnb)
```
- This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

## Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

## Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

  #### Create
  `create <class name>`
  Ex:
  `create BaseModel`

  #### Show
  `show <class name> <object id>`
  Ex:
  `show User my_id`

  #### Destroy
  `destroy <class name> <object id>`
  Ex:
  `destroy Place my_place_id`

  #### All
  `all` or `all <class name>`
  Ex:
  `all` or `all State`

  #### Quit
  `quit` or `EOF`

  #### Help
  `help` or `help <command>`
  Ex:
  `help` or `help quit`

## Alternate Syntax
Additionally the console supports 
- ##### `<class name>.<command>(<parameters>)` syntax.
  **Ex:** `City.show(my_city_id)`
- #### Named Parameters
  ##### `<command> <class name> (<named_parameters>)` syntax.
  **Ex:** `create Amenity name="WiFi"`
