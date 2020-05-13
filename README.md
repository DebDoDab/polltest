# PollTest
This API for Poll services.
#### You can [try it out](http://polltest.vadi.tel)

## Build
Run `git clone https://github.com/DebDoDab/polltest.git` <br>
Setup venv using `python3 -m venv venv` <br>
Activate venv `source venv/bin/activate` <br>
Install requirements `pip3 install -r requirements.txt` <br>
Run `python3 manage.py makemigrations` <br>
Run `python3 manage.py migrate` <br>
Run `python3 manage.py createsuperuser` <br>
Add your domain to `ALLOWED_HOSTS` <br>
Run `python3 manage.py runserver` <br>

## Usage

### Authorization
###### I'm using simpleJWT, so you can read about it
Using CLI run
`python3 manage.py createsuperuser`
then go to `/auth/jwt/create` with loginData. You'll receive an access_token and refresh_token. Save them in cookies.

### Сreate a poll
###### You should be authorized
POST a new Poll with it's name: `POST /polls` <br><br>
POST all your questions using `POST /questions`, don't forget to send your new poll's id <br>
if it's first question in your poll, than you sould leave `prev=None`, if it's last question, leave `next=None` <br><br>
POST all your answers using `POST /answers` <br>

### Get active polls 
`/polls?active=true` - get all polls that are currently available

### Get User stats
###### user_id is just a unique number
`/getstats` all info in JSON about User's polls

### Take a poll
Start with a `/questions?first_from=<:int>` where int is your poll ID. It will return you first question. <br><br>
Get answers with `/answers?question_id=<:int>` <br><br>
You can move back and forward using `prev` and `next` parameters of that question <br><br>
Send your answer with `POST /useranswers`

