# Facade Design Pattern Example
# -----------------------------
# The Facade pattern provides a simplified interface to a library, a
# framework, or any other complex set of classes. It hides the complexities
# of the subsystem and provides a single, simpler entry point for the client.
# This promotes loose coupling between the client and the subsystem.

# Complex Subsystem Classes
# These classes represent parts of a complex system that the client might
# interact with. In a real-world scenario, these could be intricate libraries
# or modules with many functionalities.

class VideoFile:
    """
    Represents a video file.
    In a real system, this class might handle file parsing, metadata extraction, etc.
    This is part of the complex subsystem.
    """
    def __init__(self, filename: str):
        """
        Initializes the VideoFile object.

        Args:
            filename (str): The name of the video file.
        """
        self.filename = filename
        # Simulate determining codec type from filename extension
        self.codec_type = filename.split('.')[-1] if '.' in filename else "unknown"
        print(f"VideoFile: Loaded '{self.filename}' with codec '{self.codec_type}'.")

    def get_codec_type(self) -> str:
        """Gets the (simulated) codec type of the video file."""
        return self.codec_type

    def __str__(self) -> str:
        """String representation of the VideoFile."""
        return self.filename


class AudioMixer:
    """
    Handles audio processing tasks.
    In a real system, this might involve volume normalization, noise reduction, etc.
    This is part of the complex subsystem.
    """
    def fix_audio(self, video_file: VideoFile) -> str:
        """
        Simulates processing and fixing audio for a given video file.

        Args:
            video_file (VideoFile): The video file whose audio needs processing.

        Returns:
            str: A string representing the processed audio data.
        """
        print(f"AudioMixer: Processing audio for '{video_file.filename}'.")
        # Simulate audio processing
        processed_audio_data = f"fixed_audio_for_{video_file.filename.split('.')[0]}"
        print(f"AudioMixer: Audio processing complete for '{video_file.filename}'.")
        return processed_audio_data


class Encoder:
    """
    Handles video and audio encoding tasks.
    In a real system, this would involve complex algorithms for compressing
    and converting media formats.
    This is part of the complex subsystem.
    """
    def encode(self, video_file: VideoFile, target_format: str, audio_data: str) -> str:
        """
        Simulates encoding a video file to a target format.

        Args:
            video_file (VideoFile): The video file to encode.
            target_format (str): The desired output format (e.g., "avi", "mkv").
            audio_data (str): The processed audio data to be included.

        Returns:
            str: The filename of the (simulated) converted video file.
        """
        print(f"Encoder: Starting encoding for '{video_file.filename}' to '{target_format}'.")
        if video_file.get_codec_type() == target_format:
            print(f"Encoder: Target format '{target_format}' is same as source. No encoding needed.")
            return video_file.filename
        
        # Simulate encoding process
        base_name = video_file.filename.split('.')[0]
        converted_filename = f"{base_name}_converted.{target_format}"
        print(f"Encoder: Processing video data from '{video_file.filename}'.")
        print(f"Encoder: Integrating processed audio: '{audio_data}'.")
        print(f"Encoder: Encoding to '{target_format}' format.")
        print(f"Encoder: Successfully encoded '{video_file.filename}' to '{converted_filename}'.")
        return converted_filename


