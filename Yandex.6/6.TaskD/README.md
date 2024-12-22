# Space settlement
To explore Mars, it is necessary to build a research 
base. The base must consist of n identical modules, 
each of which is a rectangle.

Each module is a living compartment, which has the 
shape of a rectangle measuring a by b meters. To 
increase the reliability of the modules, engineers 
can add a layer of additional protection around each 
module. The thickness of this layer must be an 
integer number of meters, and all modules must have 
the same thickness of additional protection. A 
module with protection, the thickness of which is 
equal to d meters, will have the shape of a 
rectangle measuring (a + 2d) (b + 2d) meters.

All modules must be located on a pre-prepared 
rectangular field measuring wh meters. At the same 
time, they must be organized in the form of a 
regular grid: their sides must be parallel to the 
sides of the field, and the modules must be oriented 
in the same way.

It is necessary to write a program that, given the 
number and size of modules, as well as the size of 
the field for their placement, determines the 
maximum thickness of the additional protection layer 
that can be added to each module.

## Input format
The input file contains five integers separated by 
spaces: n, a, b, w and h (1 ≤ n, a, b, w, h ≤ 1018). 
It is guaranteed that without additional protection 
all modules can be placed in the settlement as 
described.

## Output format
The output file must contain one integer: the 
maximum possible thickness of additional protection. 
If additional protection cannot be installed, the 
number 0 must be output.