def calculate_production_time(quantity, minutes_per_garment, workers, efficiency):
    total_work_minutes = quantity * minutes_per_garment
    theoretical_minutes = total_work_minutes / workers
    actual_minutes = theoretical_minutes / (efficiency/100)
    actual_hours = actual_minutes / 60
    return actual_hours


print("!! Garment Production Time Estimator!!")
quantity = int(input("enter the quantity:"))
minutes_per_garment = float(input("Enter the minutes per garment:"))
workers = int(input("Enter the number of workers:"))
efficiency = float(input("Enter the efficiency percentage:"))


production_time = calculate_production_time(quantity, minutes_per_garment, workers, efficiency)
print("\nEstimated production time:",round(production_time, 2), "hours")
  # Assuming 8 hours workday