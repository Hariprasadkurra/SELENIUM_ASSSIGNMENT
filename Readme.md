🧠 Python (Selenium) Assignment — Automated Google Form Filler
👨‍💻 Author

Kurra Hari Lakshmi Prasad

📋 Assignment Overview

This project automates the process of filling out a Google Form using Python and Selenium WebDriver.
The automation script:

Opens the provided Google Form.

Fills in all the required fields (text, textarea, date, etc.) automatically.

Submits the form.

Captures and saves a screenshot of the confirmation page.

🚀 Steps Implemented
✅ Step 1: Code to Automatically Fill a Google Form

Used Selenium WebDriver with ChromeDriver (auto-managed by webdriver_manager).

Script dynamically detects and fills:

Text fields (input[type='text'])

Email fields (input[type='email'])

Date fields (input[type='date'])

Textareas (for long answers like addresses)

Each field is matched by its label text, ensuring correct field mapping.

✅ Step 2: Used Code to Fill the Form

URL used: https://forms.gle/WT68aV5UnPajeoSc8

All fields were filled automatically using sample data such as:

Full Name

Contact Number

Email ID

Full Address

Pin Code

Date of Birth

Gender

Code

✅ Step 3: Captured Screenshot

The script takes a screenshot of the confirmation page after submission and saves it as confirmation.png.

🧩 Tech Stack
Component	Technology Used
Programming Language	Python 3
Automation Framework	Selenium WebDriver
Browser Driver	ChromeDriver (auto-installed)
Package Manager	pip
Additional Libraries	webdriver_manager, time
⚙️ Setup Instructions

Clone the repository

git clone https://github.com/Hariprasadkurra/SELENIUM_ASSSIGNMENT
cd selenium-form-automation


Install dependencies

pip install -r requirements.txt


Run the script

python auto_fill_form.py


Output

The form will be filled and submitted automatically.

Screenshot will be saved as:

confirmation.png
## Screenshot of Form Submission

![Form Submission Confirmation](confirmation.png)




Python (Selenium) Assignment - Kurra Hari Lakshmi Prasad

🧾 Project Structure
📁 selenium-form-automation

├── fill_form.py  

├── requirements.txt  

├── confirmation.png

└── README.md                

🧠 Brief Explanation of Approach

Dynamic Field Detection:
Instead of relying on field order, the script scans each form question’s label (div[role='heading']) and fills the matching input/textarea.
This ensures robustness even if the field order changes.

Browser Control:
webdriver_manager automatically installs the correct ChromeDriver version.
The browser opens, fills the form, and submits it with realistic typing delays.

Proof of Execution:

🕒 Availability

✅ Available to work full-time (10 AM to 7 PM) for the next 3–6 months.
