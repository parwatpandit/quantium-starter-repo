import pandas as pd
import os
# Step 1 - Read all 3 CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")


df = pd.concat([df1, df2, df3])
df_pink=(df[df["product"]=="pink morsel"])

if not os.path.exists("pink_morsel.csv"):
    df_pink.to_csv("pink_morsel.csv", index=False)
df_pink.to_csv("pink_morsel.csv", index=False)


# reading pink_morsel.csv file 
pink_morsel=pd.read_csv("pink_morsel.csv")

pink_morsel["price"] = pink_morsel["price"].str.replace("$", "").astype(float)

print(pink_morsel["price"])