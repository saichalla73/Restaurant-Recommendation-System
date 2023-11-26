# Function for user input
def get_user_input():
    # Take user input for the type of food
    user_input = input("Enter the type of food you desire: ")
    return user_input

# Data structure to store restaurant information in list and dictionary
restaurants = [
    {
        "Restaurant name": "Little Italy",
        "Cuisine": "Italian",
        "Rating": 4.4,
        "Location": "Jubilee Hills"
    },
    {
        "Restaurant name": "Absolute Barbecues",
        "Cuisine": "Barbecue, Asian",
        "Rating": 4.5,
        "Location": "Gachibowli"
    },
    {
        "Restaurant name": "Barbeque Nation",
        "Cuisine": "Barbecue, North Indian",
        "Rating": 4.3,
        "Location": "Banjara Hills"
    },
    {
        "Restaurant name": "The Fisherman's Wharf",
        "Cuisine": "Seafood, Goan",
        "Rating": 4.2,
        "Location": "Gachibowli"
    },
    {
        "Restaurant name": "Ohri's Jiva Imperia",
        "Cuisine": "Indian, Chinese",
        "Rating": 4.1,
        "Location": "Necklace Road"
    },
    {
        "Restaurant name": "Aish - The Park Hyderabad",
        "Cuisine": "Hyderabadi, North Indian",
        "Rating": 4.6,
        "Location": "Somajiguda"
    },
    {
        "Restaurant name": "Dialogue in the Dark",
        "Cuisine": "Unique Dining Experience",
        "Rating": 4.5,
        "Location": "Inorbit Mall, Hitech City"
    },
    {
        "Restaurant name": "Bidri - Marriott Hyderabad",
        "Cuisine": "Hyderabadi, North Indian",
        "Rating": 4.4,
        "Location": "Tank Bund Road"
    },
    {
        "Restaurant name": "Flechazo",
        "Cuisine": "Mediterranean, Asian",
        "Rating": 4.3,
        "Location": "Madhapur"
    },
    {
        "Restaurant name": "Prost Brew Pub",
        "Cuisine": "Continental, Bar Food",
        "Rating": 4.2,
        "Location": "Jubilee Hills"
    },
    {
        "Restaurant name": "Palato - Marriott Executive Apartments",
        "Cuisine": "Italian, European",
        "Rating": 4.0,
        "Location": "Tank Bund Road"
    },
    {
        "Restaurant name": "Verandah - The Park Hyderabad",
        "Cuisine": "Continental, Asian",
        "Rating": 4.3,
        "Location": "Somajiguda"
    },
    {
        "Restaurant name": "Minerva Coffee Shop",
        "Cuisine": "South Indian, North Indian",
        "Rating": 4.1,
        "Location": "SD Road, Secunderabad"
    },
    {
        "Restaurant name": "Firdaus - Taj Krishna",
        "Cuisine": "Mughlai, North Indian",
        "Rating": 4.6,
        "Location": "Banjara Hills"
    },
    {
        "Restaurant name": "Cascade - Radisson Blu Plaza Hotel",
        "Cuisine": "Multi-Cuisine Buffet",
        "Rating": 4.2,
        "Location": "Banjara Hills"
    },
    {
        "Restaurant name": "Olive Bistro",
        "Cuisine": "Mediterranean, European",
        "Rating": 4.4,
        "Location": "Jubilee Hills"
    },
    {
        "Restaurant name": "Zafraan Exotica",
        "Cuisine": "North Indian, Mughlai",
        "Rating": 4.6,
        "Location": "Hitech City"
    },
    {
        "Restaurant name": "Feast",
        "Cuisine": "Multi-Cuisine",
        "Rating": 4.2,
        "Location": "Sheraton Hyderabad Hotel, Gachibowli"
    },
    {
        "Restaurant name": "Exotica - The Park Hyderabad",
        "Cuisine": "Mediterranean, European",
        "Rating": 4.1,
        "Location": "Somajiguda"
    },
    {
        "Restaurant name": "Prego",
        "Cuisine": "Italian",
        "Rating": 4.3,
        "Location": "Madhapur"
    },
    {
        "Restaurant name": "Olive Qutub",
        "Cuisine": "Mediterranean, European",
        "Rating": 4.5,
        "Location": "Jubilee Hills"
    },
    {
        "Restaurant name": "The Square - Novotel Hyderabad Convention Centre",
        "Cuisine": "International, Asian",
        "Rating": 4.0,
        "Location": "HITEC City"
    },
    {
        "Restaurant name": "Café Bahar",
        "Cuisine": "Hyderabadi, Biryani",
        "Rating": 4.3,
        "Location": "Basheer Bagh"
    },
    {
        "Restaurant name": "Paradise - Food Court, Inorbit Mall",
        "Cuisine": "Hyderabadi, Biryani",
        "Rating": 4.1,
        "Location": "Hitech City"
    },
    {
        "Restaurant name": "Rajdhani Thali Restaurant",
        "Cuisine": "Rajasthani, Gujarati",
        "Rating": 4.2,
        "Location": "Kothapet"
    }
]


# Function to recommend restaurants based on user input
def recommend_restaurants(user_input):
    recommended_restaurants = []
    for restaurant in restaurants:
        if restaurant["Cuisine"].lower() == user_input.lower():
            recommended_restaurants.append(restaurant)
    return recommended_restaurants

# Error handling for invalid food type
def handle_invalid_input():
    print("Sorry, the entered type of food is unavailable or invalid.")

user_input = get_user_input()
recommended = recommend_restaurants(user_input)

if recommended:
    print("Recommended restaurants:")
    for restaurant in recommended:
        print(f"Name: {restaurant['Restaurant name']}, Cuisine: {restaurant['Cuisine']}, Rating: {restaurant['Rating']}, Location: {restaurant['Location']}")
else:
    handle_invalid_input()
