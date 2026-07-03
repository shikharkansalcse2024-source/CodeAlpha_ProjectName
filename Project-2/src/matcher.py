import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import clean_text


def load_faqs(filepath="data/faqs.json"):
    with open(filepath, "r", encoding="utf-8") as file:
        faqs = json.load(file)
    return faqs


def build_vectorizer(faqs):
    # Clean every FAQ question first
    cleaned_questions = [clean_text(faq["question"]) for faq in faqs]

    # Create the TF-IDF vectorizer and fit it on our FAQ questions
    vectorizer = TfidfVectorizer()
    faq_vectors = vectorizer.fit_transform(cleaned_questions)

    return vectorizer, faq_vectors


def find_best_match(user_question, faqs, vectorizer, faq_vectors, threshold=0.2):
    # Step 1: Clean the user's question the same way as FAQs
    cleaned_user_question = clean_text(user_question)

    # Step 2: Convert user's question into a vector
    user_vector = vectorizer.transform([cleaned_user_question])

    # Step 3: Compare user's vector against ALL FAQ vectors
    similarity_scores = cosine_similarity(user_vector, faq_vectors)

    # Step 4: Find the index of the highest scoring FAQ
    best_match_index = similarity_scores.argmax()
    best_score = similarity_scores[0][best_match_index]

    # Step 5: If score is too low, we don't have a good match
    if best_score < threshold:
        return "Sorry, I didn't understand that. Could you rephrase your question?", best_score

    # Step 6: Return the matching FAQ's answer
    matched_answer = faqs[best_match_index]["answer"]
    return matched_answer, best_score


if __name__ == "__main__":
    faqs = load_faqs()
    print(f"Loaded {len(faqs)} FAQs successfully!\n")

    vectorizer, faq_vectors = build_vectorizer(faqs)

    print("Vocabulary learned by TF-IDF:")
    print(vectorizer.get_feature_names_out())

    print("\nShape of FAQ vectors matrix:")
    print(faq_vectors.shape)

    test_question = "how much do you charge for shipping?"
    answer, score = find_best_match(test_question, faqs, vectorizer, faq_vectors)

    print(f"\nUser asked: {test_question}")
    print(f"Best match score: {score:.2f}")
    print(f"Bot answer: {answer}")
