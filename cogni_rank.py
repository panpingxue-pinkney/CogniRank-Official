# cogni_rank.py
# CogniRank - AI-Era Query Insight Evaluator
# Author: panpingxue-pinkney | 2025-10-23

def evaluate_question(question: str) -> int:
    """
    Evaluates the question's depth and returns a score between 0 and 10.
    This simple function uses keyword matching as a starting point for 'CogniRank'.
    """
    score = 0
    q_lower = question.lower()
    
    # Bonus for deep, critical keywords (+2 points)
    deep_keywords = ["why", "how", "future", "change", "impact", "if", "what if", "should", "critique"]
    for keyword in deep_keywords:
        if keyword in q_lower:
            score += 2
    
    # Bonus for length (complex questions are often longer) (+1 point)
    if len(question.split()) > 7: # Increased threshold slightly for better filtering
        score += 1
    
    # Penalty for basic recall phrases (-1 point)
    basic_phrases = ["what is", "define", "explain", "tell me about"]
    for phrase in basic_phrases:
        if phrase in q_lower:
            score -= 1
    
    # Bonus for interdisciplinary terms (simple word count) (+1 point)
    cross_words = ["ai", "humanity", "society", "technology", "mind", "world", "ethics", "system"]
    cross_count = sum(1 for word in cross_words if word in q_lower)
    if cross_count >= 2:
        score += 1
    
    # Ensure the final score is clipped between 0 and 10
    return max(0, min(score, 10))

def get_feedback(score: int) -> str:
    """Returns feedback advice based on the score."""
    if score >= 7:
        return "⭐ Excellent! Cross-disciplinary depth detected. Keep pushing the boundaries!"
    elif score >= 4:
        return "📈 Good. Try adding 'why,' 'how,' or framing it around 'future impact.'"
    else:
        return "💡 Suggestion: Rephrase your question using 'why' or 'how will this change...?'"

# Main execution block
if __name__ == "__main__":
    print("=== CogniRank - Evaluate Your Query Insight ===")
    print("Enter a question for a 0-10 insight score (Type 'quit' to exit)\n")
    
    while True:
        question = input("Your Question: ")
        if question.lower() == 'quit':
            print("Thank you for using CogniRank!")
            break
        
        if not question.strip():
            print("Please enter a valid question!")
            continue
        
        score = evaluate_question(question)
        feedback = get_feedback(score)
        
        print(f"\n📊 Insight Score: {score}/10")
        print(f"{feedback}\n")
        
        # Example suggestion for low scores
        if score < 4 and len(question.strip()) > 0:
            print("Example Improvement:")
            # Simple attempt to rephrase a basic 'what is' into a 'why/how' question
            improved_q = question.lower().replace("what is ", "Why is ").replace("define ", "How does ").replace("?", "") + " important to the future of AI?"
            
            print(f"Original: {question}")
            print(f"Improved: {improved_q.strip()}")
            print()