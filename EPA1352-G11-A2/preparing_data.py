#from G11_A2_run import df_roads, df_bridges

print(df_roads.head(5))

# Check the column names. Eventually we want the columns: road,id,model_type,name,lat,lon,length + bridge info
for i in df_roads:
    print(i)

# Filter on road N1
df_roadN1 = df_roads[df_roads['road'] == 'N1']

# Check on which types there are in the N1
#print(df_roadN1.type.unique())
#print(df_roadN1.type.nunique())

def change_column_names():
    """
    The column names are updated and empty columns are generated for new information
    """
    #df_roadN1.rename(columns={'type': 'model_type'}, inplace=True)
    df_roadN1['model_type'] = ''
    df_roadN1['length'] = np.nan
    df_roadN1['id'] = ''
    df_roadN1['name'] = ''
    df_roadN1['condition'] = ''
    df_roadN1['road_name'] = 'Unknown'
    df_roadN1['bridge_length'] = np.nan

def change_model_type():
    """
    This function checks if the road object is a bridge and replaces it with 'bridge'
    Thereby replaces all other objects in 'link'
    The first and last object are 'source' and 'sink'
    """
    bridge_types = ['Bridge'] # in doubt over: CrossRoad, RailRoadCrossing, Culvert

    for i in bridge_types:
        df_roadN1.loc[df_roadN1['type'].str.contains(i), 'model_type'] = 'bridge'

    df_roadN1.loc[~df_roadN1['model_type'].str.contains('bridge'), 'model_type'] = 'road'

    df_roadN1['model_type'].iloc[0] = 'source'
    df_roadN1['model_type'].iloc[-1] = 'sink'

    # Some checks
    #print(df_roadN1['model_type'])
    #print(df_roadN1.model_type.unique())

def connect_infra():
    """
    This function connects the bridges df with the road df, to obtain information about bridge condition and length
    """
    # Make bridge_id and road_id based on road and LRP
    df_roadN1['road_id'] = df_roadN1['road'] + df_roadN1['lrp']
    df_bridges['bridge_id'] = df_bridges['road'] + df_bridges['LRPName']

    # find exact match between road+LRP
    for index, row in df_roadN1.iterrows():
        if 'bridge' in row['model_type']:
            road_id = row['road_id']
            matching_bridge = df_bridges[df_bridges['bridge_id'].str.contains(road_id)]
            if not matching_bridge.empty:
                bridge_condition = matching_bridge.iloc[0]['condition']
                bridge_length = matching_bridge.iloc[0]['length']
                df_roadN1.at[index, 'condition'] = bridge_condition
                df_roadN1.at[index, 'bridge_length'] = bridge_length

    # find less exact match between road+LRP (or another way, sustain it, what will work?)
    # what do we need to do with chainage?

    df_roadN1_bridges = df_roadN1[df_roadN1['model_type'] == 'bridge']
    #print(df_roadN1_bridges[['road_id', 'model_type', 'bridge_condition', 'bridge_length']].head(5))
    #print(df_roadN1_bridges.isnull().sum())


def get_length():
    df_roadN1['length'] = abs(df_roadN1['chainage'].astype(float).diff()) * 1000
    df_roadN1['length'][0] = 0

def get_name():
    df_roadN1['name'] = df_roadN1['model_type']

def get_road_name():
    pass

def make_id():
    unique_id = 1000000
    for i in range(len(df_roadN1['id'])):
        df_roadN1.loc[i, 'id'] = unique_id
        unique_id += 1

def make_figure():
    # make a figure of N1
    sns.lmplot(x='lon', y='lat', data=df_roadN1, hue='model_type', fit_reg=False, scatter_kws={"s": 10})
    #df_roadN1.plot(x='lon', y='lat', linestyle="",marker="o",legend=False, markersize='0.5')
    #df_roadN1_bridges.plot(x='lon', y='lat', linestyle="",marker="o",legend=False, markersize='0.5', color='orange')
    plt.show()

def prepare_data():
    change_column_names()
    change_model_type()
    connect_infra()
    # Delete sideroads?
    get_length()
    get_name()
    get_road_name()
    make_id()
    make_figure()

prepare_data()

for i in df_roadN1:
    print(i)

df_roadN1.to_excel('check_N1_df.xlsx')
df_roadN1.to_csv('./data/demo_N1.csv')