#!/usr/bin/env python

from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 4000
WIDTH = 256
WINDOW_SIZE = 2 #5         # window size for moving average

def is_silent(snd_data):
    "Returns 'True' if below the 'silent' threshold"
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):
    "Trim the blank spots at the start and end"
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    # Trim to the left
    snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def add_silence(snd_data, seconds):
    "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    r = array('h', [0 for i in xrange(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in xrange(int(seconds*RATE))])
    return r

def record():
    """
    Record a word or words from the microphone and
    return the data as an array of signed shorts.

    Normalizes the audio, trims silence from the
    start and end, and pads with 0.5 seconds of
    blank sound to make sure VLC et al can play
    it without getting chopped off.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    plt.ion()
    lines = None
    fig = plt.figure(0)
    ax = fig.add_subplot(111)
    i = 0
    #signals = np.empty((WINDOW_SIZE, CHUNK_SIZE))
    while 1:
        i += 1
        if i == WINDOW_SIZE:
            i = 0
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        #r.extend(snd_data)

        #silent = is_silent(snd_data)

        #if silent and snd_started:
        #    num_silent += 1
        #elif not silent and not snd_started:
        #    snd_started = True

        #if snd_started and num_silent > 30:
        #    break
        #signals[i, :] = np.array(snd_data)
        #if i % WINDOW_SIZE == 0:
        #signal = signals.mean(axis=0)
        signal = np.array(snd_data)
        signal_fft = np.fft.fftshift(np.fft.fft(signal))
        if lines:
            ax.lines.remove(lines)
        [lines,] = ax.plot(range(WIDTH), np.abs(signal_fft[CHUNK_SIZE/2-WIDTH/2:CHUNK_SIZE/2+WIDTH/2]), 'b-')
        plt.draw()

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    r = add_silence(r, 0.5)
    print r
    return sample_width, r

#def record_to_file(path):
#    "Records from the microphone and outputs the resulting data to 'path'"
#    sample_width, data = record()
#    data = pack('<' + ('h'*len(data)), *data)

#    wf = wave.open(path, 'wb')
#    wf.setnchannels(1)
#    wf.setsampwidth(sample_width)
#    wf.setframerate(RATE)
#    wf.writeframes(data)
#    wf.close()

if __name__ == '__main__':
    #print("please speak a word into the microphone")
    #record_to_file('demo.wav')
    #print("done - result written to demo.wav")
    record()

