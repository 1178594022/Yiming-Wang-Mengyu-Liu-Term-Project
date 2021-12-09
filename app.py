from flask import Flask, render_template, request
from numpy import arctan2
from final2 import virus_plot
from final import virus
from flask import escape

app = Flask(__name__)
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0



"""Define a route of the webside to the default route"""
@app.route("/", methods=["GET", "POST"])
#define the function calculate to find the tupple of the closest station information
def calculate():
    if request.method == "POST":    #use the request method post
        a = int(request.form["a"])
        b = int(request.form["b"])
        c = int(request.form["c"])
        d = int(request.form["d"]) 
        e = int(request.form["e"]) #set veriable a as the input from the user
        # a1 = int(a)
        # a2 = int(b)
        # a3 = int(c)
        # a4 = int(d)
        # a5 = int(e)
        virus_plot(a,b,c,d,e)
        roots = virus(a,b,c,d,e)   #set root as the veriable records result returned from find_stop_near 
        if roots:
            return render_template(
                "stop_result.html", #use the templet of HTML code in the templet folder named stop_form
                e=e,
                root_1=str(escape(virus(a,b,c,d,e))).replace('\n', '<br/>'),   # root_1 record the station name
                
            )
        else:
            return render_template("stop_form.html", error=True) 
    return render_template("stop_form.html", error=None) # the result returns by the format of stop_form.html

if __name__ == "__main__":
    app.run(debug=True)