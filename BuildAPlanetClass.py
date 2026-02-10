class Planet:
    def __init__(self, name, planet_type, star):
        if not (isinstance(name, str) and isinstance(planet_type, str) and isinstance(star, str)):
            raise TypeError("name, planet type, and star must be strings")
        elif len(name) == 0 or len(planet_type) == 0 or len(star) == 0:
            raise ValueError("name, planet_type, and star must be non-empty strings")
        else:
            self.name = name
            self.planet_type = planet_type
            self.star = star

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


planet3 = Planet('Neptune', 'ice giant', 'Sun')
print(planet3.name)
print(planet3.orbit())
print(str(planet3))

planet1 = Planet('Earth', '', 'Sun')
planet2 = Planet('Jupiter', 9, 'Sun')