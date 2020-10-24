# A WhatsApp Web Clone Chat Application for those developers that like to use Django Channel for handling WebSocket request


## Screenshot of 2 users exchanging message

![image](https://user-images.githubusercontent.com/3206118/91178093-3e144000-e717-11ea-9e3b-ef16b0c40ef0.png)


## Screenshot Sharing blob image
![image](https://user-images.githubusercontent.com/3206118/93725153-66407300-fbdf-11ea-9c6e-be0ddaab869d.png)


## Screenshot Loading & Save message
![image](https://user-images.githubusercontent.com/3206118/97063435-4df2b800-15d2-11eb-9ea9-abedad56a493.png)



## Installation
```
cd django-whatsapp-web-clone/requirements

python3 -m pip install requirements

```

## How to run development server?

#### create all the required tables
```
python3 manage.py migrate
```

#### start redis service
```
docker run -p 6379:6379 -d redis:5
```

#### run the development server
```
python3 manage.py runserver
```

### Youtube video tutorial

[Youtube](youtu.be/zv7ra-xw1mu)


### Help

Need help? Open an issue in: [ISSUES](https://github.com/josnin/django-whatsapp-web-clone/issues)


### Contributing
Want to improve and add feature? Fork the repo, add your changes and send a pull request.


