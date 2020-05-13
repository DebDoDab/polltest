# PollTest
This API for Poll services.
#### You can [try it out](http://polltest.vadi.tel)

## Authorization
###### I'm using simpleJWT, so you can read about it
Using CLI run
`python3 manage.py createsuperuser`
then go to `/auth/jwt/create` with loginData. You'll receive an access_token and refresh_token. Save them in cookies.

## create poll
###### You should be authorized
POST a new Poll with it's name: `POST /polls` <br><br>
POST all your questions using `POST /questions`, don't forget to send your new poll's id <br>
if it's first question in your poll, than you sould leave `prev=None`, if it's last question, leave `next=None` <br><br>
POST all your answers using `POST /answers` <br>

## Get active polls 
`/polls?active=true` - get all polls that are currently available

## Get User stats
###### user_id is just a 