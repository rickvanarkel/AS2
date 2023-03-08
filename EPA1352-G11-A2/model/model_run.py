import pandas as pd
import random

from model import BangladeshModel

"""
    Run simulation
    Print output at terminal
"""

# ---------------------------------------------------------------

run_length = 5 * 24 * 60

df_list = pd.DataFrame(columns=["run", "avarage"])
df_list.set_index("run", inplace=True)

for i in range(1,4):

    df_list = pd.DataFrame(columns=["run", "avarage"])
    df_list.set_index("run", inplace=True)

    for k in range(2):
        seed = random.randint(1,1234567)
        sim_model = BangladeshModel(seed=seed, scenario=i)
        # Check if the seed is set
        print("SEED " + str(sim_model._seed))

        # One run with given steps
        for j in range(run_length):
            sim_model.step()
        average_time = sim_model.reporter['Time'].mean()
        df_list.loc[k] = [average_time]
        del(sim_model)

    df_list.to_csv(f'scenario{i}.csv')


