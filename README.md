# serve-this-app

Very simple command line tool to help you start your developpement webapp with a free port

## Installation

Since it's a python package : 

```
python setup.py install
```

This command may require super-user privilege to install at system level


## Usage

The ``servie-this-app`` command is pretty simple : it add a random free port at the end of the commands you passed as parameter

For exemple : 

```
serve-this-app myapp_server -p
```

Will be executed as : 

```
myapp_server -p <random_free_port>
```

You can also add a ``-s`` or ``--stick`` option if the port number need to be sticky with the initial commands, for exemple with django app :

```
serve-this-app ./manage.py localhost: -s
```

This will be executed as :

```
./manage.py localhost:<random_free_port>
```

*NB:* ``serve-this-app`` will prompt the used port
