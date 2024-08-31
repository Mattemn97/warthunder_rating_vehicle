class Vehicle:
    def __init__(self, name, speed, penetration, turret_rotation_speed, armor_thickness, rate_of_fire,
                 gun_depression, gun_elevation, reload_time, engine_power, weight, ammunition_capacity, era):
        self.name = name  # Nome del veicolo
        self.speed = speed  # Velocità massima in km/h
        self.penetration = penetration  # Penetrazione massima in mm
        self.turret_rotation_speed = turret_rotation_speed  # Velocità di rotazione della torretta in gradi/s
        self.armor_thickness = armor_thickness  # Spessore dell'armatura in mm (lista per diverse parti)
        self.rate_of_fire = rate_of_fire  # Tasso di fuoco in colpi/min
        self.gun_depression = gun_depression  # Depressione del cannone in gradi
        self.gun_elevation = gun_elevation  # Elevazione del cannone in gradi
        self.reload_time = reload_time  # Tempo di ricarica in secondi
        self.engine_power = engine_power  # Potenza del motore in hp
        self.weight = weight  # Peso del veicolo in tonnellate
        self.ammunition_capacity = ammunition_capacity  # Capacità di munizioni (numero di colpi)
        self.era = era  # Epoca storica del veicolo (da 1 a 8)
        
        # Lista delle posizioni nel rating del veicolo in ciascun ambito (esclusa l'era)
        self.ratings = [None] * 11  # Inizialmente, tutti i rating sono impostati su None

    def set_ratings(self, speed_rank, penetration_rank, turret_rotation_rank, armor_rank, rate_of_fire_rank, 
                    gun_depression_rank, gun_elevation_rank, reload_time_rank, engine_power_rank, weight_rank, 
                    ammunition_capacity_rank):
        self.ratings = [
            speed_rank,  # Posizione nel ranking per la velocità
            penetration_rank,  # Posizione nel ranking per la penetrazione
            turret_rotation_rank,  # Posizione nel ranking per la rotazione della torretta
            armor_rank,  # Posizione nel ranking per l'armatura
            rate_of_fire_rank,  # Posizione nel ranking per il tasso di fuoco
            gun_depression_rank,  # Posizione nel ranking per la depressione del cannone
            gun_elevation_rank,  # Posizione nel ranking per l'elevazione del cannone
            reload_time_rank,  # Posizione nel ranking per il tempo di ricarica
            engine_power_rank,  # Posizione nel ranking per la potenza del motore
            weight_rank,  # Posizione nel ranking per il peso
            ammunition_capacity_rank  # Posizione nel ranking per la capacità di munizioni
        ]

    def __repr__(self):
        return (f"{self.name} (Era {self.era}):\n"
                f" - Velocità: {self.speed} km/h (Posizione nel rating: {self.ratings[0]})\n"
                f" - Penetrazione: {self.penetration} mm (Posizione nel rating: {self.ratings[1]})\n"
                f" - Rotazione torretta: {self.turret_rotation_speed} °/s (Posizione nel rating: {self.ratings[2]})\n"
                f" - Armatura: {self.armor_thickness} mm (Posizione nel rating: {self.ratings[3]})\n"
                f" - Tasso di fuoco: {self.rate_of_fire} colpi/min (Posizione nel rating: {self.ratings[4]})\n"
                f" - Depressione cannone: {self.gun_depression} ° (Posizione nel rating: {self.ratings[5]})\n"
                f" - Elevazione cannone: {self.gun_elevation} ° (Posizione nel rating: {self.ratings[6]})\n"
                f" - Tempo di ricarica: {self.reload_time} s (Posizione nel rating: {self.ratings[7]})\n"
                f" - Potenza motore: {self.engine_power} hp (Posizione nel rating: {self.ratings[8]})\n"
                f" - Peso: {self.weight} t (Posizione nel rating: {self.ratings[9]})\n"
                f" - Capacità munizioni: {self.ammunition_capacity} colpi (Posizione nel rating: {self.ratings[10]})\n")
