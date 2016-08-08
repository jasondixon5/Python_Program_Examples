#! /usr/bin/env python3
#s3_pricing_region.py

<<<<<<< HEAD
def s3Price_East_Standard(usage, region):
=======
def s3Price_Standard(usage, region):
>>>>>>> 969544c267e05418cdedaff069a4c381fcc732ba
    
    """
    Function to calculate price, given a particular usage level and region
    Usage level assumed to be in GB
    
    Region arguments:
<<<<<<< HEAD
=======
    nvir = US East - Northern Virginia
>>>>>>> 969544c267e05418cdedaff069a4c381fcc732ba
    oreg = US West - Oregon
    cali = US West - California
    irel = EU - Ireland
    fran = EU - Frankfurt
    sing = Asia Pacific - Singapore
    toky = Asia Pacific - Tokyo
    sydn = Asia Pacific - Sydney
    seou = Asia Pacific - Seoul
    saop = South America - Sao Paulo
    
    Variables:
    TierX_usage sets usage level for that tier, in GB
    TierX_price sets pricing per GB for that tier
    TierX_limit calculates upper threshold in GB for that tier before usage crosses into next tier
    
    e.g., if Tier1_usage = 1000 and Tier2_usage = 49000, customer with 3000GB would be charged:
    Tier1_price per first 1000GB and Tier2_price for each remaining GB
    e.g., if Tier2_usage = 450000, customer with 55000GB would be charged:
    Tier1_price per first 1000GB + Tier2_price for next 49000GB + Tier3_price for each remaining GB
<<<<<<< HEAD
    """
    if region == oreg:
=======
    """    
        
    if region == 'nvir':
>>>>>>> 969544c267e05418cdedaff069a4c381fcc732ba
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
    
<<<<<<< HEAD
    elif region == cali:
=======
    if region == 'oreg':
>>>>>>> 969544c267e05418cdedaff069a4c381fcc732ba
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
<<<<<<< HEAD
        
    elif region == irel:
=======
    
    elif region == 'cali':
        Tier1_usage = 1000
        Tier1_price = .033
        Tier1_limit = Tier1_usage
    
        Tier2_usage = 49000
        Tier2_price = .0324
        Tier2_limit = Tier1_limit + Tier2_usage

        Tier3_usage = 450000
        Tier3_price = .0319
        Tier3_limit = Tier2_limit + Tier3_usage

        Tier4_usage = 500000
        Tier4_price = .0313
        Tier4_limit = Tier3_limit + Tier4_usage

        Tier5_usage = 4000000
        Tier5_price = .0308
        Tier5_limit = Tier4_limit + Tier5_usage

        Tier6_usage = 5000000
        Tier6_price = .0302
        Tier6_limit = Tier5_limit + Tier6_usage
        
    elif region == 'irel':
>>>>>>> 969544c267e05418cdedaff069a4c381fcc732ba
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
    
<<<<<<< HEAD
    elif region == fran:
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
    
    elif region == sing:
=======
    elif region == 'fran':
        Tier1_usage = 1000
        Tier1_price = .0324
        Tier1_limit = Tier1_usage
    
        Tier2_usage = 49000
        Tier2_price = .0319
        Tier2_limit = Tier1_limit + Tier2_usage

        Tier3_usage = 450000
        Tier3_price = .0314
        Tier3_limit = Tier2_limit + Tier3_usage

        Tier4_usage = 500000
        Tier4_price = .0308
        Tier4_limit = Tier3_limit + Tier4_usage

        Tier5_usage = 4000000
        Tier5_price = .0303
        Tier5_limit = Tier4_limit + Tier5_usage

        Tier6_usage = 5000000
        Tier6_price = .0297
        Tier6_limit = Tier5_limit + Tier6_usage
    
    elif region == 'sing':
>>>>>>> 969544c267e05418cdedaff069a4c381fcc732ba
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
    
<<<<<<< HEAD
    elif region == toky:
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
    
    elif region == sydn:
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
    
    elif region == seou:
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
    
    elif region == saop:
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
    
    else:
        print("""Please enter a valid region:
