import credentials
import tweepy

API_KEY = "gq1Cjyyvi5E1DZaeFlcYaisjP" 
API_SECRET_KEY = "T8FqcCEIG31EH2ZEJz8aUk0kvVRxRGGWIrdlk2unIbFiloyYrD"
ACCESS_TOKEN = "1388888268020781059-sQmy1ULdpqKzH5ACZjb8qfKw8I9vbo"
ACCESS_TOKEN_SECRET = "e6NDINWYZXmyGYXA2VbFiYUXjvfYSN4U41Oqykrh29ZXj"

auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


    