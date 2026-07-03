import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load English stopwords once (so we don't reload every time)
STOPWORDS = set(stopwords.words('english'))


def clean_text(sentence):
    # Step 1: Convert everything to lowercase
    sentence = sentence.lower()

    # Step 2: Remove punctuation like ? ! , .
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))

    # Step 3: Split sentence into individual words (tokenize)
    words = word_tokenize(sentence)

    # Step 4: Remove common stopwords (the, is, are, what, etc.)
    filtered_words = [word for word in words if word not in STOPWORDS]

    # Step 5: Join the cleaned words back into one string
    cleaned_sentence = " ".join(filtered_words)

    return cleaned_sentence


# This block only runs if you execute this file directly (for testing)
if __name__ == "__main__":
    test_sentence = "What ARE your Delivery Charges??"
    print("Original:", test_sentence)
    print("Cleaned :", clean_text(test_sentence))
