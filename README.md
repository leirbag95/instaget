# instaget
Unofficial API for getting profile by username
![giphy](https://user-images.githubusercontent.com/17054452/105351357-c1fe2580-5bec-11eb-97a9-3e7e55f8e8c7.gif)


## How to install

```
pip3 install -r requirements.txt
```

## Before running

Insert your instagram session id for avoid **Login Page**

### Getting sessionid

Go to <a href="https://instagram.com">https://instagram.com</a> then login to your account.

Open Inspect Element Tool, then go to **Application** tab, select **Cookies** from Storage section.

Copy *sessionid* value then past it into data/data.json in "sessionid" value

## Runing instaget

```
python3 app.py
```