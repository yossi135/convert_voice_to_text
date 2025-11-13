import whisper
import os
import streamlit as st
# record.py
import sounddevice as sd
import scipy.io.wavfile
# requirements.txt

def record_audio(filename="recorded.wav", duration=60, fs=44100):
    st.write("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    scipy.io.wavfile.write(filename, fs, recording)
    print("Saved:", filename)


def transcribe_audio(filename="recorded.wav"):
    if not os.path.exists(filename):
        return st.write("Audio file not found.")
    try:
        model = whisper.load_model('large')
        result = model.transcribe(filename)
        return result['text']
    except Exception as e:
        return  st.write(f"An error occurred during transcription: {e}")

st.title('convert audio to text')
if st.button('Record Audio🎤'):
    record_audio()
    st.session_state.audio_recorded = True


if st.session_state.get("audio_recorded", False) and os.path.exists("recorded.wav"):
    st.audio('recorded.wav', format='audio/wav')

    if st.button('📝 Transcribe Audio'):
        transcribed_text = transcribe_audio()
        st.text_area('Transcribed Text', transcribed_text)


    
 # python -m streamlit run task.py