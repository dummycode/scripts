import subprocess

def main():
    print("Converting all HEIC files to PNG")

    subprocess.run('magick mogrify -monitor -format png *.HEIC'.split(' '))


if __name__ == "__main__":
    main()
