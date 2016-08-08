#! /usr/bin/env python3

"""
Two-proportion z-test statistic

z = p1 - p2 / sqrt((p^(1-p^) / n1) + (p^(1-p^) / n2))
p^ (p-hat) is pooled proportion

"""

def two_prop_z_stat(**kwargs):
    """
    Function Parameters:
    n1 = sample size 1
    n2 = sample size 2
    success1 = number of sample1 with observed characteristic
    success2 = number of sample2 with observed characteristic
    e.g., two_prop_z_statistic(n1=500, n2=500, success1=90, success2=70)
    """
    import math
    success1 = kwargs['success1']
    success2 = kwargs['success2']
    n1 = kwargs['n1']
    n2 = kwargs['n2']
    p1 = success1 / n1
    p2 = success2 / n2

    #Compute pooled proportion of samples
    pooled_prop = (success1 + success2) / (n1 + n2)
    #Compute numerator of forumla (diff in proportions)
    z_diff = p1 - p2
    #Compute denominator of formula (standard error of this distribution)
    z_standard_error = math.sqrt((pooled_prop * (1 - pooled_prop) / n1)
                       + (pooled_prop * (1 - pooled_prop) / n2))
    #Compute the z-statistic
    z_stat = z_diff / z_standard_error
    return z_stat

"""
Two-proportion z-test statistic

z = p - pH / sqrt((pH(1-pH)) / n)
pH is hypothesized population proportion (proportion to test against)
p is the sample proportion
n is the sample size
"""
def one_prop_z_stat(**kwargs):
    """
    Function Parameters:
    success = number of sample with observed characteristic
    n = sample size
    pH = hypothesized proportion (<=1)
    """
    import math
    success = kwargs['success']
    n = kwargs['n']
    pH = kwargs['pH']
    p = success/n
    
    z_diff = p - pH
    z_standard_error = math.sqrt((pH * (1 - pH))
                        / n)
    z_stat = z_diff / z_standard_error
    return z_stat

"""
chi-square goodness of fit 
x2 = sum (observed - expected)^2 / expected    
"""
def chi_square_goodness_of_fit_stat(**kwargs):
    """Function parameters:
    original = original observed values to compare to (the hypothesized distribution)
    observed = newly observed values
    ***Note: Take care to put the values in the same category order in each group
    """
    import numpy as np
    
    original = np.array([kwargs['original']])
    observed = np.array([kwargs['observed']])
    #Note that sum(original) returns an array of the original values
    n_original = sum(sum(original))
    n_observed = sum(sum(observed))
    
    expected = original/n_original * n_observed
    differences = observed - expected
    sq_differences = differences ** 2
    individual_chi_square = sq_differences / expected
    chi_square = sum(sum(individual_chi_square))
    df = np.size(original) - 1
    print(expected)
    return [chi_square, df]

