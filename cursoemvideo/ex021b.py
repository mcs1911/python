import simpleaudio as sa

# Load the audio file
wave_obj = sa.WaveObject.from_wave_file("pon.mp3")  # Replace with your file path

# Play the audio
play_obj = wave_obj.play()

# Wait for playback to finish (optional)
play_obj.wait_done()
