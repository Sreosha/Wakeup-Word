import sounddevice as sd
from scipy.io.wavfile import write

def record_audio_save(save_path,n_times=100):
    input("Press Enter to start the audio recording...")
    for i in range(n_times):
        fs=44100 #sample rate
        seconds=2 #For how long it should record the audio
        recording=sd.rec(int(seconds*fs),samplerate=fs,channels=2)
        sd.wait()
        write(save_path + str(i) + ".wav",fs,recording)
        input(f"Press enter to next ({i+1}/{n_times})")
        

def background_audio_save(save_path,n_times=100):
    input("Press Enter to start the audio recording...")
    for i in range(n_times):
        fs=44100 #sample rate
        seconds=2 #For how long it should record the audio
        recording=sd.rec(int(seconds*fs),samplerate=fs,channels=2)
        sd.wait()
        write(save_path + str(i) + ".wav",fs,recording)
        print(f"Currently on ({i+1}/{n_times})")
print("Wakeup word recording...")
record_audio_save("wakeup_audio/")

print("Background noise recording...")
background_audio_save("bg_noise/")



