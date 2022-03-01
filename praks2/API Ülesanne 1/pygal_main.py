import pygal
from pygal.style import Style
custom_style = Style(
    colors = ('#E80080', '#484848', '#9BC850')
)

b_chart = pygal.Bar(Style=custom_style)
b_chart.title = "Github Repo Info"
b_chart.add("Python Repod", [1000])
b_chart.add("JavaScript Repod", [1500])
b_chart.render_in_browser()