import os
import csv
budget_csv = os.path.join('.','Resources','budget_data.csv')
with open(budget_csv, 'r') as csvfile:
    csvreader =csv.reader(csvfile)
    
    # skip the header row
    next(csvreader)
    folder_name = "Analyses"
    
     # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Define the file path within the folder
    file_path = os.path.join(folder_name, "output.txt")
    file = open(file_path, 'w')
    
    # define the variables
    changes = []
    months = []

    #read through each row of data after header
    for rows in csvreader:
        changes.append(int(rows[1]))
        months.append(rows[0])

    # find revenue change
    revenue_change = []

    for i in range(1, len(changes)):
        revenue_change.append((int(changes[i]) - int(changes[i-1])))
    
    # calculate average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)
    
    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(revenue_change)
    # greatest decrease in revenue
    greatest_decrease = min(revenue_change)


    # print the Results
    print("Financial Analysis")

    print("....................................................................................")

    print(f"Total months: {total_months}")

    print(f"Total: ${sum(changes)}")

    print(f"Average change: ${round(revenue_average,2)}")

    print(f"Greatest Increase in Profits: {months[revenue_change.index(max(revenue_change))+1]} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {months[revenue_change.index(min(revenue_change))+1]} (${greatest_decrease})")


    # creating output strings
    output_string = "Financial Analysis \n" + "....................................................................................\n" + f"Total months: {total_months}\n" +  f"Total: ${sum(changes)}\n" + f"Average change: ${round(revenue_average,2)}\n"
    output_string += f"Greatest Increase in Profits: {months[revenue_change.index(max(revenue_change))+1]} (${greatest_increase})\n" + f"Greatest Decrease in Profits: {months[revenue_change.index(min(revenue_change))+1]} (${greatest_decrease})"


    
    # output to a text file
    file.writelines(output_string)

    
    file.close()

    
    
