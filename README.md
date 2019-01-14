# Django_Chat_App

This is a basic django chat app using *Django channels* with good **UI**. Here, I followed [justdjango](https://github.com/justdjango/justchat) justchat example, followed first two tutorials.

#### My efforts:
* I have add timestamp to every message.
* Sorted recent 10 messages.
* Added django serializers for username, to remove quotes on frontend.
* Auto scroll down.
* Adjusted template veiw by using *jinja templating*, *css*, *javascript* (By using google debugging tool).


##### To run:

```
virtualenv env
source env/bin/activate
cd src
pip install -r requirements.txt
python manage.py makemigration
python manage.py migrate
python manage.py runserver
```

Please note this is **demo project** for learning purpose. 
