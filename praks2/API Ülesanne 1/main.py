import requests
import pygal
from pygal.style import Style

py_URL = "https://api.github.com/search/repositories?q=language:python&sort=true"
js_URL = "https://api.github.com/search/repositories?q=language:javascript&sort=true"
py_response = requests.get(py_URL)
js_response = requests.get(js_URL)

# 200 - OK, 404 - URL on vale, 403 - Rate limit
print(f"Python status code: {py_response.status_code}")
print(f"JavaScript status code: {js_response.status_code}")

# Kogun andmed ja töötlen neid
py_response_dict = py_response.json()
js_response_dict = js_response.json()

py_repo_dicts = py_response_dict['items']
js_repo_dicts = js_response_dict['items']

# Pygal Chart
py_stars = []
js_stars = []

i = 0
x = 0

for repo_dict in py_repo_dicts:
    py_stars.append(py_repo_dicts[x]['stargazers_count'])
    x += 1

for repo_dict in js_repo_dicts:
    js_stars.append(js_repo_dicts[i]['stargazers_count'])
    i += 1

custom_style = Style(
    colors = ('#E80080', '#484848', '#9BC850')
)

chart = pygal.Bar(style=custom_style, x_label_rotation=45, show_legend=True)
chart.title = "Most Starred Python And JavaScript Projects on Github"
chart.add('JavaScript', js_stars)
chart.add('Python', py_stars)
chart.render_in_browser()