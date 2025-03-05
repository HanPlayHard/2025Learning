from transformers import pipeline

# Import the pipeline from transformers
# 从transformers中导入管道pipeline

# Create a sentiment analysis tool 创建一个情感分析工具
analyzer = pipeline("sentiment-analysis")

# Try it with some example texts 用一些示例文本尝试它
texts = [
    "I love this product!",
    "This was a terrible experience.",
    "The movie was okay, nothing special.",
    "I love you.",
]

# Analyze each text
for text in texts:

    result = analyzer(text)

    print(f"\\nText: {text}")

    print(f"Sentiment: {result[0]['label']}")

    print(f"Confidence: {result[0]['score']:.4f}")

# I don't have enough on my computer, so I'm running the code on Colab
