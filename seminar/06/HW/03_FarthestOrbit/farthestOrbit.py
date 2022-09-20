# Найти орбиту самой далёкой планеты, движущейся по эллиптической траектории

from os import system
from math import pi

def find_farthest_orbit (list_of_orbits):
	list_of_elliptical_orbits = [i for i in list_of_orbits if i[0] != i[1]]
	list_of_areas = [(pi * i[0] * i[1]) for i in list_of_elliptical_orbits]
	max_area_index = list_of_areas.index(max(list_of_areas))
	return list_of_elliptical_orbits[max_area_index]

system('cls')

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(*find_farthest_orbit(orbits))
