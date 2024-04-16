
import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    t = np.arange(1, m + 1)
    coupon = face * couponRate / ppy
    
    pv_cf = np.array([(coupon / ((1 + y/ppy) ** (t_i * ppy))) for t_i in t[:-1]])
    pv_cf = np.append(pv_cf, (coupon + face) / ((1 + y/ppy) ** (m * ppy))) 
    
    duration = np.sum(t * pv_cf) / np.sum(pv_cf)
    
    return duration
