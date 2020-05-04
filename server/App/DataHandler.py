import pandas as pd
from utils.DataFilter import DataClean, DataClear, split_level

bj_bd = pd.read_excel("大数据开发.xlsx", '北京')
sh_bd = pd.read_excel("大数据开发.xlsx", '上海')
gz_bd = pd.read_excel("大数据开发.xlsx", '广州')
sz_bd = pd.read_excel("大数据开发.xlsx", '深圳')
cd_bd = pd.read_excel("大数据开发.xlsx", '成都')

bj_bd.dropna(axis=0, how='any', inplace=True)
sh_bd.dropna(axis=0, how='any', inplace=True)
gz_bd.dropna(axis=0, how='any', inplace=True)
sz_bd.dropna(axis=0, how='any', inplace=True)
cd_bd.dropna(axis=0, how='any', inplace=True)

bj_web = pd.read_excel("Web前端开发.xlsx", '北京')
sh_web = pd.read_excel("Web前端开发.xlsx", '上海')
gz_web = pd.read_excel("Web前端开发.xlsx", '广州')
sz_web = pd.read_excel("Web前端开发.xlsx", '深圳')
cd_web = pd.read_excel("Web前端开发.xlsx", '成都')

bj_web.dropna(axis=0, how='any', inplace=True)
sh_web.dropna(axis=0, how='any', inplace=True)
gz_web.dropna(axis=0, how='any', inplace=True)
sz_web.dropna(axis=0, how='any', inplace=True)
cd_web.dropna(axis=0, how='any', inplace=True)

bj_java = pd.read_excel("Java开发.xlsx", '北京')
sh_java = pd.read_excel("Java开发.xlsx", '上海')
gz_java = pd.read_excel("Java开发.xlsx", '广州')
sz_java = pd.read_excel("Java开发.xlsx", '深圳')
cd_java = pd.read_excel("Java开发.xlsx", '成都')

bj_java.dropna(axis=0, how='any', inplace=True)
sh_java.dropna(axis=0, how='any', inplace=True)
gz_java.dropna(axis=0, how='any', inplace=True)
sz_java.dropna(axis=0, how='any', inplace=True)
cd_java.dropna(axis=0, how='any', inplace=True)

# 清洗大数据方向数据
bj_bd = DataClean(bj_bd["薪资"]).main()
sh_bd = DataClean(sh_bd["薪资"]).main()
gz_bd = DataClean(gz_bd["薪资"]).main()
sz_bd = DataClean(sz_bd["薪资"]).main()
cd_bd = DataClean(cd_bd["薪资"]).main()

# 清洗Web方向数据
bj_web = DataClear(bj_web)
sh_web = DataClear(sh_web)
gz_web = DataClear(gz_web)
sz_web = DataClear(sz_web)
cd_web = DataClear(cd_web)
bj_web.unify_data()
sh_web.unify_data()
gz_web.unify_data()
sz_web.unify_data()
cd_web.unify_data()
bj_web = split_level(bj_web.salary)
sh_web = split_level(sh_web.salary)
gz_web = split_level(gz_web.salary)
sz_web = split_level(sz_web.salary)
cd_web = split_level(cd_web.salary)

# 清洗Java方向数据
bj_java = DataClear(bj_java)
sh_java = DataClear(sh_java)
gz_java = DataClear(gz_java)
sz_java = DataClear(sz_java)
cd_java = DataClear(cd_java)
bj_java.unify_data()
sh_java.unify_data()
gz_java.unify_data()
sz_java.unify_data()
cd_java.unify_data()
bj_java = split_level(bj_java.salary)
sh_java = split_level(sh_java.salary)
gz_java = split_level(gz_java.salary)
sz_java = split_level(sz_java.salary)
cd_java = split_level(cd_java.salary)



bd_low = [bj_bd["较低"], sh_bd["较低"], gz_bd["较低"], sz_bd["较低"], cd_bd["较低"]]
bd_general = [bj_bd["一般"], sh_bd["一般"], gz_bd["一般"], sz_bd["一般"], cd_bd["一般"]]
bd_medium = [bj_bd["中等"], sh_bd["中等"], gz_bd["中等"], sz_bd["中等"], cd_bd["中等"]]
bd_high = [bj_bd["较高"], sh_bd["较高"], gz_bd["较高"], sz_bd["较高"], cd_bd["较高"]]
bd_fine = [bj_bd["优秀"], sh_bd["优秀"], gz_bd["优秀"], sz_bd["优秀"], cd_bd["优秀"]]

web_low = [bj_web["较低"], sh_web["较低"], gz_web["较低"], sz_web["较低"], cd_web["较低"]]
web_general = [bj_web["一般"], sh_web["一般"], gz_web["一般"], sz_web["一般"], cd_web["一般"]]
web_medium = [bj_web["中等"], sh_web["中等"], gz_web["中等"], sz_web["中等"], cd_web["中等"]]
web_high = [bj_web["较高"], sh_web["较高"], gz_web["较高"], sz_web["较高"], cd_web["较高"]]
web_fine = [bj_web["优秀"], sh_web["优秀"], gz_web["优秀"], sz_web["优秀"], cd_web["优秀"]]

java_low = [bj_java["较低"], sh_java["较低"], gz_java["较低"], sz_java["较低"], cd_java["较低"]]
java_general = [bj_java["一般"], sh_java["一般"], gz_java["一般"], sz_java["一般"], cd_java["一般"]]
java_medium = [bj_java["中等"], sh_java["中等"], gz_java["中等"], sz_java["中等"], cd_java["中等"]]
java_high = [bj_java["较高"], sh_java["较高"], gz_java["较高"], sz_java["较高"], cd_java["较高"]]
java_fine = [bj_java["优秀"], sh_java["优秀"], gz_java["优秀"], sz_java["优秀"], cd_java["优秀"]]
