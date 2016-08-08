#! /usr/bin/env python3
#s3_pricing_calc.py

def s3Price_East_Standard(usage):
    
    """
    Function to calculate price, given a particular usage level
    Usage level assumed to be in GB
    
    Variables:
    TierX_usage sets usage level for that tier, in GB
    TierX_price sets pricing per GB for that tier
    TierX_limit calculates upper threshold in GB for that tier before usage crosses into next tier
    
    e.g., if Tier1_usage = 1000 and Tier2_usage = 49000, customer with 3000GB would be charged:
    Tier1_price per first 1000GB and Tier2_price for each remaining GB
    e.g., if Tier3_usage = 450000, customer with 55000GB would be charged:
    Tier1_price per first 1000GB + Tier2_price for next 49000GB + Tier3_price for each remaining GB
    """
    Tier1_usage = 1000
    Tier1_price = .03
    Tier1_limit = Tier1_usage
    
    Tier2_usage = 49000
    Tier2_price = .0295
    Tier2_limit = Tier1_limit + Tier2_usage

    Tier3_usage = 450000
    Tier3_price = .029
    Tier3_limit = Tier2_limit + Tier3_usage

    Tier4_usage = 500000
    Tier4_price = .0285
    Tier4_limit = Tier3_limit + Tier4_usage

    Tier5_usage = 4000000
    Tier5_price = .028
    Tier5_limit = Tier4_limit + Tier5_usage

    Tier6_usage = 5000000
    Tier6_price = .0275
    Tier6_limit = Tier5_limit + Tier6_usage
    
    #Calculate cost if usage falls into Tier6
    if Tier5_limit < usage:
        Tier6_cost = (usage - Tier5_limit) * Tier6_price
        Tier5_cost = Tier5_usage * Tier5_price
        Tier4_cost = Tier4_usage * Tier4_price
        Tier3_cost = Tier3_usage * Tier3_price
        Tier2_cost = Tier2_usage * Tier2_price
        Tier1_cost = Tier1_usage * Tier1_price
        
        Total_cost = Tier1_cost + Tier2_cost + Tier3_cost + Tier4_cost + Tier5_cost + Tier6_cost
    #Calculate cost if usage falls into Tier5
    elif Tier4_limit < usage <= Tier5_limit:
        Tier5_cost = (usage - Tier4_limit) * Tier5_price
        Tier4_cost = Tier4_usage * Tier4_price
        Tier3_cost = Tier3_usage * Tier3_price
        Tier2_cost = Tier2_usage * Tier2_price
        Tier1_cost = Tier1_usage * Tier1_price
        
        Total_cost = Tier1_cost + Tier2_cost + Tier3_cost + Tier4_cost + Tier5_cost
        
    #Calculate cost if usage falls into Tier4
    elif Tier3_limit < usage <= Tier4_limit:
        Tier4_cost = (usage - Tier3_limit) * Tier4_price
        Tier3_cost = Tier3_usage * Tier3_price
        Tier2_cost = Tier2_usage * Tier2_price
        Tier1_cost = Tier1_usage * Tier1_price
        
        Total_cost = Tier1_cost + Tier2_cost + Tier3_cost + Tier4_cost
    
    #Calculate cost if usage falls into Tier3
    elif Tier2_limit < usage <= Tier3_limit:
        Tier3_cost = (usage - Tier2_limit) * Tier3_price
        Tier2_cost = Tier2_usage * Tier2_price
        Tier1_cost = Tier1_usage * Tier1_price
        
        Total_cost = Tier1_cost + Tier2_cost + Tier3_cost
    
    #Calculate cost if usage falls into Tier2
    elif Tier1_limit < usage <= Tier2_limit:
        Tier2_cost = (usage - Tier1_limit) * Tier2_price
        Tier1_cost = Tier1_usage * Tier1_price
        
        Total_cost = Tier1_cost + Tier2_cost
    
    #Calculate cost if usage falls into Tier1
    elif usage <= Tier1_limit:
        Tier1_cost = usage * Tier1_price
        
        Total_cost = Tier1_cost
        
    return Total_cost


print(s3Price_East_Standard(500))
print(s3Price_East_Standard(2000))
print(s3Price_East_Standard(300000))
print(s3Price_East_Standard(725000))
print(s3Price_East_Standard(2398000))
print(s3Price_East_Standard(8340000))
