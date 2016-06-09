#! /usr/bin/env python3
# ANOVA_test.py
# A test script to test the functions written in ANOVA.py

low_cal = [8, 9, 6, 7, 3]
low_fat = [2, 4, 3, 5, 1]
low_carb = [3, 5, 4, 2, 3]
control = [2, 2, -1, 0, 3]

import ANOVA as a

ssb_result = a.ssb(low_cal, low_fat, low_carb, control)
sse_result = a.sse(low_cal, low_fat, low_carb, control)
f_result = a.fStatistic(low_cal, low_fat, low_carb, control)

print(ssb_result)
print(sse_result)
print(f_result)
