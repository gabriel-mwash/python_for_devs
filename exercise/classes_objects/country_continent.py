class Country:
    def __init__(self, name: str, population: int, area: int) -> None:
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
            return "{} {} {}".format(self.name, self.population, self.area)

class Continent:
    def __init__(self, continent_name: str, countries) -> None:
        self.name = continent_name
        self.countries = countries

    def total_population(self) -> int:
        total = 0
        for country in self.countries:
            total = total = country.population
        return total

    def __repr__(self):
        res = self.name
        for country in self.countries:
            res = res + "\n" + str(country)
        return res
