# A WhatsApp Web Clone Chat Application for those developers that like to use Django Channel for handling WebSocket request

[![Django CI](https://github.com/codingelle/django-whatsapp-web-clone/actions/workflows/django.yml/badge.svg)](https://github.com/codingelle/django-whatsapp-web-clone/actions/workflows/django.yml)

## Demo

#### Login User1 
* Url: https://demo.josnin.dev/django-whatsapp-clone/admin/login/ (Use Chrome Browser)
* Login: johnny2020
* Pass: johnny2020

#### Login User2 
* Url: https://demo.josnin.dev/django-whatsapp-clone/admin/login/ (Use Microsoft Edge or any browser except Chrome)
* User: jay1234
* Pass: jay1234

#### Start Chat
##### Make sure to login using User1 or User2
https://demo.josnin.dev/django-whatsapp-clone/chat/2/



## Send GIFs by GIPHY

![ezgif-7-8f0423e40e28](https://user-images.githubusercontent.com/3206118/141478058-df2f4ebb-f7f1-4666-b084-a14bcb98634e.gif)


## Screenshot of 2 users exchanging message

![image](https://user-images.githubusercontent.com/3206118/91178093-3e144000-e717-11ea-9e3b-ef16b0c40ef0.png)


## Screenshot Sharing blob image
![image](https://user-images.githubusercontent.com/3206118/93725153-66407300-fbdf-11ea-9c6e-be0ddaab869d.png)


## Screenshot Loading & Save message
![image](https://user-images.githubusercontent.com/3206118/97063435-4df2b800-15d2-11eb-9ea9-abedad56a493.png)



## Installation
```
cd django-whatsapp-web-clone/

python3.7 -m venv env
. env/bin/activate
pip install -r requirements

```

## How to run development server?

#### create all the required tables
```
python manage.py migrate
```

#### create superuser
```
python manage.py createsuperuser
```

#### start redis service using podman
```
podman run -p 6379:6379 -d redis:5
```

### create .env file 

add the following variable & replace it based on your own development keys

API_KEY=YourOwnGiphYAPIKeysdfasjfdgdf

SECRET_KEY=YourOwnSecretKey71041jkfohdslflasdfjhaljdfa


#### run the development server
```
python3 manage.py runserver
or
daphne -b 0.0.0.0 -p 8088 django_channel_tutorial.asgi:application

```

### Youtube video tutorial

[Youtube](youtu.be/zv7ra-xw1mu)


### Help

Need help? Open an issue in: [ISSUES](https://github.com/josnin/django-whatsapp-web-clone/issues)


### Contributing
Want to improve and add feature? Fork the repo, add your changes and send a pull request.


