# Subway

At some cross-platform metro stations (like 
Tretyakovskaya), trains from different directions arrive 
at different sides of the platform. Tanya had arranged to 
meet her friend at such a station, but since her friend 
was from a different time zone, she overslept due to jet 
lag, and Tanya had to wait for her for a long time. 
Trains always run exactly on schedule, and Tanya knows 
that the train stands on the platform for exactly one 
minute, and the interval between trains (the time during 
which there is no train at the platform) is a minutes for 
trains on the first track and b minutes for trains on the 
second track. That is, a train arrives on the first track 
and stands for one minute, then there is no train at the 
platform for a minute, then the next train stands at the 
platform for one minute, and so on.



While Tanya was standing on the platform, she counted n 
trains on the first track and m trains on the second 
track. Determine the minimum and maximum time that Tanya 
could have spent on the platform, or say that she 
definitely lost count.



All the trains that Tanya saw, she observed during the 
entire minute, that is, Tanya does not come or leave the 
platform in the middle of the minute when the train is 
standing on the platform.

## Input format

The first line of the input data contains the number a — 
the interval between trains on the first track. The 
second line contains the number b — the interval between 
trains on the second track. The third line contains the 
number n — the number of trains on the first track that 
Tanya saw. The fourth line contains the number m — the 
number of trains on the second track that Tanya saw. All 
numbers are integers, from 1 to 1000.

## Output format

The program should output two numbers: the minimum and 
maximum time in minutes that Tanya could have stood on 
the platform, or one number -1, if Tanya was definitely 
wrong.
