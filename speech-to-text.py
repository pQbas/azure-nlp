import azure.cognitiveservices.speech as speechsdk

# Configura tus credenciales
speech_key = "<your-speech-api-key>"
region = "<your-region>"

# Crea un objeto de cliente de voz
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=region)
audio_config = speechsdk.audio.AudioConfig(filename="audio.wav")  # Nombre del archivo de audio

# Crea el cliente de transcripción
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

# Realiza la transcripción
result = speech_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print(f"Texto reconocido: {result.text}")
else:
    print(f"Error: {result.reason}")

