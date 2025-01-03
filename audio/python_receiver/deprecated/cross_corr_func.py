#dummy file
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from receiver import Receiver

def getAngle(r, sampling_rate, frame_size, mic_distance):
    #source = "sample_gen_example1_24kHz_800Hz_0.0003ms.txt"
   # sampling_rate = 24      # kHz --> fake sampling rate of 2000 Hz or 8000 Hz
    #frame_size = 216        # #samples
    speed_sound = 343       # 343 m/sec = speed of sound in air
    #mic_distance = 260      # mm
    frame_length = frame_size / (sampling_rate * 1000)  # ms

    #r = Receiver(source, use_file=True)
    data = r.receive(frame_size)

    N = frame_size
    T = 1/(sampling_rate * 1000)
    x = np.linspace(0, N*T, N)
    y_a = data[:,0]
    y_b = data[:,1]

    yc = signal.correlate(y_a - np.mean(y_a), y_b - np.mean(y_b), mode='full')
    lag_sample_delay = yc.argmax() - (len(y_a) - 1)
    lag_time_delay = abs(lag_sample_delay) * frame_length / frame_size
    xc = np.linspace((-1 * (len(yc) / 2) - 1), (len(yc) / 2) - 1, len(yc))  # in samples
    xc = xc * frame_length / frame_size    # in ms

    incident_mic = 'both' if lag_sample_delay == 0 else ('mic_A' if lag_sample_delay < 0 else 'mic_B')
    incident_angle = (180.0 / math.pi) * math.acos(speed_sound * (lag_time_delay) / (mic_distance / 1000))
    return (incident_angle, incident_mic)
