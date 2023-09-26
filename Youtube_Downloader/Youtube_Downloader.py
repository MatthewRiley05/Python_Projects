import customtkinter
from pytube import YouTube
import os
from moviepy.editor import VideoFileClip
from PIL import Image
from CTkToolTip import *

#Setup
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

savePath = os.path.join(os.path.expanduser("~"), "Downloads")

def loadSavePath():
    global savePath
    if os.path.exists("save_path.txt"):
        with open("save_path.txt", "r") as file:
            savePath = file.read().strip()
        
def saveSavePath():
    global savePath
    with open("save_path.txt", "w") as file:
        file.write(savePath)


def openSettings():
    global savePath
    directory=customtkinter.CTkInputDialog(title="Settings",
                                           text="Enter directory path: ",
                                           )
    userPath = directory.get_input()
    if userPath:
        savePath = userPath
    else:
        savePath = os.path.join(os.path.expanduser("~"), "Downloads")
    saveSavePath()

loadSavePath()

def download():
    global savePath
    progressBar.pack(side= "bottom", pady=(0, 20))
    
    finishLabel.configure(text="")
    try:
        ytLink = link.get()
        yt = YouTube(ytLink, on_progress_callback=onProgress)

        if audioSwitch.get() == 0:
            video = yt.streams.get_highest_resolution()
            video.download(savePath)
            title.configure(text=yt.title)
            credit.configure(text="By " + yt.author)

        else:
            preferred_format = "mp4"

            video_stream = yt.streams.filter(file_extension=preferred_format).first()
            if video_stream is not None:
                video_path = video_stream.download(savePath)

                video_clip = VideoFileClip(video_path)
                audio_clip = video_clip.audio

                audio_filename = os.path.splitext(video_path)[0] + '.mp3'
                audio_clip.write_audiofile(audio_filename)

                video_clip.close()
                
                os.remove(video_path)

                title.configure(text=yt.title)
                credit.configure(text="By " + yt.author)

        finishLabel.configure(text="Download Complete", font=("Product Sans", 13, "bold"), text_color="white")

    except Exception as e:
        finishLabel.configure(text="Error: " + str(e),
                              font=("Product Sans", 13, "bold"),
                              text_color="#8C1D18")

    progressBar.pack_forget()

def onProgress(stream, chunk, bytes_remaining):
    totalSize = stream.filesize
    bytes_downloaded = totalSize - bytes_remaining
    percentage = bytes_downloaded / totalSize * 100

    progressBar.set(float(percentage) / 100)
    app.update()

#Settings Symbol
settingsImage = customtkinter.CTkImage(Image.open("settings.png")
                                        )

#UI Elements
settingsButton = customtkinter.CTkButton(app,
                                         height=30,
                                         width=30,
                                         image=settingsImage,
                                         text="",
                                         corner_radius=15,
                                         command=openSettings
                                         )
settingsButton.pack(anchor="e", padx=(0, 20), pady=(20, 0))
settingsButtonToolTip = CTkToolTip(settingsButton,
                                   delay=0.5,
                                   message="Click to open settings",
                                   font=("Product Sans", 10)
                                   )

title = customtkinter.CTkLabel(app,
                               text="YouTube Downloader",
                               font=("Product Sans", 30, "bold"),
                               wraplength=480,
                               )
title.pack(padx=(10), pady=(20, 0))

credit = customtkinter.CTkLabel(app,
                                text="By Matthew Raymundo",
                                font=("Product Sans", 15),
                                )
credit.pack(padx=(10), pady=(0, 40))

#Link Input
url = customtkinter.StringVar()
link = customtkinter.CTkEntry(app,
                              width=380,
                              height=40,
                              textvariable=url
                              )
link.pack(padx=(10), pady=(0, 10))
linkInput = CTkToolTip(link,
                       delay=0.5,
                       message="Input YouTube link here",
                       font=("Product Sans", 10)
                       )

#Download Button
download = customtkinter.CTkButton(app,
                                   text="Download",
                                   text_color="white",
                                   font=("Product Sans", 13, "bold"),
                                   command=download,
                                   corner_radius=15
                                   )
download.pack()
downloadButtonToolTip = CTkToolTip(download,
                                    delay=0.5,
                                    message="Click to begin download",
                                    font=("Product Sans", 10)
                                    )

#Finished Downloading
finishLabel = customtkinter.CTkLabel(app,
                                     text="",
                                     )
finishLabel.pack(pady=(0, 20))

#Audio Only Label
audioLabel = customtkinter.CTkLabel(app,
                                    text="   Audio Only  ",
                                    font=("Product Sans", 13, "bold"),
                                    text_color="white",
                                    fg_color=("#3b8ed0", "#1f6aa5"),
                                    corner_radius=15,
                                    )
audioLabel.pack(padx=(0, 500), pady=(0, 10))

#Audio Only Switch
audioSwitch = customtkinter.CTkSwitch(app,
                                      text="",
                                      )
audioSwitch.pack(padx=(0, 440),)
audioSwitchToolTip = CTkToolTip(audioSwitch,
                                delay=0.5,
                                message="Download audio only",
                                font=("Product Sans", 10)
                                )

#Progress Bar
progressBar = customtkinter.CTkProgressBar(app,
                                           width=380,
                                           height=5
                                           )
progressBar.set(0)

#Loop
app.mainloop()