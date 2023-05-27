from pytube import YouTube

def Download(link):
    youtube_Object = YouTube(link)
    youtube_Object = youtube_Object.streams.get_highest_resolution()
    try:
        youtube_Object.download()
    except:
        print("Sorry error has occurred")
        
    print("Download Is Completed Successfully")


link = input("Please enter the youTube video URL/link: ")

Download(link)