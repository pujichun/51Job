from typing import List
from pyecharts.charts import Pie, Line, Bar, Bar3D
from pyecharts import options as opts
from pyecharts.globals import ThemeType

levels = ["较低", "一般", "中等", "较高", "优秀"]
cities = ["北京", "上海", "广州", "深圳", "成都"]


def pies(data: List) -> Pie:
    pie = (
        Pie()
            .add(
            "北京薪资等级",
            data[0].items(),
            center=["27%", "28%"],
            radius=[50, 95],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
            .add(
            "上海薪资等级",
            data[1].items(),
            center=["58%", "28%"],
            radius=[50, 95],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
            .add(
            "广州薪资等级",
            data[2].items(),
            center=["15%", "76%"],
            radius=[50, 95],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
            .add(
            "深圳薪资等级",
            data[3].items(),
            center=["42%", "76%"],
            radius=[50, 95],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
            .add(
            "成都薪资等级",
            data[4].items(),
            center=["70%", "76%"],
            radius=[50, 95],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="北京-上海-广州-深圳-成都", subtitle="薪资饼图"),
            legend_opts=opts.LegendOpts(
                type_="scroll", pos_top="20%", pos_left="90%", orient="vertical"
            ),
        )
            .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
        )
    )
    return pie


def bars(data: List) -> Bar:
    bar = (
        Bar()
            .add_xaxis(levels)
            .add_yaxis(cities[0], list(data[0].values()))
            .add_yaxis(cities[1], list(data[1].values()))
            .add_yaxis(cities[2], list(data[2].values()))
            .add_yaxis(cities[3], list(data[3].values()))
            .add_yaxis(cities[4], list(data[4].values()))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="北京-上海-广州-深圳-成都", subtitle="薪资条形图"),
            brush_opts=opts.BrushOpts(),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    return bar


def bar3d(data: List) -> Bar3D:
    matrix = []
    for i in range(5):
        d = [[key, cities[i], value] for key, value in data[i].items()]
        matrix.extend(d)
    bar = (
        Bar3D(init_opts=opts.InitOpts(width="1600px", height="800px"))
            .add(
            series_name="",
            data=matrix,
            xaxis3d_opts=opts.Axis3DOpts(type_="category", data=levels),
            yaxis3d_opts=opts.Axis3DOpts(type_="category", data=cities),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                max_=450,
                range_color=[
                    "#313695",
                    "#4575b4",
                    "#74add1",
                    "#abd9e9",
                    "#e0f3f8",
                    "#ffffbf",
                    "#fee090",
                    "#fdae61",
                    "#f46d43",
                    "#d73027",
                    "#a50026",
                ],
            )
        )
    )
    return bar


def lines(low, general, medium, high, fine) -> Line:
    line = (
        Line(init_opts=opts.InitOpts(width="900px", height="450px"))
            .add_xaxis(cities)
            .add_yaxis(
            series_name="较低工资",
            y_axis=low
        )
            .add_yaxis(
            series_name="一般工资",
            y_axis=general
        )
            .add_yaxis(
            series_name="中等工资",
            y_axis=medium
        )
            .add_yaxis(
            series_name="较高工资",
            y_axis=high
        )
            .add_yaxis(
            series_name="优秀工资",
            y_axis=fine
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="北京-上海-广州-深圳-成都", subtitle="薪资折线图"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    return line


def three_work_pie(w, j, b) -> Pie:
    x_data = ["Web前端", "Java开发", "大数据开发"]
    y_data = [w, j, b]
    data_pair = [list(z) for z in zip(x_data, y_data)]
    pie = (
        Pie()
            .add(
            series_name="北京-优秀工资",
            data_pair=data_pair,
            rosetype="radius",
            radius="55%",
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Web-Java-大数据（北京现状）",
                pos_left="center",
                pos_top="20",
                # title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
            .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            label_opts=opts.LabelOpts(),
        )
    )
    return pie


def three_work_bar(w, j, b) -> Bar:
    data = [w, j, b]
    print(data)
    array = []
    for i in levels:
        d = [data[x][i] for x in range(3)]
        array.append(d)
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(["Web", "Java", "大数据"])
            .add_yaxis(levels[0], array[0], stack="stack1")
            .add_yaxis(levels[1], array[1], stack="stack1")
            .add_yaxis(levels[2], array[2], stack="stack1")
            .add_yaxis(levels[3], array[3], stack="stack1")
            .add_yaxis(levels[4], array[4], stack="stack1")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="Web-Java-大数据(北京现状)", subtitle="薪资柱状叠图"))
            .set_series_opts(
            label_opts=opts.LabelOpts(
                position="right",
            )
        )
    )
    return bar
