import numpy as np
from scipy import signal

# 创建低通滤波器
cutoff_frequency = 1000  # 截止频率为1000 Hz
filter_order = 3  # 滤波器阶数
b, a = signal.butter(filter_order, cutoff_frequency, 'low', fs=44100)
pitch_factor = 1.31

def change_pitch(stream_in: bytes):
    audio_in = np.frombuffer(stream_in, dtype=np.float32)
    audio_out = signal.resample_poly(audio_in, int(1.63 * pitch_factor), int(2.35 / pitch_factor))
    return audio_out.astype(np.float32).tobytes()