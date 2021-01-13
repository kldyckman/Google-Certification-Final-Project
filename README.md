# Google-Certification-Final-Project
This repository contains all of the scripts created as part of the Google IT Automation with Python Final Project.

You can find a repository containing the files needed to work on the final project of the specialization at https://github.com/google/it-cert-automation-project.

Assessment: Automate updating catalog information
--------------------------------------------------

You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs). 

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong. 

What you’ll do
---------------------------
Write a script that summarizes and processes sales data into different categories 
Generate a PDF using Python
Automatically send a PDF by email 
Write a script to check the health status of the system 

change_image.py
------------------------------

This script rotates the extracted images, changes the format to JPEG and the resolution to 128x128

supplier_image_upload.py
----------------------------------

This script takes the jpeg images from the supplier-data/images directory and uploads them to the web server fruit catalog.

run.py
-----------------------------

This script processes the text files (001.txt, 003.txt ...) from the supplier-data/descriptions directory. The script turns the data into a JSON dictionary by adding all the required fields, including the image associated with the fruit (image_name), and uploading it to http://[linux-instance-external-IP]/fruits using the Python requests library.

reports.py
----------------------------

This script generates a PDF report to supplier using the nano editor.

report_email.py
----------------------------

This script processes supplier fruit description data from supplier-data/descriptions directory. 


emails.py
----------------------------

This script sends the email using the emails.generate_email() and emails.send_email() methods.

health_check.py
----------------------------

This script runs in the background monitoring some of the system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:

Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 500MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
