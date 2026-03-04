def resistor_label(colors):
    digit = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    tolerance = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%",
    }

    def format_ohms(value):
        units = [
            (1_000_000_000, "gigaohms"),
            (1_000_000, "megaohms"),
            (1_000, "kiloohms"),
            (1, "ohms"),
        ]
        for factor, name in units:
            if value >= factor:
                scaled = value / factor
                if scaled.is_integer():
                    return f"{int(scaled)} {name}"
                return f"{scaled:g} {name}"
        return "0 ohms"

    # 1-band resistor
    if len(colors) == 1:
        if colors[0] != "black":
            raise ValueError("One-band resistor must be black.")
        return "0 ohms"

    # 4-band resistor: D1 D2 Multiplier Tolerance
    if len(colors) == 4:
        significant = digit[colors[0]] * 10 + digit[colors[1]]
        multiplier = digit[colors[2]]
        tol = tolerance[colors[3]]

    # 5-band resistor: D1 D2 D3 Multiplier Tolerance
    elif len(colors) == 5:
        significant = (
            digit[colors[0]] * 100
            + digit[colors[1]] * 10
            + digit[colors[2]]
        )
        multiplier = digit[colors[3]]
        tol = tolerance[colors[4]]

    else:
        raise ValueError("Resistor must have 1, 4, or 5 bands.")

    value = significant * (10 ** multiplier)
    return f"{format_ohms(value)} ±{tol}"

 
    

        

