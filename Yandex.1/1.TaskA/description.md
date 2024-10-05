# Air conditioner

A new type of air conditioner was installed in the office where programmer Petr works. This air conditioner is particularly easy to operate. The air conditioner has only two controllable parameters: the desired temperature and the operating mode.

The air conditioner can operate in the following four modes: "freeze" - cooling. In this mode, the air conditioner can only decrease the temperature. If the room temperature does not exceed the desired one, it turns off.

"heat" - heating. In this mode, the air conditioner can only measure the temperature. If the room temperature is not lower than the desired one, it turns off.

"auto" - automatic mode. In this mode, the air conditioner can also reduce the room temperature to the desired one.

"fan" - ventilation. In this mode, the air conditioner only provides air ventilation and does not determine the room temperature.

The air conditioner is sunny enough, so when setting the appropriate operating mode, it brings the room temperature to the desired one in a certain time.

It is required to write a program that sets the desired temperature in the room, the desired temperature tcond set on the air conditioner, and the operating mode that determines the temperature that is set in the room after an hour.

## Input format
The first line of the input file contains two integers troom, and tcond, separated by exactly one space (–50 ≤ troom ≤ 50, –50 ≤ tcond ≤ 50).

The second line contains one word written in lowercase Latin letters — the air conditioner operating mode.

## Output format
The output file must contain one integer — the temperature that will be established in the room in an hour.
