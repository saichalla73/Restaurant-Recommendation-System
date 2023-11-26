
# Program Overview
The program is designed to recommend restaurants in Hyderabad based on the type of cuisine the user desires. It consists of several components:

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

## Functions Used:

1. **`get_user_input()` Function:**
    - **Purpose:** Retrieves user input for the desired cuisine type.
    
2. **`restaurants` Data Structure:**
    - **Purpose:** Stores restaurant information for various eateries in Hyderabad.
    - **Format:** List of dictionaries, each representing a restaurant.
    - **Dictionary Keys:** "Restaurant name", "Cuisine", "Rating", "Location".

3. **`recommend_restaurants()` Function:**
    - **Purpose:** Generates a list of restaurants matching the user's desired cuisine.
    
4. **`handle_invalid_input()` Function:**
    - **Purpose:** Manages cases of invalid user input for cuisine types.

### Execution Flow:

- **User Input:** Prompts the user to enter a desired cuisine.
- **Recommendation Search:** Matches user input against stored restaurants' cuisines.
- **Display Recommendations:** Shows details of recommended restaurants (name, cuisine, rating, location).
- **Invalid Input Handling:** Manages cases of no matches or invalid input.




## Modifications and Data Addition

- To modify or add more restaurants, update the `restaurants` list of dictionaries in the `restaurant_recommendation.py` file.
- Ensure the dictionary keys remain consistent: "Restaurant name", "Cuisine", "Rating", and "Location".


## Example Usage:

```bash

Enter the type of food you desire: Italian
Recommended restaurants:
Name: Little Italy, Cuisine: Italian, Rating: 4.4, Location: Jubilee Hills
Name: Prego, Cuisine: Italian, Rating: 4.3, Location: Madhapur

![image](https://github.com/saichalla73/Restaurant-Recommendation-System/assets/140317790/c4ab870d-1aa7-4fe1-900d-623ee2c5a0d6)
