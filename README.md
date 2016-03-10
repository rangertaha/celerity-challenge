# Django Developer Coding Challenge

![Alt text](project.png "Django Developer Coding Challenge")


## Installation

In the top level directory **celerity-challenge** we need to do the following.

 * Setup the virtual environment
 * Install project dependencies


    cd celerity-challenge


Setup the virtual environment

    virtualenv env
    source env/bin/activate
    
Install project dependencies

    pip install -r requirements.txt



## Local Execution

    python manage.py runserver



## Structure

    celerity-challenge
        apps                    # Modular apps 
            demo
                templates       # The template for displaying the form          
                forms.py        # The forms
                roman.py        # The Roman/Number algorithm.
                tests.py
                urls.py
                views.py        # Serves the html and success message or errors
            
        celeritychallenge       # Global and shared components
            static
            templates
            local_settings.py   # Local setting for development
            settings.py
            urls.py
            wsgi.py
    
    .gitignore
    manage.py
    README.md
    requirements.txt
    celeritychallenge.log       # Created at runtime

