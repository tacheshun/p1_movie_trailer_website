import webbrowser

class Movie():
	"""class representation for Movie"""

	def __init__(self, title, release_date, story, poster_image_url, trailer_youtube_url):
		self.title = title
		self.release_date = release_date
		self.story = story
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

