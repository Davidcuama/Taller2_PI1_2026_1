from django.core.management.base import BaseCommand
from movie.models import Movie
import csv

class Command(BaseCommand):
    help = 'Load movies from movies_initial.csv into the Movie model'

    def handle(self, *args, **kwargs):
        # Recuerde que la consola está ubicada en la carpeta moviereviewsproject.
        # El archivo movies_initial.csv está en esa misma carpeta.
        csv_file_path = 'movies_initial.csv'

        # Load data from the CSV file
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            movies = list(reader)

        # Add movies to the database
        for i in range(100):
            movie = movies[i]
            exist = Movie.objects.filter(title=movie['title']).first()  # Se asegura que la película no exista en la base de datos
            if not exist:
                Movie.objects.create(
                    title=movie['title'],
                    image='movies/images/default.jpg',
                    genre=movie['genre'],
                    year=movie['year'],
                    description=movie['plot'],
                    url=movie.get('poster', ''),
                )

        self.stdout.write(self.style.SUCCESS('Successfully added movies to the database'))
