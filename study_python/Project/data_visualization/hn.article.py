import requests
import json

# 执行 API 调用并存储响应
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")
# 探索数据的结构
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)
"""
{
    "by": "sohkamyung",
    "descendants": 307, 文章被评论的次数
    "id": 31353677,
    "kids": [ 所有评论的 ID
        31354987,
        31354235,
        31354040,
        --snip--
    ],
    "score": 786,
    "time": 1652361401,
    "title": "Astronomers reveal first image of the black hole 
    at the heart of our galaxy", 天文学家首次展示了银河系中心黑洞的图像       
    "type": "story",
    "url": "https://public.nrao.edu/news/
    astronomers-reveal-first-image-of-the-black-hole-at-the-heart-of-our-galaxy/"
}
"""
