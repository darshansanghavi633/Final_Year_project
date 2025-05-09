import re
import yake
from collections import defaultdict

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
    Preprocess the text by removing punctuation, converting to
lowercase, and tokenizing.
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
    filtered_keywords = [kw for kw, score in keywords if kw.lower()
not in STOPWORDS and len(kw) > 2]

    # Return top N keywords
    return filtered_keywords[:top_n]

def get_keyword_description(keyword):
    """
    Provide a contextually relevant description for each keyword.
    """
    descriptions = {
        # Technology
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

        # Business and Marketing
        "marketing": "Marketing strategies are evolving to leverage data-driven insights and personalized customer experiences.",
        "branding": "Effective branding is essential for building trust and loyalty among customers.",
        "sales": "Sales strategies are becoming more customer-centric and data-driven.",
        "ecommerce": "E-commerce is reshaping the retail landscape and enabling global reach.",
        "customer experience": "Customer experience is a key differentiator in today's competitive market.",
        "social media": "Social media is a powerful tool for engagement, brand building, and customer acquisition.",
        "content marketing": "Content marketing is driving engagement and building trust with audiences.",
        "seo": "Search engine optimization (SEO) is critical for improving online visibility and driving organic traffic.",
        "analytics": "Analytics is enabling businesses to make informed decisions and optimize performance.",
        "strategy": "A well-defined strategy is essential for achieving long-term business goals.",

        # Trends and Innovation
        "trends": "Staying updated with the latest trends is crucial for maintaining a competitive edge.",
        "innovation": "Innovation drives growth and helps businesses adapt to changing market demands.",
        "disruption": "Disruption is reshaping industries and creating new opportunities for growth.",
        "sustainability": "Sustainability is becoming a key focus for businesses and consumers alike.",
        "agile": "Agile methodologies are enabling faster and more efficient project delivery.",
        "digital transformation": "Digital transformation is reshaping businesses and enabling new capabilities.",
        "future": "The future is being shaped by rapid technological advancements and changing consumer behaviors.",
        "growth": "Sustainable growth requires a focus on scalability, efficiency, and customer satisfaction.",
        "leadership": "Effective leadership is essential for guiding teams and achieving organizational goals.",
        "collaboration": "Collaboration is driving innovation and enabling cross-functional success.",

        # Industry-Specific
        "healthcare": "Healthcare is being transformed by technology, improving patient outcomes and operational efficiency.",
        "finance": "The finance industry is leveraging technology to enhance security, efficiency, and customer experience.",
        "education": "Education is evolving with the adoption of digital tools and personalized learning approaches.",
        "retail": "Retail is being reshaped by e-commerce, omnichannel strategies, and customer-centric approaches.",
        "manufacturing": "Manufacturing is becoming more efficient with automation, IoT, and data-driven insights.",
        "logistics": "Logistics is being optimized with real-time tracking, automation, and predictive analytics.",
        "energy": "The energy sector is transitioning to renewable sources and smart grid technologies.",
        "telecom": "Telecommunications is enabling global connectivity and driving digital transformation.",
        "real estate": "Real estate is being transformed by proptech and data-driven decision-making.",
        "travel": "The travel industry is leveraging technology to enhance customer experiences and streamline operations.",

        # General
        "2024": "The year 2024 is expected to bring groundbreaking advancements across various sectors.",
        "challenges": "Addressing challenges is essential for growth and innovation.",
        "opportunities": "Identifying and leveraging opportunities is key to staying ahead in the market.",
        "success": "Success requires a combination of strategy, execution, and adaptability.",
        "impact": "Understanding the impact of decisions is crucial for long-term success.",
        "change": "Embracing change is essential for staying relevant in a rapidly evolving world.",
        "vision": "A clear vision is the foundation for achieving long-term goals.",
        "strategy": "A well-defined strategy is essential for achieving business objectives.",
        "execution": "Effective execution is the key to turning ideas into results.",
        "results": "Delivering results is the ultimate measure of success.",
    }
    return descriptions.get(keyword, f"{keyword.capitalize()} is a critical factor shaping the future of this field.")

def generate_linkedin_post(topic, keywords):
    """
    Generate a well-structured and engaging LinkedIn post based on the
number of keywords.
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
        f"#Innovation #Growth #Leadership #{'#'.join([keyword.replace(' ', '') for keyword in keywords])}"
    )

    # Combine all parts
    post = intro + body + conclusion
    return post

def main():
    # Step 1: Get user input
    user_input = input("Enter the topic for your LinkedIn post: ")

    # Step 2: Extract keywords using YAKE
    keywords = extract_keywords_yake(user_input)
    print(f"Extracted Keywords: {keywords}")

    # Step 3: Generate LinkedIn post
    post = generate_linkedin_post(user_input, keywords)

    # Step 4: Display the final post
    print("\nGenerated LinkedIn Post:\n")
    print(post)

if __name__ == "__main__":
    main()
