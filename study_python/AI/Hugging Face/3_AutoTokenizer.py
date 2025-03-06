from transformers import AutoTokenizer

# AutoTokenizer 自动标记器
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
encoding = tokenizer("We are very happy to show you the 🤗 Transformers library.")
print(encoding)
"""
{'input_ids': [101, 11312, 10320, 12495, 19308, 10114, 11391, 10855, 10103, 
100, 58263, 13299, 119, 102], 
 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
"""

"""
The tokenizer returns a dictionary containing:
标记器返回一个包含以下内容的字典：

    input_ids: numerical representations of your tokens.
    你的令牌的数字表示
    attention_mask: indicates which tokens should be attended to.
    表示应该关注哪些标记。

A tokenizer can also accept a list of inputs, 
and pad and truncate the text to return a batch with uniform length:
标记器还可以接受输入列表，并填充和截断文本以返回具有统一长度的批次：
"""
# Pytorch
pt_batch = tokenizer(
    [
        "We are very happy to show you the 🤗 Transformers library.",
        "We hope you don't hate it.",
    ],
    padding=True,
    truncation=True,
    max_length=512,
    return_tensors="pt",
)
print(pt_batch)
"""
{'input_ids': 
tensor([[  101, 11312, 10320, 12495, 19308, 10114, 11391, 10855, 
10103, 100, 58263, 13299,   119,   102],
        [  101, 11312, 18763, 10855, 11530,   112,   162, 39487, 10197,   119,
           102,     0,     0,     0]]), 
'token_type_ids': tensor([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), 
'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]])}
"""
