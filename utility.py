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

        # Ranking per rapporto potenza/peso (più alto è migliore)
        era_vehicles.sort(key=lambda v: v.power_to_weight_ratio, reverse=True)
        for i, vehicle in enumerate(era_vehicles):
            vehicle.ratings[8] = i + 1

        # Ranking per capacità di munizioni (più alto è migliore)
        era_vehicles.sort(key=lambda v: v.ammunition_capacity, reverse=True)
        for i, vehicle in enumerate(era_vehicles):
            vehicle.ratings[9] = i + 1

    return vehicles

def scrape_vehicle_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Nome del veicolo
    name = soup.find('h1', {'id': 'firstHeading'}).text.strip()

    # Dati del veicolo
    # Estrazione dei dati specifici dalla pagina HTML
    try:
        stats_table = soup.find('table', {'class': 'wikitable'})
        rows = stats_table.find_all('tr')

        # Dizionario per i dati estratti
        data = {
            'speed': None,
            'penetration': None,
            'turret_rotation_speed': None,
            'armor_thickness': None,
            'rate_of_fire': None,
            'gun_depression': None,
            'gun_elevation': None,
            'reload_time': None,
            'power_to_weight_ratio': None,
            'ammunition_capacity': None
        }

        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:
                label = cols[0].get_text(strip=True).lower()
                value = cols[1].get_text(strip=True)
                if 'speed' in label:
                    data['speed'] = float(value.split()[0])
                elif 'penetration' in label:
                    data['penetration'] = float(value.split()[0])
                elif 'turret rotation' in label:
                    data['turret_rotation_speed'] = float(value.split()[0])
                elif 'armor' in label:
                    data['armor_thickness'] = [float(x) for x in value.split('/') if x]
                elif 'rate of fire' in label:
                    data['rate_of_fire'] = float(value.split()[0])
                elif 'gun depression' in label:
                    data['gun_depression'] = float(value.split()[0])
                elif 'gun elevation' in label:
                    data['gun_elevation'] = float(value.split()[0])
                elif 'reload time' in label:
                    data['reload_time'] = float(value.split()[0])
                elif 'power-to-weight ratio' in label:
                    data['power_to_weight_ratio'] = float(value.split()[0])
                elif 'ammunition capacity' in label:
                    data['ammunition_capacity'] = int(value.split()[0])

        # Supponiamo un'era fittizia per il veicolo (può essere cambiata come richiesto)
        era = 4

        vehicle = Vehicle(
            name,
            data['speed'],
            data['penetration'],
            data['turret_rotation_speed'],
            data['armor_thickness'],
            data['rate_of_fire'],
            data['gun_depression'],
            data['gun_elevation'],
            data['reload_time'],
            data['power_to_weight_ratio'],
            data['ammunition_capacity'],
            era
        )

        return vehicle
    except Exception as e:
        print(f"Errore nel parsing della pagina: {e}")
        return None
