piece_snowball = int(input())
# Best Snowball Data
best_weight = best_time = best_quality = best_calc = 0

for snowball in range(piece_snowball):
    weight_of_snowball = int(input())
    time_of_snowball = int(input())
    quality_of_snowball = int(input())

    calculation = (weight_of_snowball / time_of_snowball) ** quality_of_snowball
    if calculation > best_calc:
        best_weight = weight_of_snowball
        best_time = time_of_snowball
        best_quality = quality_of_snowball
        best_calc = int(calculation)


print(f"{best_weight} : {best_time} = {best_calc} ({best_quality})")

