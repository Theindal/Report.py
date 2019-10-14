#  File: Report.py
#  Description:
#  Student's Name:
#  Student's UT EID:
#  Course Name: CS 303E 
#  Unique Number: XXXXX
#
#  Date Created:
#  Date Last Modified:

def main():

# input data
    companyName = "Lone Star Corporation"
    date = "October 1, 2019"
    cash = 7505.54
    acctsRec = 502.21
    supplies = 313.89
    land = 6456.23
    buildings = 81598.00
    machAndEquip = 8329.99
    patents = 2000.00
    acctsPay = 93569.23
    stock = 88100.00

    print("LONE STAR CORPORATION".center(40))
    print("October 1, 2019".center(40))
    print("Balance Sheet".center(40))
    print("Liabilities and".rjust(42))
    print("Assets", "Stockholders' Equity".rjust(45))
    print("--------------------------------------------------------------------------------")
    print("Cash".rjust(7),cash,"Liabilities".rjust(39))
    print("Accounts recievable".rjust(22),acctsRec,"Accounts Payable".rjust(33))
    print("Supplies".rjust(11),supplies)
    print("Land".rjust(7),land)
    print("Buildings".rjust(12),buildings,"Stockholders' Equity:".rjust(47))
    print("Machines and Equipment".rjust(25),machAndEquip,"Capital Stock".rjust(29))
    print("Patents".rjust(10),patents)
    print("Total Assets".rjust(7))

main()