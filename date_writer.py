import os
import datetime

with open("/home/robert/airflow/dags/date_file.txt", "a+") as file:
    file.write(str(datetime.datetime.now()) + "\n")

file.close()

print(os.getcwd())