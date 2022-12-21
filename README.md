# Hackathon-22-Agriculture-Project
This project can be used as a tool by farmers in order to calculate and project costs and production yields for their farms. We have scraped data from the John Deere website to gather costs of machinery as well as https://figshare.com/articles/dataset/A_global_dataset_for_crop_production_under_conventional_tillage_and_conservation_agriculture/12155553?file=26690678. The data set gave a detailed look at crop yield based on numerous factors such as herbicide and pesitice usage, fertilizer use, as well as if the crop was planted using conventional or non-conventional tillage.

Seeds.py is an algorithm that takes in the inputs: crop type, and a minimum and maximum temperature for the area you are planning to cultivate. It ouputs an estimation of yield percentage based on data on  ideal crop growing conditions.

The index rating function takes in a variety of inputs: The farmer's farmable land (in acres), the desired crop to grow, types of machinery needed, the cost per litre of fuel, fertilizer, herbicide, and the country that the farmer is cultivating in. All of these parameters are weighed together to estimate the capital needed to begin their farming operation.

Our crop yields projection used the software Orange to create our data predictions for this project.
