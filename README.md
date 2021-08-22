# autoslide (web proof #2)

Introducing AutoSlide! An ML-powered image generator for all your crunch time needs. Visuals are often a key component of keeping the users attention and providing interest in a topic. However, one of the most time consuming tasks when making slides is simply going through all the keywords on a slide and choosing good visuals to accomodate the presentation. With AutoSlide this will never be an issue again!  AutoSlide automatically chooses images and adds them to your powerpoints based on the content of your uploaded slides. Try it out below!

# Demo

For the web dev proof, the frontend has been polished to improve the user experience. Built with HTML, CSS and Javascript, the frontpage has a blob design featuring parallax scrolling. There is also a custom-made upload ui!

![Frontpage of Autoslide](https://media.giphy.com/media/IqFYGPEEhy5xP80sQ9/giphy.gif)

<img src="https://github.com/skyflaren/autoslide/blob/proof-two/upload-ui.png?raw=true" width="640" height="360"/>

To test it yourself, you can run deploy the django server locally! Download the repository and navigate to the folder that contains the program. Install the dependencies by running:
```
pip install -r requirements.txt
```

To start the server, cd into src then run the command on the second line
```
cd src
python manage.py runserver
```

Head on over to your localhost and the pages shown above will be hosted at http://127.0.0.1:8000/ (or equivalent localhost) and http://127.0.0.1:8000/home


