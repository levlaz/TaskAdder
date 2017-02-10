# TaskAdder
Desktop Utility to add Tasks to your Kanboard from any context.

# Installation

This app has only been tested on Ubuntu 16.04 LTS with Unity. Your mileage may vary if you are using another OS.

## Requirements

* python3
* python3-tk
* python3-pip

You can install these with

```
sudo apt install python3 python3-tk python3-pip
```

## Installing with Pip

Once you have the pre requisites you can install this application with:

```
pip3 install git+https://github.com/levlaz/TaskAdder
```

# Configuration

You should create a config file called `.taskadder.cfg` with the following contents:

```
[auth]
url: $your_kanboard_url
token: $your_api_token
project: $your_project_id
```

# Usage

You can open up taskadder by typing in `taskadder` in the terminal. I have `Control+Space` bound to open up taskadder from any context so I can quickly dump a todo item and move on with whatever I am doing.



