from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# ✅ Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://forms.gle/WT68aV5UnPajeoSc8")
driver.maximize_window()
time.sleep(3)

# ✅ Your form data
details = {
    "Full Name": "Hari Kumar",
    "Contact Number": "9876543210",
    "Email ID": "hari@example.com",
    "Full Address": "123, MG Road, Chennai, Tamil Nadu",
    "Pin Code": "600001",
    "Date of Birth": "2000-01-01",  # IMPORTANT: yyyy-mm-dd format for date input
    "Gender": "Male",
    "Code": "GNFPYC"
}

# ✅ Locate each question container
questions = driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")

for q in questions:
    try:
        label = q.find_element(By.CSS_SELECTOR, "div[role='heading']").text.strip()
        for key, val in details.items():
            if key.lower() in label.lower():
                # Find input or textarea
                try:
                    # Handle text, email, or date
                    box = q.find_element(
                        By.CSS_SELECTOR,
                        "input[type='text'], input[type='email'], input[type='date']"
                    )
                except:
                    # Handle textarea
                    box = q.find_element(By.CSS_SELECTOR, "textarea")
                box.send_keys(val)
                print(f"✅ Filled {key}")
                time.sleep(0.5)
                break
    except Exception as e:
        print(f"⚠️ Skipping one field: {e}")

# ✅ Submit form
submit_button = driver.find_element(By.XPATH, '//span[text()="Submit"]/..')
submit_button.click()
time.sleep(3)

driver.save_screenshot("confirmation.png")
print("✅ Form submitted successfully! Screenshot saved as 'confirmation.png'")

input("Press Enter to close the browser...")
driver.quit()
