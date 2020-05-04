from pyecharts.charts import Pie, Line, Bar
from pyecharts import options as opts
def Pies() -> Pie:
    pie = (
        Pie()
        .add(
            "北京薪资等级",
            bj_level.items(),
            center=["27%", "28%"],
            radius=[50, 95],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .add(
            "上海薪资等级",
            sh_level.items(),
            center=["58%", "28%"],
            radius=[50, 95],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .add(
            "广州薪资等级",
            gz_level.items(),
            center=["15%", "76%"],
            radius=[50, 95],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .add(
            "深圳薪资等级",
            sz_level.items(),
            center=["42%", "76%"],
            radius=[50, 95],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .add(
            "成都薪资等级",
            cd_level.items(),
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