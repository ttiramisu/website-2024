from flask import Flask, render_template


app = Flask(__name__, static_folder='static', static_url_path='')

###############################
############ MAIN #############
###############################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about-dayuwen')
def aboutDayuwen():
    return render_template('dayuwen/about.html')

@app.route('/about-policy')
def aboutDayuwen():
    return render_template('dayuwen/policy.html')

@app.route('/about-us')
def about():
    return render_template('about.html')

@app.route('/policy')
def policy():
    return render_template('policy.html')

###############################
############ ERROR ############
###############################

# @app.errorhandler(404)
# def page_not_found(e):
# 	return render_template("404.html"), 404


# @app.errorhandler(500)
# def page_not_found(e):
# 	return render_template("500.html"), 500

###############################
######## RUN TIME CODE ########
###############################
if __name__ == "__main__":
    app.run(debug=True)