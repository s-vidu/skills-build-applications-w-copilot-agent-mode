import pymongo
from bson import ObjectId
from datetime import timedelta

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["octofit_db"]

# Drop existing collections
db.users.drop()
db.teams.drop()
db.activity.drop()
db.leaderboard.drop()
db.workouts.drop()

# Create users (superhero style)
users = [
    {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
    {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
    {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
    {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
]
db.users.insert_many(users)

# Create teams
teams = [
    {"_id": ObjectId(), "name": "Thunderbolts", "members": [users[0]["_id"], users[1]["_id"]]},
    {"_id": ObjectId(), "name": "Cyberpunks", "members": [users[2]["_id"], users[3]["_id"]]},
]
db.teams.insert_many(teams)

# Create workouts
workouts = [
    {"_id": ObjectId(), "name": "Pushups", "description": "Do 20 pushups"},
    {"_id": ObjectId(), "name": "Running", "description": "Run 1 mile"},
    {"_id": ObjectId(), "name": "Situps", "description": "Do 30 situps"},
    {"_id": ObjectId(), "name": "Jump Rope", "description": "Jump rope for 5 minutes"},
]
db.workouts.insert_many(workouts)

# Create activities
activities = [
    {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "run", "duration": 30},
    {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "walk", "duration": 20},
    {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "strength", "duration": 15},
    {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "jump rope", "duration": 10},
]
db.activity.insert_many(activities)

# Create leaderboard (team scores)
leaderboard = [
    {"_id": ObjectId(), "team": teams[0]["_id"], "score": 100},
    {"_id": ObjectId(), "team": teams[1]["_id"], "score": 80},
]
db.leaderboard.insert_many(leaderboard)

print("Monafit-style test data populated successfully.")
