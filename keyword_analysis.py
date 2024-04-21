import pandas as pd

# New list of keywords based on your selection
keywords = [
    "dystopia", "dystopian", "surveillance", "apocalypse", "apocalyptic", "collapse",
    "addiction", "addicted", "attention span", "losing focus", "digital distraction",
    "social isolation", "feeling isolated", "lack of social", "loneliness", "isolated",
    "social skills", "avoiding social", "privacy", "personal data"
]

# Function to calculate weighted sentiment based on likes
def count_weighted_dystopian_comments(comments):
    contains_keywords = comments['Comment'].str.contains('|'.join(keywords), case=False, na=False)
    weighted_keyword_sum = (contains_keywords * comments['Likes']).sum()
    total_likes = comments['Likes'].sum()
    weighted_percentage = (weighted_keyword_sum / total_likes) * 100
    return weighted_percentage

# Load comments for both videos
comments_neistat = pd.read_csv('comments_neistat.csv')
comments_mkbhd = pd.read_csv('comments_mkbhd.csv')

# Calculate weighted percentages
neistat_percentage = count_weighted_dystopian_comments(comments_neistat)
mkbhd_percentage = count_weighted_dystopian_comments(comments_mkbhd)

print(f"Weighted dystopian comment percentage for Neistat's video: {neistat_percentage}%")
print(f"Weighted dystopian comment percentage for MKBHD's video: {mkbhd_percentage}%")