# Twitter-Bot-Or-Not
Uses [Cersi (2017)](https://botometer.iuni.iu.edu/bot-repository/datasets.html) to determine if a twitter account/tweet is a trollbot or not.

Based on https://arxiv.org/abs/1707.00086 by Emilio Ferrara (who has written a [series of brilliant papers](https://scholar.google.com/citations?user=0r7Syh0AAAAJ&hl=en&oi=ao) on Bots)

The data can easily be replaced to your own or you can add your own. Currently the model has an accuracy of 98% in the training set and 97% in test set in that. I have used this model for detecting bots in US 2018 Midterm election. 

This repo currently only contains code for profile based detection. For tweet based, you can have a look at my commit histroy or attempt your own.

Currently this is a just notebooks that can be replicated. I can create a importable module if this gets enough interest.
