import json
import shutil
import textwrap
import cv2
import requests
from get_latest_using_scraping import fetch_latest_news_from_scraping
from moviepy import (
    CompositeVideoClip,
    ImageClip,
    AudioFileClip,
    TextClip,
    VideoFileClip,
)
import os
from gtts import gTTS
import os
from moviepy import VideoFileClip, concatenate_videoclips
from datetime import datetime
import random


# Your NewsAPI API Access Key
API_KEY = "908a662f92a9493d9c7cd3d90d304046"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"


def resize_video(clip, target_resolution=(1280, 720)):
    """
    Resize the video clip to the target resolution.
    """
    return clip.resized(target_resolution)


def merge_videos(video_paths, output_path, target_resolution=(1280, 720), fps=30):
    # Load all the videos from the given paths
    clips = []

    for video in video_paths:
        clip = VideoFileClip(video)

        # Resize video to the target resolution
        clip = resize_video(clip, target_resolution)

        # Set the same frame rate for all clips
        clip = clip.with_fps(fps)

        # Append the clip to the list
        clips.append(clip)

    # Concatenate the video clips
    final_clip = concatenate_videoclips(clips)

    # Write the final video to the output path
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    print(f"Merged video saved to {output_path}")


def find_mp4_files(root_folder):
    # List to store the paths of all .mp4 files
    mp4_files = []

    # Walk through the directory and subdirectories
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".mp4"):
                # Join the directory path and file name to get the full file path
                mp4_files.append(os.path.join(dirpath, filename))

    return mp4_files


def clear_folder(folder_path):
    # Remove all contents of the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # If it's a file, delete it
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        # If it's a subdirectory, delete it
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path, ignore_errors=True)
            print(f"Deleted directory: {file_path}")


# Function to fetch the latest news and download images
def fetch_news_and_download_images_using_rest_api(
    query=None,
    num_articles=5,
    download_folder=r"C:\Users\pradhana\OneDrive - Intel Corporation\Desktop\personal\eclipse_pyats\PythonAlgoProject\.settings\Amazon_Practice\trend_video_project\news_images",
):
    # Create folder if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # delete all the files from the folder
    clear_folder(download_folder)

    # Prepare search parameters for the API
    params = {
        "apiKey": API_KEY,
        "q": query,  # This is the keyword for news (e.g., "world", "technology")
        "pageSize": num_articles,  # Number of articles to fetch
    }

    # Send GET request to NewsAPI
    # response = requests.get(NEWS_API_URL, params=params)

    url = "http://newsapi.org/v2/top-headlines?country=us"
    url = "https://newsapi.org/v2/top-headlines?sources=the-hindu&pageSize=10"
    url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&pageSize=10"
    headers = {
        "Authorization": "Bearer 908a662f92a9493d9c7cd3d90d304046",  # If an API key/token is needed
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        headlines_with_images = []
        if data["totalResults"] > 0:
            for i, article in enumerate(data["articles"]):
                # Get image URL from the article
                image_url = article.get("urlToImage")
                headline = article.get("title")
                if image_url:
                    # Download the image
                    image_response = requests.get(image_url)
                    if image_response.status_code == 200:
                        # Write image to disk
                        image_path = os.path.join(download_folder, f"image_{i+1}")
                        if not os.path.exists(image_path):
                            os.makedirs(image_path)
                        clear_folder(image_path)
                        # add current timestamp to file name
                        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
                        image_path = os.path.join(
                            image_path, f"image_{i+1}_{timestamp}.jpg"
                        )

                        with open(image_path, "wb") as file:
                            file.write(image_response.content)
                        print(f"Downloaded image for article {i+1}: {image_path}")
                        headlines_with_images.append((i + 1, headline, image_path))
                    else:
                        print(f"Failed to download image for article {i+1}")
                else:
                    print(f"No image found for article {i+1}")
        else:
            print("No articles found.")
    else:
        print(f"Error fetching news articles: {response.status_code}")

    return headlines_with_images


# Function to fetch the latest news and download images
def fetch_news_and_download_images_from_scraping(
    articles,
    download_folder=r"C:\Users\pradhana\OneDrive - Intel Corporation\Desktop\personal\eclipse_pyats\PythonAlgoProject\.settings\Amazon_Practice\trend_video_project\news_images",
):
    # Create folder if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # delete all the files from the folder
    clear_folder(download_folder)

    # List of user-agent strings to simulate different browsers
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; rv:40.0) Gecko/20100101 Firefox/40.0",
    ]

    headers = {
        "User-Agent": random.choice(
            user_agents
        )  # Randomize User-Agent for each request
    }

    articles_with_images = []
    for article in articles:
        # Get image URL from the article
        image_urls = article.get("urlToImage")
        headline = article.get("title")
        if image_urls:
            # for multiple images for a single article
            # Check if the image folder is not present , then create one
            image_path = os.path.join(download_folder, f"image_{article['id']}")
            if not os.path.exists(image_path):
                os.makedirs(image_path)

            # Clear the old content of the folder
            clear_folder(image_path)
            all_images_path = []
            for image_index, image_url in enumerate(image_urls):
                # Download the image
                image_response = requests.get(image_url)
                if image_response.status_code == 200:

                    # add current timestamp to file name
                    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
                    current_image_path = os.path.join(
                        image_path,
                        f"image_{article['id']}_{image_index}_{timestamp}.jpg",
                    )

                    with open(current_image_path, "wb") as file:
                        file.write(image_response.content)
                    print(
                        f"Downloaded image for article id {article['id']}: {current_image_path}"
                    )
                    all_images_path.append(image_path)
                else:
                    print(f"Failed to download image for article id {article['id']}")
            article["image_downloaded_path"] = all_images_path
            articles_with_images.append(article)
        else:
            print(f"No image found for article id {article['id']}")
    else:
        print("No articles found.")

    return articles_with_images[:10]


