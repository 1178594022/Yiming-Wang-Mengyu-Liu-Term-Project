from flask import Flask, render_template, request
from final2 import virus_plot
from final import virus
from flask import escape
import os

PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0




"""Define a route of the webside to the default route"""
@app.route("/", methods=["GET", "POST"])
#define the function calculate to the day by day break down

def calculate():
    if request.method == "POST":    #use the request method post
        '''set veriable a as the input from the user, make sure that they are in integer format'''
        a = int(request.form["a"])
        b = int(request.form["b"])
        c = int(request.form["c"])
        d = int(request.form["d"]) 
        e = int(request.form["e"]) 
        # a1 = int(a)
        # a2 = int(b)
        # a3 = int(c)
        # a4 = int(d)
        # a5 = int(e)
        '''plot the gif and save it to the folder'''
        virus_plot(a,b,c,d,e)
        roots = virus(a,b,c,d,e)   #set root as the veriable records result returned from find_stop_near 
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'movie.gif')
        if roots:
            return render_template(
                "stop_result.html", #use the templet of HTML code in the templet folder named stop_form
                e=e,
                root_1=str(escape(virus(a,b,c,d,e))).replace('\n', '<br/>'),   # root_1 record the DAY BY DAY BREAK DOWN
                user_image = full_filename
            )
        else:
            return render_template("stop_form.html", error=True) #return the error massage
    return render_template("stop_form.html", error=None) # the result returns by the format of stop_form.html


if __name__ == "__main__":
    app.run(debug=True)