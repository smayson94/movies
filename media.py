import webbrowser

class Movie():
    """This class stores information related to
    the individual movies added to database"""


    # constructor for this class. Creates and instance of a movie
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    # funtion to open assigned trailer for a specific movie
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
