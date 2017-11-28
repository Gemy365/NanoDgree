#OOP- [Entertainments is Main] [MadMax Or Other is Object] [Media is a A class]
import SiteForMovies
import Media

Private = Media.Movie("Private", "ISA",
                        "https://us.123rf.com/450wm/72soul/72soul1401/72soul140100072/25325100-illustration-depicting-a-set-of-cut-out-printed-letters-arranged-to-form-the-word-private.jpg",
                        "https://www.youtube.com/watch?v=99a8L6rnnIg")

MeBeforeYou = Media.Movie("Me Before You", "No StoryLine",
                        "https://upload.wikimedia.org/wikipedia/en/f/fd/Me_Before_You_%28film%29.jpg",
                        "https://www.youtube.com/watch?v=ztA__cx5xDU")

BabyDriver = Media.Movie("Baby Driver", "No StoryLine",
                        "https://i.ytimg.com/vi/D9YZw_X5UzQ/maxresdefault.jpg",
                        "https://www.youtube.com/watch?v=z2z857RSfhk")

Beauty_And_The_Beast = Media.Movie("Beauty And The Beast", "No StoryLine",
                        "https://images-na.ssl-images-amazon.com/images/I/91O+Z+4UIIL._RI_SX200_.jpg",
                        "https://www.youtube.com/watch?v=e3Nl_TCQXuw")

Ratatouille = Media.Movie("Ratatouille", "No StoryLine",
                        "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")

Frozen = Media.Movie("Frozen", "No StoryLine",
                        "http://is1.mzstatic.com/image/thumb/Video/v4/d2/0d/25/d20d2512-5b85-934b-7ded-1b24251afc27/source/227x227bb.jpg",
                        "https://www.youtube.com/watch?v=b2xn0jDmiTw")

Movies = [Private, MeBeforeYou, BabyDriver, Beauty_And_The_Beast, Frozen, Ratatouille]
SiteForMovies.open_movies_page(Movies)
print(Media.Movie.__doc__)           #Documentation
print(Media.Movie.__name__)          #Name Of Class
print(Media.Movie.__module__)        #Name Of File Has This Class
