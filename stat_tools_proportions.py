#! /usr/bin/env python3
#stat_practice.py

import math

"""
Success-Failure Condition requires that there are at least 10 successes
and 10 failures observed in the sample. Returns True or False.
"""
def check_success_failure(p, n):
    threshold = 10
    return (p * n) >= threshold and (n * (1-p)) >= threshold

"""
Calculates standard error for sampling distribution of sample proportion (p-hat).
Acts as estimate of se when population proportion (p) is unknown.
"""

def standard_error(p, n):
     return math.sqrt(p * (1 - p) / n)

"""
Calculates pooled standard error for sampling distribution of difference 
of two sample proportions (p-hat1 - p-hat2).
Acts as estimate of se when population proportions (p1 and p2) are unknown.
"""
     
def standard_error_two_sample(p1, n1, p2, n2):
     se1 = (p1 * (1 - p1) / n1)
     se2 = (p2 * (1 - p2) / n2)
     return math.sqrt(se1 + se2)

"""
Calculate z-score given a sample size, n; a sample proportion, p-hat; and either
a population proportion or hypothesized proportion for comparison, p.
"""
     
def z_score(p, p_hat, n):
    return (p_hat - p) / standard_error(p, n)
     
"""
Calculates confidence interval, given a sample proportion point estimate, confidence interval
level, and sample size. Uses proportion and sample size to calculate standard error.
"""
     
def confidence_interval(p, ci, n):    
    z_scores = {.99:2.58, .95:1.96, .90:1.65}
    
    try:
        ci in z_scores
        return ((p - (z_scores[ci] * standard_error(p, n))), (p + (z_scores[ci] * standard_error(p, n))))        
    except:
        return "Confidence Interval of {} not available. Choose .99, .95, or .90.".format(ci)
    
"""
Constructs confidence interval of a difference between two proportions, 
given two proportions with sample sizes and a confidence interval level
of 99%, 95%, or 90% (entered in decimal format).

Uses proportions and sample sizes to calculate pooled standard error.
"""

def confidence_interval_two_sample(p1, n1, p2, n2, ci):
    z_scores = {.99:2.58, .95:1.96, .90:1.65}
    
    try:
        ci in z_scores
        return (((p1-p2) - (z_scores[ci] * standard_error_two_sample(p1, n1, p2, n2))), ((p1-p2) + (z_scores[ci] * standard_error_two_sample(p1, n1, p2, n2))))        
    except:
        return "Confidence Interval of {} not available. Choose .99, .95, or .90.".format(ci)    
"""
Calculates sample size needed given a desired confidence interval (), 
margin of error, and proportion.
    
Note that for a 95% confidence interval, z-score = 1.96; for a 90% confidence
interval, z-score = 1.65
"""
def sample_size_calc(ci, me, p):
    z_scores = {.99:2.58, .95:1.96, .90:1.65}
    try:
        ci in z_scores
        return z_scores[ci] ** 2 * (p * (1-p)) / (me**2)        
    except:
        return "Confidence Interval of {} not available. Choose .99, .95, or .90.".format(ci)


