import os
from matplotlib import pyplot as plt
import pandas as pd
from tqdm import tqdm
import seaborn as sns
import numpy as np


class LinePlotUtil:
    def __init__(self,dir_path="",file_path="",output_path="") -> None:
        if output_path == "":
            raise ValueError("output dir can not find")
        self.output_path  = output_path
        if dir_path == "" and file_path == "":
            raise ValueError("dir_path and file_path can not both empty")
        self.dir_path = dir_path
        self.file_path = file_path
        if dir_path != "" and file_path == "":   
            self.file_paths = []
            self._read_file_from_dir_path()
        
    
    def _read_file_from_dir_path(self):
        for dirpath, dirnames, filenames in os.walk(self.dir_path):
            for filename in filenames:
                # 将文件名与其所在的目录路径拼接起来，得到完整的文件路径
                file_path = os.path.join(dirpath, filename)
                self.file_paths.append(file_path)

    def draw(self):
        with tqdm(total=len(self.file_paths),desc="drawing") as pbar:
            for path in self.file_paths:
                simple_path = path.replace("./test_data\\","")
                info_arr = simple_path.split("#")
                metric = info_arr[0]
                initial_rate = info_arr[1].strip(".xlsx")
                data = pd.read_excel(path)

                x_ticks = np.arange(0.05, 0.30, 0.05)

                plt.figure(figsize=(8, 6))
                # 绘制折线图
                plt.plot(data.columns[1:], data.loc[0, data.columns[1:]], marker='o', label=data.loc[0, 'algorithm'])
                plt.plot(data.columns[1:], data.loc[1, data.columns[1:]], marker='o', label=data.loc[1, 'algorithm'])
                plt.plot(data.columns[1:], data.loc[2, data.columns[1:]], marker='o', label=data.loc[2, 'algorithm'])
                # 添加数据标签
                for i in range(3):
                    for j in range(len(x_ticks)):
                        plt.text(x_ticks[j], data.loc[i, data.columns[j+1]], '{:.3f}'.format(data.loc[i, data.columns[j+1]]), ha='center', va='bottom')
                # 添加图例、标题和轴标签
                if metric == "f1":
                    plt.ylim(0.4, 0.6)
                if metric == "mcc":
                    plt.ylim(0.3,0.5)
                if metric == "precision":
                    plt.ylim(0.5,0.7)
                if metric == "recall":
                    plt.ylim(0.4,0.6)
                plt.legend()
                plt.xlabel('query rate',fontsize=16)
                plt.ylabel(f"{metric} value",fontsize=16)
                plt.xticks(x_ticks)
                # 显示图形
                plt.savefig(f'{self.output_path}/{metric}-{initial_rate}.png', dpi=300, bbox_inches='tight')
                pbar.update(1)

if __name__ =="__main__":
    util = LinePlotUtil("./test_data",output_path=r'E:\code\code_back\python_project\ac_test_on_mlcq\record\AQ3\picture')
    util.draw()