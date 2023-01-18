# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data
tweets_list1 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:NashTvZimbabwe').get_items()):  # declare a username
    if i > 100:  # number of tweets you want to scrape
        break

    tweets_list1.append(
        [tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.url, tweet.source, tweet.sourceLabel,
         tweet.likeCount, tweet.replyCount, tweet.retweetCount, tweet.user.followersCount, tweet.user.displayname,
         tweet.user.mediaCount, tweet.lang, tweet.user.location])  # declare the attributes to be returned

# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweets_list1,
                          columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Url', "source", "Source of Tweet",
                                   'Like Count', 'Reply Count', 'retweet Count', 'followersCount', 'Display Name',
                                   'Media Count', 'Language', 'Location'])

# onvert the pandas dataframe to a CSV spreadsheet
tweets_df1.to_csv("Twitter_Posts.csv", index=True)


tweets_df1

import snscrape.modules.twitter as sntwitter
import requests
import urllib.request
import os
from urllib.parse import urlparse


class Video_Image():
    def __init__(self) -> None:
        pass

    def photo_save(self, photo_url):
        '''Save photo from url'''
        a = urlparse(photo_url)
        photo_name = os.path.basename(a.path)
        with open(photo_name + '.jpg', 'wb') as f:
            f.write(requests.get(photo_url).content)

    def video_save(self, url_link):
        '''Save video from url'''
        a = urlparse(url_link)
        video_name = os.path.basename(a.path)
        urllib.request.urlretrieve(url_link, video_name + '.mp4')

    def get_video_image(self):
        ''' Get User's tweets videos and images url'''

        for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:NashTvZimbabwe').get_items()):
            if tweet.media:
                for medium in tweet.media:
                    if medium.__class__.__name__ == 'Photo':
                        self.photo_save(medium.fullUrl)
                    elif medium.__class__.__name__ == 'Video':
                        for v in medium.variants:
                            if '.mp4' in v.url: self.video_save(v.url)


if __name__ == "__main__":
    cls = Video_Image()
    cls.get_video_image()