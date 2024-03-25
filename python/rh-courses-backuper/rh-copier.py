from pathlib import Path
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from config import login, password, base_dir


def main():
    login_url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/auth?response_type=code&client_id=rha-webapp-prod&redirect_uri=https%3A%2F%2Frha.ole.redhat.com%2Frha%2Fauth_idp%2F%40%40redirect&scope=profile+openid+web-origins+email+roles&state=XKqAGhPaFmbskCaH0pSSylN2CC62ib"
    urls = [
        "https://rha.ole.redhat.com/rha/app/courses/rh124-9.0/pages/ch01/18f37888-071d-4852-8fd6-c85d11d6738d",
        "https://rha.ole.redhat.com/rha/app/courses/rh134-9.0/pages/ch01/e646eaaf-c548-43fd-bf91-e87e6183576a",
        "https://rha.ole.redhat.com/rha/app/courses/rh294-9.0/pages/ch01/eddbf461-68f8-4474-b85f-5a1070cbf223",
    ]

    driver = Chrome()
    driver.get(login_url)

    login_field = driver.find_element(By.ID, "username-verification")
    login_field.send_keys(login)

    submit_btn = driver.find_element(By.ID, "login-show-step2")
    submit_btn.click()

    element_clickable = EC.element_to_be_clickable(
        (By.ID, "rh-password-verification-submit-button")
    )
    try:
        submit_btn = WebDriverWait(driver, 15).until(element_clickable)
    except TimeoutException:
        print("Error: Time out! Exiting...")
        exit()

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    submit_btn.click()

    for url in urls:
        course_folder = Path(f"{base_dir}/{url.split('/')[6].split('-')[0]}")

        if not course_folder.exists():
            course_folder.mkdir()

        while url:
            print(f"Copying: {url}...")
            driver.get(url)
            file_name = course_folder.joinpath(url.split("/")[8])

            element_present = EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "next-btn")
            )
            try:
                next_btns = WebDriverWait(driver, 10).until(element_present)
                url = next_btns[0].get_attribute("href")
            except TimeoutException:
                print(
                    "Info: Can't find the next page's button, seems it's the last page!"
                )
                url = None

            with open(f"{file_name}.html", "w", encoding="utf-8-sig") as f:
                f.write(driver.page_source)

    driver.quit()


if __name__ == "__main__":
    main()
