from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel.name),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel.name),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc.name),
            User(name='Batman', email='batman@dc.com', team=dc.name),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2026-01-10')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2026-01-11')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2026-01-12')
        Activity.objects.create(user=users[3], type='Yoga', duration=40, date='2026-01-13')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=120)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', suggested_for='Marvel')
        Workout.objects.create(name='Power Yoga', description='Strength and flexibility', suggested_for='DC')

        # Ensure unique index on email field in user collection using pymongo
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db['octofit_tracker_user'].create_index('email', unique=True)
        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data and unique index on email'))
