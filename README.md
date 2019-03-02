# Twitter-Bot-Or-Not
Uses [Cersi (2017)](https://botometer.iuni.iu.edu/bot-repository/datasets.html) to determine if a twitter account/tweet is a trollbot or not.

Based on https://arxiv.org/abs/1707.00086 by Emilio Ferrara (who has written a [series of brilliant papers](https://scholar.google.com/citations?user=0r7Syh0AAAAJ&hl=en&oi=ao) on Bots)

The data can easily be replaced to your own or you can add your own. The deep learning model has an accuracy of 98% in the training set and 97% in test set. Similary Adaboost classifier with SMOTE and ENN has a 100% acuracy in training set and 98.5% in the test set. 

This repo currently only contains code for profile based detection. For tweet based, you can have a look at my commit histroy or attempt your own.

Currently this is a just notebooks that can be replicated. I can create a importable module if this gets enough interest.
