# Graduation-Assignment
This file contains all of the coding files for my Graduation Assignment as well as folder containing mages for testing.

Test Images contains 2 subfolders 
  > Location Test contains images that should be used to test the Extract Location Data file
  > Model Test contains images that should be used to test the classification model in the Test Classifier File

Incorrect Predictions is used to store images that have been incorrectly classified. This folder can be used for future training of the model.

Extract Location Data extracts the coordinates of an image. When running this file, please check the LocationTest.csv file to ensure that it is populated with at least 1 image source

Test Classifier takes an image and passes it through the model. if an invasive species is incorrectly classified, it will move the image to the incorrect predictions foler

Train Model is where the model was built and trained - this should not be executed

Plotting Map takes the coordinates from the LocationTest.csv and plots them on a Google map. It also shades an area of the map for the competition section of the app. Please ensure that LocationTest.csv is populated with at least 1 set of coordinates before running. To ensure this, run Extract Location Data first.

Open 'invasive species map.html' to view the map itself.
