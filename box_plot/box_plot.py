import argparse
import glob
import os
from traceback import print_tb

import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

plt.rc("font", family="Times New Roman")


class BoxPlotUtil:
    def __init__(self, sk_result_dir_path, csv_data_dir_path):
        """
        初始化
        :param sk_result_dir_path:
        :param csv_data_dir_path:
        """
        self.sk_result_dir_path = sk_result_dir_path
        # 保存原生csv文件存放路径
        self.csv_data_dir_path = csv_data_dir_path
        self.all_file_path = []
        self.header = [
            'random',  'uncertainty-margin', 'uncertainty-least_confident', 'uncertainty-entropy','qbc','bmdr','err-reduction','graph_density','quire','spal','batch-rank'
        ]
        self.color_dict = {
            1: "red",
            2: "green",
            3: "blue",
            4: "orange",
            5: "purple",
            6: "yellow",
            7: "pink",
            8: "gray",
            9: "gray",
            10: "gray",
            11: "gray",
            12: "gray",
            13: "gray",
            14: "gray",
            15: "gray",
            16: "gray",
            17: "gray",
            18: "gray",
            19: "gray",
            20: "gray",
            21: "gray",
            22: "gray",
            23: "gray",
            24: "gray",
            25: "gray",
            26: "gray",
            27: "gray",
            28: "gray",
            29: "gray",
            30: "gray",
            31: "gray",
            32: "gray",
            33: "gray",
            34: "gray",
            35: "gray",
        }
        self._read_all_file_path()

    def _read_all_file_path(self):
        """
        获取文件夹下所有文件
        :return:
        """
        files = glob.glob(self.sk_result_dir_path + "/*")
        self.all_file_path = files

    def parse_txt2csv(self, txt_file_path):
        # 记录方法
        method = []
        # 记录rank排名
        rank = []
        # 读取txt文件
        lines = open(txt_file_path, "r", encoding="utf-8").readlines()
        for line in lines[1:]:
            l = line.replace("\n", "").replace('"', "").split(" ")
            method.append(l[0])
            rank.append(int(l[1]))
        if len(self.header) != len(method) or len(self.header) != len(rank):
            print("header 与 method rank 数量不一致")
            exit()
        header_rank = []
        for head in self.header:
            if head in method:
                index = method.index(head)
                header_rank.append(rank[index])
        data = [self.header, header_rank]
        return data

    def draw(self):
        with tqdm(total=len(self.all_file_path), desc="drawing") as pbar:
            for file in self.all_file_path:
                # 将txt文件转换为csv格式
                color_data = self.parse_txt2csv(file)
                # 读取csv文件
                print(file)
                csv_file_name = file.split('output\\')[1].strip(".txt")
                print(csv_file_name)
                csv_file_path = os.path.join(self.csv_data_dir_path, csv_file_name)
                all_data = pd.read_csv(csv_file_path + ".csv")
                all_data = all_data.iloc[1:, 1:].values
                color_nums = color_data[1]
                # 创建画布和子图
                fig, ax = plt.subplots(figsize=(13, 5))
                ax.tick_params(direction="in")
                figure = ax.boxplot(
                    all_data,
                    notch=False,  # notch shape
                    sym="r+",  # blue squares for outliers
                    vert=True,  # vertical box aligmnent
                    meanline=True,
                    showmeans=True,
                    patch_artist=False,
                    showfliers=False,
                    widths=0.3
                )
                # colors = [self.color_dict[int(i)] for i in color_nums]
                # for i in range(0, len(colors)):
                    # k = figure["boxes"][i]
                    # k.set(color=colors[i])
                    # k = figure["means"][i]
                    # k.set(color=colors[i])
                    # k = figure["medians"][i]
                    # k.set(color=colors[i], linewidth=2)
                    # k = figure["whiskers"][2 * i : 2 * i + 2]
                    # for w in k:
                    #     w.set(color=colors[i], linestyle="--")
                    # k = figure["caps"][2 * i : 2 * i + 2]
                    # for w in k:
                    #     w.set(color=colors[i])
                medians = [item.get_ydata()[0] for item in figure['medians']]
                for median, line in zip(medians, figure['medians']):
                    x, y = line.get_xdata()[0], median  # x坐标取中位数线的x，y坐标为中位数的值
                    ax.text(x, y, f'{y:.2f}', ha='center', va='bottom', color='orange',fontsize=12)

                for cap in figure['caps']:
                    x, y = cap.get_xdata()[0], cap.get_ydata()[0]
                    ax.text(x, y, f'{y:.2f}', ha='center', va='bottom' if cap == figure['caps'][0] else 'top', color='red', fontsize=12)
                for box in figure['boxes']:
                    x = box.get_xdata()[0]  # 获取盒子的x坐标
                    y_bottom = box.get_ydata()[0]  # Q1
                    y_top = box.get_ydata()[2]  # Q3
                    ax.text(x, y_bottom, f'{y_bottom:.2f}', ha='center', va='top', color='green', fontsize=12)
                    ax.text(x, y_top, f'{y_top:.2f}', ha='center', va='bottom', color='green', fontsize=12)
                plt.xlim((0, 12))
                lenheader = len(self.header) + 1
                plt.xticks(
                    [y for y in range(1, lenheader)],
                    self.header,
                    rotation=45,
                    weight="heavy",
                    fontsize=12,
                )
                plt.ylabel(
                        "{0}".format(csv_file_name), fontsize=24
                    )
                plt.yticks(fontsize=16)
                plt.rcParams["xtick.direction"] = "in"
                plt.rcParams["ytick.direction"] = "in"
                plt.axvline(1.5, color="black", linestyle=":")
                plt.axvline(4.5, color="black", linestyle=":")
                plt.axvline(5.5, color="black", linestyle=":")
                plt.axvline(7.5, color="black", linestyle=":")
                plt.title(
                    "                                                            US                             "
                    "            QBC             "
                    "            EER            "
                    "                             DWM          ",
                    fontsize=11,
                    loc="left",
                )
                if not os.path.exists("./pictures/"):
                    os.makedirs("./pictures/")
                output_file_path = "./pictures/RQ1_{0}.png".format(
                    csv_file_name
                )
                foo_fig = plt.gcf()
                foo_fig.savefig(
                    output_file_path, format="png", dpi=600, bbox_inches="tight"
                )
                plt.clf()
                plt.close()
                pbar.write(f"\ntxt_file:{file} csv_file:{csv_file_name}")
                pbar.update(1)


if __name__ == "__main__":
    # TODO: sk_esd 计算结果存放目录
    sk_result_path = "../sk_esd/output/"
    # TODO: raw data 存放目录
    raw_data_path = "../sk_esd/test_data/"
    util = BoxPlotUtil(sk_result_path, raw_data_path)
    util.draw()
    print("⭐⭐⭐⭐⭐ picture generate success")
