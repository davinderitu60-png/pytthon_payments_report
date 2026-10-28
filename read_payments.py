
import csv

total = 0
count = 0
largest = 0
smallest = None
target_reached = 0
below_target = 0

with open("payments.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        customer = row["customer"].strip().title()
        payment = float(row["payment"])

        total += payment
        count += 1

        if count == 1 or payment > largest:
            largest = payment

        if smallest is None or payment < smallest:
            smallest = payment

        if payment >= 1000:
            target_reached += 1
        else:
            below_target += 1

        print(f"{customer} - KSh {payment:.2f}")

if count > 0:
    average = total / count
else:
    average = 0

report_lines = [

    "       PAYMENT SUMMARY",
    
    f"Total payments: KSh {total:.2f}",
    f"Number of payments: {count}",
    f"Largest payment: KSh {largest:.2f}",
    f"Smallest payment: KSh {smallest:.2f}" if smallest is not None
    else "Smallest payment: No payments available",
    f"Average payment: KSh {average:.2f}",
    f"Payments reaching KSh 1,000: {target_reached}",
    f"Payments below KSh 1,000: {below_target}",
  
]

print("\n" + "\n".join(report_lines))

with open("payment_summary.txt", "w") as report:
    report.write("\n".join(report_lines) + "\n")

print("\nReport saved to payment_summary.txt")
