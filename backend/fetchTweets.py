import twint
from geopy.geocoders import Nominatim
import time

states = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming"
]


geolocator = Nominatim(user_agent="fetchTweets")
# location = geolocator.geocode("United States")
# print(location.raw)
#fetch all the tweets from the api which contains any city in given country
#and also contains the given keywords
#return back a data frame containing date keyword longitude latitude and tweet

#input= tweets that can be searched with keywords present
#output= latitude,longitude,country,address,disaster,tweet_content

lis = ["earthquake","mass shooting","tsunami","crime"];

def fetchTweetsFunc():
    lis = ["massshooting","tsunami","crime"]
    dict = {}
    maindict = {}
    for i in lis:
        c = twint.Config()
        c.Limit = 20
        c.Search = i
        c.Pandas = True
        c.Lang = "en"
        c.Near = "United States"
        c.Hide_output = True
        c.Timedelta = 1
        twint.run.Search(c)
        Tweets_df = twint.storage.panda.Tweets_df
        # print(Tweets_df["tweet"])
        print(Tweets_df['place'][0])
        Tweets_df = Tweets_df[['date', 'tweet']]
        for tweet in Tweets_df["tweet"]:
            for state in states:
                if state in tweet:
                    location = geolocator.geocode(state)
                    dict['latitude'] = location.latitude
                    dict['longitude'] = location.longitude
                    dict['state'] = state
                    dict['tweet'] = tweet
                    dict['disaster'] = i
                    dict['date'] = Tweets_df['date'][0]
        maindict[i] = dict
    return maindict;
            
        # print(Tweets_df["tweet"])

# print(fetchTweetsFunc())