# Facade Class
class MultimediaConverter:
    """
    The Facade class.
    It provides a simple interface to the complex multimedia conversion subsystem.
    The client interacts with this Facade rather than the subsystem classes directly.
    This simplifies the client's code and decouples it from the internal workings
    of the conversion process.
    """
    def __init__(self):
        """
        Initializes the MultimediaConverter Facade.
        It creates instances of the subsystem classes that it will manage.
        """
        print("MultimediaConverter: Ready to convert multimedia files.")
        self._video_file_cls = VideoFile # Using class for on-demand instantiation
        self._audio_mixer = AudioMixer()
        self._encoder = Encoder()

    def convert(self, original_filename: str, target_format: str) -> str:
        """
        Converts a video file from its original format to a target format.
        This method orchestrates the necessary operations on the subsystem components.

        Args:
            original_filename (str): The name of the video file to convert.
            target_format (str): The desired output format.

        Returns:
            str: The filename of the converted video file.
        """
        print(f"\nMultimediaConverter: Starting conversion of '{original_filename}' to '{target_format}'.")
        
        # 1. Load the video file (subsystem interaction, simplified for client)
        video_file = self._video_file_cls(original_filename)
        
        # 2. Process audio (subsystem interaction, simplified for client)
        # The client doesn't need to know how audio is fixed, just that it happens.
        processed_audio = self._audio_mixer.fix_audio(video_file)
        
        # 3. Encode to new format (subsystem interaction, simplified for client)
        # The client doesn't need to manage the encoder or the processed audio directly.
        converted_file = self._encoder.encode(video_file, target_format, processed_audio)
        
        print(f"MultimediaConverter: Conversion complete. Output file: '{converted_file}'.")
        return converted_file


# Client Code Example
# The client code uses the Facade (MultimediaConverter) to perform complex operations
# (video conversion) without needing to understand or interact with the individual
# subsystem components (VideoFile, AudioMixer, Encoder).
if __name__ == "__main__":
    converter = MultimediaConverter()
    
    converter = MultimediaConverter() # Client interacts with the simple Facade

    # User wants to convert a video file without knowing the complexities
    # of video file handling, audio mixing, or encoding.
    mp4_file = "my_vacation_movie.mp4"
    
    # Create a dummy file for the example to "load"
    # In a real application, this file would already exist.
    try:
        with open(mp4_file, "w") as f:
            f.write("dummy mp4 content for facade example")
    except IOError as e:
        print(f"Error creating dummy file {mp4_file}: {e}")
        # Exit if dummy file can't be created, as example depends on it.
        import sys
        sys.exit(1)

    print(f"\n--- Client Request: Convert '{mp4_file}' to 'avi' format ---")
    # The client makes a single call to the facade's convert method.
    # All the complex steps are handled internally by the facade.
    avi_file = converter.convert(mp4_file, "avi")
    print(f"Client: Conversion to AVI successful. Output file: '{avi_file}'")

    print(f"\n--- Client Request: Convert '{mp4_file}' to 'mkv' format ---")
    mkv_file = converter.convert(mp4_file, "mkv")
    print(f"Client: Conversion to MKV successful. Output file: '{mkv_file}'")

    # Example of converting to the same format (subsystem should handle this gracefully)
    another_mp4_file = "another_clip.mp4"
    try:
        with open(another_mp4_file, "w") as f:
            f.write("other dummy mp4 content for facade example")
    except IOError as e:
        print(f"Error creating dummy file {another_mp4_file}: {e}")
        # Continue if this dummy file fails, it's a secondary example
    else:
        print(f"\n--- Client Request: Convert '{another_mp4_file}' to 'mp4' (same format) ---")
        same_format_file = converter.convert(another_mp4_file, "mp4")
        print(f"Client: Conversion to MP4 (same format) attempt. Output file: '{same_format_file}'")

    # Clean up dummy files created for the demonstration
    import os
    try:
        if os.path.exists(mp4_file):
            os.remove(mp4_file)
        if os.path.exists(another_mp4_file):
            os.remove(another_mp4_file)
        # Note: The simulated converted files (e.g., *_converted.avi) are not actually
        # written to disk in this example, so no cleanup is needed for them.
        # If they were, we would add:
        # if os.path.exists(avi_file) and avi_file != mp4_file: os.remove(avi_file)
        # if os.path.exists(mkv_file) and mkv_file != mp4_file: os.remove(mkv_file)
    except OSError as e:
        print(f"Error during file cleanup: {e}")

    print("\nFacade pattern example finished.")
