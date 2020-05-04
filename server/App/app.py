from sanic import Sanic
from sanic.response import json, html
from pyecharts import options as opts
from pyecharts.charts import Bar

app = Sanic(__name__)


def bar_base() -> Bar:
    bj_java = {'较低': 1, '一般': 10, '中等': 50, '较高': 215, '优秀': 186}
    sh_java = {'较低': 1, '一般': 13, '中等': 40, '较高': 227, '优秀': 184}
    gz_java = {'较低': 4, '一般': 26, '中等': 89, '较高': 251, '优秀': 109}
    sz_java = {'较低': 1, '一般': 13, '中等': 48, '较高': 236, '优秀': 183}
    cd_java = {'较低': 12, '一般': 30, '中等': 133, '较高': 210, '优秀': 92}
    bar = (
        Bar()
            .add_xaxis(["较低", "一般", "中等", "较高", "优秀"])
            .add_yaxis("北京", list(bj_java.values()))
            .add_yaxis("上海", list(sh_java.values()))
            .add_yaxis("广州", list(gz_java.values()))
            .add_yaxis("深圳", list(sz_java.values()))
            .add_yaxis("成都", list(cd_java.values()))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="北京-上海-广州-深圳-成都"),
            brush_opts=opts.BrushOpts(),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    return bar


@app.route("/barChart", methods=["GET"])
async def draw_bar_chart(request):
    c = bar_base()
    return json(c.dump_options_with_quotes())


@app.route("/", methods=["GET"])
async def index(request):
    return html(open("./templates/index.html", encoding="utf8").read())

if __name__ == '__main__':
    app.run()