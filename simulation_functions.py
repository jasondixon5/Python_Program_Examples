#! /usr/bin/env python3

import random
import numpy as np

def proportion_diff(observations, cat1_column=0, cat2_column=1):
    """
    Calculate difference in proportions
    
    cat1_column = # of first column to calculate proportion
    (0-indexed, defaults to first column)
    cat2_column = # of second column to calculate proportion
    (0-indexed, defaults to second column)
    
    observations = each row's list of values for each column
    observations represent how many values were observed for each column category

    Example: 2x2 table with following format:

    row_category    column_category
                    c_cat1          c_cat2
    r_cat1          R1C1            R1C2
    r_cat2          C1R2            C2R2

    r_cat1_observations = [R1C1, R1C2...]
    r_cat2_observations = [C1R2, C2R2...]
    observations = [r_cat1_observations, r_cat_2_observations]
    """
    c_cat1_idx = cat1_column
    c_cat2_idx = cat2_column
    r_cat1_idx = 0
    r_cat2_idx = 1
    
    #Calculate sample size (n) for each row category
    r_cat1_n = sum(observations[0])
    r_cat2_n = sum(observations[1])
    
    proportion_C1R1 = observations[r_cat1_idx][c_cat1_idx] / r_cat1_n
    proportion_C1R2 = observations[r_cat2_idx][c_cat1_idx] / r_cat2_n
    
    proportion_difference = proportion_C1R1 - proportion_C1R2
    
    return proportion_difference
    
def proportion_simulation(observations, sim_size=10000, cat1_column=0):
    
    #Form list of just observed values in column category 1
    c_cat1_idx = cat1_column
    c_cat1_obs = []

    for i in range(len(observations)):
        c_cat1_obs.append(observations[i][c_cat1_idx])
    
    simulated_cat1_n = sum(c_cat1_obs)
    
    large_sim_diff_rate_R1toR2 = []
    
    for _ in range(sim_size):
        simulated_results_C1R1 = 0
        simulated_results_C1R2 = 0
    
        for _ in range(simulated_cat1_n):
            if random.random() < 0.5:
                simulated_results_C1R2 += 1
            else:
                simulated_results_C1R1 += 1
        
        simulated_rate_C1R2 = simulated_results_C1R2 / simulated_cat1_n
    
        simulated_rate_C1R1 = simulated_results_C1R1 / simulated_cat1_n
    
        diff_in_simulated_rate_R1toR2 = simulated_rate_C1R1 - simulated_rate_C1R2
        
        large_sim_diff_rate_R1toR2.append(diff_in_simulated_rate_R1toR2)

    count_diffs_as_large = 0
    
    category_proportion_diff = proportion_diff(observations)
    
    for i in large_sim_diff_rate_R1toR2:
        if i >= category_proportion_diff:
            count_diffs_as_large += 1
    
    p_value_proportion_difference = count_diffs_as_large / sim_size
    
    return ("""
    proportion difference: {}
    p-value: {}
    sim_size: {}""".format(category_proportion_diff, p_value_proportion_difference, sim_size))

class Proportion_Stats():
    
    def __init__(self, observations, cat1_column=0):
        self.observations = observations
        self.cat1_column = cat1_column
        self.diff = self.proportion_diff()

    def proportion_diff(self):
        
        """
        Calculate difference in proportions
    
        cat1_column = # of first column to calculate proportion
        (0-indexed, defaults to first column)
        observations = each row's list of values for each column
        observations represent how many values were observed for each column category

        Example: 2x2 table with following format:

        row_category    column_category
                        c_cat1          c_cat2
        r_cat1          R1C1            R1C2
        r_cat2          C1R2            C2R2

        r_cat1_observations = [C1R1, C2R1...]
        r_cat2_observations = [C1R2, C2R2...]
        observations = [r_cat1_observations, r_cat_2_observations]
        """
        c_cat1_idx = self.cat1_column
        r_cat1_idx = 0
        r_cat2_idx = 1
    
        #Calculate sample size (n) for each row category
        r_cat1_n = sum(self.observations[0])
        r_cat2_n = sum(self.observations[1])
    
        proportion_C1R1 = self.observations[r_cat1_idx][c_cat1_idx] / r_cat1_n
        proportion_C1R2 = self.observations[r_cat2_idx][c_cat1_idx] / r_cat2_n
    
        proportion_difference = proportion_C1R1 - proportion_C1R2
    
        return proportion_difference
        
    def proportion_simulation(self, sim_size=10000):
    
        #Form list of just observed values in column category 1
        c_cat1_idx = self.cat1_column
        c_cat1_obs = []

        for i in range(len(self.observations)):
            c_cat1_obs.append(self.observations[i][c_cat1_idx])
    
        simulated_cat1_n = sum(c_cat1_obs)
    
        large_sim_diff_rate_R1toR2 = []
    
        for _ in range(sim_size):
            simulated_results_C1R1 = 0
            simulated_results_C1R2 = 0
    
            for _ in range(simulated_cat1_n):
                if random.random() < 0.5:
                    simulated_results_C1R2 += 1
                else:
                    simulated_results_C1R1 += 1
        
            simulated_rate_C1R2 = simulated_results_C1R2 / simulated_cat1_n
    
            simulated_rate_C1R1 = simulated_results_C1R1 / simulated_cat1_n
    
            diff_in_simulated_rate_R1toR2 = simulated_rate_C1R1 - simulated_rate_C1R2
        
            large_sim_diff_rate_R1toR2.append(diff_in_simulated_rate_R1toR2)

        count_diffs_as_large = 0
    
        category_proportion_diff = self.diff
    
        for i in large_sim_diff_rate_R1toR2:
            if i >= category_proportion_diff:
                count_diffs_as_large += 1
    
        p_value = count_diffs_as_large / sim_size
    
        return p_value