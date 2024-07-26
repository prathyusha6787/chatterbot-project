# Spam detection program

# List of spam words
spam_words = ["win", "free", "offer", "prize", "credit", "loan", "money", "deal", "gift", "subscribe"]

# Function to check if a message is spam
def is_spam(message):
    # Convert message to lowercase for case-insensitive comparison
    message = message.lower()

    # Split message into words
    words = message.split()

    # Check if any spam words appear in the message
    for word in words:
        if word in spam_words:
            return True

    # If no spam words are found, return False
    return False

# Example usage
message = "You have won a free prize! Subscribe now for more deals."
if is_spam(message):
    print("This message is spam.")
else:
    print("This message is not spam.")
