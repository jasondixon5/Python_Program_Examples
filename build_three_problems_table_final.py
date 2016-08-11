#! /usr/bin/env python3
# read_in_problems.py - A script to build, from survey responses, count of problems selected, by gender

"""
Process a file containing results of a survey.
File includes a column for respondent's gender and a column for the survey 
question: "Choose the 3 main problems you think women face in Nepal."
Problem responses available: 'Career choice', 'Child marriage', 
                            'Domestic violence', 'Education', 'Health care', 
                            'Lack of opportunity', 'Poverty', 'Trafficking'

Script builds a list of the counts of each problem selected, by gender and 
also other totals and proportions related to them.
"""

import openpyxl
import csv
filename = open('Women_Leadership_Survey.xlsx', 'rb')
wb = openpyxl.load_workbook(filename)
sheet = wb.get_sheet_by_name('Responses')

survey_question = 'Choose the 3 main problems you think women face in Nepal.'
problem_list = ['Career choice', 'Child marriage', 'Domestic violence', 
                'Education', 'Health care', 'Lack of opportunity', 'Poverty', 
                'Trafficking']

def make_default_count_dict():
    return { 'Male':0, 'Female':0, 'Total':0 }

# Build dict with key as problem and value as the default counter dict
# Use a "dictionary comprehension", which has the form:
# { k: v for e in list } --- use 'e' to make k, v, or both (or neither?)

problem_dict = { problem: make_default_count_dict() 
                for problem in problem_list }

total_respondents_by_gender = make_default_count_dict()

highest_row = sheet.max_row

#For each row, count each problem selected in the '3 Main Problems' column
for row in range(2, highest_row + 1):
    gender = sheet['F' + str(row)].value
    three_problems = sheet['I' + str(row)].value
    total_respondents_by_gender[gender] += 1
    total_respondents_by_gender['Total'] += 1
    
    for problem in problem_dict.keys():
        problem_dict[problem][gender] += three_problems.count(problem)

problem_dict['Total'] = make_default_count_dict()
# Add up total counts for all problems by gender
problem_totals = make_default_count_dict()

for problem in problem_dict.keys():
    gender = 'Female'
    problem_totals[gender] += problem_dict[problem][gender]

for problem in problem_dict.keys():
    gender = 'Male'
    problem_totals[gender] += problem_dict[problem][gender]
    
for problem, sub_dict in problem_dict.items():
    for gender in sub_dict.keys():
        problem_dict['Total'][gender] = problem_totals[gender]
    
for problem in problem_dict.keys():
    problem_dict[problem]['Total'] = problem_dict[problem]['Male'] \
                                    + problem_dict[problem]['Female']

# Create dict of proportion of respondents who identified each problem
problem_dict_proportions = { problem: make_default_count_dict()
                            for problem in problem_dict.keys()
                            }

for problem in problem_dict_proportions.keys():
    for gender in problem_dict_proportions[problem].keys():
        problem_dict_proportions[problem][gender] \
            = problem_dict[problem][gender] \
            / total_respondents_by_gender[gender]

# Create dict of proportion of this problem to other problems identified
problem_comparison_prop_dict = { problem: make_default_count_dict()
                                for problem in problem_dict.keys()
                                }

for problem in problem_comparison_prop_dict.keys():
    for gender in problem_comparison_prop_dict[problem].keys():
        problem_comparison_prop_dict[problem][gender] \
             =  problem_dict[problem][gender] / problem_dict['Total'][gender]

#Clean up % totals that won't make sense if printed
problem_dict_proportions['Total']['Female'] = None
problem_dict_proportions['Total']['Male'] = None
problem_dict_proportions['Total']['Total'] = None

headers = ['Problem Facing Women', 
            'Number of Female Respondents Who Identified This Problem', 
            'Number of Male Respondents Who Identified This Problem', 
            'Total Respondents Who Identified This Problem', 
            'Proportion of Female Respondents Who Identified This Problem', 
            'Proportion of Male Respondents Who Identified This Problem', 
            'Proportion of Total Respondents Who Identified This Problem', 
            'Among Females, Proportion of This Problem to Other Problems Identified', 
            'Among Males, Proportion of This Problem to Other Problems Identified', 
            'Among Total Respondents, Proportion of This Problem to Other Problems Identified'
            ]

output = open('Three_Problems_Table_Final.csv', 'w', newline='')
writer = csv.writer(output)

writer.writerow([survey_question])
writer.writerow(headers)
for problem in problem_dict.keys():
    writer.writerow([problem, 
                    problem_dict[problem]['Female'], 
                    problem_dict[problem]['Male'],
                    problem_dict[problem]['Total'],
                    problem_dict_proportions[problem]['Female'],
                    problem_dict_proportions[problem]['Male'],
                    problem_dict_proportions[problem]['Total'],
                    problem_comparison_prop_dict[problem]['Female'],
                    problem_comparison_prop_dict[problem]['Male'],
                    problem_comparison_prop_dict[problem]['Total'],
                    ])

output.close()