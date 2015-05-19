import media
import fresh_tomatoes


toy_story= media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4") 
avatar= media.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
interstellar= media.Movie("Interstellar", "A man travels space in order to save humanity, damn legendary movie", "http://vignette2.wikia.nocookie.net/interstellarfilm/images/4/46/Interstellar_poster.jpg/revision/latest?cb=20140606051928","https://www.youtube.com/watch?v=0vxOhd4qlnA")
miss_granny= media.Movie("Miss Granny", "A woman in her 70s who magically finds herself in the body of her 20-year-old self","http://upload.wikimedia.org/wikipedia/en/4/45/Miss_Granny_poster.jpg","https://www.youtube.com/watch?v=HUIkT3JA0_Q" )
inglorious_bastards= media.Movie("Inglorious Bastards","he film tells the fictional alternate history story of two plots to assassinate Nazi Germany's political leadership","http://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg","https://www.youtube.com/watch?v=6AtLlVNsuAc")
into_the_wild= media.Movie("Into the Wild","It is an adaptation of the 1996 non-fiction book of the same name by Jon Krakauer based on the travels of Christopher McCandless across North America and his life spent in the Alaskan wilderness in the early 1990s.","http://upload.wikimedia.org/wikipedia/en/8/8a/Into-the-wild.jpg","https://www.youtube.com/watch?v=2LAuzT_x8Ek")

print(avatar.trailer_youtube_url)

#toy_story.show_trailer()

interstellar.show_trailer()


movies=[toy_story,avatar, interstellar, miss_granny,inglorious_bastards, into_the_wild]

fresh_tomatoes.open_movies_page(movies)
