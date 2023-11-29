import os

def create_desktop_file(url, name):
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    desktop_file_path = os.path.join(desktop_path, f'{name}.desktop')

    desktop_file_content = f"""[Desktop Entry]
Name={name}
Exec=xdg-open {url}
Type=Application
"""

    with open(desktop_file_path, 'w') as desktop_file:
        desktop_file.write(desktop_file_content)

    print(f"Desktop file created at: {desktop_file_path}")

def main():
    url = input("Enter the URL: ")
    name = input("Enter the name for the desktop icon, this is not a photo: ")

    create_desktop_file(url, name)

if __name__ == "__main__":
    main()
