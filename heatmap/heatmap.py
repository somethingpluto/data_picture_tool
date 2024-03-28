from email.policy import strict
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tqdm import tqdm
from matplotlib.colors import LinearSegmentedColormap

class HeatMapUtil:
    def __init__(self,dir_path="",file_path="") -> None:
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
                # 获取查询策略
                info_arr = simple_path.split("#")
                metric = info_arr[0]

                data = pd.read_excel(path)
                # 设置热力图的大小
                plt.figure(figsize=(12, 6))

                # 生成热力图
                # 使用rate_combination作为索引
                data_indexed = data.set_index('algorithm')
                sns.heatmap(data_indexed, annot=True, cmap="hot_r", fmt=".3f",vmin=0.2,vmax=0.9)

                plt.title(f'{metric} Heatmap')
                plt.xticks(rotation=45,fontsize=14)
                plt.ylabel('Classifier',fontsize=16)
                plt.xlabel('active learning method',fontsize=16)
                plt.tight_layout()  # 调整布局以适应标签和标题
                plt.savefig(f"./picture/hm-{metric}.png")
                pbar.update(1)

if __name__ =="__main__":
    util = HeatMapUtil("./test_data")
    util.draw()