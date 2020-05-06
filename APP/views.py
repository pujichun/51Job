from sanic import Sanic
from sanic.response import json, html
from utils.PlotMould import bars, lines, pies
from DataHandler import *

app = Sanic(__name__)


# 饼图
@app.route("/Pie/<way>")
async def web_pie(request, way):
    pie = pies(bd)
    if way == "Web":
        pie = pies(web)
    elif way == "Java":
        pie = pies(java)
    return json(pie.dump_options_with_quotes())


# 柱状图
@app.route("/Bar/<way>")
async def web_bar(request, way):
    bar = bars(bd)
    if way == "Web":
        bar = bars(web)
    elif way == "Java":
        bar = bars(java)
    return json(bar.dump_options_with_quotes())


# 折线图
@app.route("/Line/<way>")
async def web_line(request, way):
    print(way)
    line = lines(web_low, web_general, web_medium, web_high, web_fine)
    if way == "bd":
        line = lines(bd_low, bd_general, bd_medium, bd_high, bd_fine)
    elif way == "Java":
        line = lines(java_low, java_general, java_medium, java_high, java_fine)
    return json(line.dump_options_with_quotes())


@app.route("/", methods=["GET"])
async def index(request):
    return html(open("./templates/index.html", encoding="utf8").read())
