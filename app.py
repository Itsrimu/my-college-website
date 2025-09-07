from flask import Flask, request, redirect
import smtplib
from email.mime.text import MIMEText

# Create a Flask web app
app = Flask(__name__)

# This route will handle form submissions
@app.route("/formHandler", methods=["POST"])
def form_handler():
    # Get data from the form
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Build the email text
    email_subject = "📩 New Contact Form Submission"
    email_body = f"""
    Name: {name}
    Email: {email}
    Subject: {subject}
    Message: {message}
    """

    # Your email settings (use your Gmail here)
    sender_email = "your_email@gmail.com"
    receiver_email = "your_email@gmail.com"  # where you want to receive messages
    password = "your_app_password"  # create an app password in Google Account

    # Create the email object
    msg = MIMEText(email_body)
    msg['Subject'] = email_subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Try sending the email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)   # login to Gmail
            server.sendmail(sender_email, receiver_email, msg.as_string())  # send
    except Exception as e:
        return f"❌ Something went wrong: {str(e)}"

    # After sending, go back to the contact page
    return redirect("/contact.html")


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
