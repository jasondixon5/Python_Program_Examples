#! /usr/bin/env python3
# ANOVA.py
# Calculates the analysis of variance (f-statistic) for comparing strength of effect of a categorical variable on a quantitative variable.
# The ANOVA f test asks, "Are the differences among the sample means due to true differences among the population means or merely sampling variability?
# It is calculated as F = variability among groups' sample means / variability within groups

def mu(data):
    return sum(data)/len(data)

#ssb = Sum of Squares Between (Groups)
def ssb(*args):
    """
    The sum of squares between groups is a variance calculation obtained by the following calculations:
    -Overall mean for all results
    -Individual means for each group
    -For each group, difference between the mean for that group and the overall mean
    -Square of each difference
    -Sum of the squares
    """
    
    groups = args
    
    #Creates a master list of all results for purposes of calculating length and mean for all results
    all_results = [x for group in groups for x in group]
    num_total_obs = len(all_results)
    overall_mean = mu(all_results)

    #Finds the mean and length for each individual group
    group_means = [mu(group) for group in groups]
    group_lengths = [len(group) for group in groups]
    
    #Finds the difference between the mean for each group and the overall mean
    #Squares each difference
    diff_group_mu_overall_mu = [(item - overall_mean) for item in group_means]
    squared_diffs = [item**2 for item in diff_group_mu_overall_mu]
    
    import numpy as np
    
    #Creates numpy arrays for number of results in each group and squared diffs (latter calc'd above)
    #Uses those arrays to find number of results * squared diffs for each group
    #The number of results in each group acts as a weighting for the squared diff for that group
    #Finally, sums the weighted squared differences
    group_lengths_np = np.array(group_lengths)
    squared_diffs_np = np.array(squared_diffs)
    squares_b = group_lengths_np * squared_diffs_np
    sum_squares_b = sum(squares_b)
    return sum_squares_b

#sse = Sum of Squares for Errors
def sse(*args):
    """
    The sum of squares for errors (aka residuals) is a variance calculation obtained by the following calculations:
    -Overall mean for each group
    -Difference between each observed value in a group and the group mean
    -Square of each difference
    -Sum of the squared differences within each group
    -Sum of the totals of all groups
    """
    groups = args
    
    #Finds the mean for each individual group
    group_means = [mu(group) for group in groups]
    
    #For each value in each group, finds the difference between the value and the group's mean
    diff_obs_and_group_means = []
    for i in range(len(groups)):
        temp_list = []
        for value in groups[i]:
            diff = value - group_means[i]
            temp_list.append(diff)
        diff_obs_and_group_means.append(temp_list)

    #Squares each difference and adds it to a new list
    
    squared_diff_obs_and_group_means = []
    for i in range(len(diff_obs_and_group_means)):
        temp_list = [value**2 for value in diff_obs_and_group_means[i]]
        squared_diff_obs_and_group_means.append(temp_list)
    
    #Finds sum of squared differences within each group
    sum_each_squared_diff_obs_and_group_means = []
    [sum_each_squared_diff_obs_and_group_means.append(sum(l)) for l in squared_diff_obs_and_group_means]

    #Finds sum of totals of all groups (i.e., sum of total of squared differences found above)
    sum_squared_errors = sum(sum_each_squared_diff_obs_and_group_means)

    return sum_squared_errors

def fStatistic(*args):
    """
    The f-statistic is a ratio calculation obtained with the following inputs and calculations:
    -Input: Sum of squares between treatements (SSB)
    -Calculation: Degrees of freedom for groups (Number of groups - 1)
    -Calculation: Mean squares between groups aka MSB (SSB / degrees of freedom)
    -Input: Sum of squares for errors/residuals (SSE)
    -Calculation: Degrees of freedom for errors/residuals (Total number of values - number of groups)
    -Calculation: Mean squares for errors/residuals aka MSE (SSE / degrees of freedom)
    -Calculation: The f-statistic (MSB/MSE)
    """
    groups = args
    #Calculates number of groups
    #Calculates total number of observations
    k = len(groups)
    all_results = [x for group in groups for x in group]
    num_total_obs = len(all_results)

    #Calculate degrees of freedom for Between Treatement (B) and Error/Residual (E)
    dfB = k - 1
    dfE = len(all_results) - k
    
    #Calculate means squares for Between Treatment (B) and Error/Residual (E)
    ms_B = ssb(*args)/dfB
    ms_E = sse(*args)/dfE
    
    f = ms_B/ms_E
    
    return f
