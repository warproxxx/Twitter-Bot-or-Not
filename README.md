# Twitter-Bot-Or-Not
Uses Data during the US Midterm Election 2018 to determine if a twitter account/tweet is created by a trollbot or not.

Based on https://arxiv.org/abs/1707.00086

This repository uses Bot and Human data obtained by using [Botometer](https://botometer.iuni.iu.edu/#!/) and [Bot Sentinal](https://botsentinel.com/) to train a neural network that can detect whether or not the given twitter account is a trollbot or not. Botometer API is free but takes time while to obtain the bot data set from Bot Sentinal require at least 5$ donation in their [gofundme](https://www.gofundme.com/bot-sentinel) you can insted use other sources of data like manual classification or these.

Currently this is a just notebooks that can be replicated. I can create a importable module if this gets enough interest.

## Steps:

1) First Live data should be collected and stored. This repository can be used for that purpose: 
That repostory stores live profile and and tweet data in the required format. If you collect it manually, the data should be in the format:



2) Then configure botometer and for now

3) Clean it obtain it, run it