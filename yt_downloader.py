from pytube import YouTube

link = 'youtube_video_link'
yt = YouTube(link)

print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length, "seconds")
print("Ratings: ", yt.rating)

ys = yt.streams.get_highest_resolution()
ys.download(r'your_folder_path')

ys.download()
