import webbrowser
class Movie:
    def __init__(self, title, storyline, image_url, video_url):
        self.title = title
        self.storyline  = storyline
        self.poster_image_url = image_url
        self.trailer_youtube_url  = video_url

    def Show_Trailer(self):
        webbrowser.open(self.video_url)