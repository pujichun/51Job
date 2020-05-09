import pandas as pd
from utils.DataFilter import DataClean, DataClear, split_level

bj_bd = pd.read_excel("../大数据开发.xlsx", '北京')
sh_bd = pd.read_excel("../大数据开发.xlsx", '上海')
gz_bd = pd.read_excel("../大数据开发.xlsx", '广州')
sz_bd = pd.read_excel("../大数据开发.xlsx", '深圳')
cd_bd = pd.read_excel("../大数据开发.xlsx", '成都')

bj_bd.dropna(axis=0, how='any', inplace=True)
sh_bd.dropna(axis=0, how='any', inplace=True)
gz_bd.dropna(axis=0, how='any', inplace=True)
sz_bd.dropna(axis=0, how='any', inplace=True)
cd_bd.dropna(axis=0, how='any', inplace=True)

bj_web = pd.read_excel("../Web前端开发.xlsx", '北京')
sh_web = pd.read_excel("../Web前端开发.xlsx", '上海')
gz_web = pd.read_excel("../Web前端开发.xlsx", '广州')
sz_web = pd.read_excel("../Web前端开发.xlsx", '深圳')
cd_web = pd.read_excel("../Web前端开发.xlsx", '成都')

bj_web.dropna(axis=0, how='any', inplace=True)
sh_web.dropna(axis=0, how='any', inplace=True)
gz_web.dropna(axis=0, how='any', inplace=True)
sz_web.dropna(axis=0, how='any', inplace=True)
cd_web.dropna(axis=0, how='any', inplace=True)

bj_java = pd.read_excel("../Java开发.xlsx", '北京')
sh_java = pd.read_excel("../Java开发.xlsx", '上海')
gz_java = pd.read_excel("../Java开发.xlsx", '广州')
sz_java = pd.read_excel("../Java开发.xlsx", '深圳')
cd_java = pd.read_excel("../Java开发.xlsx", '成都')

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
bd = [
    split_level(bj_bd),
    split_level(sh_bd),
    split_level(gz_bd),
    split_level(sz_bd),
    split_level(cd_bd)
]

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

web = [
    split_level(bj_web.salary),
    split_level(sh_web.salary),
    split_level(gz_web.salary),
    split_level(sz_web.salary),
    split_level(cd_web.salary)
]
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

java = [
    split_level(bj_java.salary),
    split_level(sh_java.salary),
    split_level(gz_java.salary),
    split_level(sz_java.salary),
    split_level(cd_java.salary)
]

bd_low = [item["较低"] for item in bd]
bd_general = [item["一般"] for item in bd]
bd_medium = [item["中等"] for item in bd]
bd_high = [item["较高"] for item in bd]
bd_fine = [item["优秀"] for item in bd]

web_low = [item["较低"] for item in web]
web_general = [item["一般"] for item in web]
web_medium = [item["中等"] for item in web]
web_high = [item["较高"] for item in web]
web_fine = [item["优秀"] for item in web]

java_low = [item["较低"] for item in java]
java_general = [item["一般"] for item in java]
java_medium = [item["中等"] for item in java]
java_high = [item["较高"] for item in java]
java_fine = [item["优秀"] for item in java]

if __name__ == '__main__':
    print(web)
    print(java)
    print(bd)
