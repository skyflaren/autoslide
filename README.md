# autoslide (web proof #2)

Introducing AutoSlide! An ML-powered image generator for all your crunch time needs. One of the most time consuming tasks when making slides is simply choosing good visuals to accomodate the presentation. With AutoSlide this will never be an issue again!  AutoSlide automatically chooses images and adds them to your powerpoints based on the content of your uploaded slides. Try it out below!

Download the repository and navigate to the folder that contains the program. Install the dependencies by running:
```
pip install -r requirements.txt
```

To see a demo with the currently uploaded powerpoint:
```
python presentation_reader.py
```

If you'd like to test it with your own powerpoint, add it to the folder and change line 6 in presentation_reader.py to:
```
prs = Presentation("{powerpoint-name}")
```


