import numpy as np
cupcakes = np.array([2,0.75,2,1,0.5])
recipes = np.genfromtxt('recipes.csv',delimiter=',')
print(recipes)
eggs = recipes[:,2]
print(eggs)
eggs = eggs[eggs==1]
cookies = recipes[3,:]
double_batch = cupcakes * 2
grocery_liat = double_batch + cookies