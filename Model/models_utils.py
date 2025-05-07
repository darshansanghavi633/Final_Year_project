# model_utils.py

import re
import yake

# Custom stopwords list (can be expanded)
STOPWORDS = set([
    "a", "an", "the", "and", "or", "but", "if", "in", "on", "with", "as", "by",
    "for", "of", "at", "to", "from", "up", "down", "out", "over", "under",
    "again", "further", "then", "once", "it", "its", "they", "them", "their",
    "what", "which", "who", "whom", "this", "that", "these", "those", "is",
    "are", "was", "were", "be", "been", "being", "have", "has", "had", "do",
    "does", "did", "will", "would", "should", "can", "could", "may", "might",
    "must", "shall", "should"
])

def preprocess_text(text):
    """
    Preprocess the text by removing punctuation, converting to lowercase, and tokenizing.
    """
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    tokens = text.lower().split()  # Convert to lowercase and split into words
    return tokens

def extract_keywords_yake(text, top_n=5):
    """
    Extract meaningful keywords from the text using YAKE.
    """
    # Initialize YAKE keyword extractor
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(text)

    # Filter out stopwords and short words
    filtered_keywords = [kw for kw, score in keywords if kw.lower() not in STOPWORDS and len(kw) > 2]

    # Return top N keywords
    return filtered_keywords[:top_n]

def get_keyword_description(keyword):
    """
    Provide a contextually relevant description for each keyword.
    """
    descriptions = {
        "digital": "Digital technologies are transforming industries and creating new opportunities for innovation.",
        "technology": "Advancements in technology are driving efficiency and enabling new business models.",
        "ai": "Artificial intelligence is revolutionizing industries by automating processes and enabling smarter decision-making.",
        "machine learning": "Machine learning is unlocking new possibilities by analyzing vast amounts of data.",
        "blockchain": "Blockchain technology is enhancing transparency and security across various sectors.",
        "cloud computing": "Cloud computing is enabling scalable and flexible solutions for businesses.",
        "cybersecurity": "Cybersecurity is critical for protecting sensitive data and ensuring business continuity.",
        "iot": "The Internet of Things (IoT) is connecting devices and enabling smarter ecosystems.",
        "automation": "Automation is streamlining workflows and reducing manual effort across industries.",
        "big data": "Big data is providing actionable insights and driving data-driven decision-making.",
        # Add more descriptions here
    }
    return descriptions.get(keyword, f"{keyword.capitalize()} is a critical factor shaping the future of this field.")

def generate_linkedin_post(topic, keywords):
    """
    Generate a well-structured and engaging LinkedIn post based on the number of keywords.
    """
    # Dynamic introduction
    intro = f"🚀 **{topic}: Key Insights You Need to Know** 🚀\n\n"
    intro += f"In today's ever-evolving landscape, staying ahead means understanding the latest trends and innovations. Here are the crucial aspects of {topic} that are shaping the future:\n\n"

    # Dynamic body based on the number of keywords
    body = ""
    for keyword in keywords:
        description = get_keyword_description(keyword)
        body += f"✅ **{keyword.capitalize()}** – {description}\n"

    # Dynamic conclusion
    conclusion = (
        f"\nSuccess in {topic} requires keeping up with these trends and leveraging them for strategic growth. Let's innovate and embrace the future together! 💡✨\n\n"
        f"#Innovation #Growth #Leadership #{' #'.join([keyword.replace(' ', '') for keyword in keywords])}"
    )

    # Combine all parts
    post = intro + body + conclusion
    return post
