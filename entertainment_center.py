import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about toys.",
                        "https://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
the_incredibles = media.Movie("The Incredibles",
                              "The most incredible movie ever.",
                              "https://pixarplanet.com/blog/wp-content/uploads/2015/09/the_incredibles_movie-wallpaper.jpg",
                              "https://www.youtube.com/watch?v=eZbzbC9285I")
frozen = media.Movie("Frozen",
                     "Let it go!",
                     "http://img.lum.dolimg.com/v1/images/homepage_hero_frozen_winter_18c81bd7.jpeg?region=0%2C0%2C480%2C240",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")
aladdin = media.Movie("Aladdin",
                      "Prince Ali",
                     "https://i.ytimg.com/vi/8dVObCM54Xo/maxresdefault.jpg",
                     "https://www.youtube.com/watch?v=QapaqcDucmg")
movies = (toy_story, the_incredibles, frozen, aladdin)
fresh_tomatoes.open_movies_page(movies)