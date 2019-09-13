import tweepy
import csv

consumer_key ='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

handles_list = ["wougnet", "RestlessDev",
                "encryptUg","Andela_UG", "ThinVoid", "Africastalking", "DesignHubKla", "InnovationVilla", "OutboxHub",
                "hivecolab", "AfricaResilient", "RIL_Uganda", "wituganda", "chapter4uganda","barefootlawUG","CPA_Horn",
                "laspnetUg", "justice_care", "ug_lawsociety","UHRC_UGANDA", "HurinetU","HURIFO",
                "cehurduganda","FHRI2","HRCU"]

def get_all_tweets(screen_name, writer):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    recenttweets = []
    recent_tweets = api.user_timeline(screen_name = handle, count=50)
    new_tweets = api.user_timeline(screen_name=handle, count=200)
    recenttweets.extend(new_tweets)

    Resultingtweets= [[tweet.user.name, tweet.user.screen_name, tweet.user.description, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in recenttweets]

    writer.writerow(["User Name","Twitter_Handle","Twitter_User_Description","tweet_id","created_at","Tweet_text"])
    writer.writerows(Resultingtweets)

if __name__ == '__main__':
    with open('all_tweets.csv', 'w', encoding='utf-8') as f_all:
        writer = csv.writer(f_all)

        for handle in handles_list:
            get_all_tweets("handles", writer)
            print ("Done.")
