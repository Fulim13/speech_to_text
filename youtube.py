from langchain_community.document_loaders.blob_loaders.youtube_audio import (
    YoutubeAudioLoader,
)


from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import (
    OpenAIWhisperParser,
)

from dotenv import load_dotenv

load_dotenv()

# https://python.langchain.com/v0.1/docs/integrations/document_loaders/youtube_transcript/
urls = ["https://www.youtube.com/watch?v=LKCVKw9CzFo"]
save_dir = "data/youtube/"

loader = GenericLoader(YoutubeAudioLoader(
    urls, save_dir), OpenAIWhisperParser())

docs = loader.load()

# Define the file path where you want to save the content
file_path = "data/youtube/transcript.txt"

# Save the content to the file
with open(file_path, "w", encoding="utf-8") as file:
    file.write(docs[0].page_content[:])

print(f"Transcript saved to {file_path}")
