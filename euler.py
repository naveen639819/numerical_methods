#Euler method

def euler_method():
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
        u_new = u + h * du_dt(u, v)
        v_new = v + h * dv_dt(u, v)
        u = u_new
        v = v_new
        x += h
        print(f'When x={x:.7f}, u={u:.7f}, v={v:.7f}')
euler_method()