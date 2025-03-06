from transformers import pipeline

# Import the pipeline from transformers
# 从transformers中导入管道pipeline

# Create a sentiment analysis tool 创建一个情感分析工具
analyzer = pipeline("sentiment-analysis")

# Try it with some example texts 用一些示例文本尝试它
texts = [
    "I love this product!",  # POSITIVE 0.9999
    "This was a terrible experience.",  # NEGATIVE 0.9990
    "The movie was okay, nothing special.",  # NEGATIVE 0.9925
    "I love you.",  # POSITIVE 0.9999
]

# Analyze each text
for text in texts:

    result = analyzer(text)

    print(f"\\nText: {text}")

    print(f"Sentiment: {result[0]['label']}")

    print(f"Confidence: {result[0]['score']:.4f}")

# I don't have enough on my computer, so I'm running the code on Colab
"""
No model was supplied, defaulted to 
distilbert/distilbert-base-uncased-finetuned-sst-2-english and
revision 714eb0f 
(https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english).
Using a pipeline without specifying a model name and
revision in production is not recommended.
未提供模型，默认为xxxxxx。
不推荐在生产环境中使用未指定型号和版本的管道。

Device set to use cpu
\nText: I love this product!
Sentiment: POSITIVE
Confidence: 0.9999
\nText: This was a terrible experience.
Sentiment: NEGATIVE
Confidence: 0.9990
\nText: The movie was okay, nothing special.
Sentiment: NEGATIVE
Confidence: 0.9925
\nText: I love you.
Sentiment: POSITIVE
Confidence: 0.9999

"""

classifier = pipeline("sentiment-analysis")
classifier("We are very happy to show you the 🤗 Transformers library.")
"""
Device set to use cpu
[{'label': 'POSITIVE', 'score': 0.9997795224189758}]
"""
