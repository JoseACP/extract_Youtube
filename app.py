from youtube_transcript_api import YouTubeTranscriptApi
# Enter the YouTube video ID
video_id = "3tK5dH7XMnQ"
try:
    # Fetch the transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])
    # Combine transcript lines
    script = "\n".join([f"{item['text']}" for item in transcript])
    # Save the transcript to a file
    with open("transcript.txt", "w") as file:
        file.write(script)
    print("Transcript saved successfully!")
except Exception as e:
    print(f"Error: {e}")