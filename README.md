
# Program Overview
The program is designed to recommend restaurants in Hyderabad based on the type of cuisine the user desires. It consists of several components:

`get_user_input() Function:

This function takes user input for the type of food/cuisine they desire.

restaurants Data Structure:

Contains information about various restaurants in Hyderabad in the form of a list of dictionaries. Each dictionary represents a restaurant with keys such as "Restaurant name", "Cuisine", "Rating", and "Location".

recommend_restaurants() Function:

Takes the user input as an argument and matches it with the restaurants' cuisines in the restaurants list.
If there are matches, it creates a list of recommended restaurants based on the user's desired cuisine.

handle_invalid_input() Function:

Handles cases where the user enters an invalid or unavailable cuisine type.

Execution Logic:

Retrieves user input for the type of cuisine.
Uses the recommend_restaurants() function to find restaurants that match the user's input.
If matches are found, it displays the recommended restaurants' details (name, cuisine, rating, location). Otherwise, it notifies the user of an invalid input.

# Restaurant Recommender

This Python script recommends restaurants based on the type of cuisine entered by the user.

## Setup Instructions

Firstly installed python latest version from the official webiste. Used this link: (https://www.python.org/) for installing.
After installation, opened cmd ->> entered python --version, to check if it is installed and up to date. Later, using cmd, created two files :

restaurant_recommendation.py
test_recommendation.py

## How to Use

1. **Running the Script:**
    - After Ensuring I have Python installed in my system.
    - In a terminal or command prompt.
    - Navigate to the directory containing the `restaurant_recommender.py` file.
    - Run the script by executing `python restaurant_recommender.py`.

2. **Input:**
    - The script will prompt you to enter the type of food you desire.
    - user can enter their desired food type like "Italian", "Italian, European", "Seafood, Goan" etc..

3. **Output:**
    - If restaurants matching the entered cuisine are found in the database, the script will display their names, cuisines, ratings, and locations.
    - If no matching restaurants are found or if the input is invalid, an appropriate message will be displayed.

## File Structure

- `restaurant_recommendation.py`: Contains the Python script for restaurant recommendation.
- `test_recommendation.py: It Contains Test Cases
- `README.md`: This file, providing instructions and information about the script.

## Modifications and Data Addition

- To modify or add more restaurants, update the `restaurants` list of dictionaries in the `restaurant_recommendation.py` file.
- Ensure the dictionary keys remain consistent: "Restaurant name", "Cuisine", "Rating", and "Location".


Enter the type of food you desire: Italian
Recommended restaurants:
Name: Little Italy, Cuisine: Italian, Rating: 4.4, Location: Jubilee Hills
Name: Prego, Cuisine: Italian, Rating: 4.3, Location: Madhapur
