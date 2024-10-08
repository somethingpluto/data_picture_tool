library(ScottKnottESD)
library(readxl)
# 数据文件夹路径
# TODO: 所有路径统一采用绝对路径 间隔符采用 \\ 同时 末尾保留 \\
data_path <- "E:\\code\\code_back\\python_project\\data_picture_tool\\sk_esd\\test_data\\"
# esd 离群检测法结果存放路径
sk_esd_result_path <- 'E:\\code\\code_back\\python_project\\data_picture_tool\\sk_esd\\output\\'
# 获取所有csv文件名称
file_list <- list.files(data_path)

for (file in file_list){
  print(file)
  # 生成绝对路径
  path <-paste0(data_path,file)
  # 读取xlsx文件
  data <- read_excel(path)
  print(data)
  # 删除第一列
  data <- data[,-1]
  # 进行sk_esd分析
  sk <- sk_esd(data)
  splited_str <- gsub(".xlsx","",file)
  print(splited_str)
  result_path <- paste0(sk_esd_result_path,splited_str,".txt")
  print(result_path)
  write.table(sk[['groups']],file = result_path)
  print("data parsed successed")
}
print("all finished")