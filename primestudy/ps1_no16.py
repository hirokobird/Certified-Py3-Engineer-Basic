# 16

def shop(name, *arguments, **keywords):
    print("flowershop:", name)
    for arg in arguments:
        print(arg)
    print("**Recommended**")
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

shop(
    "Iris", 
    "Open: 9:30am", "Close: 10:30 pm", "Monday and holidays are closed.", 
    bouquet="Sunflower", plants="Pachira", dried="Rose"
    )

