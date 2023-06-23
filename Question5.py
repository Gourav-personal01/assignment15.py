#The url_for() function is used to build a URL to the specific function dynamically. The first argument is the name of the specified function, and then we can pass any number of keyword argument corresponding to the variable part of the URL.

from flask import *  
   
app = Flask(__name__)  
  
@app.route('/admin')  
def admin():  
    return 'admin'  
  
@app.route('/librarion')  
def librarion():  
    return 'librarion'  
  
@app.route('/student')  
def student():  
    return 'student'  
  
@app.route('/user/<name>')  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))  
    if name == 'librarion':  
        return redirect(url_for('librarion'))  
    if name == 'student':  
        return redirect(url_for('student'))  
if __name__ =='__main__':  
    app.run(debug = True)  