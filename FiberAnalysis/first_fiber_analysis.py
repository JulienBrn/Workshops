import pandas as pd
def display_as_table(d):
    print(pd.DataFrame(d))
    
df = pd.read_csv("Data/Events.csv")
data = list(df.to_dict(orient="index").values())

print(data)



display_as_table(data)