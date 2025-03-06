"""
The pipeline() can also iterate over an entire dataset for any task you like. 
For this example, let’s choose automatic speech recognition as our task:
pipeline()也可以遍历整个数据集，执行任何你喜欢的任务。
对于这个例子，让我们选择自动语言识别作为我们的任务：
"""

import torch
from transformers import pipeline
from datasets import load_dataset, Audio

speech_recognizer = pipeline(
    "automatic-speech-recognition", model="facebook/wav2vec2-base-960h"
)
dataset = load_dataset("PolyAI/minds14", name="en-US", split="train")
dataset = dataset.cast_column(
    "audio", Audio(sampling_rate=speech_recognizer.feature_extractor.sampling_rate)
)
"""
调用“audio”列时，音频文件会自动加载并重新采样。从前4个样本中提取原始波形数组，
并将其作为一个列表传递给管道：
"""
result = speech_recognizer(dataset[:4]["audio"])
print([d["text"] for d in result])
"""
['I WOULD LIKE TO SET UP A JOINT ACCOUNT WITH MY PARTNER HOW 
DO I PROCEED WITH DOING THAT', "FONDERING HOW I'D SET UP A JOIN TO HELL T 
WITH MY WIFE AND WHERE THE AP MIGHT BE",.....................
"""
"""
对于输入较大的大型数据集（如语音或视觉），您将需要传递一个生成器而不是列表，
以将所有输入加载到内存中。查看pipeline API参考以获取更多信息。
"""
