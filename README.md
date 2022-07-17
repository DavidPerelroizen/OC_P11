# gudlift-registration

1. Why


    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 


3. Installation

    - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a virtual python environment within that directory.

    - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing

    You are free to use whatever testing framework you like-the main thing is that you can show what tests you are using.

    We also like to show how well we're testing, so there's a module called 
    [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.

   ### Trigger the tests
   
      Use pytest to trigger the tests.

      #### Trigger the unit_tests
         Go to the unit_tests directory and type the following command in your terminal: <code>pytest</code>

      #### Trigger the integration_tests
         Go to the integration_tests directory and type the following command in your terminal: <code>pytest</code>
      
      ### Trigger the functional_tests
         1. Open terminal and execute the following command from the main directory: <code>python .\server.py</code>
         2. Open another terminal window, go to the functional_tests directory and type the following command: <code>pytest</code>

6. Test coverage
   
   In order to check the test coverage go to each of the test directories and type the following command:
   ````bash
   pytest --cov
   ````
   Note that in order to get the functional tests coverage, you must trigger the server.py in another terminal window.

7. Performance check
   
   Run the server.py to trigger the app:
   ```bash
   python server.py
   ```
   In another terminal window go to the tests directory run the following command:
   ```bash
   locust
   ```
   In your navigator go to the url: http://localhost:8089/.

   Select the number of users, the spawn rate, and type http://127.0.0.1:5000 has host.
   Then start swarming and check performance either online or by typing <code>ctrl-c</code> in the terminal window where you started locust.


8. Flake8 set-up and checks

   ### Flake 8 configuration

   In the project directory, create a file as follows:
   ```bash
   setup.cfg
   ```

   In this file, write the following:
   ```bash
   [flake8]
   max-line-length = 119
   exclude = venv, __init__.py, *.txt, *.csv, *.md
   ```
   We restrict the maximum number of characters per line at 119. So flake8 won't consider as errors a line as long as it
   has fewer characters.
   We exclude from the flake8 checks the followings:
  - Our virtual environment libraries
  - Our packages init files
  - Our requirement file
  - Our readme file
  - Our CSV databases
  - Our migrations files


   ### Execute flake8 report

   In case the user requests a regular flake8 check on the terminal, proceed as follows:
   ```bash
   flake8 path/to/project/directory
   ```

   In case a html reporting is preferred, proceed as follows:
   ```bash
   flake8 --format=html --htmldir=flake-report
   ```