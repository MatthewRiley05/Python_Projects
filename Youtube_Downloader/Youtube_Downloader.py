import customtkinter
from pytube import YouTube
import os
import time

save_path = os.path.join(os.path.expanduser("~"), "Downloads")

def download():
    progressBar.pack()
    try:
        ytLink = link.get()
        yt = YouTube(ytLink, on_progress_callback=onProgress)
        video = yt.streams.get_highest_resolution()
        video.download(save_path)

        title.configure(text=yt.title)
        credit.configure(text="By " + yt.author)
    except:
        finishLabel.configure(text="Unable to Download", text_color="#8C1D18")
        return
    finishLabel.configure(text="Download Complete")

def onProgress(stream, chunk, bytes_remaining):
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
                               text="YouTube Video Downloader",
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
link.pack(padx=(10), pady=(0, 20))

#Download Button
download = customtkinter.CTkButton(app,
                                   text="Download",
                                   font=("Product Sans", 13),
                                   command=download,
                                   corner_radius=15
                                   )
download.pack()

#Finished Downloading
finishLabel = customtkinter.CTkLabel(app,
                                     text="",
                                     )
finishLabel.pack(pady=(0, 20))

#Progress Bar
progressBar = customtkinter.CTkProgressBar(app,
                                           width=380,
                                           height=5
                                           )
progressBar.set(0)

#Loop
app.mainloop()