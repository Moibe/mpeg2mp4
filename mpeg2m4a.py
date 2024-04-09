import subprocess

# Define input and output filenames
input_file = "file.mpeg"
output_file = "final.m4a"

# Command to use ffmpeg for conversion
ffmpeg_command = ["ffmpeg", "-i", input_file, "-c:a copy", "-c:v copy", output_file]

# Run ffmpeg using subprocess
try:
  subprocess.run(ffmpeg_command, check=True)
  print(f"Conversion successful! {input_file} converted to {output_file}")
except subprocess.CalledProcessError as error:
  print(f"Error converting file: {error}")
