"""
Project: 04_ai_sentiment_analyzer.py
Description: A beginner-friendly introduction to Natural Language Processing (NLP) and AI sentiment analysis.
             Analyzes customer or user feedback using lexicon-based sentiment scoring and negation detection.
"""

POSITIVE_WORDS = {
    "excellent", "great", "good", "amazing", "love", "awesome", "fantastic",
    "superb", "helpful", "clean", "fast", "reliable", "brilliant", "wonderful", "easy"
}

NEGATIVE_WORDS = {
    "bad", "terrible", "awful", "horrible", "hate", "slow", "broken",
    "useless", "confusing", "poor", "worst", "buggy", "expensive", "frustrating"
}

NEGATION_WORDS = {"not", "never", "no", "hardly", "barely"}

def clean_tokens(text: str) -> list[str]:
    """Tokenizes text into lowercase clean words without punctuation."""
    cleaned = "".join(ch.lower() if ch.isalnum() or ch.isspace() else " " for ch in text)
    return [word for word in cleaned.split() if word]

def analyze_sentiment(text: str) -> dict:
    """Analyzes text sentiment and returns score, category, and detected emotional words."""
    tokens = clean_tokens(text)
    
    pos_score = 0
    neg_score = 0
    matched_pos = []
    matched_neg = []

    for i, word in enumerate(tokens):
        # Look behind for negation (e.g., "not good")
        has_negation = (i > 0 and tokens[i - 1] in NEGATION_WORDS)

        if word in POSITIVE_WORDS:
            if has_negation:
                neg_score += 1.5
                matched_neg.append(f"not {word}")
            else:
                pos_score += 1.0
                matched_pos.append(word)

        elif word in NEGATIVE_WORDS:
            if has_negation:
                pos_score += 1.0
                matched_pos.append(f"not {word}")
            else:
                neg_score += 1.0
                matched_neg.append(word)

    total_matched = pos_score + neg_score
    net_score = pos_score - neg_score

    if net_score > 0.5:
        category = "POSITIVE"
    elif net_score < -0.5:
        category = "NEGATIVE"
    else:
        category = "NEUTRAL"

    confidence = (abs(net_score) / total_matched * 100) if total_matched > 0 else 50.0

    return {
        "text": text,
        "category": category,
        "net_score": net_score,
        "confidence": confidence,
        "positive_signals": matched_pos,
        "negative_signals": matched_neg
    }

def main():
    print("=" * 70)
    print("           BEGINNER AI SENTIMENT ANALYSIS ENGINE              ")
    print("=" * 70)

    sample_reviews = [
        "The Python AI tutorial is amazing, easy to understand and super helpful!",
        "The app is slow, buggy, and frustrating to use.",
        "The material was okay, neither good nor bad.",
        "The customer service was not helpful and the loading time was slow.",
        "I was worried at first, but the results were not bad at all, actually great!"
    ]

    for review in sample_reviews:
        result = analyze_sentiment(review)
        print(f"\nFeedback   : \"{result['text']}\"")
        print(f"Sentiment  : [{result['category']}] (Confidence: {result['confidence']:.1f}%)")
        print(f"Signals    : Pos -> {result['positive_signals']} | Neg -> {result['negative_signals']}")

    print("\n" + "=" * 70)
    print("[AI Context] In real-world enterprise AI, this task is solved using")
    print("             Transformer models (like BERT, RoBERTa, or GPT) trained on")
    print("             millions of text samples.")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()

