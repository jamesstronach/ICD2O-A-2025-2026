observations = {
    1: {
        "time": "2:40",
        "cars": 47,
        "pedestrians": 1,
        "bikes": 1,
        "intersection_type": "4-way stop",
        "infractions": "None",
        "notes": "Sunny"
    },
    2: {
        "time": "2:43",
        "cars": 90,
        "pedestrians": 6,
        "bikes": 0,
        "intersection_type": "4-way stop",
        "infractions": "N/A",
        "notes": "Sunny"
    },
    3: {
        "time": "2:48",
        "cars": 96,
        "pedestrians": 3,
        "bikes": 0,
        "intersection_type": "4-way stop",
        "infractions": "None",
        "notes": "Sunny"
    },
    4: {
        "time": "2:50",
        "cars": 106,
        "pedestrians": 3,
        "bikes": 1,
        "intersection_type": "4-way stop",
        "infractions": "1 car no turn signal",
        "notes": "It's sunny outside"
    },
    5: {
        "time": "2:54",
        "cars": 90,
        "pedestrians": 6,
        "bikes": 1,
        "intersection_type": "4-way stop",
        "infractions": "None",
        "notes": "It's sunny outside"
    },
    6: {
        "time": "2:56",
        "cars": 92,
        "pedestrians": 4,
        "bikes": 0,
        "intersection_type": "4-way stop",
        "infractions": "None",
        "notes": "It's sunny outside"
    },
    7: {
        "time": "2:58",
        "cars": 93,
        "pedestrians": 2,
        "bikes": 1,
        "intersection_type": "4-way stop",
        "infractions": "2 car no turn signal",
        "notes": "It's sunny outside"
    }
}


# ===============================
#   ACCESSING A SINGLE OBSERVATION
# ===============================

def get_observation(observations, number):
    # Returns the observation dictionary for a specific observation number.
    # For example: get_observation(observations, 1) returns the first observation.
    # Returns: dict (e.g. {'time': '10:05', 'cars': 14, ...})
    return observations[number]


# ===============================
#   ACCESSING INDIVIDUAL DATA POINTS
# ===============================

def get_observation_time(obs):
    # Returns the time string from a single observation.
    # Returns: str
    return obs["time"]

def get_observation_cars(obs):
    # Returns the number of cars counted during one observation.
    # Returns: int
    return obs["cars"]

def get_observation_pedestrians(obs):
    # Returns the number of pedestrians counted during one observation.
    # Returns: int
    return obs["pedestrians"]

def get_observation_bikes(obs):
    # Returns the number of bikes counted during one observation.
    # Returns: int
    return obs["bikes"]

def get_observation_type(obs):
    # Returns the type of intersection (e.g. '4-way stop', 'Traffic light').
    # Returns: str
    return obs["intersection_type"]

def get_observation_notes(obs):
    # Returns the notes recorded for a single observation.
    # Returns: str
    return obs["notes"]


# ===============================
#   AGGREGATION FUNCTIONS (WORK FOR ANY SIZE DICTIONARY)
# ===============================

def get_num_observations(observations):
    # Returns the total number of observations recorded.
    # Returns: int
    return len(observations)

def get_total_cars(observations):
    # Calculates the total number of cars across all observations.
    # Returns: int
    total = 0
    for obs_num in observations:
        obs = get_observation(observations, obs_num)
        total += get_observation_cars(obs)
    return total

def get_total_pedestrians(observations):
    # Calculates the total number of pedestrians across all observations.
    # Returns: int
    total = 0
    for obs_num in observations:
        obs = get_observation(observations, obs_num)
        total += get_observation_pedestrians(obs)
    return total

def get_average_bikes(observations):
    # Calculates the average number of bikes per observation.
    # Returns: float
    total = 0
    for obs_num in observations:
        obs = get_observation(observations, obs_num)
        total += get_observation_bikes(obs)
    return total / get_num_observations(observations)


# ===============================
#   FORMATTING & PRINTING HELPERS
# ===============================

def format_observation_row(obs_num):
    # Formats a single row of observation data for display in a table.
    # Returns: str (a nicely formatted line of data)
    obslist = get_observation(observations, obs_num)
    return f"{obs_num} | {get_observation_time(obslist)} | {get_observation_cars(obslist)} | {get_observation_pedestrians(obslist)} | {get_observation_bikes(obslist)} | {get_observation_type(obslist)} | {get_observation_notes(obslist)}"

def print_table_header():
    # Prints the header section for the table of observations.
    # Returns: None
    return(f"obs # | Time | {"Cars":>5} | Peds | Bikes | Type {"|":>5} Notes") 

def print_totals(get_total_cars, get_total_pedestrians, get_average_bikes):
    # Prints the total cars, total pedestrians, and average bikes
    # after all observations are displayed.
    # Returns: None
    print(f"TOTAL CARS: {get_total_cars(observations)}")
    print(f"TOTAL PEDESTRIANS: {get_total_pedestrians(observations)}")
    print(f"AVERAGE BIKES: {get_average_bikes(observations):.1f}")

print("INTERSECTION OBSERVATIONS")
print("-"*100)
print(print_table_header())
print("-"*100)
# ob1 = (get_observation(observations,1))
# ob2 = (get_observation(observations,2))
# ob3 = (get_observation(observations,3))
# ob4 = (get_observation(observations,4))
# ob5 = (get_observation(observations,5))
# ob6 = (get_observation(observations,6))
# ob7 = (get_observation(observations,7))

for ob in observations:
    print(format_observation_row(ob))

# print(ob1)
# print(ob2)
# print(ob3)
# print(ob4)
# print(ob5)
# print(ob6)
# print(ob7)
# print("-"*100)

print("-"*100)
print_totals(get_total_cars, get_total_pedestrians, get_average_bikes)