# From -> From where we want to import
# calcuelate_ten/twenty -> Especific Functions Imported
from finance.functions import calculate_ten, calculate_twenty
from finance.functions import define_as as renamed_function


value_ten = calculate_ten(10)
value_twenty = calculate_twenty(20)
value_rename = renamed_function()

print(f"First Price: {value_ten} | Second Price: {value_twenty}")
print(f"Renamed function {value_rename}")
