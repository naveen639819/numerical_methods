def runge_kutta_method():
    def du_dt(u, v):
        return -3 * u + 2 * v
    def dv_dt(u, v):
        return 3 * u - 4 * v
    u0 = 0.0
    v0 = 0.5
    h = 0.2
    x_target = 1.0  
    x = 0.0
    u = u0
    v = v0
    print(f'When x={x:.2f}, u={u:.2f}, v={v:.2f}')
    while x < x_target:
        k1_u = h * du_dt(u, v)
        k1_v = h * dv_dt(u, v)
        k2_u = h * du_dt(u + 0.5 * k1_u, v + 0.5 * k1_v)
        k2_v = h * dv_dt(u + 0.5 * k1_u, v + 0.5 * k1_v)
        k3_u = h * du_dt(u + 0.5 * k2_u, v + 0.5 * k2_v)
        k3_v = h * dv_dt(u + 0.5 * k2_u, v + 0.5 * k2_v)
        k4_u = h * du_dt(u + k3_u, v + k3_v)
        k4_v = h * dv_dt(u + k3_u, v + k3_v)
        u += (k1_u + 2 * k2_u + 2 * k3_u + k4_u) / 6
        v += (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6
        x += h
        print(f'When x={x:.7f}, u={u:.7f}, v={v:.7f}')

runge_kutta_method()
