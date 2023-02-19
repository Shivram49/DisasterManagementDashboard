import json
from flask import Flask, jsonify
from fetchTweets import fetchTweetsFunc

class TweetDisaster:
    def __init__(self, latitude, longitude, state, tweet, disaster, date):
        self.latitude = latitude
        self.longitude = longitude
        self.state = state
        self.tweet = tweet
        self.disaster = disaster
        self.date = date

data = fetchTweetsFunc()
#create an array of TweetDisaster objects from data
tweetDisasterArray = []
for disaster in data:
    tweetDisaster = TweetDisaster(data[disaster]['latitude'], data[disaster]['longitude'], data[disaster]['state'], data[disaster]['tweet'], data[disaster]['disaster'], data[disaster]['date'])
    tweetDisasterArray.append(tweetDisaster)



# Read the data from the JSON file
# with open('disasters.json', 'r') as f:
#     data = json.load(f)
app = Flask(__name__)

@app.route('/data')
def get_data():

    # # Return the page data as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
