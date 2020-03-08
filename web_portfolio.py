from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


# This is our homepage
@app.route('/')
def homepage():
	return render_template('index.html')


"""
I could just copy and paste the upper code for each page but then I would have to do the same
for each page I wanna add on the web portfolio.
A more dynamic way to make the server work is this
"""


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)


"""
Up until now, we were grabbing data from the contact.html but it wasn't saved anywhere.
With the function bellow, we take that data and store it in a dictionary, so we can
manipulate it later.
"""


# This stores our data in a file on the same directory
# If we want to store the data in a file that is in a different directory, we need to specify it
# Here, we just write our data in a txt file
def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\nEmail: {email} \nSubject:{subject} \nMessage: {message}\n')


# What we need to do is write it in a file that is
# more appropriate and easier to read, like an excel.
# We use csv for that
def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_file(data)
			write_to_csv(data)
			# After the form is submitted, we redirect the user in a 'thank you' page
			return redirect('/thankyou.html')
		except:
			return 'did not save to database'
	else:
		return 'Something went wrong. Try again.'
