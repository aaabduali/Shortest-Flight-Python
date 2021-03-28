import numpy as np
import pandas as pd

routes=np.fromfile('routes.dat')
df=pd.DataFrame(routes)
print(df.head())