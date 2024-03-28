import pandas as pd

data = pd.read_excel("../sk_esd/test_data/f1-ini0.05-query0.1.xlsx")
data.to_csv("./f1-ini0.05-query0.1.csv",index=False)
