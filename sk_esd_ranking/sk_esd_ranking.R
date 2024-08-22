library(ScottKnottESD)
library(readxl)

data_path <- "E:\\code\\code_back\\python_project\\data_picture_tool\\sk_esd_ranking\\test_data\\"
sk_esd_ranking_result_path <- 'E:\\code\\code_back\\python_project\\data_picture_tool\\sk_esd_ranking\\output'
file_names <- list.files(data_path)
for(file in file_names){
  if(grepl(pattern = ".xlsx$",x=file)){
    # 获取文件名
    parts <- strsplit(file,split = "#")[[1]]
    dataset <- parts[1]
    metric <- sub("\\.xlsx","",parts[2])

    # 凭借文件路径
    file_path <- paste0(data_path,file)
    print(file_path)
    data <- read_excel(file_path)
    data <- data[,-1]
    sk <- sk_esd(data)
    picutre_file_name <- paste0('RQ2_Ranking_',dataset,"-",metric,".jpg")
    picutre_file_path <- paste0(sk_esd_ranking_result_path,picutre_file_name)
    print(picutre_file_path)
    jpeg(file=picutre_file_path,width =2500,height =1600,units = 'px',res = 600)
    plot(sk,
         mar=c(0,0,0,0)+0.1,
         las=2,
         cex=0.7,
         cex.axis=0.1,
         cex.lab=0.9,
         xlab = '',
         ylab = 'Rankings',
         mgp = c(3,2,0),
         # xgap.axis = 3,
         # axis.line=3,
         family = "serif",
         title=NULL,
         ylim  = c(0.2,0.6)
        )
      dev.off()
  }
}
