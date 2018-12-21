import pandas as pd
import botometer
import os
from multiprocessing.pool import Pool
from functools import partial

users = pd.read_csv('data/top_15k.csv', header=None)

if (os.path.isfile('data/currentResults.csv')):
    resultDf = pd.read_csv('data/currentResults.csv')
    starting_account =  resultDf['username'].iloc[-1]
    
    starting_num = users[users[0] == starting_account].index[0]
    print("Starting from: {}".format(starting_num))
    
    users = users[starting_num:]
else:
    resultDf = pd.DataFrame(columns=['username', 'result'])

mashape_key = ""
twitter_app_auth = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token': '',
    'access_token_secret': '',
  }

botometer_api_url = 'https://botometer-pro.p.mashape.com'

bom = botometer.Botometer(botometer_api_url=botometer_api_url,
                          wait_on_ratelimit=True,
                          mashape_key=mashape_key,
                          **twitter_app_auth)

# def get_tweet(account):

#     try:
#         my_acc = bom.check_account(account)
#     except:
#         my_acc = "Dosen't exist"

#     return [account, my_acc]


# p = Pool(20)
    
# for i in range(20, resultDf.shape[0], 20):
#     currAccounts = users[0].values[i-20:i]
    
#     for res in p.imap_unordered(partial(get_tweet), currAccounts):
#         resultDf = resultDf.append({'username': res[0], 'result': res[1]}, ignore_index=True)
#         resultDf.to_csv('currentResults.csv', index=False)
#         print(i)

i = 1

for screen_name, result in bom.check_accounts_in(users[0].values):
    resultDf = resultDf.append({'username': screen_name, 'result': result}, ignore_index=True)
    resultDf.to_csv('data/currentResults.csv', index=False)
    print(i)
    i = i + 1
