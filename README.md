# Twitter-Bot-Or-Not
Uses Data during the US Midterm Election 2018 to determine if a twitter account/tweet is created by a trollbot or not.

Based on https://arxiv.org/abs/1707.00086 by Emilio Ferrara (who has written a [series of brilliant papers](https://scholar.google.com/citations?user=0r7Syh0AAAAJ&hl=en&oi=ao) on Bots)

This repository uses Bot and Human data obtained by using [Botometer](https://botometer.iuni.iu.edu/#!/) and [Bot Sentinal](https://botsentinel.com/) to train a neural network that can detect whether or not the given twitter account is a trollbot or not. Botometer API is free but takes time while to obtain the bot data set from Bot Sentinal require at least 5$ donation in their [gofundme](https://www.gofundme.com/bot-sentinel) you can insted use other sources of data like manual classification or these.

Currently this is a just notebooks that can be replicated. I can create a importable module if this gets enough interest.

## Steps:

1) First Live data should be collected and stored. This repository can be used for that purpose: https://github.com/warproxxx/Twitter-Live-Data-Collection

If you use that repository you will need to update the number of likes and retweets. You can use this repository for that purpose:
https://github.com/warproxxx/Tweet-Details-Scraper

If you do this manually you will require data in this format:

**Tweet Data:**

| ID | Tweet | Time | User | Likes | Replies | Retweets | in_response_to | response_type
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: 
| The ID of the tweet | The tweet text. Contains retweeted and quoted information too if they exist | Unix timestamp of the tweet in UTC Time | Username of the use who posted the tweet | Total number of likes the tweet received. It will be zero  as  we are collecting live | Same as likes | Same as likes | ID of tweet in whose response the current tweet was made. None if it's a parent tweet | "tweet" or "retweet" or "quoted_retweet"

**Profile Data:**

| username | created | location | has_location | is_verified | total_tweets | total_following | total_followers | total_likes | has_avatar | has_background | is_protected | profile_modified
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:  | :---: | :---: | :---: | :---: 
| Username of the use who posted the tweet | The date the profile was created in on YYYY-MM-DD format | Profile Location | 1 if profile has a location 0 if it dosen't | 1  if profile is verified 0 if it isn't  | Total number of tweets created by the user | Total accounts following | Total Followers | Total likes the user has received | 1 if account  has an avatar 0 if it dosen't  | 1 if account has an background 0 if it dosen't | 1 if account is protected 0 if it isn't | 1 if profile is  modified. 0 if it isn't


*If you just want to use the model view the model notebooks and skip the steps below:*

2) Then you will need a list of bot accounts i obtained mine from https://botsentinel.com/ I cannot provide the data here as they require payment for their data but i can privately provide it to you if you are a researcher.  Paste the file you obtain from there inside "data/bot_detection" folder. If you use other sources of data, you will have to modify the notebooks accordingly. 

3) Select some top n tweets (I chose 15000) and use the file to obtain bot or not data from Botometer (botometer_api.py does this). To obtain the top tweets from live data, you will have to count the number of times the tweet was retweeted (in the given dataset) or use the scraper i mentioned.

4) Now you have tweets created by bots or non bots. Insted of Botometer you can manually classify for your requirement.

4) Convert the tweets to required format using "Tweet based data cleaning" notebook. You will have to modify your path directory.

3) Then you can use the notebooks for bot detection models based on account data or tweet data. I obtained an accuracy of around 80%. You can improve that by algorithm mentioned in https://arxiv.org/abs/1802.04289 like Synthetic Minority Data Oversampling algorithm.



You can use this algorithm to detect not just bots, but selected kind of troll bots (Russian, Iranian and others) and use your own model/encoding. The possiblites are endless.