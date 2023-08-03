from nicegui import ui
from pytube import YouTube
ui.label("Hallo Welt")
url = ui.input(placeholder="Input YouTube-URL")
def download():
    yt = YouTube(url=url.value)
ui.run()
