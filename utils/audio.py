
import pyaudio
import wave
import sys

import sounddevice as sd
from scipy.io.wavfile import write

from playsound import playsound



def play_audio(filename):

  playsound(filename)



def record_v1(seconds, filename):
    
    fs = 44100  # Sample rate

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    print('Recording: ', seconds, "seconds *********")
    sd.wait()  # Wait until recording is finished
    print('**** Finished recording')
    write(filename, fs, myrecording)  # Save as WAV file 
    print('**** Save audio: ', filename)



def record(seconds, filename):
    """
    Grabación de audio
    """
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording *********')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames
    actual = -1
    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        
        data = stream.read(chunk)
        frames.append(data)
        times = int(i*(chunk/fs))
        
        if not actual==times:
            if times%2:
                print("... ", times+1, " segundos")
            actual=times

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('**** Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()