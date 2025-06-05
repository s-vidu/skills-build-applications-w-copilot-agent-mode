import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["octofit_db"]

# Clear existing data
db.users.delete_many({})
db.teams.delete_many({})
db.activity.delete_many({})
db.leaderboard.delete_many({})
db.workouts.delete_many({})

# Users
db.users.insert_many([
    {"email": "alice@example.com", "name": "Alice", "password": "alicepass"},
    {"email": "bob@example.com", "name": "Bob", "password": "bobpass"},
    {"email": "carol@example.com", "name": "Carol", "password": "carolpass"}
])

# Teams
db.teams.insert_many([
    {"name": "Team Alpha", "members": ["alice@example.com", "bob@example.com"]},
    {"name": "Team Beta", "members": ["carol@example.com"]}
])

# Workouts
db.workouts.insert_many([
    {"name": "Pushups", "description": "Do 20 pushups"},
    {"name": "Running", "description": "Run 1 mile"}
])

# Activities
db.activity.insert_many([
    {"user": "alice@example.com", "activity_type": "run", "duration": 30},
    {"user": "bob@example.com", "activity_type": "walk", "duration": 20},
    {"user": "carol@example.com", "activity_type": "strength", "duration": 15}
])

# Leaderboard
db.leaderboard.insert_many([
    {"team": "Team Alpha", "points": 50},
    {"team": "Team Beta", "points": 30}
])

print("Test data populated successfully.")
