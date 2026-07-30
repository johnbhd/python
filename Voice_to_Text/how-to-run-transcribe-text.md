# Voice to Text

A simple Python program that converts audio and video recordings into text using Faster-Whisper.

The transcription runs locally on your computer. Your recording is not intentionally uploaded to OpenAI, Google, or any cloud transcription service.

## Supported Files

Examples of supported formats:

* `.mp3`
* `.wav`
* `.m4a`
* `.mp4`
* `.webm`

## Requirements

You need:

* Python 3.10 or newer
* Internet connection for the first Whisper model download
* Enough storage for the Whisper model

After the model is downloaded, you can disconnect from the internet and transcribe recordings locally.

## Folder Structure

```text
Voice to Text/
├── transcribe.py
├── requirements.txt
├── recordings/
├── models/
└── README.md
```

Put your recordings inside the `recordings` folder.

Example:

```text
recordings/
└── interview.m4a
```

# Installation

There are two ways to install Faster-Whisper.

## Option 1: Simple Installation

This installs Faster-Whisper using your normal Python installation.

Open PowerShell inside the project folder:

```powershell
cd "Voice to Text"
```

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install Faster-Whisper:

```powershell
python -m pip install faster-whisper
```

Check if it was installed correctly:

```powershell
python -c "from faster_whisper import WhisperModel; print('Faster-Whisper is ready')"
```

Expected result:

```text
Faster-Whisper is ready
```

This method is enough for a simple personal project.

## Option 2: Virtual Environment

A virtual environment is optional but recommended.

It keeps this project's Python libraries separate from your other Python projects.

Create the environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

You should see:

```text
(.venv) PS C:\your-folder\Voice to Text>
```

Install Faster-Whisper:

```powershell
python -m pip install --upgrade pip
python -m pip install faster-whisper
```

When finished, deactivate it:

```powershell
deactivate
```

# Requirements File

Create a file named `requirements.txt`:

```text
faster-whisper
```

Install the dependencies using:

```powershell
python -m pip install -r requirements.txt
```

# Running the Program

Run an M4A audio file:

```powershell
python transcribe.py "recordings\interview.m4a"
```

Run an MP3 file:

```powershell
python transcribe.py "recordings\interview.mp3"
```

Run an MP4 video:

```powershell
python transcribe.py "recordings\interview.mp4"
```

For filenames containing spaces, always use quotation marks:

```powershell
python transcribe.py "recordings\Interview Recording.m4a"
```

You can also use a complete Windows file path:

```powershell
python transcribe.py "C:\Users\YourName\Downloads\Interview Recording.m4a"
```

# Whisper Models

The default model is:

```text
small
```

Run using the default model:

```powershell
python transcribe.py "recordings\interview.m4a"
```

Choose another model:

```powershell
python transcribe.py "recordings\interview.m4a" --model base
```

Available models include:

```text
tiny
base
small
medium
large-v3
turbo
```

Recommended models:

| Model      | Description                               |
| ---------- | ----------------------------------------- |
| `tiny`     | Fastest but less accurate                 |
| `base`     | Lightweight and reasonably fast           |
| `small`    | Recommended balance of speed and accuracy |
| `medium`   | More accurate but slower                  |
| `large-v3` | Most accurate but requires more memory    |

For an 8 GB RAM laptop, start with:

```powershell
python transcribe.py "recordings\interview.m4a" --model small
```

If it is too slow, use:

```powershell
python transcribe.py "recordings\interview.m4a" --model base
```

# Language

For automatic language detection:

```powershell
python transcribe.py "recordings\interview.m4a"
```

Automatic detection is recommended for English, Filipino, and Taglish recordings.

Force English:

```powershell
python transcribe.py "recordings\interview.m4a" --language en
```

Force Filipino:

```powershell
python transcribe.py "recordings\interview.m4a" --language tl
```

# Output Files

The program creates:

```text
interview.txt
interview.srt
```

The `.txt` file contains the readable transcript.

The `.srt` file contains subtitle timestamps.

Example:

```text
recordings/
├── interview.m4a
├── interview.txt
└── interview.srt
```

# First Model Download

During the first run, Faster-Whisper downloads the selected model from Hugging Face.

You may see warnings such as:

```text
You are sending unauthenticated requests to the HF Hub.
```

or:

```text
Your machine does not support symlinks.
```

These are normally warnings, not errors.

The program is downloading the Whisper model to your computer. It is not intentionally uploading your recording.

Do not press `Ctrl + C` while the model is downloading.

When the model finishes loading, the transcription will begin.

# Stop the Transcription

Press:

```text
Ctrl + C
```

If the script saves every completed segment using:

```python
txt_file.flush()
srt_file.flush()
```

the completed transcript should remain saved.

The few seconds currently being processed may not be included.

# Common Errors

## Faster-Whisper Is Missing

Error:

```text
ModuleNotFoundError: No module named 'faster_whisper'
```

Install it using:

```powershell
python -m pip install faster-whisper
```

Check the installation:

```powershell
python -c "from faster_whisper import WhisperModel; print('Ready')"
```

## Wrong Python Installation

Check which Python is running:

```powershell
python -c "import sys; print(sys.executable)"
```

Check where Faster-Whisper is installed:

```powershell
python -m pip show faster-whisper
```

Using `python -m pip` helps ensure the library is installed into the same Python that runs the script.

## PowerShell Blocks Virtual Environment Activation

Error:

```text
running scripts is disabled on this system
```

Run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Press `Y`, close PowerShell, and open it again.

This is only needed when using a virtual environment.

## Broken Virtual Environment

Delete it:

```powershell
Remove-Item -Recurse -Force .venv
```

Create it again:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install Faster-Whisper:

```powershell
python -m pip install faster-whisper
```

## Audio File Not Found

Check the filename:

```powershell
Get-ChildItem recordings
```

Then run the correct path:

```powershell
python transcribe.py "recordings\correct-file-name.m4a"
```

## Low Memory or Slow Processing

Use a smaller model:

```powershell
python transcribe.py "recordings\interview.m4a" --model base
```

Close unnecessary applications while transcribing long recordings.

# Privacy

This project does not intentionally use:

* OpenAI API
* Google Speech-to-Text
* Gemini API
* Cloud transcription APIs
* Automatic uploads
* Analytics
* Remote logging

The Whisper model requires internet during its first download.

After the model is downloaded, you can turn off Wi-Fi before transcribing confidential recordings.

Your processing flow is:

```text
Recording
   ↓
Local Faster-Whisper model
   ↓
TXT and SRT transcript
```

# GitHub Safety

Do not upload confidential recordings or transcripts to a public GitHub repository.

Add this to `.gitignore`:

```gitignore
.venv/
models/
recordings/
transcripts/
*.txt
*.srt
__pycache__/
*.pyc
```

You may add empty `.gitkeep` files inside folders that you want GitHub to keep:

```text
recordings/.gitkeep
models/.gitkeep
transcripts/.gitkeep
```
