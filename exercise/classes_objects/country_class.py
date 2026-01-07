class Country:
    def __init__(self, name: str, population: int, area: int) -> None:
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, Other) -> bool:
        """ return true iff country has large area than second"""

        return self.area > Other.area

    def population_density(self) -> int:
        pop_density = self.population / self.area
        return pop_density

    def __str__(self) -> str:
        return "{} has a population of {} and is {} square km".format(
            self.name, self.population, self.area)

    def __repr__(self) -> str:
        return "{} ('{}', {}, {})".format(self.name, self.name, self.population, self.area)
