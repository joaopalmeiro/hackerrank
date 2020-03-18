# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import acos, pi, sqrt

AB = int(input())
BC = int(input())

AC = sqrt((AB**2 + BC**2))

MC = MB = AC / 2.0

# Law of Cosines
angle = acos((MB**2 + BC**2 - MC**2) / (2 * MB * BC))

angle = int(round((180 * angle) / pi))

print(f"{angle}°")
