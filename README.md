## Agenda Alerter

A script I made for myself that automatically texts my daily schedule everyday! This python script grabs my scheduled events from my Google Calendar using the Google Calendar API, and then texts it to me using the Twilio API. The script runs using a CRON job, which runs on an AWS EC2 instance. This instance was created using Terraform, and I configured the EC2 instance with Ansible to run the script everyday at 9 AM.

## Project Status

As of now, the project does not run. I deactivated the instances and API's to save on costs. However, I have pictures of texts and documentation!

## Project Screen Shot(s)
Here are the texts:

Here is a picture which shows the flow of the app. 

## Installation and Setup Instructions 
  

## Reflection

This was a 2 week long side project built during my junior year. Project goals included using technologies learned up until this point and familiarizing myself with documentation for new features. I'm proud becuase this is a project that I can really use IRL! I practiced more with using REST API's, and learned how to use Ansible and Terraform. 

I originally wanted to make this into an app, but I realized I can just make an automated script. I thought to myself, how can I run this script all the time, not using my local machine? That's where Terraform and Ansible came in. I read alot of documentation on the new technologies, and managed to get a working, running EC2 instance that runs my script!

At the end of the day, the technologies implemented in this project are Python (and multiple libraries), Git, Ansible (YAML), Terraform, AWS, and Linux. I learned how work with JSON, as well.  
