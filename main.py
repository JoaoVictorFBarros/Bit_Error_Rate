import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

def generate_bits(num_bits):
    return np.random.randint(0, 2, num_bits)

def bpsk_modulation(bits):
    return np.where(bits == 0, -1, 1)

def add_awgn_noise(signal, snr_db):
    snr_linear = 10 ** (snr_db / 10) 
    signal_power = np.mean(np.abs(signal)**2)
    noise_power = signal_power / snr_linear
    noise = np.sqrt(noise_power) * np.random.randn(len(signal))
    return signal + noise

def bpsk_demodulation(received_signal):
    return np.where(received_signal < 0, 0, 1)

def calculate_ber(original_bits, received_bits):
    errors = np.sum(original_bits != received_bits)
    ber = errors / len(original_bits)
    return ber

def update_plot(*args):
    try:
        num_bits = int(num_bits_var.get())
        snr_min = int(snr_min_var.get())
        snr_max = int(snr_max_var.get())
        snr_step = int(snr_step_var.get())

        snr_values = np.arange(snr_min, snr_max + 1, snr_step)
        ber_values = []

        bits = generate_bits(num_bits)

        modulated_signal = bpsk_modulation(bits)

        for snr in snr_values:
            noisy_signal = add_awgn_noise(modulated_signal, snr)
            received_bits = bpsk_demodulation(noisy_signal)
            ber = calculate_ber(bits, received_bits)
            ber_values.append(ber)

        ax.clear()

        ax.semilogy(snr_values, ber_values, marker='o')
        ax.set_xlabel("SNR (dB)")
        ax.set_ylabel("BER")
        ax.set_title("Taxa de Erro de Bits (BER) vs SNR")
        ax.grid(True)

        canvas.draw()

    except ValueError:
        pass 

root = tk.Tk()
root.title("Simulação BER vs SNR")

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=2, rowspan=6, padx=20, pady=20)

num_bits_var = tk.StringVar(value="1000")
snr_min_var = tk.StringVar(value="0")
snr_max_var = tk.StringVar(value="9")
snr_step_var = tk.StringVar(value="1")

num_bits_var.trace_add("write", update_plot)
snr_min_var.trace_add("write", update_plot)
snr_max_var.trace_add("write", update_plot)
snr_step_var.trace_add("write", update_plot)

ttk.Label(root, text="Número de Bits:").grid(column=0, row=0, padx=10, pady=10)
num_bits_entry = ttk.Entry(root, textvariable=num_bits_var)
num_bits_entry.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(root, text="SNR Mínimo (dB):").grid(column=0, row=1, padx=10, pady=10)
snr_min_entry = ttk.Entry(root, textvariable=snr_min_var)
snr_min_entry.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(root, text="SNR Máximo (dB):").grid(column=0, row=2, padx=10, pady=10)
snr_max_entry = ttk.Entry(root, textvariable=snr_max_var)
snr_max_entry.grid(column=1, row=2, padx=10, pady=5)

ttk.Label(root, text="Passo do SNR (dB):").grid(column=0, row=3, padx=10, pady=10)
snr_step_entry = ttk.Entry(root, textvariable=snr_step_var)
snr_step_entry.grid(column=1, row=3, padx=10, pady=5)

update_plot()
root.mainloop()