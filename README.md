# Setup & installation
- git clone https://github.com/SarangT123/Compute-engine-aka-amazon-lambda-using-python

### Thats it

# How to use


## How to run the server 
- In order to run the server type in `python3 main.py`


## How to add a function to the server
- You can use the cdn.py in this project to do that 
- To add a function first make a file which can contain your function in the `functions` folder
- Then you have to code the function (just the code without function name)
- After you are done you can do `python3 cdn.py add <function name> <function args> <filename which contains the function code>`
The function will be added to the server
- Try it out right now using `python3 cdn.py add sum a,b add.func`
### Please read the rules given at the end before making functions

## How to edit/remove the functions
- For now its impossible to just do it with just the cdn 
- Type in `python3 cdn.py editor`
- This will open your functions file in the nano text editor (edit on `website/config.py`)

### support issues
- Only supports gnome based versions
- Edit your terminal on the cdn.py file

## How to run functions and get output
- go to the url `http://<host>/run/<function>/<token>/<args(optional)>` or send a get request to the url


------------------------------

# rules & facts
- The function return type must be a string, dict, tuple, Response instance, or WSGI callable (user made funcs)
- The args always come in as strings it is adviced to convert them if needed and add checks for the types
- You can't name your functions the following - ping_server,ping,cust_funcs,TOKEN,config,flask,render_template, url_for, flash, redirect, session, request,FLASK,dotenv,load_dotenv,os,website,app,serverless_functions,views,functions etc
