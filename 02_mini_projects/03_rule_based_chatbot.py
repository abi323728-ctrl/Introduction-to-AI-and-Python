"""
Project: 03_rule_based_chatbot.py
Description: A beginner-friendly rule-based AI assistant demonstrating pattern matching,
             string methods, dictionary lookups, and conversational state.
             This demonstrates how classic symbolic/rule-based AI systems work compared to modern ML.
"""

# Knowledge Base: Dictionary mapping intent patterns to responses
INTENT_RESPONSES = {
    "greeting": [
        "Hello! I am your AI study assistant. How can I assist your Python journey today?",
        "Hi there! Ready to explore AI and Python concepts together?"
    ],
    "what_is_ai": [
        "Artificial Intelligence (AI) is the simulation of human intelligence by machines, enabling them to reason, learn, and solve problems."
    ],
    "difference_ai_ml": [
        "AI is the broad umbrella of intelligent machines. Machine Learning (ML) is a subset of AI where systems learn patterns directly from data rather than explicit hand-coded rules."
    ],
    "difference_ml_dl": [
        "Deep Learning is a specialized branch of Machine Learning using multi-layered artificial neural networks inspired by the human brain, ideal for raw unstructured data like images and audio."
    ],
    "python_benefits": [
        "Python is the top language for AI because of its readable syntax, rich scientific ecosystem (NumPy, Pandas, Scikit-learn, PyTorch), and vast community support."
    ],
    "farewell": [
        "Goodbye! Keep practicing your Python programs and keep learning AI!",
        "Catch you later! Don't forget to push your code to GitHub!"
    ]
}

KEYWORD_RULES = [
    (["hi", "hello", "hey", "greetings"], "greeting"),
    (["what is ai", "define ai", "meaning of ai"], "what_is_ai"),
    (["difference between ai and ml", "ai vs ml", "ai or ml"], "difference_ai_ml"),
    (["deep learning", "ml vs dl", "neural network"], "difference_ml_dl"),
    (["why python", "benefits of python", "python for ai"], "python_benefits"),
    (["bye", "exit", "quit", "goodbye"], "farewell"),
]

def classify_intent(user_input: str) -> str:
    """Classifies user query intent using token-aware matching (Rule-Based AI)."""
    normalized = user_input.lower().strip()
    # Clean punctuation for exact word matching
    words = [w.strip("?,!.:;") for w in normalized.split()]
    
    for keywords, intent in KEYWORD_RULES:
        for kw in keywords:
            # If keyword is multiple words, check substring with boundaries or exact phrase
            if " " in kw:
                if kw in normalized:
                    return intent
            else:
                # Single word keyword must match a distinct token
                if kw in words:
                    return intent
    return "unknown"

def generate_response(intent: str) -> str:
    """Fetches appropriate response for the identified intent."""
    if intent in INTENT_RESPONSES:
        return INTENT_RESPONSES[intent][0]
    return "I'm not quite sure about that yet! Try asking about: 'What is AI?', 'AI vs ML', 'Deep Learning', or 'Why Python?'"

def run_sample_dialogue():
    """Runs a simulated conversation showing the assistant in action."""
    print("=" * 65)
    print("         RULE-BASED AI CONVERSATIONAL ASSISTANT DEMO          ")
    print("=" * 65)

    sample_queries = [
        "Hello assistant!",
        "Can you explain what is AI?",
        "What is the difference between AI and ML?",
        "How does Deep Learning fit in?",
        "Why Python for machine learning?",
        "Can you cook spaghetti?",
        "Goodbye!"
    ]

    for query in sample_queries:
        print(f"\nUser       : {query}")
        intent = classify_intent(query)
        response = generate_response(intent)
        print(f"Assistant  : {response}")
        print(f"[Debug Tag]: Classified Intent -> '{intent}'")

    print("\n" + "=" * 65)
    print("[Note] This rule-based bot illustrates classical AI (Expert Systems/Rules)")
    print("       Modern Generative AI uses deep neural networks to produce text.")
    print("=" * 65)

if __name__ == "__main__":
    run_sample_dialogue()