=======
    elif region == 'toky':
        Tier1_usage = 1000
        Tier1_price = .033
        Tier1_limit = Tier1_usage
    
        Tier2_usage = 49000
        Tier2_price = .0324
        Tier2_limit = Tier1_limit + Tier2_usage

        Tier3_usage = 450000
        Tier3_price = .0319
        Tier3_limit = Tier2_limit + Tier3_usage

        Tier4_usage = 500000
        Tier4_price = .0313
        Tier4_limit = Tier3_limit + Tier4_usage

        Tier5_usage = 4000000
        Tier5_price = .0308
        Tier5_limit = Tier4_limit + Tier5_usage

        Tier6_usage = 5000000
        Tier6_price = .0302
        Tier6_limit = Tier5_limit + Tier6_usage
    
    elif region == 'sydn':
        Tier1_usage = 1000
        Tier1_price = .033
        Tier1_limit = Tier1_usage
    
        Tier2_usage = 49000
        Tier2_price = .0324
        Tier2_limit = Tier1_limit + Tier2_usage

        Tier3_usage = 450000
        Tier3_price = .0319
        Tier3_limit = Tier2_limit + Tier3_usage

        Tier4_usage = 500000
        Tier4_price = .0313
        Tier4_limit = Tier3_limit + Tier4_usage

        Tier5_usage = 4000000
        Tier5_price = .0308
        Tier5_limit = Tier4_limit + Tier5_usage

        Tier6_usage = 5000000
        Tier6_price = .0302
        Tier6_limit = Tier5_limit + Tier6_usage
    
    elif region == 'seou':
        Tier1_usage = 1000
        Tier1_price = .0314
        Tier1_limit = Tier1_usage
    
        Tier2_usage = 49000
        Tier2_price = .0308
        Tier2_limit = Tier1_limit + Tier2_usage

        Tier3_usage = 450000
        Tier3_price = .0303
        Tier3_limit = Tier2_limit + Tier3_usage

        Tier4_usage = 500000
        Tier4_price = .0297
        Tier4_limit = Tier3_limit + Tier4_usage

        Tier5_usage = 4000000
        Tier5_price = .0293
        Tier5_limit = Tier4_limit + Tier5_usage

        Tier6_usage = 5000000
        Tier6_price = .0287
        Tier6_limit = Tier5_limit + Tier6_usage
    
    elif region == 'saop':
        Tier1_usage = 1000
        Tier1_price = .0408
        Tier1_limit = Tier1_usage
    
        Tier2_usage = 49000
        Tier2_price = .0401
        Tier2_limit = Tier1_limit + Tier2_usage

        Tier3_usage = 450000
        Tier3_price = .0394
        Tier3_limit = Tier2_limit + Tier3_usage

        Tier4_usage = 500000
        Tier4_price = .0387
        Tier4_limit = Tier3_limit + Tier4_usage

        Tier5_usage = 4000000
        Tier5_price = .0380
        Tier5_limit = Tier4_limit + Tier5_usage

        Tier6_usage = 5000000
        Tier6_price = .0374
        Tier6_limit = Tier5_limit + Tier6_usage
    
    else:
        print("""Region {} was not recognized. Please enter a valid region:
>>>>>>> 969544c267e05418cdedaff069a4c381fcc732ba
        oreg = US West - Oregon
        cali = US West - California
        irel = EU - Ireland
        fran = EU - Frankfurt
        sing = Asia Pacific - Singapore
        toky = Asia Pacific - Tokyo
        sydn = Asia Pacific - Sydney
        seou = Asia Pacific - Seoul
        saop = South America - Sao Paulo
<<<<<<< HEAD
         """)
=======
         """.format(region))
>>>>>>> 969544c267e05418cdedaff069a4c381fcc732ba
    
    #Calculate cost based on usage
        
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

<<<<<<< HEAD

print(s3Price_East_Standard(500))
print(s3Price_East_Standard(2000))
print(s3Price_East_Standard(300000))
print(s3Price_East_Standard(725000))
print(s3Price_East_Standard(2398000))
print(s3Price_East_Standard(8340000))
=======
try:
    print(s3Price_Standard(500, 'oreg'))
    print(s3Price_Standard(2, 'irel'))
    print(s3Price_Standard(2000, 'irel'))
    print(s3Price_Standard(300000, 'toky'))
    print(s3Price_Standard(725000, 'cali'))
    print(s3Price_Standard(2398000, 'saop'))
    print(s3Price_Standard(8340000, 'cali'))        
    print(s3Price_Standard(8340000, 'soap'))        
except Exception:
    print("Hmm, something went wrong, probably with the values supplied. Check the docstring for guidance.")
>>>>>>> 969544c267e05418cdedaff069a4c381fcc732ba
