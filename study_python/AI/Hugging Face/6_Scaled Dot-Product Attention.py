# Let’s implement Scaled Dot-Product Attention in Python:
# 让我们在Python中实现缩放点积注意力：
import torch
import torch.nn.functional as F


def attention(Q, K, V):
    d_k = Q.shape[-1]  # Get key dimension 获取键维度
    # Dot-product + Scaling 点积+缩放
    scores = torch.matmul(Q, K.T) / torch.sqrt(torch.tensor(d_k))

    attention_weights = F.softmax(scores, dim=-1)  # Apply softmax
    # Weighted sum of Values  值的加权和
    output = torch.matmul(attention_weights, V)

    return output


# Example Q, K, V (random)

# Query (What are we looking for?)我们在找什么？
Q = torch.tensor([[1.0, 0.5]])
# Keys (Memory of past words) 记忆过去的单词
K = torch.tensor([[1.0, 0.8], [0.5, 0.2]])
# Values (What each word offers) 每个单词的含义
V = torch.tensor([[10.0, 5.0], [1.0, 2.0]])

output = attention(Q, K, V)
print("Attention Output:", output)
# Attention Output: tensor([[6.7399, 3.9133]])

"""
Key Takeaways:关键要点：

High similarity → High attention score → More weight given to Value.
相似度高→关注度高→价值权重大。

Scaling prevents extreme softmax values.缩放可以防止极端的softmax值。

Attention decides which words matter most in a sentence!
注意力决定了句子中哪些词最重要！


Q = What you seek, K = What’s available, V = The information you get.
Q = 你要找的东西，K = 可用的东西，V = 你得到的信息。

Softmax assigns importance. Scaling prevents large numbers.
Softmax分配重要性。缩放可以防止大的数字。

Attention helps AI focus on the most relevant words!
注意力帮助AI专注于最相关的单词！

"""
