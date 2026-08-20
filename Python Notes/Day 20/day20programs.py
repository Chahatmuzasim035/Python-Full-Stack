
# ============================================================
# DAY 20
# FILE OPERATIONS, DIRECTORIES AND EMAIL AUTOMATION
# ============================================================


# ============================================================
# PART A - FILE OPERATIONS
# ============================================================

import os
import shutil


# ------------------------------------------------------------
# 1. CREATE AND WRITE TO A FILE
# ------------------------------------------------------------

print("\n1. Creating and writing to a file")

with open("example.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is file handling practice.")

print("File created successfully")


# ------------------------------------------------------------
# 2. READ THE COMPLETE FILE
# ------------------------------------------------------------

print("\n2. Reading complete file")

with open("example.txt", "r") as file:
    content = file.read()

print(content)


# ------------------------------------------------------------
# 3. READ ONE LINE
# ------------------------------------------------------------

print("\n3. Reading one line")

with open("example.txt", "r") as file:
    line = file.readline()

print(line)


# ------------------------------------------------------------
# 4. READ ALL LINES
# ------------------------------------------------------------

print("\n4. Reading all lines")

with open("example.txt", "r") as file:
    lines = file.readlines()

print(lines)


# ------------------------------------------------------------
# 5. APPEND DATA
# ------------------------------------------------------------

print("\n5. Appending data")

with open("example.txt", "a") as file:
    file.write("\nThis line was added later.")

print("Data appended successfully")


# ------------------------------------------------------------
# 6. READ AFTER APPENDING
# ------------------------------------------------------------

print("\n6. Reading updated file")

with open("example.txt", "r") as file:
    print(file.read())


# ------------------------------------------------------------
# 7. WRITE MULTIPLE LINES USING writelines()
# ------------------------------------------------------------

print("\n7. Using writelines()")

languages = [
    "Python\n",
    "Java\n",
    "C++\n",
    "JavaScript\n"
]

with open("languages.txt", "w") as file:
    file.writelines(languages)

print("Multiple lines written")


# ------------------------------------------------------------
# 8. CHECK WHETHER A FILE EXISTS
# ------------------------------------------------------------

print("\n8. Checking file existence")

if os.path.exists("example.txt"):
    print("example.txt exists")
else:
    print("example.txt does not exist")


# ------------------------------------------------------------
# 9. FILE SIZE
# ------------------------------------------------------------

print("\n9. File size")

if os.path.exists("example.txt"):
    size = os.path.getsize("example.txt")
    print("Size:", size, "bytes")


# ------------------------------------------------------------
# 10. ABSOLUTE FILE PATH
# ------------------------------------------------------------

print("\n10. Absolute path")

print(os.path.abspath("example.txt"))


# ------------------------------------------------------------
# 11. os.path.join()
# ------------------------------------------------------------

print("\n11. Creating a file path")

folder = "Documents"

file_path = os.path.join(folder, "notes.txt")

print(file_path)


# ------------------------------------------------------------
# 12. CREATE A DIRECTORY
# ------------------------------------------------------------

print("\n12. Creating directory")

if not os.path.exists("Documents"):
    os.mkdir("Documents")
    print("Documents folder created")
else:
    print("Documents folder already exists")


# ------------------------------------------------------------
# 13. CREATE A FILE INSIDE DIRECTORY
# ------------------------------------------------------------

print("\n13. Creating file inside directory")

document_path = os.path.join("Documents", "notes.txt")

with open(document_path, "w") as file:
    file.write("Python file stored inside a folder.")

print("File created:", document_path)


# ------------------------------------------------------------
# 14. CREATE NESTED DIRECTORIES
# ------------------------------------------------------------

print("\n14. Creating nested directories")

nested_path = os.path.join("Project", "Data", "Files")

if not os.path.exists(nested_path):
    os.makedirs(nested_path)
    print("Nested directories created")
else:
    print("Nested directories already exist")


# ------------------------------------------------------------
# 15. LIST DIRECTORY CONTENTS
# ------------------------------------------------------------

print("\n15. Directory contents")

for item in os.listdir("."):
    print(item)


# ------------------------------------------------------------
# 16. LIST CONTENTS OF DOCUMENTS
# ------------------------------------------------------------

print("\n16. Documents folder contents")

if os.path.exists("Documents"):

    for item in os.listdir("Documents"):
        print(item)


# ------------------------------------------------------------
# 17. RAW STRING PATH
# ------------------------------------------------------------

print("\n17. Raw string path")

windows_path = r"C:\Users\Student\Documents\notes.txt"

print(windows_path)


# ------------------------------------------------------------
# 18. r+ MODE
# ------------------------------------------------------------

print("\n18. r+ mode")

with open("read_write.txt", "w") as file:
    file.write("Original content.")

with open("read_write.txt", "r+") as file:

    content = file.read()

    print("Before:", content)

    file.write("\nNew content added.")


# ------------------------------------------------------------
# 19. w+ MODE
# ------------------------------------------------------------

print("\n19. w+ mode")

with open("write_read.txt", "w+") as file:

    file.write("Data written using w+.")

    file.seek(0)

    print(file.read())


# ------------------------------------------------------------
# 20. a+ MODE
# ------------------------------------------------------------

print("\n20. a+ mode")

with open("append_read.txt", "a+") as file:

    file.write("New appended data.\n")

    file.seek(0)

    print(file.read())


