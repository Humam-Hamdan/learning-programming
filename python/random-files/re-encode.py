import os
import subprocess


def convert_mp3_to_opus_ogg(root_dir: str):
    """Convert all .mp3 files in root_dir to Ogg Opus (.ogg) using automatic VBR."""
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(".mp3"):
                mp3_path = os.path.join(dirpath, filename)
                base_name = os.path.splitext(filename)[0]
                ogg_path = os.path.join(dirpath, f"{base_name}.ogg")

                if os.path.exists(ogg_path):
                    print(f"Skipping (already exists): {ogg_path}")
                    continue

                print(f"Converting (auto‑bitrate): {mp3_path}")

                try:
                    subprocess.run(
                        [
                            "ffmpeg",
                            "-y",
                            "-i",
                            mp3_path,
                            "-vn",
                            "-ac",
                            "1",
                            "-c:a",
                            "libopus",
                            "-vbr",
                            "on",
                            "-application",
                            "voip",
                            "-compression_level",
                            "10",
                            ogg_path,
                        ],
                        check=True,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.STDOUT,
                    )
                    print(f"✅ Done: {ogg_path}\n")

                except subprocess.CalledProcessError:
                    print(f"❌ Conversion failed for {mp3_path}\n")


if __name__ == "__main__":
    folder = input("Enter directory to scan for .mp3 files: ").strip()
    if not os.path.isdir(folder):
        print("Error: Provided path is not a valid directory.")
    else:
        convert_mp3_to_opus_ogg(folder)
        print("All conversions completed.")
