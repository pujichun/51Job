from typing import List
from pyecharts.charts import Pie, Line, Bar, Bar3D
from pyecharts import options as opts


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
            title_opts=opts.TitleOpts(title="北京-上海-广州-深圳-成都薪资等级饼图"),
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
            .add_xaxis(["较低", "一般", "中等", "较高", "优秀"])
            .add_yaxis("北京", list(data[0].values()))
            .add_yaxis("上海", list(data[1].values()))
            .add_yaxis("广州", list(data[2].values()))
            .add_yaxis("深圳", list(data[3].values()))
            .add_yaxis("成都", list(data[4].values()))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="北京-上海-广州-深圳-成都"),
            brush_opts=opts.BrushOpts(),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    return bar


def bar3d(data: List) -> Bar3D:
    levels = ["较低", "一般", "中等", "较高", "优秀"]
    cities = ["北京", "上海", "广州", "深圳", "成都"]
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
    city_list = ["北京", "上海", "广州", "深圳", "成都"]
    line = (
        Line(init_opts=opts.InitOpts(width="900px", height="450px"))
            .add_xaxis(city_list)
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
            title_opts=opts.TitleOpts(title="大数据工资", subtitle="折线图"),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    return line
