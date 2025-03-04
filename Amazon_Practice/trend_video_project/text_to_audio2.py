import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init('espeak')  # Using espeak instead of SAPI5

# Get current speech rate (speed)
rate = engine.getProperty('rate')
print(f"Current speech rate: {rate}")

# Set the rate (speed) of speech
engine.setProperty('rate', 150)  # 150 words per minute

# Set volume (0.0 to 1.0)
engine.setProperty('volume', 1)  # Maximum volume

# Set pitch (espeak allows pitch adjustments)
engine.setProperty('pitch', 75)  # 50 is normal, 0 is low, 100 is high

# Set voice to default (espeak has multiple voices)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Select different voices based on index

# Text you want to convert to speech
text = "नमस्ते, आप कैसे हैं?"

# Convert text to speech
engine.say(text)

# Wait until the speech is finished
engine.runAndWait()
