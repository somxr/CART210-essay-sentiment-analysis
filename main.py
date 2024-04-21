import csv
from textblob import TextBlob

# Function to read comments and their like counts from a CSV file
def read_comments_from_file(filename='comments_mkbhd.csv'):
    comments_with_likes = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            comment, likes = row
            comments_with_likes.append((comment, int(likes)))
    return comments_with_likes

# Function to analyze sentiments and account for like count as weight
def weighted_sentiment_analysis(comments_with_likes):
    total_weighted_sentiment = 0
    total_likes = 0
    for comment, likes in comments_with_likes:
        sentiment = TextBlob(comment).sentiment.polarity
        total_weighted_sentiment += sentiment * likes
        total_likes += likes

    # Avoid division by zero if there are no likes
    if total_likes > 0:
        weighted_average_sentiment = total_weighted_sentiment / total_likes
    else:
        weighted_average_sentiment = 0
    return weighted_average_sentiment

# Read comments and likes from CSV file
comments_with_likes = read_comments_from_file()

# Analyze sentiments
average_sentiment = weighted_sentiment_analysis(comments_with_likes)

print(f"Weighted average sentiment of the comments: {average_sentiment:.2f}")

#######################################################################################
#########################################################################################
#########################################################################################

# import csv
# from textblob import TextBlob
#
# # Function to read comments from a CSV file
# def read_comments(filename='comments_mkbhd.csv'):
#     comments = []
#     with open(filename, 'r', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip the header
#         for row in reader:
#             comments.append(row[0])  #comments are in the first column
#     return comments
#
# # Function to analyze sentiments of the comments
# def analyze_sentiments(comments):
#     sentiments = []
#     for comment in comments:
#         blob = TextBlob(comment)
#         sentiments.append(blob.sentiment.polarity)
#     # Calculate the average sentiment
#     average_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
#     return average_sentiment
#
# # Read comments from the CSV file
# comments = read_comments()
#
# # Analyze sentiments of the comments
# average_sentiment = analyze_sentiments(comments)
#
# print(f"Average sentiment of the comments: {average_sentiment:.2f}")

