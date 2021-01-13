#!/usr/bin/env python3
import os
import datetime
import reports
import emails

current_date = datetime.datetime.now().strftime('%Y-%m-%d')

def generate_pdf(path):
  pdf = ""
  files = os.listdir(path)
  for file in files:
    if file.endswith(".txt"):
      with open(path + file, 'r') as f:
        inline = f.readlines()
        name = inline[0].strip()
        weight = inline[1].strip()
        pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
  return pdf

if __name__ == "__main__":
  path = "supplier-data/descriptions/"
  attachment = "/tmp/processed.pdf"
  title = "Process Updated on " + current_date
  paragraph = generate_pdf(path)
  reports.generate_report(attachment, title, paragraph)

  sender = "automation@example.com"
  receiver = "username@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = "/tmp/processed.pdf"

  message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(message)