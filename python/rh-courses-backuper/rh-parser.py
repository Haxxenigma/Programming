from os import listdir
from bs4 import BeautifulSoup
from config import base_dir


def main():
    folders = ["rh124", "rh134", "rh294"]

    for folder in folders:
        course_folder = f"{base_dir}\\{folder}"
        for file in listdir(course_folder):
            course_file = f"{course_folder}\\{file}"
            print(f"Parsing: {course_file}...")

            with open(course_file, "r") as f:
                html = f.read()
                soup = BeautifulSoup(html, "html.parser")
                navigation_bar = soup.find("div", {"class": "navigation"})

                if navigation_bar is None:
                    print("ERROR: Can't find navigation bar, skipping...")
                    continue

                sibling = navigation_bar.find_next_sibling("div")

            with open(course_file, "w") as f:
                print(f"Writing: {course_file}...")
                f.write(str(sibling))


if __name__ == "__main__":
    main()
