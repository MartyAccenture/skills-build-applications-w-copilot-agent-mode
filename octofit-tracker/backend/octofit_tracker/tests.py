from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team', description='A test team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team.name)
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2026-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=50)
        self.workout = Workout.objects.create(name='Test Workout', description='A test workout', suggested_for=self.team.name)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'test@example.com')

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'Running')

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.points, 50)

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, 'Test Workout')