# Example usage: Fetch latest articles about "technology" and download images
# fetch_news_and_download_images_using_rest_api('technology', num_articles=5)


def generate_script(news_list):
    # script = "Here are today's top trending news headlines:\n\n"
    script = ""
    for i, news_item, image in news_list:
        script += f"{news_item}\n"
    return script


def text_to_speech(
    text,
    article_id,
    audio_folder="news_images/audio/",
):
    # Create the audio folder if not created
    audio_path = os.path.join(audio_folder, f"audio_{article_id}")

    if not os.path.exists(audio_path):
        os.makedirs(audio_path)

    clear_folder(audio_path)

    audio_path = os.path.join(audio_path, f"audio_{article_id}.mp3")
    # Just the 1st paragraph
    tts = gTTS(text=text[0], lang="en")
    tts.save(audio_path)


def create_video(image_file, audio_file, output_file="video.mp4"):
    image_clip = ImageClip(image_file, duration=10)
    audio_clip = AudioFileClip(audio_file)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.write_videofile(output_file, fps=24)


def create_video_from_images_and_audio(
    headlines, image_folder, output_video_path, audio_path, article_id
):
    # Load image files from the folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith(".jpg")]
    image_files.sort()  # Ensure images are sorted alphabetically (or by some naming convention)

    # Check if there are any images
    if len(image_files) == 0:
        print("No images found in the folder!")
        return

    # Read the first image to get the width and height
    first_image = cv2.imread(os.path.join(image_folder, image_files[0]))
    height, width, _ = first_image.shape

    # Create video folder if not present and clear the content
    if not os.path.exists(output_video_path):
        os.makedirs(output_video_path)
    clear_folder(output_video_path)

    output_video_file = os.path.join(output_video_path, f"video_{article_id}.mp4")

    # Initialize video writer (We use 1 fps initially to write frames for each image)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(output_video_file, fourcc, 1, (width, height))

    # Add each image to the video
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        frame = cv2.imread(image_path)

        if frame is None:
            print(f"Failed to read image: {image_file}")
            continue

        # Resize frame to match video size if necessary
        if frame.shape[1] != width or frame.shape[0] != height:
            frame = cv2.resize(frame, (width, height))

        video_writer.write(frame)  # Write each image as a frame in the video

    # Release video writer after adding all images
    video_writer.release()

    # Now, integrate the audio using MoviePy
    video_clip = VideoFileClip(output_video_file)
    audio_clip = AudioFileClip(audio_path)

    # Calculate duration for each image based on audio length
    duration_per_image = audio_clip.duration / len(image_files)

    # Set each image duration
    video_clip = video_clip.with_duration(duration_per_image * len(image_files))

    # Adjust the audio duration to match the video length
    video_duration = video_clip.duration
    audio_clip = audio_clip.subclipped(0, video_duration)

    # Set the audio of the video clip
    video_clip = video_clip.with_audio(audio_clip)

    # Add the headline text as overlay
    headline_text = "Today's Top HeadLines"

    footer_text = str(headlines)  # Set your footer text

    # Calculate the maximum number of characters that can fit based on video width
    # Assuming each character takes up approximately 10px in width (you can adjust this factor)
    char_width = 5
    max_width = video_clip.w - 40  # Leave some margin on both sides (20px total)
    max_chars_per_line = max_width // char_width

    # Wrap the header and footer text based on the calculated max width
    wrapped_header_text = textwrap.fill(headline_text, width=max_chars_per_line)
    wrapped_footer_text = textwrap.fill(footer_text, width=max_chars_per_line)

    # Create the text clip for the headline
    header = TextClip(
        font="C:\\Windows\\Fonts\\Arial.ttf",
        text=wrapped_header_text,
        font_size=20,
        color="white",
        size=(video_clip.w, 100),  # Set height of the footer clip to 100 pixels
        method="caption",
    )

    # Create the footer text clip
    footer = TextClip(
        font="C:\\Windows\\Fonts\\Arial.ttf",
        text=wrapped_footer_text,
        font_size=10,  # Adjust text size for footer
        color="white",
        size=(video_clip.w, 100),  # Set height of the footer clip to 100 pixels
        method="caption",
    )

    # Set the position for header and footer
    header = header.with_position(("center", "top")).with_duration(video_clip.duration)
    footer = footer.with_position(("center", video_clip.size[1] - 90)).with_duration(
        video_clip.duration
    )  # Footer with margin from bottom

    # Combine the video with the header and footer
    final_video = CompositeVideoClip([video_clip, header, footer])

    # Write the final video with audio and text overlay
    final_video.write_videofile(output_video_file, codec="libx264", audio_codec="aac")

    print(f"Video with audio and text overlay saved to {output_video_file}")


