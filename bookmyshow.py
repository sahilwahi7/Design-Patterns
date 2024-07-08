from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime

class Ticket(Enum):
    BOOKED = "Booked"
    AVAILABLE = "Available"

class BookingStatus(Enum):
    CANCELLED = "Cancelled"
    BOOKED = "Booked"
    IN_PROCESS = "In Process"
    PAYMENT_INITIATED = "Payment Initiated"

class CinemaType(Enum):
    SINGLE_SCREEN = "Single Screen"
    MULTIPLEX = "Multiplex"

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using credit card")

class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} in cash")

class Movie:
    def __init__(self, title, language, genre, release_date):
        self.title = title
        self.language = language
        self.genre = genre
        self.release_date = release_date
        self.shows = []

    def add_show(self, show):
        self.shows.append(show)

class Cinema:
    def __init__(self, name, city, cinema_type):
        self.name = name
        self.city = city
        self.cinema_type = cinema_type
        self.halls = []

    def add_hall(self, hall):
        self.halls.append(hall)

class CinemaHall:
    def __init__(self, number, capacity, shows):
        self.number = number
        self.capacity = capacity
        self.shows = shows
        self.seats = {i: Ticket.AVAILABLE for i in range(1, capacity + 1)}

    def book_seat(self, seat_number):
        if self.seats.get(seat_number) == Ticket.AVAILABLE:
            self.seats[seat_number] = Ticket.BOOKED
            print(f"Seat {seat_number} booked")
        else:
            print("Seat already booked")

class MovieShow:
    def __init__(self, movie, show_time):
        self.movie = movie
        self.show_time = show_time

class BookingSystem:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def notify(self, message):
        for customer in self.customers:
            customer.receive_notification(message)

class Customer:
    def __init__(self, name, payment_method):
        self.name = name
        self.payment_method = payment_method

    def book_ticket(self, show, seat_number):
        print(f"{self.name} is booking a ticket for {show.movie.title} at {show.hall.number}")
        show.hall.book_seat(seat_number)
        self.payment_method.pay(10)  # Assuming ticket price is $10

    def receive_notification(self, message):
        print(f"{self.name} received notification: {message}")

class MovieSearch(ABC):
    @abstractmethod
    def search_movies(self, movies, criteria):
        pass

class NameMovieSearch(MovieSearch):
    def search_movies(self, movies, criteria):
        result = [movie for movie in movies if criteria.lower() in movie.title.lower()]
        return result

class GenreMovieSearch(MovieSearch):
    def search_movies(self, movies, criteria):
        result = [movie for movie in movies if criteria.lower() in movie.genre.lower()]
        return result

class LanguageMovieSearch(MovieSearch):
    def search_movies(self, movies, criteria):
        result = [movie for movie in movies if criteria.lower() == movie.language.lower()]
        return result

class CityMovieSearch(MovieSearch):
    def search_movies(self, cinemas, criteria):
        result = []
        for cinema in cinemas:
            for hall in cinema.halls:
                for show in hall.shows:
                    if criteria.lower() == cinema.city.lower():
                        result.append(show.movie)
        return result

class Admin:
    def __init__(self):
        self.movies = []
        self.upcoming_movies = []
        self.events = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def add_upcoming_movie(self, movie):
        self.upcoming_movies.append(movie)

    def add_event(self, event):
        self.events.append(event)

    def get_available_shows(self, movie_title):
        available_shows = []
        for movie in self.movies:
            if movie.title.lower() == movie_title.lower():
                for show in movie.shows:
                    if show.show_time > datetime.now():
                        available_shows.append(show)
        return available_shows

# Usage
if __name__ == "__main__":
    # Create admin
    admin = Admin()

    # Add movies
    inception = Movie("Inception", "English", "Action", datetime(2010, 7, 16))
    dark_knight = Movie("The Dark Knight", "English", "Action", datetime(2008, 7, 18))
    interstellar = Movie("Interstellar", "English", "Science Fiction", datetime(2014, 11, 7))

    # Add upcoming movies
    upcoming_inception = Movie("Inception 2", "English", "Action", datetime(2024, 7, 16))
    upcoming_dark_knight = Movie("The Dark Knight 2", "English", "Action", datetime(2024, 7, 18))
    upcoming_interstellar = Movie("Interstellar 2", "English", "Science Fiction", datetime(2024, 11, 7))

    admin.add_movie(inception)
    admin.add_movie(dark_knight)
    admin.add_movie(interstellar)

    admin.add_upcoming_movie(upcoming_inception)
    admin.add_upcoming_movie(upcoming_dark_knight)
    admin.add_upcoming_movie(upcoming_interstellar)

    # Add events
    class Event:
        def __init__(self, name, event_time):
            self.name = name
            self.event_time = event_time

    event1 = Event("Concert", datetime(2024, 5, 10, 20, 0))
    event2 = Event("Comedy Show", datetime(2024, 5, 15, 18, 30))

    admin.add_event(event1)
    admin.add_event(event2)

    # Define cinemas
    cineplex = Cinema("Cineplex", "New York", CinemaType.MULTIPLEX)
    cineplex.add_hall(CinemaHall(1, 100, [MovieShow(inception, datetime(2024, 5, 12, 14, 30)),
                                           MovieShow(dark_knight, datetime(2024, 5, 12, 16, 30)),
                                           MovieShow(interstellar, datetime(2024, 5, 12, 18, 30))]))

    cinemas = [cineplex]

    # Search movies
    name_search = NameMovieSearch()
    genre_search = GenreMovieSearch()
    language_search = LanguageMovieSearch()
    city_search = CityMovieSearch()

    print("Movies matching 'Inception':", name_search.search
