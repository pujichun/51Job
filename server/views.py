from sanic import Sanic
from sanic.response import json, html
from utils.PlotMould import bars, lines, pies
from DataHandler import *

app = Sanic(__name__)


# 饼图
@app.route("/WebPie", methods=["GET"])
async def web_pie(request):
    pie = pies(web)
    return json(pie.dump_options_with_quotes())


@app.route("/JavaPie", methods=["GTE"])
async def java_pie(request):
    pie = pies(java)
    return json(pie.dump_options_with_quotes())


@app.route("/bdPie", methods=["GTE"])
async def java_pie(request):
    pie = pies(bd)
    return json(pie.dump_options_with_quotes())


# 柱状图
@app.route("/WebBar", methods=["GTE"])
async def web_bar(request):
    bar = bars(web)
    return json(bar.dump_options_with_quotes())


@app.route("/JavaBar", methods=["GTE"])
async def web_bar(request):
    bar = bars(java)
    return json(bar.dump_options_with_quotes())


@app.route("/bdBar", methods=["GTE"])
async def web_bar(request):
    bar = bars(bd)
    return json(bar.dump_options_with_quotes())


# 折线图
@app.route("/WebLine", methods=["GTE"])
async def web_pie(request):
    line = lines(web_low, web_general, web_medium, web_high, web_fine)
    return json(line.dump_options_with_quotes())


@app.route("/JavaLine", methods=["GTE"])
async def java_pie(request):
    line = lines(java_low, java_general, java_medium, java_high, java_fine)
    return json(line.dump_options_with_quotes())


@app.route("/bdLine", methods=["GTE"])
async def bd_pie(request):
    line = lines(bd_low, bd_general, bd_medium, bd_high, bd_fine)
    return json(line.dump_options_with_quotes())


@app.route("/", methods=["GET"])
async def index(request):
    return html(open("./templates/index.html", encoding="utf8").read())