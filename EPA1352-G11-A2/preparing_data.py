import pandas as pd

link_roads = './data/_roads3.csv'
link_bridges = './data/BMMS_overview.xlsx'

df_roads = pd.read_csv(link_roads)
df_bridges = pd.read_excel(link_bridges)

print(df_roads.head(5))

# Check the column names. Eventually we want the columns: road,id,model_type,name,lat,lon,length + bridge info
for i in df_roads:
    print(i)

# Filter on road N1
df_roadN1 = df_roads[df_roads['road'] == 'N1']

# Check on which types there are in the N1
print(df_roadN1.type.unique())
print(df_roadN1.type.nunique())

# Connect bridge condition from df_bridges to obtain bridge condition and length into the df