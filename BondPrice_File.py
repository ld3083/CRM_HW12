import numpy as np

def getBondPrice(y, face, couponRate, m, ppy):
    n = m * ppy
    r = y / ppy
    periods = np.arange(1, n + 1)
    coupon_payment = face * couponRate / ppy
    coupons_pv = coupon_payment / ((1 + r) ** periods)
    face_pv = face / ((1 + r) ** n)
    bond_price = np.sum(coupons_pv) + face_pv
    return bond_price

