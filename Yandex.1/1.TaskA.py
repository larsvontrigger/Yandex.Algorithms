temp_room = int(input("What's temperature in your room?: "))
temp_want = int(input("What's temperature do you want?: "))
mode = input("What's mode do you want to choose?: ").lower()
freeze_temp = 0
heat_temp = 0
if mode == "freeze":
    if temp_room >= temp_want:
        freeze_temp = temp_want
    else:
        freeze_temp = temp_room
    print(freeze_temp)
if mode == "heat":
    if temp_room <= temp_want:
        heat_temp = temp_want
    else:
        heat_temp = temp_room
    print(heat_temp)
if mode == "auto":
    print(temp_want)
if mode == "fan":
    print(temp_room)

