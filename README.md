![autoslide](https://user-images.githubusercontent.com/46911128/130352764-b5b9ee17-6052-4f2e-8e01-16b61c723ff5.png)

# AutoSlide
[**Figma Design Link**](https://www.figma.com/file/OOPC6cp2QRsSnUe0ay4Z7y/AutoSlide?node-id=0%3A1)

---

Introducing AutoSlide: an ML-powered slideshow generator for all your crunch time needs. One of the most time consuming tasks when making slides is simply choosing good visuals to accomodate the presentation. With AutoSlide this will never be an issue again! AutoSlide automatically chooses images and adds them to your powerpoints based on the content of your uploaded slides. Try it out below!


# Installation 

To begin, make sure that you have installed pipenv.
```
>> pip install pipenv
```

Make sure the directory is the project file then activate the virtual environment by typing,
```
>> pipenv shell
```

All the dependancies can be installed by running,
```
>> pipenv sync
```

After installing the dependancies, navigate to the src folder and run the server by typing
```
>> cd src
>> python manage.py runserver
```

Head on over to your localhost and the pages shown above will be hosted at http://127.0.0.1:8000/ (or equivalent localhost).
