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
    {"email": "carol@example.com", "name": "Carol", "password": "carolpass"},
    {"email": "dave@example.com", "name": "Dave", "password": "davepass"},
    {"email": "eve@example.com", "name": "Eve", "password": "evepass"},
    {"email": "frank@example.com", "name": "Frank", "password": "frankpass"},
    {"email": "grace@example.com", "name": "Grace", "password": "gracepass"},
    {"email": "hank@example.com", "name": "Hank", "password": "hankpass"},
    {"email": "ian@example.com", "name": "Ian", "password": "ianpass"},
    {"email": "jane@example.com", "name": "Jane", "password": "janepass"},
    {"email": "lisa@example.com", "name": "Lisa", "password": "lisapass"},
    {"email": "mike@example.com", "name": "Mike", "password": "mikepass"},
    {"email": "nina@example.com", "name": "Nina", "password": "ninapass"},
    {"email": "oliver@example.com", "name": "Oliver", "password": "oliverpass"},
    {"email": "paula@example.com", "name": "Paula", "password": "paulapass"},
    {"email": "quentin@example.com", "name": "Quentin", "password": "quentinpass"},
    {"email": "ryan@example.com", "name": "Ryan", "password": "ryanpass"},
    {"email": "sophia@example.com", "name": "Sophia", "password": "sophiapass"},
    {"email": "thomas@example.com", "name": "Thomas", "password": "thomaspass"}
])

# Teams
db.teams.insert_many([
    {"name": "Team Alpha", "members": ["alice@example.com", "bob@example.com"]},
    {"name": "Team Beta", "members": ["carol@example.com"]},
    {"name": "Team Gamma", "members": ["dave@example.com", "eve@example.com"]},
    {"name": "Team Delta", "members": ["frank@example.com", "grace@example.com"]},
    {"name": "Team Epsilon", "members": ["hank@example.com"]},
    {"name": "Team Zeta", "members": ["ian@example.com", "jane@example.com"]},
    {"name": "Team Eta", "members": ["kyle@example.com"]},
    {"name": "Team Theta", "members": ["lisa@example.com", "mike@example.com"]},
    {"name": "Team Iota", "members": ["nina@example.com"]},
    {"name": "Team Kappa", "members": ["oliver@example.com", "paula@example.com"]},
    {"name": "Team Lambda", "members": ["quentin@example.com"]},
    {"name": "Team Mu", "members": ["ryan@example.com", "sophia@example.com"]},
    {"name": "Team Nu", "members": ["thomas@example.com"]}
])

# Workouts
db.workouts.insert_many([
    {"name": "Pushups", "description": "Do 20 pushups"},
    {"name": "Running", "description": "Run 1 mile"},
    {"name": "Situps", "description": "Do 30 situps"},
    {"name": "Jump Rope", "description": "Jump rope for 5 minutes"},
    {"name": "Plank", "description": "Hold a plank for 1 minute"},
    {"name": "Burpees", "description": "Do 15 burpees"},
    {"name": "Squats", "description": "Do 25 squats"},
    {"name": "Lunges", "description": "Do 20 lunges"},
    {"name": "Mountain Climbers", "description": "Do 30 mountain climbers"},
    {"name": "High Knees", "description": "Do high knees for 1 minute"},
    {"name": "Pushups Advanced", "description": "Do 50 pushups"},
    {"name": "Sprint", "description": "Sprint for 2 minutes"},
    {"name": "Box Jumps", "description": "Do 20 box jumps"},
    {"name": "Pull-ups", "description": "Do 10 pull-ups"}
])

# Activities
db.activity.insert_many([
    {"user": "alice@example.com", "activity_type": "run", "duration": 30},
    {"user": "bob@example.com", "activity_type": "walk", "duration": 20},
    {"user": "carol@example.com", "activity_type": "strength", "duration": 15},
    {"user": "dave@example.com", "activity_type": "jump rope", "duration": 10},
    {"user": "eve@example.com", "activity_type": "situps", "duration": 25},
    {"user": "frank@example.com", "activity_type": "plank", "duration": 1},
    {"user": "grace@example.com", "activity_type": "burpees", "duration": 15},
    {"user": "hank@example.com", "activity_type": "run", "duration": 45},
    {"user": "ian@example.com", "activity_type": "squats", "duration": 25},
    {"user": "jane@example.com", "activity_type": "lunges", "duration": 20},
    {"user": "kyle@example.com", "activity_type": "run", "duration": 50},
    {"user": "lisa@example.com", "activity_type": "mountain climbers", "duration": 30},
    {"user": "mike@example.com", "activity_type": "high knees", "duration": 60},
    {"user": "nina@example.com", "activity_type": "run", "duration": 55},
    {"user": "oliver@example.com", "activity_type": "pushups advanced", "duration": 50},
    {"user": "paula@example.com", "activity_type": "sprint", "duration": 2},
    {"user": "quentin@example.com", "activity_type": "run", "duration": 60},
    {"user": "ryan@example.com", "activity_type": "box jumps", "duration": 20},
    {"user": "sophia@example.com", "activity_type": "pull-ups", "duration": 10},
    {"user": "thomas@example.com", "activity_type": "run", "duration": 65}
])

# Leaderboard
db.leaderboard.insert_many([
    {"team": "Team Alpha", "points": 50},
    {"team": "Team Beta", "points": 30},
    {"team": "Team Gamma", "points": 40},
    {"team": "Team Delta", "points": 60},
    {"team": "Team Epsilon", "points": 35},
    {"team": "Team Zeta", "points": 70},
    {"team": "Team Eta", "points": 40},
    {"team": "Team Theta", "points": 80},
    {"team": "Team Iota", "points": 45},
    {"team": "Team Kappa", "points": 90},
    {"team": "Team Lambda", "points": 50},
    {"team": "Team Mu", "points": 100},
    {"team": "Team Nu", "points": 55}
])

print("Test data populated successfully.")
