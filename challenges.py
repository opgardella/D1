from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


#Task 2 : Dynamic URLS
    #edit the view function to display 'Welcome to <course_name>' on localhost:5000/course/<course>
@app.route('/course/<course_name>')
def courseView(course_name):
    return "Welcome to " + course_name

#Task 3.1 Basic HTML Form
    #Set the method and action of the HTML form, such that form data is sent to /result using POST method
    #The form should have a text field in which you can enter an ingredient (milk, eggs, etc)
@app.route('/form')
def formView():
    html_form = '''
    <html>
    <body>
    <form action = "/result" method = "POST">
        <label for = "i"> Enter an ingredient : </label>
        <br>
        <input type = "text" name = "ingredient" id = "i"></input>
        <input type = "submit" name = "Submit"></input>
    </form>
    </body>
    </html>
    '''
    #do all above in a string, name is what you're storing the input in
    #the id is attaching the label to the input with that id, not super important right now though
    #good practice to link label and input though with an id
    #the action = "/result" means that when you press submit on form, it takes you to /result page
    return html_form

#Task 3.2 : Processing Form Data
@app.route('/result', methods = ['GET', 'POST'])
def resultView():
    # Make an API request to Recipe API for the ingredient entered in the form and display the recipe results
    #Step 1 : Receive the ingredient from the form if request type is POST
    if request.method == "POST":
        ingredient = request.form.get("ingredient", "Didn't get anything") #2nd one in case doesn't work
        #request.args is a dictionary (key-value pair) which gives ingredients like {"ingredient": "eggs"}
        #to access value, used to be p["ingredient"] --> NOW .get("ingredient")
        print(ingredient) #should print "eggs" in terminal if I put eggs in form

    #Step 2 : Create paramaters JSON with the ingredient received in step 1 in the form required by http://www.recipepuppy.com/about/api/
        params = {}
        params["i"] =  ingredient
        baseurl = "http://www.recipepuppy.com/api/"

    #Step 3 : Make an API request to Recipe API and parameters in Step 2
        response = requests.get(baseurl, params = params) #essentially creating http://www.recipepuppy.com/api/?i={ingredient}

    #Step 4 : Parse the response from API request in JSON
        #response --> text, status_code
        response_json = json.loads(response.text)

    #Step 5 : Display the response in browser (remember : HTML takes only strings)
        response_str = str(response_json)
    return response_str


if __name__ == '__main__':
    app.run(debug=True)
#this auto dectects changes so you don't have to run app again and again
