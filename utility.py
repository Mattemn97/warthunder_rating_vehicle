def rank_vehicles(vehicles):
    # Filtriamo i veicoli per ciascuna era
    eras = set(vehicle.era for vehicle in vehicles)
    
    for era in eras:
        era_vehicles = [vehicle for vehicle in vehicles if vehicle.era == era]

        # Ranking per velocità (più alto è migliore)
        era_vehicles.sort(key=lambda v: v.speed, reverse=True)
        for i, vehicle in enumerate(era_vehicles):
            vehicle.ratings[0] = i + 1

        # Ranking per penetrazione (più alto è migliore)
        era_vehicles.sort(key=lambda v: v.penetration, reverse=True)
        for i, vehicle in enumerate(era_vehicles):
            vehicle.ratings[1] = i + 1

        # Ranking per velocità di rotazione della torretta (più alto è migliore)
        era_vehicles.sort(key=lambda v: v.turret_rotation_speed, reverse=True)
        for i, vehicle in enumerate(era_vehicles):
            vehicle.ratings[2] = i + 1

        # Ranking per spessore dell'armatura (più alto è migliore, quindi sommiamo gli spessori)
        era_vehicles.sort(key=lambda v: sum(v.armor_thickness), reverse=True)
        for i, vehicle in enumerate(era_vehicles):
            vehicle.ratings[3] = i + 1

        # Ranking per tasso di fuoco (più alto è migliore)
        era_vehicles.sort(key=lambda v: v.rate_of_fire, reverse=True)
        for i, vehicle in enumerate(era_vehicles):
            vehicle.ratings[4] = i + 1

        # Ranking per depressione del cannone (più basso è migliore, negativo è migliore)
        era_vehicles.sort(key=lambda v: v.gun_depression)
        for i, vehicle in enumerate(era_vehicles):
            vehicle.ratings[5] = i + 1

        # Ranking per elevazione del cannone (più alto è migliore)
        era_vehicles.sort(key=lambda v: v.gun_elevation, reverse=True)
        for i, vehicle in enumerate(era_vehicles):
            vehicle.ratings[6] = i + 1

        # Ranking per tempo di ricarica (più basso è migliore)
        era_vehicles.sort(key=lambda v: v.reload_time)
        for i, vehicle in enumerate(era_vehicles):
            vehicle.ratings[7] = i + 1

        # Ranking per potenza del motore (più alto è migliore)
        era_vehicles.sort(key=lambda v: v.engine_power, reverse=True)
        for i, vehicle in enumerate(era_vehicles):
            vehicle.ratings[8] = i + 1

        # Ranking per peso (più basso è migliore)
        era_vehicles.sort(key=lambda v: v.weight)
        for i, vehicle in enumerate(era_vehicles):
            vehicle.ratings[9] = i + 1

        # Ranking per capacità di munizioni (più alto è migliore)
        era_vehicles.sort(key=lambda v: v.ammunition_capacity, reverse=True)
        for i, vehicle in enumerate(era_vehicles):
            vehicle.ratings[10] = i + 1

    return vehicles
