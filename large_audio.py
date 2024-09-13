from pydub import AudioSegment
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Load the audio file
audio_file = AudioSegment.from_file("data/tut.mp3")

# Define the maximum chunk size (in milliseconds)
chunk_size_ms = 10 * 60 * 1000  # 10 minutes

# Split the audio into chunks
chunks = [audio_file[i:i + chunk_size_ms]
          for i in range(0, len(audio_file), chunk_size_ms)]

# Process each chunk
transcriptions = []
for i, chunk in enumerate(chunks):
    chunk.export(f"data/tut_chunk_{i}.mp3", format="mp3")
    with open(f"data/tut_chunk_{i}.mp3", "rb") as audio_chunk_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_chunk_file,
            language="en"
        )
        # Append the text attribute of the transcription object
        transcriptions.append(transcription.text)

# Save the transcription to a file
output_file_path = "tut.txt"
with open(output_file_path, "w") as f:
    f.write(" ".join(transcriptions))
