
import numpy as np
import scipy.stats as st

#define sample dataa
gfg_data = np.random.randint(5,10,100)

#create 90% confidence interval
# for population mean weight

print(st.norm.interval(confidence=0.90,loc=np.mean(gfg_data),scale=st.msem(gfg_data)))

"""
intervalo para la media poblacional con nivel de confianza de 90%
(6.80039199240999,7.2596080075790015)

"""