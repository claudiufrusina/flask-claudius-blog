# flask-claudius-blog
This is My first project written in python using Flask framework.

For the first time during the setup you should run the command: 
    pip install -r requirements.txt.
This command will download for you all the dependencies is needed.
Then add a new .env file in where you need to put a parameter called SECRET_KEY=... a hash key generated for example by running in your cmd:
    python
    >>> import uuid
    >>> print(uuid.uuid4().hex)
    then you should copy that hash into the .env
    like this : SECRET_KEY=askjdbkasdkasn212ekjbdkjbaaf....

Remember that this hash will be use for crypting the password when this will be insert into the User table by SQLite.
(Passwords should be always encrypted into your db for security reason because if somebody compromise your server and stole your .db file they should know your users password! So this is always a best practice to encrypt your data)
Finally, for running this application you could use the Visual Studio Debugger( because it is alrealy detected as Flask app) or from your cmd with the command : Flask run

If your purpose is to deploy the blog on a VPS is raccomanded to execute che command for installing all the dependencies needed on a VPS running Ubuntu:

>> sudo apt-get install python3-pip python3-dev python3-venv build-essential libssl-dev libffi-dev python3-setuptools supervisor nginx 

Then, is you wish you could create a new user named flask
for the deploy, add it to sudo group and create a virtual enviroment in python then active it:
>> adduser flask
>> gpasswd -a flask sudo
>> su - flask
>> python3 -m venv venv
>> source venv/bin/activate