# Import necessary libraries
import yt_dlp  # yt-dlp for downloading videos
from moviepy.editor import VideoFileClip
import requests
import os

# Step 1: Function to download YouTube video
def download_youtube_video(url, output_path):
    """
    Downloads a YouTube video and saves it to the specified path.

    :parameter url: URL of the YouTube video to download.
    :parameter output_path: Local path to save the downloaded video.
    :return: Path to the downloaded video.
    """
    try:
        ydl_opts = {
            'outtmpl': output_path,  # Template for output filename
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Download the video
        print(f"Downloaded video at: {output_path}")
        return output_path
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None

# Step 2: Function to extract audio from the video
def extract_audio_from_video(video_path, output_audio_path):
    """
    Extracts audio from a video file and saves it as a .wav file.

    :parameter video_path: Path to the input video file.
    :parameter output_audio_path: Path to save the extracted audio.
    :return: Path to the extracted audio file.
    """
    try:
        video = VideoFileClip(video_path)  # Load the video file
        video.audio.write_audiofile(output_audio_path)  # Extract audio
        video.close()  # Close the video to free resources
        print(f"Extracted audio at: {output_audio_path}")
        return output_audio_path
    except Exception as e:
        print(f"Error extracting audio: {e}")
        return None

# Step 3: Transcribe audio using Deepgram API
def transcribe_audio_deepgram(audio_path, api_key):
    headers = {
        'Authorization': f'Token {api_key}',  # Authorization header with API key
        'Content-Type': 'audio/wav',  # Content type for audio file
    }

    try:
        with open(audio_path, 'rb') as audio_file:
            response = requests.post(
                'https://api.deepgram.com/v1/listen',  # Deepgram API endpoint
                headers=headers,
                data=audio_file
            )

        if response.status_code == 200:
            transcription = response.json()['results']['channels'][0]['alternatives'][0]['transcript']
            print("Audio to text:", transcription)
            return transcription
        else:
            print(f"Transcription failed: HTTP {response.status_code}")
            print("Error details:", response.json())  # Detailed error info
            return None
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

# Function to save transcription to a text file
def save_transcription_to_file(transcription, output_file):
    """
    Saves the transcription text to a specified text file.

    :parameter transcription: Transcription text to save.
    :parameter output_file: Path to the output text file.
    """
    try:
        with open(output_file, 'w') as file:
            file.write(transcription)  # Write transcription to file
        print(f"Transcription saved to: {output_file}")
    except Exception as e:
        print(f"Error saving transcription: {e}")

# Step 4: Generate audio from text using Eleven Labs API
def generate_audio_eleven_labs(text, api_key, voice_id, output_audio_path):
    """
    Generates audio from text using the Eleven Labs API.

    :parameter text: Text to convert to audio.
    :parameter api_key: API key for the Eleven Labs API.
    :parameter voice_id: ID of the voice to use for audio generation.
    :parameter output_audio_path: Path to save the generated audio file.
    :return: Path to the generated audio file.
    """
    try:
        url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'  # Eleven Labs API endpoint

        headers = {
            'xi-api-key': api_key,
            'Content-Type': 'application/json',
        }

        data = {
            'text': text,
            'voice_settings': {
                'stability': 0.5,
                'similarity_boost': 0.75
            }
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            with open(output_audio_path, 'wb') as audio_file:
                audio_file.write(response.content)  # Save generated audio
            print(f"Generated audio at: {output_audio_path}")
            return output_audio_path
        else:
            print(f"Error in generating audio: {response.status_code}, {response.text}")
            return None
    except Exception as e:
        print(f"Error with Eleven Labs API: {e}")
        return None

# Main function to run all steps
def process_youtube_to_audio_transcription(video_url, deepgram_api_key, eleven_labs_api_key, voice_id, video_path, audio_path, transcription_path):
    """
    Coordinates the entire process from downloading the video to generating audio from transcription.

    :parameter video_url: URL of the YouTube video to process.
    :parameter deepgram_api_key: API key for the Deepgram API.
    :param eleven_labs_api_key: API key for the Eleven Labs API.
    :param voice_id: Voice ID to use with Eleven Labs API.
    :param video_path: Path to save the downloaded video.
    :param audio_path: Path to save the extracted audio.
    :param transcription_path: Path to save the transcription text.
    :return: Path to the generated audio file, if successful.
    """
    # Step 1: Download YouTube video
    video_path = download_youtube_video(video_url, video_path)

    if not video_path:
        print("Failed to download video.")
        return None

    # Step 2: Extract audio from video
    audio_path = extract_audio_from_video(video_path, audio_path)

    if not audio_path:
        print("Failed to extract audio from video.")
        return None

    # Step 3: Convert audio to text using Deepgram
    transcription = transcribe_audio_deepgram(audio_path, deepgram_api_key)

    if transcription:
        # Save the transcription to a text file
        save_transcription_to_file(transcription, transcription_path)

        # Step 4: Generate audio using Eleven Labs
        generated_audio_path = generate_audio_eleven_labs(transcription, eleven_labs_api_key, voice_id,output_audio_path='test.mp3')
        return generated_audio_path
    else:
        print("Transcription failed, unable to generate audio.")
        return None

# Example usage
if __name__ == "__main__":  # Corrected this line
    # User input for YouTube video URL and file paths
    video_url = input("Enter the YouTube video URL: ")
    video_path = input("Enter the path to save the downloaded video (e.g., C:\\path\\to\\video.mp4): ")
    audio_path = input("Enter the path to save the extracted audio (e.g., C:\\path\\to\\audio.wav): ")
    transcription_path = input("Enter the path to save the transcription (e.g., C:\\path\\to\\transcription.txt): ")

    # Replace these with your actual API keys and voice ID
    deepgram_api_key = "15957b4ce28c2765fa11df96729f00af5bfab70e"
    eleven_labs_api_key = "sk_10119956a2c5820d0dc7795d71b3c3041d380c4ecaac4f08"
    voice_id = "Xb7hH8MSUJpSbSDYk0k2"
    # Process the video and generate audio from transcription
    process_youtube_to_audio_transcription(video_url, deepgram_api_key, eleven_labs_api_key, voice_id, video_path, audio_path, transcription_path)