# ------------------------------------------------------------
# 21. REMOVE A FILE
# ------------------------------------------------------------

print("\n21. Removing a file")

if os.path.exists("languages.txt"):

    os.remove("languages.txt")

    print("languages.txt removed")


# ------------------------------------------------------------
# 22. REMOVE AN EMPTY DIRECTORY
# ------------------------------------------------------------

print("\n22. Removing empty directory")

empty_folder = "EmptyFolder"

if not os.path.exists(empty_folder):
    os.mkdir(empty_folder)

if os.path.exists(empty_folder):
    os.rmdir(empty_folder)
    print("Empty folder removed")


# ------------------------------------------------------------
# 23. SHUTIL - REMOVE NON-EMPTY DIRECTORY
# ------------------------------------------------------------

print("\n23. shutil.rmtree() example")

delete_folder = "DeleteMe"

if not os.path.exists(delete_folder):

    os.makedirs(delete_folder)

    with open(
        os.path.join(delete_folder, "file.txt"),
        "w"
    ) as file:

        file.write("Temporary data.")

if os.path.exists(delete_folder):

    shutil.rmtree(delete_folder)

    print("Folder and its contents removed")


# ============================================================
# PART B - EMAIL SENDING
# ============================================================

import smtplib
from email.message import EmailMessage


# ------------------------------------------------------------
# 24. EMAIL DETAILS
# ------------------------------------------------------------

sender_email = "your_email@gmail.com"

receiver_email = "receiver@example.com"

app_password = "your_app_password_here"


# ------------------------------------------------------------
# 25. CREATE EMAIL MESSAGE
# ------------------------------------------------------------

print("\n24. Creating email message")

subject = "Python Email Test"

body = """Hello,

This is an email generated using Python.

Regards,
Python Learner
"""

msg = EmailMessage()

msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

msg.set_content(body)

print("Email message created")


# ------------------------------------------------------------
# 26. SEND EMAIL USING GMAIL SMTP
# ------------------------------------------------------------

print("\n25. Sending email")

try:

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465
    ) as smtp:

        smtp.login(
            sender_email,
            app_password
        )

        smtp.send_message(msg)

    print("Email sent successfully!")

except Exception as e:

    print("Error sending email:", e)


# ------------------------------------------------------------
# 27. EMAIL USING USER INPUT
# ------------------------------------------------------------

print("\n26. Email using user input")

receiver = input(
    "Enter receiver email: "
)

subject = input(
    "Enter subject: "
)

body = input(
    "Enter message: "
)

user_message = EmailMessage()

user_message["Subject"] = subject

user_message["From"] = sender_email

user_message["To"] = receiver

user_message.set_content(body)


# Uncomment the following section when you want
# to actually send the user-input email.

# try:
#
#     with smtplib.SMTP_SSL(
#         "smtp.gmail.com",
#         465
#     ) as smtp:
#
#         smtp.login(
#             sender_email,
#             app_password
#         )
#
#         smtp.send_message(user_message)
#
#     print("Custom email sent successfully!")
#
# except Exception as e:
#
#     print("Error:", e)


# ------------------------------------------------------------
# 28. EMAIL SENDING FUNCTION
# ------------------------------------------------------------

def send_email(receiver, subject, body):

    message = EmailMessage()

    message["Subject"] = subject

    message["From"] = sender_email

    message["To"] = receiver

    message.set_content(body)

    try:

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:

            smtp.login(
                sender_email,
                app_password
            )

            smtp.send_message(message)

        print("Email sent successfully!")

    except Exception as e:

        print("Error sending email:", e)


# Example:
#
# send_email(
#     "receiver@example.com",
#     "Reminder",
#     "This is your reminder."
# )


# ------------------------------------------------------------
# 29. READ EMAIL ADDRESSES FROM A FILE
# ------------------------------------------------------------

print("\n27. Reading email addresses from a file")

recipient_file = "recipients.txt"

if os.path.exists(recipient_file):

    with open(recipient_file, "r") as file:

        recipients = file.readlines()

    for email in recipients:

        email = email.strip()

        if email:
            print("Recipient:", email)

else:

    print(
        "recipients.txt not found."
    )


# ------------------------------------------------------------
# 30. SCHEDULED EMAIL
# ------------------------------------------------------------
#
# Install schedule first:
#
# pip install schedule
#
# Then remove the comments below to use scheduling.


# import schedule
# import time


# def scheduled_email():

#     receiver = "receiver@example.com"

#     subject = "Daily Reminder"

#     body = """Hello,
#
# This is your scheduled reminder.
#
# Have a great day!
# """

#     message = EmailMessage()

#     message["Subject"] = subject
#     message["From"] = sender_email
#     message["To"] = receiver

#     message.set_content(body)


#     try:

#         with smtplib.SMTP_SSL(
#             "smtp.gmail.com",
#             465
#         ) as smtp:

#             smtp.login(
#                 sender_email,
#                 app_password
#             )

#             smtp.send_message(message)

#         print("Scheduled email sent!")

#     except Exception as e:

#         print("Error:", e)


# Schedule every day at 10:00 AM
#
# schedule.every().day.at(
#     "10:00"
# ).do(scheduled_email)


# Keep scheduler running
#
# while True:
#
#     schedule.run_pending()
#
#     time.sleep(60)


# ============================================================
# END OF DAY 20
# ============================================================