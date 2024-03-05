from pathlib import Path

import numpy as np
import pandas as pd
import yaml
from scipy.stats import wilcoxon

# 取消计算过程中的警告
import warnings

warnings.filterwarnings("ignore")

from tqdm import tqdm


class WilcoxonUtil:
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

    def wilcoxon_signed_rank_test(self, metric_datas, method_list, metric, base):
        p_values = []
        sorted_p_values = []
        bhp_values = []
        for i in range(1, len(metric_datas)):
            # 计算pValue 即base 和 data的计算
            pValue = self.calc_wilcoxon(metric_datas[0], metric_datas[i])
            p_values.append(pValue)
            sorted_p_values.append(pValue)

            if metric == "Recall" or metric == "PofB":
                print("compute p-value between %s and CBSplus: %s" % (method_list[i - 1], pValue))

                print("compute average improvement between {0} and CBSplus: {1}".format(method_list[i - 1],
                                                                                        self.average_improvement(
                                                                                            metric_datas[i],
                                                                                            metric_datas[
                                                                                                0])))
        # 从大到小排序
        sorted_p_values.sort()

        for i in range(len(p_values)):
            bhpValue = p_values[i] * (len(p_values)) / (sorted_p_values.index(p_values[i]) + 1)
            bhp_values.append(bhpValue)
            print("compute Benjamini—Hochberg p-value between %s and CBSplus: %s" % (method_list[i - 1], bhpValue))

        Path(f"./output/p_{metric}").mkdir(parents=True, exist_ok=True)
        output_path = f"./output/p_{metric}/{base}.csv"
        # 剔除base 方法
        method_list.pop()
        output = pd.DataFrame(data=[p_values], columns=method_list)
        output.to_csv(output_path, encoding='utf-8')

    def average_improvement(self, col1, col2):
        avgCol1 = round(np.average(col1), 3)
        avgCol2 = round(np.average(col2), 3)
        imp = round((avgCol1 - avgCol2), 3)
        return imp

    def calc_wilcoxon(self, l1, l2):
        p_value = wilcoxon(l1, l2, correction=False)
        return p_value.pvalue

    def calculate(self):
        """
        计算每个metric
        :return:
        """
        with tqdm(total=len(self.metrics) * len(self.base_line), desc="calculating...") as pbar:
            for metric in self.metrics:
                # 读取对应的metric文件
                datas = self._read_data(metric)
                for base in self.base_line:
                    print(f"---{metric}---{base}---")
                    method_list, metric_datas = self._process_data(datas, base)
                    self.wilcoxon_signed_rank_test(metric_datas, method_list, metric, base)
                    pbar.update(1)
        print("⭐⭐⭐⭐SUCCESS!")


if __name__ == '__main__':
    with open('./wilcoxon_config.yaml', 'r', encoding='utf-8') as f:
        result = yaml.load(f.read(), Loader=yaml.FullLoader)
    print("config file data:")
    print(result)

    wilcoxon_util = WilcoxonUtil(
        method_list=result['method_list'],
        metrics=result['metrics'],
        base_line=result['base_line_list'],
        data_path=result['data_path'])
    wilcoxon_util.calculate()
