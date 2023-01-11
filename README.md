# flask-claudius-blog
My first project written in python using Flask framework.

For the first time during the setup you should run the command: pip install -r requirements.txt.
This command will download the dependencies.
Then add a .env file in where have to put the parameter called SECRET_KEY= a hash key generated for example : 
    python
    >>> import uuid
    >>> print(uuid.uuid4().hex)
    then you should copy the that hash into the .env

Remember that this hash will be use for crypting the password when this will be insert into the User table using SQLite.
Finally for running the app the Visual Studio Debug or from cmd launch : Flask run .