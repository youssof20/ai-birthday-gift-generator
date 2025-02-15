import openai
import json
import os

# Make sure you set your OpenAI API key in your environment variables or replace with your key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Replace with your OpenAI key if you don't use env vars.

# Function to interact with OpenAI's API and generate gift ideas
def get_gift_ideas(name, age, gender, interests, relationship, budget, personalized_message=None):
    """
    Generates personalized birthday gift ideas using OpenAI GPT.

    Args:
        name (str): The name of the recipient.
        age (int): Age of the recipient.
        gender (str): Gender of the recipient.
        interests (str): A comma-separated list of recipient's interests (e.g., "gaming, cooking, traveling").
        relationship (str): Relationship of the giver to the recipient (e.g., "friend, sibling, partner").
        budget (str): The budget for the gift (e.g., "under $50", "luxury").
        personalized_message (str, optional): Any specific message or requirements for the gift.

    Returns:
        list: A list of personalized gift ideas.
    """
    # Creating a prompt based on the input details
    prompt = f"""
    Generate personalized birthday gift ideas for the following person:
    Name: {name}
    Age: {age}
    Gender: {gender}
    Interests: {interests}
    Relationship: {relationship}
    Budget: {budget}
    If there is any personalized message: {personalized_message if personalized_message else "No specific message."}
    
    Make sure to give creative, unique, and thoughtful gift suggestions.
    """
    
    # Call the OpenAI GPT model to generate gift ideas
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Choose the most suitable model
            prompt=prompt,
            max_tokens=250,
            n=1,
            stop=None,
            temperature=0.7,
        )
        
        gift_ideas = response.choices[0].text.strip()
        return gift_ideas

    except Exception as e:
        print(f"Error occurred: {e}")
        return None


# Function to get user input and customize the gift generation process
def main():
    print("Welcome to the Birthday Gift Idea Generator!")
    
    # Collecting user inputs
    name = input("Enter the recipient's name: ")
    age = int(input("Enter the recipient's age: "))
    gender = input("Enter the recipient's gender (male/female/other): ")
    interests = input("Enter the recipient's interests (comma-separated, e.g., gaming, cooking): ")
    relationship = input("Enter your relationship to the recipient (friend, partner, sibling, etc.): ")
    budget = input("Enter your budget for the gift (e.g., under $50, luxury, etc.): ")
    personalized_message = input("Enter any specific requirements or message for the gift (optional): ")

    # Generating gift ideas
    gift_ideas = get_gift_ideas(name, age, gender, interests, relationship, budget, personalized_message)
    
    if gift_ideas:
        print("\nHere are some unique birthday gift ideas:\n")
        print(gift_ideas)
    else:
        print("Sorry, we couldn't generate gift ideas at the moment. Please try again later.")

# Entry point
if __name__ == "__main__":
    main()
