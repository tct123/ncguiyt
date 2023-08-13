from nicegui import ui
from pytube import YouTube
def download(e):
    yt = YouTube(url=url.value)
    print("Downloading")
    yt.streams.get_highest_resolution().download(output_path="./videos")
ui.label("Hallo Welt")
url = ui.input(placeholder="Input YouTube-URL")
dlbtn = ui.button(text="Download",on_click=download)
ui.run(title="NCGUIYT")
