from flask import Flask, render_template, request, redirect, url_for

# Create the Flask app
app = Flask(__name__)

# A list to store posts (like Instagram posts)
posts = []

# Homepage with career options and a search bar
@app.route('/')
def home():
    return render_template('home.html', posts=posts)

# Page to add a new post
@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        # Get the text from the form
        post_text = request.form['post_text']
        # Add the post to the list
        posts.append(post_text)
        # Go back to the homepage
        return redirect(url_for('home'))
    return render_template('add_post.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
