from transformers import BertTokenizer, BertModel

# funny way to study：Imagine Hugging Face as a dating app for AI models.
"""
把Hugging Face想象成一个神奇的AI宠物动物园,
——像BERT这样的模型是你可以训练的可爱但强大的动物.
"""
"""
BertTokenizer:将文本转换为BERT能理解的数字。
BertMode:l处理这些数字并给出一个花哨的“隐藏状态”。
"bert-base-uncased": 是BERT的一个更小、更友好的版本。
"""
# Summon the mighty BERT
# 召唤强大的伯特
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# Tokenize some text (Let's see what BERT thinks of your cat!)
# 标记化一些文本
text = "My cat is plotting world domination!"
tokens = tokenizer(text, return_tensors="pt")

# Feed to BERT 喂BERT
output = model(**tokens)

# Print output
print("BERT has spoken:", output.last_hidden_state.shape)
# BERT has spoken: torch.Size([1, 9, 768])
"""
"Hugging Face lets me adopt AI pets.  Today, I met BERT.  
He eats tokens and spits out embeddings.  10/10 would adopt again."
"""
"""
最后的输出代表什么意思？
1:Batch size批量大小 = 1→我们只给BERT提供了一句话。
2:Sequence length序列长度 = 9→BERT将我们的句子分割为9个标记
（包括像[CLS]和[SEP]这样的特殊标记）。
print(tokenizer.tokenize("My cat is plotting world domination!")),
['my', 'cat', 'is', 'plotting', 'world', 'domination', '!'],
['[CLS]', 'my', 'cat', 'is', 'plotting', 'world', 'domination', '!', '[SEP]'],

3:Hidden size隐藏大小 = 768→每个token得到一个768维向量（BERT的神奇嵌入）。
"""
# If you want to see the actual numbers BERT spits out, try:
print(output.last_hidden_state)
# Warning: It’s a HUGE tensor with 9 tokens × 768 numbers each.too big to read!

"""
通俗解释：
你给了BERT一句话 a sentence。
BERT将它分成9块（token）。
每件块 都有一个代表其含义的768个数字的密码。a 768-number secret code
BERT喜欢高维数学 high-dimensional。
"""
# 如果你想获得整个句子的单个向量，你可以获取[CLS]标记的表示（索引0）：
sentence_embedding = output.last_hidden_state[:, 0, :]
print(sentence_embedding.shape)  # torch.Size([1, 768])
# 现在你有了一个表示整个句子的768维向量！a single 768-dimension vector

"""
让我们让BERT嵌入变得有趣且易于理解！BERT embeddings  

Analogy: BERT is a Master Chef,
Imagine BERT is a world-class chef, and your sentence is a dish you want to cook.
Step 1: Tokenization = Chopping Ingredients.
Before cooking, you need to chop up your ingredients.
For example, if your sentence is:
"My cat is plotting world domination!"
BERT chops it into tokens:
类比：BERT是一位烹饪大师
假设BERT是一个世界级的厨师，你要说的是一个你想做的菜。
步骤1：标记化=切碎配料.
在烹饪之前，你需要把食材切碎。
例如，如果你的句子是：
“我的猫正在密谋统治世界！”
BERT将其切分为token：
"""
# ['[CLS]', 'my', 'cat', 'is', 'plotting', 'world', 'domination', '!', '[SEP]']
"""
Step 2: Embeddings = Turning Ingredients into a Fancy Dish.
Each token goes into BERT’s magic kitchen (neural network), 
where it gets processed.
Instead of raw words, BERT transforms each one into 
a unique 768-dimensional "flavor profile."
Think of it like this:
第二步：嵌入=把食材变成一道菜.
每个token都会进入BERT的魔法厨房（神经网络），在那里进行处理。
BERT将每一个单词都转换成一个独特的768维“味道剖面”，而不是原始的单词。
可以这样想：
Token	        Flavor Profile (768-Dim Vector)
cat	            Salty, umami, soft, furry
world	        Bold, spicy, large
domination	    Powerful, aggressive, intense
BERT不仅仅是记住单词——它像专业厨师混合味道一样捕捉它们的含义和关系。
"""

"""
Step 3: Sentence Embedding = The Final Dish.
If you want one vector for the whole sentence, just take BERT’s [CLS] token 
at the start—it’s like the final taste of the entire dish.
步骤3：句子嵌入=最后的菜.
如果你想要整个句子的一个向量，只需在开始时使用BERT的[CLS]标记，它就像整道菜的最终味道。
sentence_embedding = output.last_hidden_state[:, 0, :]
这个768维向量总结了BERT对你的句子了解的所有内容，就像餐厅评论家的最终评论一样
"""

"""
Why Is This Cool?
1:Same words, different meanings → BERT knows "bank" in "river bank" vs.  
"money bank" is different.  
2:Context matters 上下文关系 → "Mouse" in "My cat caught a mouse" vs.  
"I bought a new mouse for my laptop."  
3:Useful for AI magic → Search engines, chatbots, 
and recommendation systems all use embeddings to "understand" text!  
"""


"""
Tokens = Ingredients (words broken down) 成分（分解后的单词）
Embeddings = Flavors (words transformed into 768-d vectors)
口味（将单词转换为768维向量）
Sentence Embedding 句子嵌入 = Final Dish (BERT’s overall meaning of the sentence)
最后一道菜（BERT的句子整体含义）

So when you run output.last_hidden_state, 
BERT is just serving you a fancy dish of word representations! 
所以当你运行output.last_hidden_state时，
BERT只是为您提供了一盘漂亮的单词表示菜肴！
"""
