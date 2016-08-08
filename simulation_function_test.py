#! /usr/bin/env python3

import simulation_functions as sf

male_observed = [21, 3]
female_observed = [14, 10]
all_results = [male_observed, female_observed]

m2f_diff_results = sf.proportion_diff(all_results)
m2f_sim_diff_results = sf.proportion_simulation(all_results)



ps = sf.Proportion_Stats(all_results)

observed_diff = ps.diff
p_value_observed_diff = ps.proportion_simulation()

print("Observed proportion difference: {}, p-value: {}".format(observed_diff, p_value_observed_diff))