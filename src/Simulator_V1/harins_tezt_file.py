import numpy as np
import car_gen
import a_star
# import pygame

s,g = car_gen.main()
path = a_star.main(s,g)