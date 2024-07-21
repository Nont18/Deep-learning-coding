calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days*calculation_to_hours} {name_of_unit}")
    print(custom_message)


# print(f"20 days are {20*calculation_to_seconds} seconds")
# print(f"35 days are {35*24*60} seconds")
# print(f"50 days are {50*24*60} seconds")
# print(f"110 days are {110*24*60} seconds")

days_to_units(20, "Awesome!")
days_to_units(35, "Looks good!")