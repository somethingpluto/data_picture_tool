import argparse
import warnings
from pathlib import Path

import pandas as pd
import yaml
from cliffs_delta import cliffs_delta
from tqdm import tqdm

warnings.filterwarnings("ignore")


class CliffDeltaUtil:
    def __init__(self, method_list, metrics, base_line, data_path):
        """
        初始化
        :param method_list: 待比较的方法列表
        :param metrics: 比较的指标
        :param base_line: base 方法
        :param data_path: 数据存放的位置
        """
        self.method_list = method_list
        self.metrics = metrics
        self.data_path = data_path
        self.base_line = base_line

    def _read_data(self, metric):
        """
        读取metric文件 获取method - data 映射表
        :param metric: 待读取的指标
        :return: method - data 映射表
        """
        datas = {}
        for method in self.method_list:
            # 读取文件
            data_path = "{0}/{1}.xlsx".format(self.data_path, metric)
            raw_data = pd.read_excel(data_path)
            # 获取 method 列数据
            raw_data = raw_data[method].values
            # 存入 map
            datas[method] = raw_data
        return datas

    def _process_data(self, datas: dict, base_line_method):
        """
        获取 method_list metric_data_list 第一个item即为base line
        :param datas:
        :param base_line_method:
        :return:
        """
        metric_datas = []
        method_list = []
        # 获取baseline 方法对应的data
        baseline_data = datas[base_line_method]
        # 第一个默认为 base_line
        method_list.append(base_line_method)
        metric_datas.append(baseline_data)
        for key, value in datas.items():
            if key == base_line_method:
                continue
            method_list.append(key)
            metric_datas.append(value)
        return method_list, metric_datas

    def calculate_cliff_delta(self, metric_datas, method_list, metric, base):
        cliffs = []
        for i in range(1, len(metric_datas)):
            print(f"compute cliffs delta between {base} and {method_list[i - 1]}")
            cliffs_d, res = cliffs_delta(metric_datas[0], metric_datas[i])
            print(cliffs_d, res)
            cliffs.append(cliffs_d)
        method_list.pop()
        Path(f"./output/cliff_{metric}/").mkdir(parents=True, exist_ok=True)
        cliff_path = f"./output/cliff_{metric}/{base}.csv"

        output_cliff = pd.DataFrame(data=[cliffs], columns=method_list)
        output_cliff.to_csv(cliff_path, encoding='utf-8',index=False)

    def calculate(self):
        with tqdm(total=len(self.metrics) * len(self.base_line), desc="calculating...") as pbar:
            for metric in self.metrics:
                datas = self._read_data(metric)
                for base in self.base_line:
                    method_list, metric_datas = self._process_data(datas, base)
                    self.calculate_cliff_delta(metric_datas, method_list, metric, base)
                    pbar.update(1)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", required=False, help="config file path", type=str,
                        default="./cliff_delta_config.yaml")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    with open(args.f, 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
    print("config file data:")
    print(result)

    cliff_delta_util = CliffDeltaUtil(
        method_list=result['method_list'],
        metrics=result['metrics'],
        base_line=result['base_line_list'],
        data_path=result['data_path'])
    cliff_delta_util.calculate()
