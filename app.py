import dash
from dash import html, dcc
import pandas as pd
import os
# reading all the csv file provided
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")


# only taking product with name 'pink morsel'
df = pd.concat([df1, df2, df3])
df_pink=(df[df["product"]=="pink morsel"])

# if exist do nothing
if not os.path.exists("data/pink_morsel.csv"):
    df_pink.to_csv("data/pink_morsel.csv", index=False)



# reading pink_morsel.csv file 
pink_morsel=pd.read_csv("data/pink_morsel.csv")

# removing the $sign form the price so i can calculate the sales
pink_morsel["price"] = pink_morsel["price"].str.replace("$", "").astype(float)

# calculating sales totoal
pink_morsel["sales"] = pink_morsel["price"] * pink_morsel["quantity"]
# print(pink_morsel["sales"])

# writing before 2021-01-25 and after  2021-01-25 self  of pink_morsel 
before = pink_morsel[pink_morsel["date"] < "2021-01-15"]
after = pink_morsel[pink_morsel["date"] >= "2021-01-15"]
# spliting the sales before and after 15th Jand 2021
def SalesBeforeAfter():
    return{
        "Before:", before["sales"].sum(),
        "After:", after["sales"].sum()
    }
SalesBeforeAfter

# display before and after and save to file as well
output = pd.DataFrame({
    "sales": [before["sales"].sum(), after["sales"].sum()],
    "date": ["before 15th Jan 2021", "after 15th Jan 2021"]
})

output.to_csv("data/output.csv", index=False)
print(output)


# task 2 output fogmat displaying in a new file
filtered_df = pink_morsel[["sales", "date", "region"]]
filtered_df.to_csv("data/task_2.csv", index=False)


# reading task_2.csv for dash_app
dash_df = pd.read_csv("data/task_2.csv")
app = dash.Dash(__name__)


# header of the dash app
# and line chart
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(
        id="sales-chart",
        figure={
            "data": [
                {
                    "x": dash_df["date"],
                    "y": dash_df["sales"],
                    "type": "line"
                }
            ],
            "layout": {
                "title": "Sales Over Time",
                "xaxis": {"title": "Date"},
                "yaxis": {"title": "Sales ($)"}
            }
        }
    )
])

if __name__ == "__main__":
    app.run(debug=True)


