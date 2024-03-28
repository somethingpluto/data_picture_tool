library(ScottKnottESD)
library(readxl)
# TODO: 所有路径统一采用绝对路径 间隔符采用 \\ 同时 末尾保留 \\
data_path <- "E:\\code\\code_back\\python_project\\data_picture_tool\\sk_esd_ranking\\test_data\\"
sk_esd_ranking_result_path <- 'E:\\code\\code_back\\python_project\\data_picture_tool\\sk_esd_ranking\\picture\\'
file_names <- list.files(data_path)
for(file in file_names){
  if(grepl(pattern = ".csv$",x=file)){
    # 获取文件名
    file_name <- strsplit(file,split = ".xlsx")[[1]][1]
    print(file_name)
    # 凭借文件路径
    file_path <- paste0(data_path,file)
    print(file_path)
    data <- read.csv(file_path)
    data <- data[-1]
    sk <- sk_esd(data)
    picutre_file_name <- paste0('RQ1_Ranking_',file_name,".jpg")
    picutre_file_path <- paste0(sk_esd_ranking_result_path,picutre_file_name)
    print(picutre_file_path)
    jpeg(file=picutre_file_path,width = 5000,height = 20000,units = 'px',res = 600)
    plot(sk,
         mar=c(7,1,1,1),
         las=2,
         #cex=0.6,
         #cex.axis=0.1,
         cex.lab=1.2,
         xlab = '',
         ylab = 'Rankings',
         #mgp = c(3,2,0),
         #xgap.axis = 3,
         #axis.line=3,
         family = "serif",
         title=NULL
        )
      dev.off()

  }
}
