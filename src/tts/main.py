import sys
from google.cloud import texttospeech

# take in text and output to a file
def synthesize_text(text, file_name):
    """
    text:
    ====
    string of text to output to speech

    file_name:
    ====
    name of the file to output to
    """
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-D",
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )
    with open(file_name, "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "{0}"'.format(file_name))
        out.close()

# CLI 
def main():
    with open(sys.argv[1], "r") as f:
        text = f.read() # take in the text file
        synthesize_text(text, sys.argv[2]) # output the read in text to audio file
        f.close()

if __name__ == "__main__":
    main()

