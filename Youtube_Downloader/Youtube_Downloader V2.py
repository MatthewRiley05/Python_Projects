import customtkinter
from pytube import YouTube
import os
from moviepy.editor import VideoFileClip

def download():
    save_path = os.path.join(os.path.expanduser("~"), "Downloads")
    progressBar.pack(side= "bottom", pady=(0, 20))

    finishLabel.configure(text="")
    try:
        ytLink = link.get()
        yt = YouTube(ytLink, on_progress_callback=onProgress)

        if audioSwitch.get() == 0:
            video = yt.streams.get_highest_resolution()
            video.download(save_path)
            title.configure(text=yt.title)
            credit.configure(text="By " + yt.author)

        else:
            preferred_format = "mp4"

            video_stream = yt.streams.filter(file_extension=preferred_format).first()
            if video_stream is not None:
                video_path = video_stream.download(save_path)

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

def onProgress(stream, bytes_remaining):
    totalSize = stream.filesize
    bytes_downloaded = totalSize - bytes_remaining
    percentage = bytes_downloaded / totalSize * 100
    per = str(int(percentage))

    progressBar.set(float(percentage) / 100)
    app.update()

#Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#UI Elements
title = customtkinter.CTkLabel(app,
                               text="YouTube Downloader",
                               font=("Product Sans", 30, "bold"),
                               wraplength=480,
                               )
title.pack(padx=(10), pady=(40, 0))

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



#Download Button
download = customtkinter.CTkButton(app,
                                   text="Download",
                                   font=("Product Sans", 13, "bold"),
                                   command=download,
                                   corner_radius=15
                                   )
download.pack()

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
                                    fg_color="#1f6aa5",
                                    corner_radius=15,
                                    )
audioLabel.pack(padx=(0, 500), pady=(0, 10))

#Audio Only Switch
audioSwitch = customtkinter.CTkSwitch(app,
                                      text="",
                                      )
audioSwitch.pack(padx=(0, 440),)

#Progress Bar
progressBar = customtkinter.CTkProgressBar(app,
                                           width=380,
                                           height=5
                                           )
progressBar.set(0)

#Loop
app.mainloop()