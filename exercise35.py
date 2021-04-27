# Exercise 35

import json
from collections import Counter


filename = "info.json"

def open_file(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def return_months(data):
    list_of_dates = []
    for i in data:
        list_of_dates.append(data[i])
    months = []
    for j in list_of_dates:
        day, month, year = j.split("/", 3)
        months.append(month)
    return months


def convert_months_to_string(months_list):
    for i in range(0, len(months_list)):
        if months_list[i] == "01":
            months_list[i] = "January"
        if months_list[i] == "02":
            months_list[i] = "February"
        if months_list[i] == "03":
            months_list[i] = "March"
        if months_list[i] == "04":
            months_list[i] = "April"
        if months_list[i] == "05":
            months_list[i] = "May"
        if months_list[i] == "06":
            months_list[i] = "June"
        if months_list[i] == "07":
            months_list[i] = "July"
        if months_list[i] == "08":
            months_list[i] = "August"
        if months_list[i] == "09":
            months_list[i] = "September"
        if months_list[i] == "10":
            months_list[i] = "October"
        if months_list[i] == "11":
            months_list[i] = "November"
        if months_list[i] == "12":
            months_list[i] = "December"
    return months_list


def month_counter(month_string):
    c = Counter(month_string)
    return c

def main():
    data = open_file(filename)
    months_numerical = return_months(data)
    print(months_numerical)
    months_string = convert_months_to_string(months_numerical)
    print(months_string)
    counts = month_counter(months_string)
    print(counts)


if __name__ == "__main__":
    main()
