import pandas as pd
import numpy as np

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

# Make bridge_id and road_id based on road and LRP
df_roadN1['road_id'] = df_roadN1['road'] + df_roadN1['lrp']
df_bridges['bridge_id'] = df_bridges['road'] + df_bridges['LRPName']

# Reset index
df_roadN1 = df_roadN1.reset_index(drop=True)
df_bridges = df_bridges.reset_index(drop=True)
df_roadN1['road_id'] = df_roadN1['road_id'].astype(str)
df_bridges['bridge_id'] = df_bridges['bridge_id'].astype(str)

'''
# Connect bridge condition from df_bridges to obtain bridge condition and length into the df
df_roadN1['bridge_condition'] = np.where((df_roadN1['road_id'].astype(str) == df_bridges['bridge_id'].astype(str)), df_bridges['condition'], np.nan)
df_roadN1['bridge_length'] = np.where((df_roadN1['road_id'] == df_bridges['bridge_id']), df_bridges['length'], np.nan)
'''

for index, row in df_roadN1.iterrows():
    road_id = row['road_id']
    matching_bridge = df_bridges[df_bridges['bridge_id'].str.contains(road_id)]
    if not matching_bridge.empty:
        bridge_condition = matching_bridge.iloc[0]['condition']
        df_roadN1.at[index, 'bridge_condition'] = bridge_condition


print(df_roadN1[['road_id', 'type', 'bridge_condition']].head(5))