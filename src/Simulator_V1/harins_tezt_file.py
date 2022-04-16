import numpy as np
import car
import a_star

s,g = car.main()
a_star.main(s[0],s[1],g[0],g[1])

# A = np.array([[1,2],[3,4],[5,6],[7,8],[9,0]])
# a_star.main(60,14,17,6)


# x = A[2]
# print(x)