from random import randint

__version__ = "1.2"

import matplotlib.pyplot as plt

MSG_MOVIE_DOESNT_EXIST = "This movie doesn't exist!"
MSG_RATING_IS_NOT_NUMERIC = "Rating is not a number!"
MSG_INVALID_INPUT = "Invalid Input!"
MSG_NO_RESULTS = 'No Results!'
MSG_WRONG_RATING = "Enter a rating in range: 0 - 10"

def compare_two_strings(a: str, b: str) -> int:
    return any([b.count(char) >= a.count(char) and char in b for char in a])

def error(msg: str) -> None:
    """ prints a text in ✨fancy red✨ """
    print(f"\033[0;31m{msg}\033[0m")
    
def convert_to_float(text:str) -> bool | float:
    """
    Return the float: convert is possible
    Return False: Error occured
    """
    if text.count(".") == 0 and text.isdecimal():
        return float(text)
    if text.count(".") == 1 and text != '.':
        a,b = text.split(".")
        if a + b == 2: return False #Is not a float
        return float(f"{a + '.' if a.isdecimal() else '0.'}{b if b.isdecimal() else '0'}")
    return False

def get_user_input_colorized(msg):
    _ret = input(f"{msg}\033[1;32m")
    print("\033[0m",end="")
    return _ret

class MovieRank:
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
        """ Show all movies in a table """
        print(f"Movies in total: {len(self.movies)}")
        print(f"{'Movie':<25} {'Rating':<7}")
        for key in self.movies:
            print(f"{key:<25} {self.movies[key]:<7}")
            
    def add_movie(self):
        """
        Get user input & use it to add a new movie to ``self.movies``
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
        Get user input & use it to remove a movie from ``self.movies``
        """
        title =  get_user_input_colorized("Movie title: ")
        if title in self.movies:
            self.movies.pop(title)
        else:
            error(MSG_MOVIE_DOESNT_EXIST)
            
    def edit_movie(self):
        """
        Get user input & use it to edit a movie in ``self.movies``
        """
        title =  get_user_input_colorized("Movie title: ")
        
        if title in self.movies:
            error(MSG_MOVIE_DOESNT_EXIST)
            return
        
        rating = get_user_input_colorized("Movie rating: ")
        
        if not rating: 
            error(MSG_RATING_IS_NOT_NUMERIC)
            return
        if rating > 10:
            error(MSG_WRONG_RATING)
            return
        if title in self.movies:
            self.movies[title] = rating
        else:
            error(MSG_MOVIE_DOESNT_EXIST)
            
    def print_stats(self):
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
        worst, ratingW = "",11
        best, ratingB = "",-1
        
        for key in self.movies:
            if self.movies[key] > ratingB:
                best = key
                ratingB = self.movies[key]
            if self.movies[key] < ratingW:
                worst = key
                ratingW = self.movies[key]
        
        print(f"Average rating: {round(average,2)}. Median rating: {median}. Worst Rating: {worst} with {ratingW}/10. Best Rating: {best} with {ratingB}/10")
        
    def print_random_movie(self):
        rndMovie = [i for i in self.movies][randint(0,len(self.movies)-1)]
        print(f"{rndMovie}: {self.movies[rndMovie]}")
    
    def print_movies_by_rank(self):
        listed = [[i,self.movies[i]] for i in self.movies]
        listed = sorted(listed,key=lambda x: x[1],reverse=True)
        for n, r in listed:
            print(f"{n:<35} {r}/10")
    def print_search(self):
        value = get_user_input_colorized("Search: ").lower()
        normal_movies = list(self.movies)
        low_movies = [m.lower() for m in normal_movies]
        results = 0
        if value in low_movies:
            #normal_movies[low_movies.index(value)]
            results += 1
            print(normal_movies[low_movies.index(value)])
        if not results:
            for movie in self.movies:
                if compare_two_strings(value, movie):
                    print(movie)
    def plot_movies(self):
        plt.hist([self.movies[i] for i in self.movies])
        plt.show()
        
    def update(self,inp):
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
