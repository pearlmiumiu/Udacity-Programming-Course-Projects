import webbrowser

class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title=movie_title
		self.storyline=movie_storyline
		self.poster_image_url=poster_image
		self.trailer_youtube_url=trailer_youtube

    def show_trailer(self):
    	webbrowser.open(self.trailer_youtube_url)


import media
toy_story=media.movie("toy story", "a story of a boy and his toys that come to lief",
	"https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450",
	"https://www.youtube.com/watch?v=c3986gGp3Qs")   



avatar=media.movie("avatar", "a marine on an alien planet", 
	"https://static.independent.co.uk/s3fs-public/thumbnails/image/2016/07/28/16/avatar.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")


