# Function for user input
def get_user_input():
    # Take user input for the type of food
    user_input = input("Enter the type of food you desire: ")
    return user_input

# Data structure to store restaurant information
restaurants = [
    {"name": "Restaurant 1", "cuisine": "Italian", "rating": 4.5, "location": "City 1"},
    {"name": "Restaurant 2", "cuisine": "Chinese", "rating": 4.0, "location": "City 2"},
    # Add more restaurant entries
]

# Function to recommend restaurants based on user input
def recommend_restaurants(user_input):
    recommended_restaurants = []
    for restaurant in restaurants:
        if restaurant["cuisine"].lower() == user_input.lower():
            recommended_restaurants.append(restaurant)
    return recommended_restaurants

# Error handling for invalid food type
def handle_invalid_input():
    print("Sorry, the entered type of food is unavailable or invalid.")

# Test cases for recommendation system
# Write test cases to ensure the functionality of recommend_restaurants()

# User Interaction
user_input = get_user_input()
recommended = recommend_restaurants(user_input)

if recommended:
    print("Recommended restaurants:")
    for restaurant in recommended:
        print(f"Name: {restaurant['name']}, Cuisine: {restaurant['cuisine']}, Rating: {restaurant['rating']}, Location: {restaurant['location']}")
else:
    handle_invalid_input()