import sounddevice as sd
import soundfile as sf
import numpy as np
import torch
import mlx_whisper
from openpipe import OpenAI
import keyboard 
from tkinter import *
from pynput import keyboard

client = OpenAI()

# def record_audio(output_file, record_seconds, sample_rate=44100):
#     print("Recording...")
#     audio_data = sd.rec(int(record_seconds * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
#     sd.wait()  # Wait until recording is finished
#     print("Finished recording.")

#     # Save the recorded data as a FLAC file
#     sf.write(output_file, audio_data, sample_rate, format='FLAC')

def record_audio(output_file, sample_rate=44100):
    recording = False
    audio_data = None

    def start_recording():
        nonlocal recording, audio_data
        if not recording:
            print("Recording started...")
            audio_data = sd.rec(int(10 * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
            sd.wait()  # Wait until recording is finished
            recording = True

    def stop_recording():
        nonlocal recording
        if recording:
            print("Recording stopped.")
            sf.write(output_file, audio_data, sample_rate, format='FLAC')
            recording = False

    def toggle_recording(event):
        
        if recording:
            stop_recording()
        else:
            start_recording()
    
    def toggle():
        # Implement your toggle functionality here
        print("Toggle function called!")
        # Add your toggle logic here

    def on_activate():
        toggle_recording()

    # Define your hotkey combination
    with keyboard.GlobalHotKeys({
            '<ctrl>+<shift>+a': on_activate,
        }) as h:
        h.join()

    # Set the hotkey combination (e.g. ctrl+shift+f)
    # try:
    #     keyboard.add_hotkey('space', toggle_recording)
    #     keyboard.wait('esc')
    # except KeyboardInterrupt:
    #     print("Exiting...")


def transcribe(filepath):
    text = mlx_whisper.transcribe(filepath, path_or_hf_repo='mlx-community/whisper-large-v3-mlx')["text"]
    print(text)
    return text

def postprocess(text):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
            {"role": "system", "content": "You are an AI text formatting assistant. You take in a transcript of a dictation of a message, potentially with mistakes and typos, and your job is to fix typos and format the text into a structure. If you detect the intended format is an email, format as an email. If you think the format is a text/SMS, then format as such. You will add bullet points whenever lists are mentioned."},
            {"role": "user", "content": text}
        ]
    )

    return completion.choices[0].message.content

def extract_entities(text):
    print(text)

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
            {"role": "system", "content": "You are an entity extraction model, particularly for contacts and names. You will take in text and output a JSON list of entities in this structure: entities: [{{ name: }}]"},
            {"role": "user", "content": text}
        ]
    )

    print(completion.choices[0].message.content)

record_audio('output.flac')
out = transcribe(filepath='output.flac')
out = postprocess(out)
extract_entities(out)