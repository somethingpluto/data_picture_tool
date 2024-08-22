import csv
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# 文件路径
input_file_path = './data.txt'
output_file_path = './llm_count.csv'

# 读取文件内容并统计单词出现次数
with open(input_file_path, 'r', encoding='utf-8') as file:
    words = file.read().splitlines()

word_count = Counter(words)

# 将统计结果按数量由高到低排序
sorted_word_count = word_count.most_common()

# 将结果保存为CSV文件
with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Word', 'Count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for word, count in sorted_word_count:
        writer.writerow({'Word': word, 'Count': count})

print(f'Results saved to {output_file_path}')

# 提取前10个单词绘制饼图，如果单词较多可以选择前N个单词
top_words = sorted_word_count[:10]
labels = [word for word, _ in top_words]
sizes = [count for _, count in top_words]

# 绘制饼图
plt.figure(figsize=(10, 7))
wedges, texts, autotexts = plt.pie(sizes, autopct='%1.1f%%', startangle=140, textprops=dict(color="w"))

# 调整百分比标签的位置
for autotext in autotexts:
    autotext.set_size(10)
    autotext.set_color('black')
    autotext.set_ha('center')
    autotext.set_va('center')
    autotext.set_bbox(dict(facecolor='white', edgecolor='none', pad=0))

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')
plt.title('Top 10 Words Frequency Distribution')
plt.show()