# pip install duckduckgo-search==6.4.1
# pip install pandas==2.2.3


from re import search

import pandas as pd
from duckduckgo_search import DDGS

search_query = 'python programming'

results = DDGS().text(
    keywords = search_query,
    region = "cn-zh",
    safesearch = 'off',
    timelimit = '7d',
    max_results=5
)

# print(results)

# 拼接字符串
results = "\n".join(f"{item['title']} - {item['href']} - {item['body']}" for item in results)

print(results)



# results_df = pd.DataFrame(results)

# results_df.to_csv('duckduckgo_tutorial.csv', index=False)


