import numpy as np

mat = np.array([[2.2,1.7],[5.1,6.3],[7.2,1.2]])
mat.ndim

# ****************
mat = np.array([[[[[[2.2,1.7],[5.1,6.3],[7.2,1.2]],[[2.2,1.7],[5.1,6.3],[7.2,1.2]]]]]])
mat.ndim
mat.shape

# ***************************
np.empty(4, dtype=int)

# ************************
np.eye(5,6)

# ************************
tab1 = np.arange(10)
tab2 = tab1.reshape(2, 5)
print("tab2 : \n", tab2)

# ************************
arr = np.array([])
arr.shape
