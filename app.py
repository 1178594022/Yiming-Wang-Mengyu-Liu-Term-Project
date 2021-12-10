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
#define the function calculate to find the day by day virus inffection and the gif of virus growth
def calculate():
    if request.method == "POST":    #use the request method post
        '''set veriable a as the input from the user, make sure that they are in intager format'''
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
        roots = virus(a,b,c,d,e)   #set root as the veriable records result returned from virus 
        if roots:
            return render_template(
                "stop_result.html", #use the templet of HTML code in the templet folder named stop_form
                e=e, # need to use the e, the day veriable in the html
                root_1=str(escape(virus(a,b,c,d,e))).replace('\n', '<br/>'),   # return the day by day break down
                
            )
        else:
            return render_template("stop_form.html", error=True) #return the error massage
    return render_template("stop_form.html", error=None) # the result returns by the format of stop_form.html

if __name__ == "__main__":
    app.run(debug=True)