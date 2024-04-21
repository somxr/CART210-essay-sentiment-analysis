
from googleapiclient.discovery import build
import csv
from googleapiclient.errors import HttpError
import time

# Function to fetch all comments from a YouTube video given its ID and the API key
def fetch_comments(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    all_comments = []

    # Initial API call
    response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText',
        maxResults=100,  # maximum allowed by the API
        order='relevance'  # You can change this to 'time' to get newer comments first
    ).execute()

    # Loop to iterate through all pages of results
    while response:
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            likes = item['snippet']['topLevelComment']['snippet']['likeCount']
            all_comments.append((comment, likes))

        print(f"Fetched {len(all_comments)} comments so far...")

        # Check for the nextPageToken to paginate, else break the loop
        if 'nextPageToken' in response:
            try:
                response = youtube.commentThreads().list(
                    part='snippet',
                    videoId=video_id,
                    textFormat='plainText',
                    pageToken=response['nextPageToken'],
                    maxResults=100,
                    order='relevance'
                ).execute()
            except HttpError as e:
                print(f"An HTTP error occurred: {e.resp.status} {e.content}")
                break  # or use time.sleep and retry logic
        else:
            print("No next page token, ending fetch.")
            break

    return all_comments

# Function to save comments to a CSV file
def save_comments_to_file(comments, filename='comments_mkbhd.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Comment', 'Likes'])  # Writing header
        writer.writerows(comments)

# Replace 'YOUR_API_KEY' with your actual YouTube Data API key
api_key = '############################'
# Replace 'VIDEO_ID' with the YouTube video ID you want to analyze
video_id = 'dtp6b76pMak&t'


# Fetching all comments
comments = fetch_comments(video_id, api_key)
# Saving comments to CSV file
save_comments_to_file(comments)

print(f"Total comments fetched: {len(comments)}")
print("Comments have been saved to comments.csv")
