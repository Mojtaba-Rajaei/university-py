
class Color:
    RED = "red"
    BLUE = "blue"
    GREEN = "green"

color = input("what is your color:")

match color:
    case Color.RED:
        print("Color is Red")
    case Color.BLUE:
        print("Color is Blue")
    case Color.GREEN:
        print("Color is Green")
    case _:
        raise ValueError("There is nothing")
    