# # Main pipeline
print("Getting latest news from ")
# news = get_latest_news()
# news = fetch_news_and_download_images_using_rest_api()


# Clear news_images,video and audio folder
clear_folder(
    r"C:\Users\pradhana\OneDrive - Intel Corporation\Desktop\personal\eclipse_pyats\PythonAlgoProject\.settings\Amazon_Practice\trend_video_project\news_images"
)
clear_folder(
    r"C:\Users\pradhana\OneDrive - Intel Corporation\Desktop\personal\eclipse_pyats\PythonAlgoProject\.settings\Amazon_Practice\trend_video_project\video"
)
clear_folder(
    r"C:\Users\pradhana\OneDrive - Intel Corporation\Desktop\personal\eclipse_pyats\PythonAlgoProject\.settings\Amazon_Practice\trend_video_project\audio"
)

# Scraping section
url = "https://www.bbc.com/news"  # Replace with any news URL
articles = fetch_latest_news_from_scraping(url)
articles_with_image_download_path = fetch_news_and_download_images_from_scraping(
    articles
)
# print(articles_with_image_download_path)
# add current timestamp to file name
timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

with open(
    rf"C:\Users\pradhana\OneDrive - Intel Corporation\Desktop\personal\eclipse_pyats\PythonAlgoProject\.settings\Amazon_Practice\trend_video_project\articles_with_image_download_path_{timestamp}.json",
    "w",
) as file:
    json.dump(articles_with_image_download_path, file, indent=4, sort_keys=True)

print("Generating Speech from Text")

# script = generate_script(news)
for article in articles_with_image_download_path:
    text_to_speech(
        article["description"],
        article["id"],
        r"C:\Users\pradhana\OneDrive - Intel Corporation\Desktop\personal\eclipse_pyats\PythonAlgoProject\.settings\Amazon_Practice\trend_video_project\audio",
    )
    create_video_from_images_and_audio(
        article["title"],
        image_folder=rf"C:\Users\pradhana\OneDrive - Intel Corporation\Desktop\personal\eclipse_pyats\PythonAlgoProject\.settings\Amazon_Practice\trend_video_project\news_images\image_{article['id']}",
        output_video_path=rf"C:\Users\pradhana\OneDrive - Intel Corporation\Desktop\personal\eclipse_pyats\PythonAlgoProject\.settings\Amazon_Practice\trend_video_project\video\video_{article['id']}",
        audio_path=rf"C:\Users\pradhana\OneDrive - Intel Corporation\Desktop\personal\eclipse_pyats\PythonAlgoProject\.settings\Amazon_Practice\trend_video_project\audio\audio_{article['id']}\audio_{article['id']}.mp3",
        article_id=article["id"],
    )

mp4_files = find_mp4_files(
    r"C:\Users\pradhana\OneDrive - Intel Corporation\Desktop\personal\eclipse_pyats\PythonAlgoProject\.settings\Amazon_Practice\trend_video_project\video"
)
print(mp4_files)
# add current timestamp to file name
timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
merge_videos(
    mp4_files,
    rf"C:\Users\pradhana\OneDrive - Intel Corporation\Desktop\personal\eclipse_pyats\PythonAlgoProject\.settings\Amazon_Practice\trend_video_project\bbc_output_merged_video_{timestamp}.mp4",
)
# import os
# os.system("start audio.mp3")  # For Windows
# create_video_from_images_and_audio()
# create_video("image.jpg", "audio.mp3")


print("Done creating text to speech")
