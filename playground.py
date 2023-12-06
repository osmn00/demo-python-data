"""
可以使用如下的 Prompt 来生成一个新的数据分析图：

你是一个大数据分析专家，非常擅长使用python来做数据分析，精通 numpy、pandas、matplotlib等库。

我的excel数据源(olympic.xlsx)表头格式如下 event name age birthplace attend2016 attend2012 attend2008 attendtimes gold silver bronze medal xz gender birthday height weight arm leg

下面是我的诉求：
1. 我需要根据这份结构的数据，使用matplotlib生成一张playground.png图片
2. 这一张图片中，每个运动项目(event)应该都有一张小图
3. 小图的内容是统计这个分类的运动项目下运动员的年龄分布
4. 年龄分布的统计，需要使用birthday字段，按照年代区分统计总数，使用70s、80s、90s这三个年代
5. 每张小图上都应该有这三个年代的数据，即使某个年代的数据为0，也需要展示出来，组成一张曲线小图
6. 最终生成的大图中，每行三个小图，删除多余的空图
"""


"""
生成之后可以持续优化

优化一下小图的样式，让曲线都能居中显示，曲线中有圆点表示当前的值，并且在圆点上方有真实值展示出来
"""
