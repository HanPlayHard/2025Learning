import torch
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Use another model and tokenizer in the pipeline 在管道中使用另一个模型和标记器
"""
例如，如果您想要一个能够处理法语文本的模型，请使用 Hub 上的标签来筛选合适的模型。
顶部的筛选结果返回一个针对法语文本的情绪分析进行了微调的多语言BERT 模型：
"""
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
# 使用AutoModelForSequenceClassification和
# AutoTokenizer加载预训练模型及其相关的标记器
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
# 在pipeline()中指定模型和标记器，现在您可以将其应用于classifier法语文本：

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
classifier(
    "Nous sommes très heureux de vous présenter la bibliothèque 🤗 Transformers."
)
"""
Device set to use cpu
[{'label': '5 stars', 'score': 0.7272651195526123}]
"""

"""
如果您找不到适合您用例的模型，则需要对您的数据进行预训练模型的微调。
查看我们的微调教程以了解如何操作。
"""
