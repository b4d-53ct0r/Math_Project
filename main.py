
from flask import Flask,render_template,request
from math import *
from sympy import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/TVI_result',methods=['GET', 'POST'])
def TVI_result():
    a = request.args.get('a', default = 0.5, type = float)
    b = request.args.get('b', default = 2, type = float)
    _function = request.args.get('function', default = "log(x)", type = str)
    e= exp
    ln = log
    def check(f , a, b):
        x = a
        y_a = eval(f)
        x = b
        y_b = eval(f)
        if y_a*y_b > 0 :
            flag = 0
            return 0
        else:
            return 1
    def find_interval(f,a,b,p):
        mid = (b+a)/2
        x = a
        y_a = eval(f)
        x = b
        y_b = eval(f)
        x = mid
        y_mid = eval(f)
            
        if y_mid * y_a < 0:
            return find_interval(f,a,mid,1)
        if y_mid * y_b  < 0:
            return find_interval(f,mid,b,0)
        if y_mid * y_a > 0 and y_mid * y_b > 0:
            if p == 1:
                a = mid*2-b
            if p == 0:
                b=2*(mid)-a
        return [a,b]
    if check(_function,a,b) == 0:
        interval = "interval not found"
    else:
        interval = find_interval(_function,a,b,2)
    return render_template("TVI_result.html", f = _function,interval=interval )
@app.route('/DL')
def DevLim():
    return render_template("DL.html")
@app.route('/DL_result')
def DL_result():
    e=exp
    ln = log
    x = symbols('x')
    f = request.args.get('function', default = "log(x)", type = str)
    N = request.args.get('N', default = 2, type = int)
    A = request.args.get('A', default = 2, type = int)
    def der(f,n):
        df = str(diff(f.replace("e","exp"),x,n)).replace("exp","e")
        return df
    def fact(x):
        s=1
        for i in range(1,x+1):
            s=s*i
        return s
    l=[]
    for i in range(0,N+1):
        c=eval(str(der(f,i)).replace("x",str(A)))
        l=l+[c/fact(i)]
    lf=""
    for i in range(0,N+1):
        lf = lf + "+"+str(((x-A)**i)*l[i])
    lhal = "f(x) = "+str(eval(lf))
    
    return render_template("DL_result.html", result = lhal,N=N,A=A,f=f)

@app.route('/TVI')
def TVI():
    return render_template("TVI.html")



if __name__ == "__main__":
    app.run(debug=True)