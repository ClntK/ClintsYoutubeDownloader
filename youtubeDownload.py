from pytube import YouTube
from tkinter import Tk, filedialog

########################### INPUT ###################################

link = input("\n\nEnter the youtube share link here(format: youtu.be/<ID#>): ")
yt = YouTube(link)


########################### VIDEO INFO ###################################

# Video Title
print("\n\n########## VIDEO INFO ##########\n\n")

print("Video Title: ", yt.title)

# Number of Views
print("\nViews: ", yt.views)

# Video Length
print("\nVideo Length: ", yt.length, " seconds")

# Video Description
print("\nDescription:\n", yt.description)

# Video Rating
print("\nRating: ", yt.rating)


########################### STREAMS & FILTERS ###################################

print("\n\n########## AVAILABLE STREAMS ##########\n\n")

# List All Available Streams
# streams = yt.streams
# for stream in streams:
#     print(stream)

# Audio stream filter
print("\n", 100 * '-')
print("\nAudio Only Streams: \n")
print(100 * '-', "\n")
audios = yt.streams.filter(only_audio=True)
for audio in audios:
    print(audio)

# Video stream filter
print("\n", 100 * '-')
print("\nVideo Only Streams: \n")
print(100 * '-', "\n")
videos = yt.streams.filter(only_video=True)
for video in videos:
    print(video)

# Filter progressive streams - limited to 720p and it contains both audio and video codec files
print("\n", 100 * '-')
print("\nProgressive Streams(Limited to 720p. Includes video & audio): \n")
print(100 * '-', "\n")
progs = yt.streams.filter(progressive=True)
for prog in progs:
    print(prog)

# show highest res prog stream
lowRes = yt.streams.get_lowest_resolution()
print("\n\nFastest Download Option is: ", lowRes, "\n")
highRes = yt.streams.get_highest_resolution()
print("\nHighest Resolution Option is: ", highRes, "\n\n")

# choose stream by itag
print("\n", 100 * '-')
print("\nChoose Your Stream:\n")
print(100 * '-', "\n")
itag = input(
    "Enter the -> itag <- number listed next to the stream you'd like to download: ")
ys = yt.streams.get_by_itag(itag)

########################### BEGIN DOWNLOADING ###################################

print("\n\n########## BEGIN DOWNLOAD ##########\n\n")

# open file dialog box to select folder to download to
root = Tk()
root.withdraw()  # hides small tkinter window
print("Please select a folder to download to! Be aware larger files take longer to download!")
# opens dialog window in front of all other windows
root.attributes('-topmost', True)
download = filedialog.askdirectory()  # returns opened path as a string

if download == '':
    print("\n\nThe download has been canceled.\n\n")
else:
    # download selected stream
    ys.download(download)
    print("\n\nVideo Successfully Downloaded to", download, "\n\n")
