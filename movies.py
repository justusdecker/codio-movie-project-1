from random import randint

import matplotlib.pyplot as plt

from bin.constants import *
from bin.modules import *

class MovieRank:
    max_rating: int = 10.
    def __init__(self):
        self.movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
        }
        
    def list_movies(self):
        """
        Prints a formatted list of all movies currently stored in the collection.

        This method first displays the total number of movies. Then, it prints a header
        for "Movie" and "Rating" columns. Finally, it iterates through each movie
        in the `self.movies` dictionary and prints its title and corresponding rating
        in a clean, tabular format.
        """
        print(f"Movies in total: {len(self.movies)}")
        print(f"{'Movie':<25} {'Rating':<7}")
        for key in self.movies:
            print(f"{key:<25} {self.movies[key]:<7}")
            
    def add_movie(self):
        """
        Prompts the user to add a new movie and its rating to the collection.

        This method guides the user through entering a movie title and its rating.
        It performs validation on the rating to ensure it's a numeric value and
        within the acceptable range (0-10). If the rating is invalid, an error
        message is displayed, and the process is stopped.

        If the movie title does not already exist in the `self.movies` dictionary,
        the new movie and its rating are added. If the movie title already exists,
        it will not be updated by this method (it will simply be skipped, as the
        `if title not in self.movies` condition prevents overwriting).
        """
        title =  get_user_input_colorized("Movie title: ")
        rating = convert_to_float(get_user_input_colorized("Movie rating: "))
        if not rating: 
            error(MSG_RATING_IS_NOT_NUMERIC)
            return
        if rating > 10:
            error(MSG_WRONG_RATING)
            return
        if title not in self.movies:
            self.movies[title] = rating
            
    def remove_movie(self):
        """
        Prompts the user for a movie title and removes it from the collection.

        This method asks the user for the title of the movie they wish to remove.
        It checks if the provided title exists as a key in the `self.movies` dictionary.
        If found, the movie and its rating are removed. If the movie is not found,
        an `MSG_MOVIE_DOESNT_EXIST` error message is displayed.
        """
        title =  get_user_input_colorized("Movie title: ")
        if title in self.movies:
            self.movies.pop(title)
        else:
            error(MSG_MOVIE_DOESNT_EXIST)
            
    def edit_movie(self):
        """
        Allows the user to update the rating of an existing movie.

        This method first prompts the user to enter the title of the movie they wish to edit.
        It checks if the movie exists in the `self.movies` collection. If the movie
        is not found, an error message (`MSG_MOVIE_DOESNT_EXIST`) is displayed, and the
        function returns.

        If the movie is found, the user is then prompted to enter a new rating for it.
        The new rating is validated to ensure it's a numeric value and is within the
        acceptable range (0-10). Invalid ratings will result in an error message
        (`MSG_RATING_IS_NOT_NUMERIC` or `MSG_WRONG_RATING`) and the function returning.

        Upon successful validation, the existing movie's rating in `self.movies` is
        updated with the new value.
        """
        title =  get_user_input_colorized("Movie title: ")
        
        if title not in self.movies:
            error(MSG_MOVIE_DOESNT_EXIST)
            return
        
        rating = convert_to_float(get_user_input_colorized("Movie rating: "))
        
        if not rating: 
            error(MSG_RATING_IS_NOT_NUMERIC)
            return
        if rating > self.max_rating:
            error(MSG_WRONG_RATING)
            return
        if title in self.movies:
            self.movies[title] = rating
        else:
            error(MSG_MOVIE_DOESNT_EXIST)
            
    def print_stats(self):
        """
        Calculates and prints various statistics about the movie ratings.

        This method computes the average, median, worst, and best ratings 
        from the 'movies' attribute of the instance. It then prints these statistics
        in a user-friendly format.
        """
        ratings = [self.movies[i] for i in self.movies]
        median = ratings.copy()
        median.sort()
        median_hlen = len(median)//2
        if len(median) % 2:
            median = median[median_hlen]
        else:
            
            _median_1 = median[median_hlen]
            median.sort(reverse=True)
            median = round((median[median_hlen] +_median_1) / 2,2)
            print(median)
        average = sum(ratings) / len(ratings)
        worst, rating_w = [],11
        best, rating_b = [],-1
        ma, mi = max([self.movies[i] for i in self.movies]) , min([self.movies[i] for i in self.movies])
        for key in self.movies:
            if self.movies[key] == ma:
                best.append(key)
                rating_b = self.movies[key]
            if self.movies[key] == mi:
                worst.append(key)
                rating_w = self.movies[key]
        pass
        print(f"Average rating: {round(average,2)}. Median rating: {median}.\n{"-"*15}")
        print(f'Best Rating{"s" if len(best) > 1 else ""}\n{"-"*15}')
        for b in best:
            print(f"Rating: {b} with {rating_b}/10")
        print(f'Worst Rating{"s" if len(worst) > 1 else ""}\n{"-"*15}')
        for w in worst:
            print(f"Rating: {w} with {rating_w}/10. ")
        
    def print_random_movie(self):
        """ 
        Selects and prints a random movie and its rating from the instance's collection.

        This method randomly picks one movie from the 'movies' attribute and
        displays its title along with its corresponding rating to the console.
        """
        rndMovie = [i for i in self.movies][randint(0,len(self.movies)-1)]
        print(f"{rndMovie}: {self.movies[rndMovie]}")
    
    def print_movies_by_rank(self):
        """
        Prints all movies stored in the instance, sorted by their rating in descending order.

        Each movie's name and its rating (out of 10) are printed to the console.
        The movie name is left-aligned and padded to a width of 35 characters.
        """
        listed = [[i,self.movies[i]] for i in self.movies]
        listed = sorted(listed,key=lambda x: x[1],reverse=True)
        for n, r in listed:
            print(f"{n:<35} {r}/10")
    def print_search(self):
        """
        Searches for and prints movie titles that contain a user-provided string (case-insensitive).

        The search is performed against the keys (movie titles) in the `self.movies` dictionary.
        The user is prompted to enter a search term, and any movie title containing
        this term (regardless of case) will be printed to the console.
        """
        value = get_user_input_colorized("Search: ").lower()
        for key in self.movies:
            if value.lower() in key.lower():
                print(key)

    def plot_movies(self):
        """ Generates and displays a histogram of movie ratings. """
        plt.hist([self.movies[i] for i in self.movies])
        plt.show()
        
    def update(self,inp):
        """
        Acts as a dispatcher for various movie management operations based on user input.

        This method takes a string input, typically representing a user's menu choice,
        and calls the corresponding movie-related method within the class.
        """
        match inp:
            case "1": self.list_movies()
            case "2": self.add_movie()
            case "3": self.remove_movie()
            case "4": self.edit_movie()
            case "5": self.print_stats()
            case "6": self.print_random_movie()
            case "7": self.print_search()
            case "8": self.print_movies_by_rank()
            case "9": self.plot_movies()
            case _: error(MSG_INVALID_INPUT)         

def main():
    while 1:
        print("""\033[J
********** My Movies Database **********

Menu:
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Create Rating Histogram 
        """)

        MR.update(get_user_input_colorized("Enter choice 1-9: "))
    
        get_user_input_colorized("Press Enter to continue")


if __name__ == "__main__":
    MR = MovieRank()
    main()
