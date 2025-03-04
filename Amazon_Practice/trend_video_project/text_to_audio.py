from gtts import gTTS
import os


# Convert to hindi

from googletrans import Translator

# Create a translator object
translator = Translator()

# Text you want to convert to speech
english_text = "The story of the sad caterpillar.\
A sad caterpillar lived on a mango tree in a big garden. She was sad because she was alone and nobody played with her.\
“I am so slow. I cannot jump like the grasshopper, run like the cat, swim like the fish in the garden pond, fly like the bird, and collect sweet nectar like the bees to make honey. I am so useless. Nobody likes me,” the caterpillar said to herself sadly.\
“I can only crawl slowly from leaf to leaf and eat leaves everyday. I cannot go anywhere. It is not fair,” cried the caterpillar.\
So the caterpillar became very angry and unhappy with herself and also with all her animal friends.\
One sunny day, a beautiful butterfly flew into the garden and rested on the mango tree. She saw the sad-looking caterpillar. The beautiful butterfly asked the caterpillar why she looked so sad and unhappy.\
“I am sad because I cannot fly like the bird, jump like the grasshopper, run like the cat or collect sweet nectar to make honey like the bees,” the caterpillar answered in an angry voice.\
“And all I eat are these leaves everyday!”\
The beautiful butterfly smiled and answered the caterpillar.\
“Do not be sad. In a little while you will also be able to fly anywhere you want and to drink sweet nectar from flowers. When I was young, I was like you and when you grow older, you will be as beautiful as me.”\
“Believe me and be patient,” smiled the butterfly.\
Then the butterfly flew away."

# Translate to Hindi
translated_text = translator.translate(english_text, src='en', dest='hi')
translated_text = translated_text.text

print(translated_text)
 
# Set the language to Hindi (or any Indian language)
language = 'hi'  # 'hi' for Hindi, 'ta' for Tamil, 'te' for Telugu, etc.


file_path = "output2.mp3" 
if os.path.exists(file_path):
    os.remove(file_path)  # Delete the file
    print(f"{file_path} has been deleted.")
else:
    print(f"{file_path} does not exist.")

# Create the gTTS object
tts = gTTS(text=translated_text, lang=language, slow=True)
    
# Save the audio file
tts.save("output2.mp3")

# Play the generated speech (For Windows use `start`, for Linux/Mac use `mpg321` or `afplay`)
os.system("start output2.mp3")  # For Windows
# For Linux/Mac, use: os.system("mpg321 output.mp3")
