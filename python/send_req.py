from requests import request, exceptions
from os.path import dirname, realpath
from re import search, IGNORECASE
from pathlib import Path
from sys import argv

base_dir = Path(dirname(realpath(__file__)))
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
}


def extract_tag_content(html: str, tag: str):
    res = None
    re_obj = search(f"<{tag}>.*</{tag}>", html, flags=IGNORECASE)

    if re_obj:
        res = re_obj.group().split(">")[1].split("<")[0]

    return res


def send_request(
    url: str,
    method: str = "GET",
    params: dict = {},
    data: dict = {},
    write_output: bool = False,
):
    try:
        response = request(method, url, params=params, headers=headers, json=data)
    except exceptions.ConnectionError as e:
        print(f"Connection Error: {e}")
        return
    except (exceptions.InvalidSchema, exceptions.InvalidURL):
        print(
            "Please provide the correct URL as 'http(s)://<domain|ip-addr>[/path/to/resource]'"
        )
        return

    title = extract_tag_content(response.text, "title")
    result = f"{url}: {response.status_code}/{response.reason}"
    if title:
        result += f" | {title}"

    if write_output:
        file_name = base_dir.joinpath(url.split("/")[2] + ".html")
        with open(file_name, "w") as f:
            f.write(response.text)

    return result


def main():
    url = argv[1] if (len(argv) > 1) else "https://www.google.com/"
    result = send_request(url)
    print(result)


if __name__ == "__main__":
    main()
