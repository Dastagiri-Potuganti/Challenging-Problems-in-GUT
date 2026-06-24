'''
8.A bike starts with 20 litres of fuel.
Every trip consumes some fuel.
Input trip consumptions until fuel becomes 0 or less.
print:
Total trips completed
Remaining fuel'''
fuel=int(input("Enter total fuel:"))
trips_count=0
'''while True:
    trip_fuel=int(input("Enter fuel consumed in this trip:"))
    if trip_fuel<fuel:
        trips_count+=1
        fuel-=trip_fuel
    else:
        print("Total Trips Completed:",trips_count)
        print("Fuel Empty")
        break'''
fuel_consumed=0
while True:
    trip_fuel=int(input("Enter fuel consumed in this trip:"))
    fuel_consumed+=trip_fuel
    if fuel_consumed>20:
        print("Total Trips Completed:",trips_count)
        print("Fuel Empty")
        break
    trips_count+=1
    