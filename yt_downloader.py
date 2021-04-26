from pytube import YouTube

# Put you link here:
link = 'https://youtu.be/hgZjlHYU4ng'
yt = YouTube(link)

print("Title: ", yt.title)

print("Number of views: ", yt.views)

print("Length of video: ", yt.length, "seconds")

print("Ratings: ", yt.rating)

ys = yt.streams.get_highest_resolution()
ys.download('Youtube Videos Downloaded')

ys.download()
