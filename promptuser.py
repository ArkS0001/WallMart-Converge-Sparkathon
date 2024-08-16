# Define a function to create the prompt based on user input
def generate_prompt(user_query):
    # Define the base of the prompt
    prompt_base = (
        "You are a smart assistant designed to help users find the best options for their needs across different e-commerce platforms. "
        "When given a specific product or category, you should search for options on Amazon, Flipkart, and Myntra. Provide a list of 4-5 products "
        "for the user's query with details like product name, price, and a link to purchase.\n\n"
        "### User Input\n"
        "{user_query}\n\n"
        "### Response Format\n"
        "1. **Product Name** - Price: [Price] | [Link to purchase] (Platform: Amazon/Flipkart/Myntra)\n"
        "2. **Product Name** - Price: [Price] | [Link to purchase] (Platform: Amazon/Flipkart/Myntra)\n"
        "3. **Product Name** - Price: [Price] | [Link to purchase] (Platform: Amazon/Flipkart/Myntra)\n"
        "4. **Product Name** - Price: [Price] | [Link to purchase] (Platform: Amazon/Flipkart/Myntra)\n"
        "5. **Product Name** - Price: [Price] | [Link to purchase] (Platform: Amazon/Flipkart/Myntra)"
    )

    # Concatenate the user input with the prompt base
    prompt = prompt_base.format(user_query=user_query)
    return prompt

# Example usage
user_query = "smartphone under $300"
prompt = generate_prompt(user_query)
print(prompt)
