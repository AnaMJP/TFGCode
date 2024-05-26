import numpy as np
import scipy.integrate as integrate

class DataProcessor:
    def calculate_velocity(self, t, A1, A2, A3):
        Vx = integrate.cumtrapz(A1, t, initial=0)
        Vy = integrate.cumtrapz(A2, t, initial=0)
        Vz = integrate.cumtrapz(A3, t, initial=0)

        Vx -= np.mean(Vx)
        Vy -= np.mean(Vy)
        Vz -= np.mean(Vz)

        return Vx, Vy, Vz

    def calculate_acceleration(self, t, filtered_A1, filtered_A2, filtered_A3):
        filtered_A = filtered_A1 + filtered_A2 + filtered_A3
        return filtered_A


