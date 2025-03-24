# OrderBot Project
The project to track new orders on exchanges and notify the user with a telegram bot about it

## Navigation

- [Required packages](#required-packages)
- [Installation](#installation)

## Required Packages
You can see the required packages in the requirements.txt file

## Installation
To install this repository, use:
```
git clone https://github.com/Razraab/orderbot.git
```

For a complete installation and a project ready to run, you need:
1. Create virtualenv to separate the dependencies of this project from the other installed packages on the machine. Command for this:
```
python3 -m venv .venv
```
2. Activate virtualenv and install the required packages:

    - On Unix systems:
    ```bash
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
    - On Windows

    ```cmd
    .venv\Scripts\activate
    pip install -r requirements.txt
    ```
3. To run the project on your bot, you must also create an .env file in the root of the project, here is a template for this file:
```bash
TOKEN="YOUR_TOKEN"
DB_CONNECTION_STRING="YOUR_DB_CONNECTION_STRING"
REDIS_URL="YOUR_REDIS_URL"
# Other settings
```
4. Now we can run the bot, if your OS is Windows you can run the run.bat file or run.sh if you are in a Bash terminal (virtualenv must be named .venv otherwise the scripts will not run). Alternatively you can run the src/main.py file with virtualen activated
