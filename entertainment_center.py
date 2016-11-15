import media
import fresh_tomatoes

# class instantiating section

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", #noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc") #noqa

inside_man = media.Movie("Inside Man",
                         "The volatile showdown between a determined",
                         "cop and a perfectionist bank robber",
                         "is sent spiraling toward disaster when a scheming power broker steps",
                         "in to take control of the situation",
                         "https://upload.wikimedia.org/wikipedia/en/a/a2/Inside_Man_%28film_poster%29.jpg", #noqa
                         "https://www.youtube.com/watch?v=3WRxsmqercg") #noqa

the_big_short = media.Movie("The Big Short",
                            "In 2005, eccentric hedge fund manager Michael",
                            "Burry discovers that the United States",
                            "housing market is extremely unstable,",
                            " being based on high-risk subprime loans.",
                            "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRCb6lxfYBkprudGKI83kGztRtUd2_BTpCurkpIUjSxUI4ruiJB8g", #noqa
                            "https://www.youtube.com/watch?v=vgqG3ITMv1Q") #noqa
the_martian = media.Movie("The Martian",
                          "During a manned mission to Mars, Astronaut Mark Watney",
                          " (Matt Damon) is presumed dead",
                          "after a fierce storm and left behind by his crew.",
                          " But Watney has survived",
                          "and finds himself stranded and alone on the hostile planet.",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/c/cd/The_Martian_film_poster.jpg/220px-The_Martian_film_poster.jpg", #noqa
                          "https://www.youtube.com/results?search_query=the+martian") #noqa

pulp_fiction = media.Movie("Pulp Fiction",
                           "Hitmen Jules Winnfield and Vincent Vega are",
                           " on their way to retrieve a briefcase from Brett,",
                           "who has transgressed against their boss, gangster Marsellus Wallace.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Pulp_Fiction_%281994%29_poster.jpg/220px-Pulp_Fiction_%281994%29_poster.jpg", #noqa
                           "https://www.youtube.com/watch?v=Mnb_3ibUp38") #noqa

enter_the_dragon = media.Movie("Enter the Dragon",
                               "The story finds Lee as a martial-arts expert determined",
                               "to help capture the narcotics dealer whose gang was responsible",
                               " for his sister's death.",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/e/ef/Enter_the_dragon.jpg/220px-Enter_the_dragon.jpg", #noqa
                               "https://www.youtube.com/watch?v=tB-QGOChuQc") #noqa
django_unchained = media.Movie("Django Unchained",
                               "Schultz is on the trail of the murderous Brittle brothers,",
                               " and only Django can lead him to his bounty.",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/8/8b/Django_Unchained_Poster.jpg/220px-Django_Unchained_Poster.jpg", #noqa
                               "https://www.youtube.com/watch?v=eUdM9vrCbow") #noqa
monsters_inc = media.Movie("Monsters, INC.",
                           "Hulking, blue-furred behemoth James P. Sullivan (John Goodman)",
                           " and his one-eyed assistant",
                           "Mike Wazowski (Billy Crystal) are employed by Monsters, Inc.,",
                           " a scream processing factory.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/6/63/Monsters_Inc.JPG/220px-Monsters_Inc.JPG", #noqa
                           "https://www.youtube.com/watch?annotation_id=annotation_24492&feature=iv&src_vid=cvOQeozL4S0&v=Ue_SfrHHBAc") #noqa

#appending movies to list:
movies = [toy_story, inside_man, the_big_short, the_martian, pulp_fiction, enter_the_dragon, django_unchained, monsters_inc]
#calls external rendering function to add each movie to webpage:
fresh_tomatoes.open_movies_page(movies)

                        
                           
                           
                        
                        
                          
                         
                        
