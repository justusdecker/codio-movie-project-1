# Movie Project Part 1

## What is this project?

The result of an assignment for [Masterschool](https://learn.masterschool.com/). ![NO IMAGE](https://img.shields.io/badge/Movie%20Project%20Part%201-100-4574E0)



A terminal application to CRUD & analyse movie ratings.

## How to use?

> [!NOTE]
> To run this app you need to have `matplotlib` installed.
> 
> Tested on `Python 3.13.3`

1. Open movies.py
2. Select your desired option

## Masterschool Codio Description

## Living in a Movie

This exercise is the first step of the project. In the upcoming units take the Masterschool code and extend it to support additional features.

Build a movie application. This application will store movie names and their ratings.

Communicate with the user via a command line, i.e., print information to the terminal and expect user input.

### Command Types

#### CRUD - Create, Read, Update, Delete

Almost every application implements CRUD commands, since you want to add movies (Create), view the existing movies (Read), update movies (Update), and delete movies (Delete).
> [!NOTE]
> Almost every application implements CRUD commands
> |cmd|desc|
> |---|---|
> |create|add movies|
> |read|view existing movies|
> |update|update movies|
> |delete|delete movies|

#### Analytics

Analytics, such as getting the top-rated movie, the least-rated movie etc.

### Specification

#### Movie Data Structure
Store the movies in a dictionary. Each key in the dictionary stores the movie name, and each value stores the movie’s rating.

```json
{
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
```

#### Menu
When opening the application on the first time, the application should display a title of the application (for example, My Movies Database).
After the title, a menu should be displayed with the different options in the application. Each menu item is printed with a number next to it. Then, the user is requested to enter a choice from the menu.

```
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

Enter choice (1-8): 
```

When the user enters a choice, the command is executed, and then the menu is displayed again so the user can select more options.