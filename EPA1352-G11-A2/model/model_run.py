import pandas as pd
import random
import model
from components import Source

"""
    Run simulation
    Print output at terminal
"""

# ---------------------------------------------------------------

run_length = 5 * 24 * 60

for i in range(9):

    df_list = pd.DataFrame(columns=["run", "avarage"])
    df_list.set_index("run", inplace=True)

    for k in range(10):

        seed = random.randint(1,1234567)
        sim_model = model.BangladeshModel(seed=seed, scenario=i)
        # Check if the seed is set
        print("SEED " + str(sim_model._seed))

        # One run with given steps
        for j in range(run_length):
            sim_model.step()
        average_time = sim_model.reporter['Time'].mean()
        df_list.loc[k] = [average_time]
        Source.truck_counter = 0

    df_list.to_csv(f'LBscenario{i}.csv')

