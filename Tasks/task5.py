from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a_very_secret_and_unique_key_12345'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def handle_contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        print("-" * 30)
        print("NEW CONTACT FORM SUBMISSION")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message[:50]}...")
        print("-" * 30)

        flash(f'Thank you, {name}! Your message has been received. I will be in touch shortly.', 'success')

        return redirect(url_for('index'))
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)