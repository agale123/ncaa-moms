# ncaa-moms

The goal of this script is to analyze the impact of Holly Rowe's report on Adia
Barnes breastfeeding her child and pumping during halftime.

## Methodology

I searched for Tweets on 4/4 and 4/5 with combinations of "Adia Barnes" and
"Arizona coach" with "breastfeeding", "pumping", and "mother". For each Tweet I
included details on the content of the Tweet, whether it was a retweet, and
how many favorites and retweets it got. Using this method I collected 360 Tweets.

## Findings

The first analysis I did was to plot the Tweets over time to see when there was
the most activity. From the histogram below, you see a large spike after 4PM on
Sunday which is when the feature from Holly Rowe aired. There was also another
spike on Monday morning.

![A histogram showing tweets over time](https://github.com/agale123/ncaa-moms/blob/main/tweets_over_time.png?raw=true)

## Usage

When cloning this repository, you will need to create a `.env` file with two keys:
CONSUMER_KEY and CONSUMER_SECRET_KEY. Those are the API key & secret from the
Twitter Developer Portal.
