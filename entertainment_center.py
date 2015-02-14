import media
import fresh_tomatoes

#create the objects intantiating the Movie Class. Each object must have the movie title for better reading
training_day = media.Movie('Training Day', '2001', 'The story of an undercover police', 'http://upload.wikimedia.org/wikipedia/en/b/b3/Training_Day_Poster.jpg','https://www.youtube.com/watch?v=vKQi3bBA1y8')
matrix = media.Movie('The Matrix', '1999', 'What is the Matrix?', 'http://www.cyber-cinema.com/gallery/MatrixC.jpg', 'https://www.youtube.com/watch?v=m8e-FF8MsqU')
avatar = media.Movie('Avatar', '2009', 'On the lush alien world of Pandora live the Na\'vi, beings who appear primitive but are highly evolved.', 'http://th05.deviantart.net/fs71/PRE/f/2010/192/b/e/Avatar_Special_Edition_Poster_by_J_K_K_S.jpg', 'https://www.youtube.com/watch?v=_Tkc5pQp_JE')

#create a list storing the favorite movies
fav_movies = [training_day, matrix, avatar]

#call the open_movies_page from fresh_tomatoes module
fresh_tomatoes.open_movies_page(fav_movies)
