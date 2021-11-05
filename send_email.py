import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# message = Mail(from_email='paul.stillbreathing@gmail.com',
#                to_emails='pmflemingdev@gmail.com',
#                subject='Test Sendgrid',
#                plain_text_content='This is a test email. Great success if you can see this',
#                html_content='<strong>This is a test email. Great success if you can see this</strong>')
# 
# try:
#     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)