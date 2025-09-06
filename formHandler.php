<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $visitor_email = $_POST['email'];
    $subject = $_POST['subject'];
    $message = $_POST['Message']; 

    $email_from = "youremail@example.com";  // must be a valid email
    $email_to = "khairun.n.n.rimu@gmail.com";

    $email_subject = "New Form Submission";
    $email_body = "User Name: $name.\n".
                  "User Email: $visitor_email.\n".
                  "Subject: $subject.\n".
                  "User Message: $message.\n";

    $headers = "From: $email_from\r\n";
    $headers .= "Reply-To: $visitor_email\r\n";

    if (mail($email_to, $email_subject, $email_body, $headers)) {
        header("Location: contact.html?success=true");
        exit();
    } else {
        echo "Email sending failed.";
    }

