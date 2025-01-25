from pydub import AudioSegment
import speech_recognition as sr
import os

def convert_m4a_to_wav(input_path, output_path):
    """Convert an .m4a file to .wav format."""
    try:
        print(f"Converting {input_path} to {output_path}...")
        audio = AudioSegment.from_file(input_path, format="m4a")
        audio.export(output_path, format="wav")
        print("Conversion successful!")
    except Exception as e:
        print(f"Error during conversion: {e}")
        exit()

def transcribe_audio(audio_path):
    "Transcribe a .wav audio file to text."
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            print("Processing audio for transcription...")
            audio_data = recognizer.record(source)  # Read the entire file
            transcription = recognizer.recognize_google(audio_data)
            print("Transcription completed:")
            return transcription
    except sr.UnknownValueError:
        return "Sorry, the audio was unclear and could not be transcribed."
    except sr.RequestError as e:
        return f"Error with the transcription service: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

def main():
    input_audio_path = "C:\Code\Projects\Language\Python\Convert_audio_to_text\Recording.m4a"  # Replace with your .m4a file path
    output_audio_path = "Recording.wav"

    # Check if the input file exists
    if not os.path.exists(input_audio_path):
        print(f"Input file not found: {input_audio_path}")
        return

    # First lets convert .m4a to .wav
    convert_m4a_to_wav(input_audio_path, output_audio_path)

    # THen transcribe the .wav file
    transcription = transcribe_audio(output_audio_path)

    # Print and save transcription
    print(transcription)
    with open("transcription.txt", "w") as file:
        file.write(transcription)

if __name__ == "__main__":
    main()
