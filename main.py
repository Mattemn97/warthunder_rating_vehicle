import vehicle
import utility

vehicles = [
    vehicle.Vehicle("Tiger I", 45, 203, 14, [100, 80, 80], 8, -8, 15, 6.5, 700, 57, 92, 4),
    vehicle.Vehicle("Sherman", 38, 135, 20, [63, 38, 38], 10, -10, 25, 5.0, 450, 33, 97, 4),
    vehicle.Vehicle("Panther", 55, 198, 15, [80, 50, 40], 7.5, -5, 20, 7.1, 700, 45, 79, 4),
    vehicle.Vehicle("T-34", 53, 115, 24, [45, 45, 40], 12, -6, 22, 4.5, 500, 30, 100, 4),
    vehicle.Vehicle("KV-1", 35, 85, 10, [75, 75, 70], 6, -3, 20, 8.0, 500, 48, 50, 4)
]

ranked_vehicles = utility.rank_vehicles(vehicles)

for vehicle in ranked_vehicles:
    print(vehicle)

url = "https://wiki.warthunder.com/AB_41"
vehicle = utility.scrape_vehicle_data(url)

if vehicle:
    print(vehicle)
else:
    print("Veicolo non trovato o errore nel parsing.")
