# Rock Band Function Scenario
# You’re managing a rock band climbing the charts. You’ll use the functions below to book gigs, calculate revenue, track fans, and keep your band from falling apart.
# Some functions return one value, some return multiple, and some just print things out. Use them to complete the tasks that follow.
# Provided Functions

# Calculates ticket revenue
# Accepts ticket price (float) and number of tickets sold (int)
# Returns total revenue (float)
def calculate_revenue(price, sold):
    return price * sold

# Adds a new city to the tour schedule
# Accepts tour list and city name (str)
# Adds city to the list (in-place)
def add_city(tour, city):
    tour.append(city)

# Calculates band’s popularity score
# Accepts number of fans (int) and albums sold (int)
# Returns popularity score (int)
def calculate_popularity(fans, albums):
    return fans + (albums * 10)

# Displays your current tour schedule
# Accepts tour list
# Returns nothing, just prints
def display_tour(tour):
    print("Tour Schedule:")
    for stop in tour:
        print("- " + stop)

# Signs a new sponsor deal
# Accepts sponsor name (str), deal amount (float)
# Returns a message and the deal amount
def sign_sponsor(name, amount):
    return f"Signed with {name} for ${amount}", amount

# Records a new album
# Accepts album title (str), number of songs (int)
# Returns a string summary and average song length (float)
def record_album(title, songs):
    avg_length = 3.5  # assume average song length
    return f"Album '{title}' recorded with {songs} tracks", songs * avg_length

# Calculates band expense
# Accepts travel cost (float), food cost (float), and gear cost (float)
# Returns total expense (float)
def calculate_expenses(travel, food, gear):
    return travel + food + gear

# Promotes a single
# Accepts song title (str)
# Returns nothing, prints a message
def promote_single(song):
    print(f"🔥 New single '{song}' is trending on RockTube!")

# Checks if band is eligible for award
# Accepts albums sold (int), years active (int)
# Returns True or False
def is_award_eligible(albums, years):
    return albums >= 5 and years >= 3

# Gets band status
# Accepts name (str), popularity score (int), current city (str)
# Returns a formatted status string
def band_status(name, popularity, city):
    return f"{name} is rocking {city} with a score of {popularity}!"

# Tasks
# 1.	Calculate the revenue for a concert where 3,000 tickets were sold at $45 each.
# 2.	Add “Los Angeles” and “Nashville” to your tour schedule.
# 3.	Display your full tour schedule.
# 4.	Your band has 8,000 fans and has sold 300 albums. Calculate your popularity score.
# 5.	Sign a $150,000 sponsorship deal with “Guitar King Inc.” and print the message.
# 6.	Record an album titled “Loud & Legendary” with 12 songs. Store the summary and total length.
# 7.	Calculate your total expenses for a tour with $12,000 travel, $4,000 food, and $6,000 in gear.
# 8.	Promote your new single called “Neon Lightning.”
# 9.	Check if the band is eligible for an award after selling 7 albums in 4 years.
# 10.	Print your band’s current status with the name “Thunder Strike,” a popularity score of 15,000, and currently touring in Chicago.

#1.
price = 45
sold = 3000
calculate_revenue(price, sold)

#2. 
tour_schedule = ["Nashville"]
city = "Los Angeles"
add_city(tour_schedule, city)

#3.
print(tour_schedule)

#4.
fans = 8000
albums = 300
calculate_popularity(fans, albums)

#5. 
name = "Guitar King Inc."
amount = 150000
sign_sponsor(name, amount)

#6.
title = "Loud & Legendary"
songs = 12
record_album(title, songs)

#7.
travel = 12000
food = 4000
gear = 6000
calculate_expenses(travel, food, gear)

#8.
song = "Neon Lightning"
promote_single(song)

#9.
albums = 7
years = 4
is_award_eligible(albums, years)

name = "Thunder Strike"
popularity = 15000
city = "Chicago"
band_status(name, popularity, city)
