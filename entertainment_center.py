from media import Movie
from fresh_tomatoes import create_movie_tiles_content, open_movies_page

movies = [
	Movie(title="Finding Nemo", storyline="We have to find Nemo!",
		trailer_youtube_url="https://youtu.be/XWuPGKLJXe8",
		poster_image_url="https://lumiere-a.akamaihd.net/v1/images/uk_findingnemo_pt_digitaldownload_n_42b8cdb1.png?region=0,0,450,450"),
	Movie(title="Toy Story", storyline="When toys come to life",
		trailer_youtube_url="https://www.youtube.com/watch?v=LJnlmJ4lqik",
		poster_image_url="https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450"),
	Movie(title="Little Mermaid", storyline="She justs wants to see the other side",
		trailer_youtube_url="http://video.disney.com/watch/a-dinglehopper-clip-the-little-mermaid-4dde22bbc81f14aec1d35686",
		poster_image_url="https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-1kf2c8m_4f614e59.jpeg?region=0%2C0%2C300%2C450")
]

#Generate HTML file
open_movies_page(movies)

