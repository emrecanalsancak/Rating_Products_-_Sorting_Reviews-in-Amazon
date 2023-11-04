# Rating Products & Sorting Reviews in Amazon

This project focuses on rating products and sorting reviews in an Amazon-like platform. It involves analyzing customer reviews and calculating weighted average ratings based on the review date. The goal is to provide more meaningful and reliable product ratings for customers.

## Dataset

The dataset used in this project contains the following variables:

- `reviewerID`: ID of the reviewer (e.g., A2SUAM1J3GNN3B)
- `asin`: ID of the product (e.g., 0000013714)
- `reviewerName`: Name of the reviewer
- `helpful`: Helpfulness rating of the review (e.g., 2/3)
- `reviewText`: Text of the review
- `overall`: Rating of the product
- `summary`: Summary of the review
- `unixReviewTime`: Time of the review (Unix time)
- `reviewTime`: Time of the review (raw)
- `day_diff`: Number of days since assessment
- `helpful_yes`: The number of times the evaluation was found useful
- `total_vote`: Number of votes given to the evaluation

## Calculating Weighted Average Ratings

The project involves calculating a time-based weighted average rating for reviews. The weighting factors are defined as `w1`, `w2`, `w3`, and `w4`. The time periods are divided into quantiles, and the weighted averages are calculated for each period. These weighted averages provide a more accurate representation of product ratings, considering the recency of reviews.

## Identifying Top 20 Reviews

The project identifies the top 20 reviews that should be displayed on the product detail page. This is done by calculating the Wilson Lower Bound (WLB) score for each review. The WLB score is used to rank the reviews, ensuring that the most helpful and informative reviews are displayed prominently.

## Data Preprocessing

Before calculating scores and rankings, the dataset is preprocessed to generate the `not_helpful` variable, which represents the number of unhelpful votes for each review. Additional variables such as `score_pos_neg_diff`, `score_average_rating`, and `wilson_lower_bound` are calculated to provide insights into the quality of reviews.

## Conclusion

This project aims to improve the customer experience by providing accurate and helpful product ratings based on the recency of reviews and the helpfulness of votes. By sorting and displaying reviews effectively, customers can make informed purchasing decisions.

Explore the project code and data files for more details and insights.
