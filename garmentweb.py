import streamlit as st_instance
def calculate_production_time(quantity, minutes_per_garment, workers, efficiency):
    total_work_minutes = quantity * minutes_per_garment
    theoretical_minutes = total_work_minutes / workers
    actual_minutes = theoretical_minutes / (efficiency/100)
    actual_hours = actual_minutes / 60
    return actual_hours


st_instance.title("Garment Production Time Estimator!!")

quantity = st_instance.number_input("Enter the quantity:", min_value=0)
minutes_per_garment = st_instance.number_input("Enter the minutes per garment:", min_value=0.1)
workers = st_instance.number_input("Enter the number of workers:", min_value=0)
efficiency = st_instance.number_input("Enter the efficiency in percentage:", min_value=0.1)

if st_instance.button("Calculate"):
    production_time = calculate_production_time(quantity, minutes_per_garment, workers, efficiency)
    st_instance.write("Estimated production time:",round(production_time, 2), "hours")
    