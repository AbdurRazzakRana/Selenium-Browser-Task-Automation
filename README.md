# Objective
This is a demonstration of a project to collect data from one site and submit those data to another site for a massive amount of more than 10,000 times.

# Addressing Current Problem
To do this task, previously, a human had to go through each person processing to site A and collect necessary data from that site, and manually put those data into site B in a different environment.
Processing each person takes at least 7 minutes without breaks. Therefore to process more than 10,000 such scenario would take a lot of time.

# Counter Measure
This code is to process one such instance. Since the steps of work are constant for each processing, therefore, a set of instructions is written using Google Selenium Browser automation clicking sequence.
If this process loops through all the instances, it would solve that big problem overnight without human involvement.

# Constrains
1. The click or data filing sequences in the code have to be changed according to one's requirement.
2. Has to put inside loop to do repetitive tasks.
3. If any of the sites dynamically changes the ID of those HTML fields, this static process would not work.

# Installation
1. Install python (version has to be greater than 3.4)
2. Install selenium using: pip install selenium
3. Update the main.py file based on your HTML ID by clicking/filling data sequence
4. Run the file using: python3 main.py
5. If there is any error, please see the error printed and encounter that error.
