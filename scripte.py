import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep


def send_email(recipient_email, user_name, certificate_url):
    # HTML content with placeholders for the student's name and certificate URL
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <body>
        <header>
            <h1 style="text-align: center; color:green;">Mastering C++ Round Certification</h1>
        </header>
        <main style="background-color: #eeeaea; padding: 10px; width: 450px;">
            <p style="font-weight: bold;">Dear {user_name},</p>
            <p style="font-weight: bold;">We are thrilled to extend our heartfelt congratulations to you for successfully completing the "Mastering C++" course! Your dedication and hard work throughout this journey have truly paid off, and we couldn't be prouder of your achievements.</p>
            <p style="font-weight: bold;">As a token of our appreciation, we are pleased to present you with a Certificate of Completion, recognizing your commitment to mastering C++. We hope this achievement will serve as a stepping stone for your future endeavors in the world of programming.</p>
            <p style="font-weight: bold;">We would love to see you continue to grow and participate in future learning opportunities with us. Be sure to stay connected and follow us on our platforms to keep up with the latest updates, courses, and events:</p>
            <p style="font-weight: bold;">Once again, congratulations! We look forward to seeing you excel and hope to have you join us in our upcoming rounds.🤩</p>
            <p style="font-weight: bold; font-size: 15px">Best regards,</p>
            <p style="font-weight: bold; font-size: 15px;">Summarize Administration</p>
            <a href="{certificate_url}" target="_blank" style="font-size: 20px; font-weight: bold; color: rgb(12, 189, 12);">View Your Certificate</a>
            <div class="connection" style="padding-top: 16px;">
                <span style="font-weight: bold; font-size: 20px;">Stay Connected: </span> 
                <a href="https://www.facebook.com/profile.php?id=61561908061240" target="_blank" style="text-decoration: none; font-size: 20px; color: blue; font-weight: bold;">Facebook Page</a>
                <span style="margin-right: 10px;"></span>
                <a href="https://chat.whatsapp.com/F5dKok3uu4PHighLjLuGLy" target="_blank" style="text-decoration: none; font-size: 20px; color: green; font-weight: bold;">Whatsapp Group</a>
            </div>
        </main>
    </body>
    </html>
    """

    # Setting up the email
    msg = MIMEMultipart()
    msg["From"] = f"Summarize Team <{sender_email}>"
    msg["To"] = recipient_email
    msg["Subject"] = subject

    # Attach the HTML content
    msg.attach(MIMEText(html_content, "html"))

    # Sending the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Replace with your SMTP server and port
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print(f"- Email sent successfully to {user_name} ({recipient_email})!" )
    except Exception as e:
        print(f"Failed to send email to {user_name} ({recipient_email}): {e}")

# Email credentials
sender_email = "email@email"
sender_password = "password"  # Consider using environment variables for security
subject = "Mastering C++ Round Certification!"

# List of students with their name, email, and certificate URL
students = []
with open("users.xlsx", "r") as file:
    students = [line.strip().split(",") for line in file]
    
# print(students)
# students = [
#     ("", "mahmoodgamal045@gmail.com", ""),
#     ("", "ahmedkhairy0106@gmail.com", ""),
#     ("matter", "agtmasu@gmail.com", ""),
#     # Add more students here
# ]

# Send email to each student
for student in students:
    user_name, recipient_email, certificate_url = student
    send_email(recipient_email, user_name, certificate_url)    
    sleep(1)
