import webbrowser
class Movie():
    ''' This Is Documentation About This Class'''        #Documentation
    #__init__ is Special Method.. it's Construtor
    def __init__(self, movie_Title, movie_StoryLine, movie_Poster_Image,
                 movie_Trailer_Youtube): #Self it's Default == Name Of Object

        self.title = movie_Title
        self.storyLine = movie_StoryLine
        self.poster_image_url = movie_Poster_Image
        self.trailer_youtube_url = movie_Trailer_Youtube

    def Show_Trailer(self):
        webbrowser.open(self.trailerYoutube)
