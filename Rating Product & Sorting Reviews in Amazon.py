##########################################################################
# Rating Products & Sorting Reviews in Amazon.
##########################################################################

import pandas as pd
import math
import scipy.stats as st


pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", lambda x: "%.5f" % x)

###################################################
# Calculating Average Rating According to Current Reviews and Comparing it with the Existing Average Rating.
###################################################

# The aim of this task is to evaluate the scores by weighting them by date. The initial average score should be compared with the weighted score by date.


df = pd.read_csv("amazon_review.csv")

# df["overall"].mean()

###################################################
# Calculating the time_based_weighted_average
###################################################


def time_based_weighted_average(dataframe, w1=28, w2=26, w3=24, w4=22):
    return (
        dataframe.loc[
            dataframe["day_diff"] <= dataframe["day_diff"].quantile(0.25), "overall"
        ].mean()
        * w1
        / 100
        + dataframe.loc[
            (dataframe["day_diff"] > dataframe["day_diff"].quantile(0.25))
            & (dataframe["day_diff"] <= dataframe["day_diff"].quantile(0.50)),
            "overall",
        ].mean()
        * w2
        / 100
        + dataframe.loc[
            (dataframe["day_diff"] > dataframe["day_diff"].quantile(0.50))
            & (dataframe["day_diff"] <= dataframe["day_diff"].quantile(0.75)),
            "overall",
        ].mean()
        * w3
        / 100
        + dataframe.loc[
            (dataframe["day_diff"] > dataframe["day_diff"].quantile(0.75)), "overall"
        ].mean()
        * w4
        / 100
    )


time_based_weighted_average(df)


# There is no helpful_no variable in the dataset, let's generate it over existing variables.

df.sort_values(by="total_vote", ascending=False).head()
df["not_helpful"] = df["total_vote"] - df["helpful_yes"]

###################################################
# Calculate score_pos_neg_diff, score_average_rating and wilson_lower_bound Scores and Add to Data
###################################################


def score_up_down_diff(up, down):
    return up - down


df["score_pos_neg_diff"] = df.apply(
    lambda x: score_up_down_diff(x["helpful_yes"], x["not_helpful"]), axis=1
)
df["score_pos_neg_diff"].sort_values(ascending=False).head()


def score_average_rating(up, down):
    if up + down == 0:
        return 0
    return up / (up + down)


df["score_average_rating"] = df.apply(
    lambda x: score_average_rating(x["helpful_yes"], x["not_helpful"]), axis=1
)
df["score_average_rating"].sort_values(ascending=False).head()


def wilson_lower_bound(up, down, confidence=0.95):
    """
    Wilson Lower Bound Score hesapla
    - The lower limit of the confidence interval to be calculated for the Bernoulli parameter p is considered as the WLB score.
    - The score is used for product ranking.
    - Note:
    If the scores are between 1-5, 1-3 can be marked as negative and 4-5 as positive and can be made Bernoulli compatible.
    This brings some problems with it. For this reason, it is necessary to make a Bayesian average rating.

    Parameters
    ----------
    up: int
        up count
    down: int
        down count
    confidence: float
        confidence

    Returns
    -------
    wilson score: float

    """
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (
        phat
        + z * z / (2 * n)
        - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)
    ) / (1 + z * z / n)


df["wilson_lower_bound"] = df.apply(
    lambda x: wilson_lower_bound(x["helpful_yes"], x["not_helpful"]), axis=1
)

##################################################
# First 20 comments.
###################################################
df.sort_values(by="wilson_lower_bound", ascending=False).head(20)
