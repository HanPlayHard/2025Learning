import requests

# 执行 API 调用并查看响应
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>20000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# 将响应转换为字典
response_dict = r.json()

# 处理结果
print(response_dict.keys())
"""
Status code: 200
dict_keys(['total_count', 'incomplete_results', 'items'])
"""

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
# 探索有关仓库的信息
repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")
"""
Total repositories: 248
Complete results: True
Repositories returned: 30
"""

# 研究第一个仓库
repo_dict = repo_dicts[0]
# print(f"\Keys:{len(repo_dict)}")  # \Keys:80
# for key in sorted(repo_dict.keys()):
#     print(key)
"""
allow_forking
archive_url
archived
assignees_url
blobs_url
branches_url
clone_url
collaborators_url
comments_url
commits_url
compare_url
contents_url
contributors_url
created_at
default_branch
deployments_url
description
disabled
downloads_url
events_url
fork
forks
forks_count
forks_url
full_name
git_commits_url
git_refs_url
git_tags_url
git_url
has_discussions
has_downloads
has_issues
........
"""
print("\nSelected information about first repository:")
# for repo_dict in repo_dicts:
print(f"Name: {repo_dict['name']}")  # Name: public-apis
print(f"Owner: {repo_dict['owner']['login']}")  # Owner: public-apis
print(f"Stars: {repo_dict['stargazers_count']}")  # Stars: 328648
print(f"Repository: {repo_dict['html_url']}")
# Repository: https://github.com/public-apis/public-apis
print(f"Created: {repo_dict['created_at']}")  # Created: 2016-03-20T23:49:42Z
print(f"Updated: {repo_dict['updated_at']}")  # Updated: 2025-02-28T07:33:17Z
print(f"Description: {repo_dict['description']}")
# Created: 2016-03-20T23:49:42Z
