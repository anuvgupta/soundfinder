import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from receiver import Receiver

source = "sample_gen_example1_24kHz_800Hz_0.0003ms.txt"  # "/dev/cu.SLAB_USBtoUART"  # "sample_gen_example1_24kHz_800Hz_0.0003ms.txt"
source_use_file = True
sampling_rate = 32      # kHz --> fake sampling rate of 2000 Hz or 8000 Hz
frame_size = 1024       # #samples
speed_sound = 343       # 343 m/sec = speed of sound in air
mic_distance = 260      # mm
frame_length = frame_size / (sampling_rate * 1000)  # ms

r = Receiver(source, use_file=source_use_file)
data = r.receive(frame_size)

N = frame_size
T = 1/(sampling_rate * 1000)
x = np.linspace(0, N*T, N)
y_a = data[:,0]
y_b = data[:,1]

# yc = signal.correlate(y_a - np.mean(y_a), y_b - np.mean(y_b), mode='full')
# lag_sample_delay = yc.argmax() - (len(y_a) - 1)
# lag_time_delay = abs(lag_sample_delay) * frame_length / frame_size
# xc = np.linspace((-1 * (len(yc) / 2) - 1), (len(yc) / 2) - 1, len(yc))  # in samples
# xc = xc * frame_length / frame_size    # in ms

# incident_mic = 'both' if lag_sample_delay == 0 else ('mic_A' if lag_sample_delay < 0 else 'mic_B')
# incident_angle = (180.0 / math.pi) * math.acos(speed_sound * (lag_time_delay) / (mic_distance / 1000))

# print("Sample Delay/Lag: {} samples".format(lag_sample_delay))
# print("Time Delay/Lag: {} ms".format(lag_time_delay))
# print("Correlation: {}".format(round(yc[lag_sample_delay], 3)))
# print("Incident Mic: {}".format(incident_mic))
# print("Incident Angle: {}deg".format(round(incident_angle, 3)))

plt.ylabel("Sample Value")
plt.xlabel("Sample #")
plt.plot(x, y_a, marker='o', color='red')
plt.plot(x, y_b, color='blue')
# plt.annotate('argmax={}@{}ms'.format(round(yc[lag_sample_delay], 3), lag_time_delay),  (lag_time_delay, yc[yc.argmax()]), ha='center')
plt.show()

