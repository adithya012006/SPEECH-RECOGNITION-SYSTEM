# SPEECH-RECOGNITION-SYSTEM

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*:  NALLAGATLA ADITHYA

*INTERN ID*: CT04DM719

*DOMAIN*: Artificial intelligence

*DURATION*:  4 weeks

*MENTOR*:  Neela Santhosh

#discription: This Python script performs automatic speech recognition (ASR) by converting spoken audio into written text using the Vosk API, a powerful offline speech recognition toolkit. Executed within the Google Colab environment, this code enables transcription of audio files (e.g., WAV, MP3) using a compact, lightweight Vosk model (e.g., vosk-model-small-en-us-0.15). It effectively demonstrates how ASR tasks can be achieved without requiring internet access or high computational resources, making it a practical and scalable solution for a wide range of applications.

The key tools and libraries utilized include:

vosk: An offline-capable speech recognition toolkit built on Kaldi, used here to load pre-trained language models and decode spoken audio into transcribed text.

pydub: A high-level audio processing library used to read and convert various audio formats into WAV format with the required properties (16-bit, mono, 16 kHz) for Vosk compatibility.

wave and json: Python standard libraries for reading raw WAV data and parsing JSON outputs from the recognizer, respectively.

os: Used for basic file management tasks, including checking file existence and cleaning up temporary files.

The script follows a structured workflow:

It takes an input audio file path and checks for the availability of the Vosk model and the audio file itself.

It uses pydub to load and normalize the input audio to Vosk's required format: 16 kHz sample rate, mono channel, and 16-bit PCM WAV.

The preprocessed audio is then fed into a KaldiRecognizer using the Vosk model. The recognizer processes the audio stream in chunks and accumulates recognized text as it progresses.

Once complete, the script combines intermediate recognition results with the final result to produce clean, full transcription.

All temporary artifacts (e.g., converted WAV files) are deleted afterward to maintain a clean runtime environment.

This entire process is highly suited for execution on Google Colab, a free cloud-based development environment provided by Google. Colab supports Python, allows users to install additional packages (such as vosk and pydub), and gives access to virtual CPUs and GPUs for accelerated processing—though GPU isn’t required for this ASR task. Running this code on Colab also removes the need for setting up Python environments locally, making it more accessible for learners, educators, or developers prototyping speech-based systems.

Real-world applications for this speech-to-text system are extensive. It can be used in:

Meeting transcription for businesses or classrooms,

Accessibility tools for the hearing impaired,

Voice-controlled applications or virtual assistants,

Content indexing in media and journalism,

Podcast or video subtitling, especially for creators seeking automated workflows,

Voice logs or report generation in domains like healthcare or law enforcement.

In summary, this project illustrates how Vosk and Python can be integrated for efficient offline voice recognition, with Colab serving as an ideal platform for development and experimentation. It showcases an important intersection of natural language processing and real-time user interaction with high potential in modern AI applications.

#output:

