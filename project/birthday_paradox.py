""" Birthday paradox simulation,
explore the suprising possibilites of the birthday paradox
"""

import datetime
import random


def getBirthdays(numberOfBirthdays):
    """ returns a list of no random date objects for birthdays..."""
    birthdays = []

    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001,  1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """ returns the date object of a birthday that occurs more than once
    in the birthday list. """
    if len(birthdays) == len(set(birthdays)):
        return None  # all birthdays are unique, so return None

    # compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA  # return the matching birthday


# display the intro
print(""" the birthday paradox shows us that in a group of N people, the odds
      that two people have matching birthdays is surprsingly large.
      this program does a monte carlo simulation (repeated random simulation)
      to explore this concept""")

MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


def getUserInput() -> int:
    while True:
        print("how many birthdays shall I generate? max 100)")
        response = input("> ")
        if response.isdecimal() and (0 < int(response) <= 100):
            numBDays = int(response)
            break
    return numBDays


def birth_days_text(numBDays) -> None:
    print("here are", numBDays, "birthdays:")
    birthdays = getBirthdays(numBDays)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            # display a comman for each birthday after the first birthday
            print(", ", end="")

        monthName = MONTHS[birthday.month - 1]
        dateText = "{} {}".format(monthName, birthday.day)
        print(dateText, end="")
    print()


# display the results:
def display_result():
    match = getMatch(getBirthdays(numBDays))
    print("in this simulation, ", end="")
    if match is not None:
        monthName = MONTHS[match.month - 1]
        dateText = "{} {}".format(monthName, match.day)
        print("mutliple people have a birthday on", dateText)
    else:
        print("there are no matching birthdays.")
    print()


def runSimulation():
    print("Generating", numBDays, "random birthdays 100,000 times...")
    input("Press enter to begin...")
    print("lets run another 100,000 sims")
    simMatch = 0
    for i in range(100_000):
        if i % 10_000 == 0:
            print(i, "simulations run....")
        birthdays = getBirthdays(numBDays)
        if getMatch(birthdays) is not None:
            simMatch += 1
    print(simMatch)
    print("100,000 simulations run")
    return simMatch


def probability(outcomes) -> float:
    return round(outcomes / 100_000 * 100, 2)


if __name__ == "__main__":
    numBDays = getUserInput()
    birth_days_text(numBDays)
    display_result()
    simMatch = runSimulation()
    print("out of 100,000 simulations of", numBDays, "people, there was a")
    print("matching birthday in that group", simMatch, "times. This means")
    print("that", numBDays, "people have a", probability(simMatch), "% chance of")
    print("having a matching birthday in their group.")
    print("that's probably more than you would think!")
