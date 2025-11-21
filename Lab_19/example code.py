import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode

def system(n, d):
    # transfer function:
    system = TransferFunction(n, d)

    # zeros & poles:
    zeros = system.zeros
    poles = system.poles

    print("Zeros =", zeros)
    print("Poles =", poles)

    # stable:
    stable = all(abs(p) < 1 for p in poles)
    print("Stability =", "Stable" if stable else "Unstable")

    # causal:
    causal = len(n) <= len(d)
    print("Causality =", "Causal" if causal else "Non-Causal")

    # time invariant:
    print("Time Invariance = Time-Invariant")

    # plot:
    w, mag, phase = bode(system)
    plt.figure(figsize=(10, 7))
    plt.subplot(2, 1, 1)
    plt.semilogx(w, mag)
    plt.title("Magnitude Plot")
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude(dB)")
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.semilogx(w, phase)
    plt.title("Phase Plot")
    plt.xlabel("Frequency")
    plt.ylabel("Phase (degre)")
    plt.grid()
    plt.tight_layout()
    plt.show()

n = [1, 0.5]
d = [1, -1.5, 0.5]

system(n, d)
