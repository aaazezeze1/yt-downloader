# https://towardsdatascience.com/build-a-youtube-downloader-with-python-8ef2e6915d97

# Install needed python modules
# pip install pytube

from pytube import YouTube

# Put you link here:
link = 'https://youtu.be/hgZjlHYU4ng'
yt = YouTube(link)

# Print the title of the youtube video
print("Title: ", yt.title)

# Print the number of views of the youtube video
print("Number of views: ", yt.views)

# Print the length of the youtube video
print("Length of video: ", yt.length, "seconds")

# Print the ratings of the youtube video
print("Ratings: ", yt.rating)

ys = yt.streams.get_highest_resolution()
ys.download(r'C:\Users\Amazing\Documents\Youtube Videos Downloaded')

ys.download()
