from matcher import load_faqs, build_vectorizer, find_best_match


def run_chatbot():
    # Load FAQs and prepare the vectorizer ONCE at the start
    faqs = load_faqs()
    vectorizer, faq_vectors = build_vectorizer(faqs)

    print("=" * 50)
    print("Welcome to the E-commerce FAQ Chatbot!")
    print("Ask me anything about orders, shipping, returns, etc.")
    print("Type 'exit' or 'quit' to stop chatting.")
    print("=" * 50)

    # Keep chatting until user wants to exit
    while True:
        user_input = input("\nYou: ")

        # Check if user wants to leave
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Thank you for chatting! Goodbye!")
            break

        # Find the best matching answer
        answer, score = find_best_match(user_input, faqs, vectorizer, faq_vectors)

        # Display the bot's response
        print(f"Bot: {answer}")


# Run the chatbot when this file is executed directly
if __name__ == "__main__":
    run_chatbot()
