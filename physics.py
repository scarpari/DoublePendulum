import math
import numpy as np

class dp_physics:

    def __init__(self, g, m, t1, t2, w1, w2, L):
        self.g = g
        self.m = m
        self.t1 = t1  # teta
        self.t2 = t2
        self.L = L  # comprimento das hastes
        self.w1 = w1  # omega
        self.w2 = w2

    def potential_energy(self):
        '''Verificado'''
        g = self.g
        m = self.m
        t1 = self.t1
        t2 = self.t2
        L = self.L

        h1 = -0.5*L*math.cos(t1) # Parametrizando o teto X0 como referencia
        h2 = 2*h1 - 0.5*L*math.cos(t2)
        return m*g*h1 + m*g*h2

    def kinetic_energy_A(self):
        m= self.m
        w1 = self.w1
        L = self.L
        I1 = (m / 12) * (L) ** 2

        return 0.5*m*0.5*0.5*L*L*w1*w1 + 0.5*I1*w1*w1

    def kinetic_energy_B(self):
        m = self.m
        t1 = self.t1
        t2 = self.t2
        L = self.L
        w1 = self.w1
        w2 = self.w2
        I2 = (m/12)*(L)**2
        K2 = 0.5*m*((L*w1)**2 + (0.5*L*w2)**2 + L*L*w1*w2*math.cos(t1 - t2)) + 0.5*I2*w2*w2
        return K2

    def kinetic_energy(self):
        return self.kinetic_energy_A() + self.kinetic_energy_B()

    def mec_energy(self):
        return self.kinetic_energy() + self.potential_energy()

    def double_pendulum_physics(self, t1, t2, w1, w2):
        m = self.m
        L = self.L
        g = self.g
        I1 = (m / 12) * (L) ** 2
        I2 = (m / 12) * (L) ** 2
        c1 = m * 0.5 * 0.5 * 0.5 * L * L + I1 * 0.5 + m * L * L * 0.5
        c2 = m * 0.5 * 0.5 * 0.5 * L * L + I2 * 0.5
        c3 = m * L * L * 0.5
        c4 = g * m * 1.5 * L
        c5 = g * m * 0.5 * L
        aux1 = 2*c2*c4*math.sin(t1) + c3*c3*w1*w1*math.sin(t1-t2)*math.cos(t1-t2)+2*c2*c3*w2*w2*math.sin(t1-t2) - c2*c5*math.cos(t1-t2)*math.sin(t2)
        aux2 = c3*c3*math.cos(t1-t2)*math.cos(t1-t2) - 4*c1*c2
        aux3 = 2*c1*c5*math.sin(t2) + c3*c3*w2*w2*math.sin(t1-t2)*math.cos(t1-t2)-2*c1*c3*w1*w1*math.sin(t1-t2) - c3*c4*math.cos(t1-t2)*math.sin(t1)
        '''aux1 = 0.5*math.cos(t1 - t2)
        aux2 = math.cos(t1 - t2)
        aux3 = -0.5*(w2**2)*math.sin(t1 - t2) - \
            (g/L)*math.sin(t1)
        aux4 = (w1**2)*math.sin(t1 - t2) - (g/L)*math.sin(t2)'''

        total_1 = aux1/aux2     # total_1 na verdade é a aceleracao angular da haste 1
        total_2 = aux3/aux2     # total_2 na verdade é a aceleracao angular da haste 2

        return np.array([w1, w2, total_1, total_2])

    def time_step(self, dt):
        # Peguei do github
        """
                Advances one time step using RK4 (classical Runge-Kutta method).
                                                                                    """
        t1 = self.t1
        w1 = self.w1
        t2 = self.t2
        w2 = self.w2

        y = np.array([t1, t2, w1, w2])  #array de coordenadas tetas e omegas

        # compute the RK4 constants
        k1 = self.double_pendulum_physics(*y)
        k2 = self.double_pendulum_physics(*(y + dt * k1 / 2))
        k3 = self.double_pendulum_physics(*(y + dt * k2 / 2))
        k4 = self.double_pendulum_physics(*(y + dt * k3))

        # compute the RK4 right-hand side
        R = 1.0 / 6.0 * dt * (k1 + 2.0 * k2 + 2.0 * k3 + k4)

        # update the angles and angular velocities
        self.t1 += R[0]
        self.t2 += R[1]
        self.w1 += R[2]
        self.w2 += R[3]