import os
import argparse

def create_desktop_file(url, name, path):
    desktop_file_path = os.path.join(path, f'{name}.desktop')

    desktop_file_content = f"""[Desktop Entry]
Name={name}
Exec=xdg-open {url}
Type=Application
"""

    with open(desktop_file_path, 'w') as desktop_file:
        desktop_file.write(desktop_file_content)

    print(f"Desktop file created at: {desktop_file_path}")

def main():
    parser = argparse.ArgumentParser(description="WebLauncher - Create a desktop icon to open a specified URL.")
    parser.add_argument("url", help="The URL to open")
    parser.add_argument("name", help="The name for the desktop icon")
    parser.add_argument("-p", "--path", help="Specify a custom path for the desktop file")
    parser.add_argument("-h", "--home", action="store_true", help="Put the desktop file on the desktop where the terminal is opened")

    args = parser.parse_args()

    if args.home:
        path = os.path.join(os.path.expanduser('~'), 'Desktop')
    elif args.path:
        path = args.path
    else:
        path = os.path.abspath(os.path.curdir)

    create_desktop_file(args.url, args.name, path)

if __name__ == "__main__":
    main()
