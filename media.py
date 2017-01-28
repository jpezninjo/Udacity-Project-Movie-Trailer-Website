# An object for keeping info about a single movie
class Movie():
	def __init__(self, title, storyline, trailer_youtube_url, poster_image_url):
		self.title = title
		self.storyline = storyline
		self.trailer_youtube_url = trailer_youtube_url
		self.poster_image_url = poster_image_url
