import csv
from collections import Counter

# 读取文件并统计标签
with open('test.txt', 'r', encoding='utf-8') as file:
    # 使用Counter来计数每个标签的出现频率
    counts = Counter(file.read().splitlines())

# 将计数结果排序（按照出现次数从高到低）
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

# 写入到CSV文件
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # 写入表头
    writer.writerow(['llm', 'count'])
    # 写入统计数据
    writer.writerows(sorted_counts)

print("CSV文件已生成。")
