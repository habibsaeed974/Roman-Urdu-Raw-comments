import googleapiclient.discovery
def fetch_youtube_comments():
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyB1XnZ04ZtcHOM2I-73kYJh9cbinB5ZS3Y"
    url = input("Enter YouTube video URL: ").strip()
    video_id = None

    if "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]
    elif "youtube.com/watch?v=" in url:
        video_id = url.split("watch?v=")[1].split("&")[0]  
    if not video_id:
        print("Invalid YouTube URL! Please enter a valid link.")
        return []
    
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)
    comments = []
    next_page_token = None

    while True:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken = next_page_token 
        )
        response = request.execute()

        # Store comments in list
        for item in response.get("items", []):
            comment_text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            print(comment_text)
            comments.append(comment_text)

        next_page_token = response.get("nextPageToken")
        if not  next_page_token:
            break
    return comments

youtube_comments = fetch_youtube_comments()

print("Collected Comments:")
print(youtube_comments)


