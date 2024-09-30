# YouTube Video Downloader and Transcription Tool

This Python project allows users to download YouTube videos, extract audio, transcribe the audio to text, and generate audio from the transcription using various APIs.

## Features

- Download YouTube videos using `yt-dlp`.
- Extract audio from downloaded videos.
- Transcribe audio files using the Deepgram API.
- Generate audio from transcription using the Eleven Labs API.

## Requirements

- Python 3.6 or higher
- `yt-dlp` library
- `moviepy` library
- `requests` library

You can install the required libraries using pip:

```bash
pip install yt-dlp moviepy requests
```

## Usage

1. Clone this repository or download the script file.

2. Run the script:

   ```bash
   python your_script_name.py
   ```

3. Follow the prompts to enter:
   - The YouTube video URL.
   - The path to save the downloaded video.
   - The path to save the extracted audio.
   - The path to save the transcription.
   - Your Deepgram API key.
   - Your Eleven Labs API key.
   - The voice ID for Eleven Labs.

## Example

When prompted, enter the following details:

```
Enter the YouTube video URL: https://www.youtube.com/watch?v=ZXsQAXx_ao0
Enter the path to save the downloaded video (e.g., C:\path\to\video.mp4): C:\Users\DANISH IBRAHIM\Videos\powervoice\video.mp4
Enter the path to save the extracted audio (e.g., C:\path\to\audio.wav): C:\Users\DANISH IBRAHIM\Videos\powervoice\audio.wav
Enter the path to save the transcription (e.g., C:\path\to\transcription.txt): C:\Users\DANISH IBRAHIM\Videos\powervoice\transcription.txt
Enter your Deepgram API key: your_deepgram_api_key
Enter your Eleven Labs API key: your_eleven_labs_api_key
Enter the voice ID for Eleven Labs: your_voice_id
```

## Notes

- Ensure that you have valid API keys for the Deepgram and Eleven Labs APIs.
- Make sure the specified paths for saving files are valid and writable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for downloading videos.
- [moviepy](https://zulko.github.io/moviepy/) for audio processing.
- [Deepgram API](https://deepgram.com/) for audio transcription.
- [Eleven Labs API](https://elevenlabs.io/) for text-to-speech generation.
