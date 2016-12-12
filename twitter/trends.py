#Working as of 12/12/16

import tweepy
import time

#Could change I guess
ckey = "04Jw2IZctxYCawbwZw1hSSAKo"
csecret = "E35K3mqpbEXWGz5pepmAvRbMt6QKqEFJ1Ywj6FrqCHivLeP7wi"
access_token = "1284117354-0ZeVEHecvaddwwPAdjBH7iblxKQx6ouQWpEq4sS"
access_secret = "xTI5aeol24nXJnEsrx1nDEHixLebAThHMyiUEWwmSBgCP"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

while True:
    trends1 = api.trends_place(23424975)
    data = trends1[0] 
    trends = data['trends']
    names = [trend['name'] for trend in trends]
    count = 0
    for name in names:
        print(name + "\n")
        count += 1
        if count == 10:
            break
    #Wait 2 min
    time.sleep(120)
    print('\n')
