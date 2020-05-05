from typing import List, Iterable, Dict
import re
from pandas import DataFrame


class DataClean(object):
    def __init__(self, data: Iterable) -> None:
        self.data = data
        self.wan_yue = []
        self.qian_yue = []
        self.wan_nian = []
        self.qian_nian = []
        self.yuan_tian = []

    def sort_data(self) -> None:
        for i in self.data:
            if "万" in i:
                if "月" in i:
                    self.wan_yue.append(i)
                else:
                    self.wan_nian.append(i)
            elif "月" in i:
                if "月" in i:
                    self.qian_yue.append(i)
                else:
                    self.qian_nian.append(i)
            else:
                self.yuan_tian.append(i)
        del self.data

    def unify_data(self) -> None:
        for i in range(len(self.wan_yue)):
            item = self.wan_yue[i]
            if "-" in item:
                num = re.findall("(.*?)-(.*?)万", item)[0]
                result = float(num[0]) + float(num[1])
                self.wan_yue[i] = result / 2 * 10
            else:
                num = item.split("万")[0]
                self.wan_yue[i] = float(num) * 10
        for i in range(len(self.wan_nian)):
            item = self.wan_nian[i]
            if "-" in item:
                num = re.findall("(.*?)-(.*?)万", item)[0]
                result = float(num[0]) + float(num[1])
                self.wan_nian[i] = result / 24 * 10
            else:
                num = item.split("万")[0]
                self.wan_nian[i] = float(num) * 10 / 12
        for i in range(len(self.qian_yue)):
            item = self.qian_yue[i]
            if "-" in item:
                num = re.findall("(.*?)-(.*?)千", item)[0]
                result = float(num[0]) + float(num[1])
                self.qian_yue[i] = result / 2
            else:
                num = item.split("千")[0]
                self.qian_yue[i] = float(num)
        for i in range(len(self.qian_nian)):
            item = self.qian_nian[i]
            if "-" in item:
                num = re.findall("(.*?)-(.*?)千", item)[0]
                result = float(num[0]) + float(num[1])
                self.qian_nian[i] = result / 24
            else:
                num = item.split("千")[0]
                self.qian_nian[i] = float(num) / 12
        self.yuan_tian = [i for i in self.yuan_tian if "元" in i and "天" in i]
        for i in range(len(self.yuan_tian)):
            item = self.yuan_tian[i]
            num = item.split("元")[0]
            self.yuan_tian[i] = int(num) * 30 / 1000

    def main(self) -> List:
        self.sort_data()
        self.unify_data()
        return self.wan_yue + self.qian_yue + self.wan_nian + self.qian_nian + self.yuan_tian


class DataClear(object):
    def __init__(self, data: DataFrame) -> None:
        self.salary = list(data["薪资"])
        self.unit = list(data["单位"])
        self.nan_list = []

    def unify_data(self) -> None:
        for i in range(len(self.unit)):
            if "年" in self.unit[i]:
                self.salary[i] = self.salary[i] / 12000
            elif "月" in self.unit[i]:
                self.salary[i] = self.salary[i] / 1000
            else:
                self.nan_list.append(i)
        if self.nan_list:
            temp = 0
            for i in self.nan_list:
                del self.salary[i - temp]
                temp += 1


def split_level(squ: List) -> Dict:
    level: Dict[str, int] = {"较低": 0, "一般": 0, "中等": 0, "较高": 0, "优秀": 0}
    for i in squ:
        if 0 < i < 3:
            level["较低"] += 1
        elif 3 <= i < 5:
            level["一般"] += 1
        elif 5 <= i < 8:
            level["中等"] += 1
        elif 8 <= i < 12:
            level["较高"] += 1
        elif i >= 12:
            level["优秀"] += 1
    return level
