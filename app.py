from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

audio_file = open("tips.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    language="en"
)
print(transcription.text)

# Save the transcription to a file
output_file_path = "transcription.txt"
with open(output_file_path, "w") as f:
    f.write(transcription.text)
