import os
import json
from  flask import Flask, render_template, request, flash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    data = []
    with open("data/techniques.json", "r") as json_data:
        data = json.load(json_data)
    return render_template('about.html', page_title='About',
                           techniques = data)
    
@app.route("/about/<technique_name>")
def about_technique(technique_name):
    technique = {}
    
    with open("data/techniques.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == technique_name:
                technique = obj
                
    return render_template("technique.html", technique=technique)

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        flash("Thanks {}, we have received your message!".format(
            request.form["name"]))
        
        message = Mail(from_email='paul.stillbreathing@gmail.com',
               to_emails='pmflemingdev@gmail.com',
               subject='New email from ' + format(request.form["name"]),
               plain_text_content=format(request.form["message"]),
               html_content="<strong>" + format(request.form["message"]) + "</strong>")

        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
        
    return render_template('contact.html', page_title='Contact')

@app.route("/classes")
def classes():
    return render_template('classes.html', page_title='Classes')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)