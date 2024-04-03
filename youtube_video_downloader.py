from pytube import YouTube

# URL of the YouTube video I wanted to download
video_url = input("Enter the video URL:")

#creating a youtube object
yt = YouTube(video_url)

# Get the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Set the output file path
output_path = r'C:\Users\JAMAL\OneDrive\Desktop\ytdownload'  # Change this to your desired file path

# Download the video
try:
    stream.download(output_path)
except:
    print("An error occurred :(")
#print a message so that you know when it's done !
print("Download completed successfully!")



