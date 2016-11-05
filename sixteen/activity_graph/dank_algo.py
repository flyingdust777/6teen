import distanceCalc from gis
import numpy as np

def dankAlgo (user1, busines1):
    # Calculate the rating for busines
    # Distance, Gaussian decay from Zero
    userloc     = (user1.latitude, user1.longitude)
    distance    = distanceCalc(userloc, busines1)
    distfactor  = 5 * np.exp(-d**2 / 1000)

    # Yelp Contribution: between 0 and 1
    yelpfactor  = 0.2 * busines1.yelp_rate

    # Boosts strength of application rating on amount of use
    # Boosts by 0.01 for every rating from 1 up to 2
    usageBoost = 1 + 0.01 * user1.rate_counts
    if (rate_counts > 100):
        usageBoost = 2

    # Affinity Ranking: Equal parts category and environment
    partialType =   business1.aqua * user1.aqua + \
                    business1.novel * user1.novel + \
                    business1.leisure * user1.leisure + \
                    business1.coolShit * user1.coolShit

    partialEnv  =   business1.forest * user1.forest + \
                    business1.mount * user1.mount + \
                    business1.water * user1.water

    partials    =   usageBoost (partialType * 0.25 + partialEnv / 3)

    rank        = distfactor(partials + yelpfactor)

    return rank
