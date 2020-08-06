#!/usr/bin/env python3

import locale as lc

def main():
    print("Sales Report")
    print()

    sales = [[1540.0, 2010.0, 2450.0, 1845.0],  # Region 1
             [1130.0, 1168.0, 1847.0, 1491.0],  # Region 2
             [1580.0, 2305.0, 2710.0, 1284.0],  # Region 3
             [1105.0, 4102.0, 2391.0, 1576.0]]  # Region 4

    head_line = "{:8}{:>12}{:>12}{:>12}{:>12}"
    data_line = "{:<8d}{:12,.2f}{:12,.2f}{:12,.2f}{:12,.2f}"
    
    # print all sales    
    print(head_line.format("Region", "Q1", "Q2", "Q3", "Q4"))
    region_number = 1
    for region in sales:
        q1 = region[0]
        q2 = region[1]
        q3 = region[2]
        q4 = region[3]
        print(data_line.format(region_number, q1, q2, q3, q4))
        region_number += 1
    print()
    
    # print sales by region
    print("Sales by region:")
    region_number = 1
    for region in sales:
        total = 0
        for quarter in region:
            total += quarter
        print("Region " + str(region_number) + ": " +
              "{:,.2f}".format(total))
        region_number += 1
    print()

    # print sales by quarter
    print("Sales by quarter:")
    for quarter in range(4):
        total = 0.0
        for region in range(len(sales)):
            total += sales[region][quarter]
        quarter_number = quarter + 1            
        print("Q" + str(quarter_number) + ": " + 
              "{:,.2f}".format(total))
    print()

    # print the total annual sales
    total = 0.0
    for region in sales:
        for quarter in region:
            total += quarter
    print("Total annual sales, all regions: $" + 
          "{:,.2f}".format(total))

if __name__ == "__main__":
    main()
