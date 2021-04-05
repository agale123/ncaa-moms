# ncaa-moms

The goal of this script is to analyze the impact of Holly Rowe's report on Adia
Barnes breastfeeding her child and pumping during halftime.

## Methodology

I searched for Tweets on 4/4 and 4/5 with combinations of "Adia Barnes" and
"Arizona coach" with "breastfeeding", "pumping", "mother", "nursing", and
"normalize". For each Tweet I included details on the content of the Tweet,
whether it was a retweet, and how many favorites and retweets it got. Using
this method I collected 377 Tweets.

## Findings

### Tweets over time

The first analysis I did was to plot the Tweets over time to see when there was
the most activity. From the histogram below, you see a large spike after 4PM on
Sunday which is when the feature from Holly Rowe aired. There was also another
spike on Monday morning.

![A histogram showing tweets over time](https://github.com/agale123/ncaa-moms/blob/main/tweets_over_time.png?raw=true)

The next step was to find the top favorited and retweeted tweets. The five Tweets
with the most likes and the Tweets with the most retweets were the same set. The
table below highlights these tweets with links to the original content. The top
Tweet from [@TheUndefeated](https://twitter.com/TheUndefeated) also embedded a
video with over 51,000 views.

### Top Tweets

| Tweet | Favorites | Retweets |
|-------|-----------|----------|
| ["Let's normalize working mothers and all that they have to do to make it happen." 🗣️🗣️🗣️ @sportsiren's report on Arizona head coach Adia Barnes pumping at halftime of the national championship.](https://twitter.com/TheUndefeated/status/1378857455283802115) | 1268 | 326 |
| [Last night, Holly Rowe highlighted that Arizona head coach Adia Barnes was delayed coming out of the locker room after halftime because she was pumping. In the words of Holly, "Let's normalize working mothers and all that they have to do to make it happen." #MomsAreSuperheroes](https://twitter.com/OnHerTurf/status/1379071211674730500) | 221 | 28 |
| [“Let’s normalize working mothers and all that they have to do to make it happen.” Tremendous report from @sportsiren on Arizona coach Adia Barnes pumping at halftime of the national championship game.](https://twitter.com/SeifertESPN/status/1378852974911438851) | 176 | 35 |
| [Wow, Arizona Coach Adia Barnes is still a nursing Mom. Including halftime of this game. And I love the announcer who just said, 'If you think this is too much information, let's normalize working Moms.' For the win, indeed.](https://twitter.com/LauraChapin/status/1378852548468109314) | 154 | 13 |
| [It’s Stanford women for the win!  But props are owed to Arizona coach & new mom Adia Barnes. As the announcer said, “She's still a nursing Mom with an infant, including pumping at halftime of this game. If you think that's too much information, let's normalize working moms.”](1378888028446289920) | 61 | 3 |

### Tweet sentiment

The final analysis I performed was sentiment analysis on the contents of the Tweets
to see if there is overall positive feedback to Holly Rowe's report on Adia Barnes.
I did find that 60% of the Tweets were marked as having positive sentiment. When I
looked closer at the tweets with the stronger "negative" sentiment, I found that for
some reason the quote from the feature: "For those of you who think this is too much
information,' [ESPN’s Holly Rowe] told viewers from the sideline, 'let’s normalize
working mothers and all they have to do." is calculated to have negative sentiment.
Of the tweets analyzed, all of the ones marked as having "negative" sentiment were
actually positive Tweets. This indicates a broader issue with how sentiment
analysis scores statements like these. So overall all the Tweets I analyzed were
supportive of Adia Barnes and the profile of her during the game.

## Developer notes

When cloning this repository, you will need to create a `.env` file with two keys:
CONSUMER_KEY and CONSUMER_SECRET_KEY. Those are the API key & secret from the
Twitter Developer Portal.
