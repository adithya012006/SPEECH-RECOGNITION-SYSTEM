import os
import wave
import json
from vosk import Model, KaldiRecognizer, SetLogLevel
from pydub import AudioSegment

SetLogLevel(-1)

def transcribe_audio_vosk_direct(audio_file_path, vosk_model_path="vosk-model-small-en-us-0.15"):
    temp_wav_path = "temp_vosk_input.wav"  # Define before try block

    if not os.path.exists(vosk_model_path):
        return f"❌ Error: Vosk model not found at '{vosk_model_path}'. Please download and extract it."

    if not os.path.exists(audio_file_path):
        return f"❌ Error: Audio file not found at '{audio_file_path}'."

    try:
        # Load and convert audio to WAV (16kHz mono 16-bit)
        audio = AudioSegment.from_file(audio_file_path)
        if audio.channels != 1 or audio.frame_rate != 16000 or audio.sample_width != 2:
            audio = audio.set_channels(1).set_frame_rate(16000).set_sample_width(2)

        audio.export(temp_wav_path, format="wav")

        # Initialize model and recognizer
        model = Model(vosk_model_path)
        rec = KaldiRecognizer(model, 16000)

        result_text = ""
        with wave.open(temp_wav_path, "rb") as wf:
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    result_json = json.loads(rec.Result())
                    result_text += result_json.get("text", "") + " "

            final_result_json = json.loads(rec.FinalResult())
            result_text += final_result_json.get("text", "")

        return result_text.strip() or "⚠ No speech detected or transcription failed."

    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"

    finally:
        if os.path.exists(temp_wav_path):
            os.remove(temp_wav_path)


def main():
    print("--- 🎙 Simple Speech Recognition System (Vosk Direct) ---")
    audio_file = input("Enter the path to your audio file (e.g., 'audio.wav' or 'audio.mp3'): ").strip()
    vosk_model_dir = "vosk-model-small-en-us-0.15"  # Update this path if model is elsewhere

    transcribed_text = transcribe_audio_vosk_direct(audio_file, vosk_model_dir)
    print("\n--- 📝 Transcription Result ---")
    print(transcribed_text)
    print("----------------------------------------------------------")


if _name_ == "_main_":
    main()
