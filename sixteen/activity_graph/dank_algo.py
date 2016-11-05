import distanceCalc from gis
import numpy as np

def dankAlgo (user1, busines1):
    # Calculate the rating for busines
    # Sports Category, Environment Category
    #Yelp Rating, Cost

    # Distance, Gaussian decay from Zero
    userloc     = (user1.latitude, user1.longitude)
    distance    = distanceCalc(userloc, busines1)
    distfactor  = 5 * np.exp(-d**2 / 1000)


    yelpfactor  = 0.2 * busines1.yelp_rate

    usagefactor = 1 + 0.01 * user1.rate_counts
    if (rate_counts > 100):
        usageBoost = 2

    # Affinity Ranking
    partialType =   business1.aqua * user1.aqua + \
                    business1.novel * user1.novel + \
                    business1.leisure * user1.leisure + \
                    business1.coolShit * user1.coolShit

    partialEnv  =   business1.forest * user1.forest + \
                    business1.mount * user1.mount + \
                    business1.water * user1.water

    rank        = distfactor(usagefactor * partials + yelpfactor)

    return rank
