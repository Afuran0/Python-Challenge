import csv
from pathlib import Path


csv_path = Path("budget_data.csv")

total_months = 0
net_total_profit_losses = 0
previous_profit_loss = None
changes = []
dates = []
greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}


with open(csv_path, mode='r') as f:
    csv_reader = csv.DictReader(f)
    
   
    for row in csv_reader:
        total_months += 1
        current_profit_loss = int(row['Profit/Losses'])  
        net_total_profit_losses += current_profit_loss

        
        if previous_profit_loss is not None:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = row['Date']
                greatest_increase["amount"] = change
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = row['Date']
                greatest_decrease["amount"] = change

        previous_profit_loss = current_profit_loss
        dates.append(row['Date'])


average_change = sum(changes) / len(changes) if changes else 0


analysis = (
    f"Financial Analysis\n"
    f"-------------------------------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total Profit/Loss: ${net_total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)


print(analysis)

with open("financial_analysis.txt", mode='w') as file:
    file.write(analysis)
                                             
