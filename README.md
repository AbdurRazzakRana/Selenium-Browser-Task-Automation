# Objective
This is a demonstration of a project to collect data from one site and submit those data into another site for a massive amount of more than 10,000 times.

# Addressing Current Problem
To do this task, previously, a human has to go through each person processing to a site A and collect necessary data from that site and manually put those data into site B in different environment.
Processing each person takes at least 7 mins without breaks. Therefore to process more than 10,000 such scenaio would take a lot of time.

# Counter Measure
This code is to process one such instance. Since the steps of work is constant for each processing, thereofore, a set of instructions is written using Google Selenium Browser automation clicking sequence.
If this process loop through all the instance, it would solve that big problem overnight without human involvement.

# Constrains
1. The click or data filing sequnces in the code has to be changed accroding to one's requirement.
2. Has to put inside loop to do repeatative task.
3. If any of the sites dynamically changes the id of those html fields, this static process would not work.

# Installaltion
1. Install python (version has to be greater than 3.4)
2. Install selenium using: pip install selenium
3. Update the main.py file based on your html id clicking/filling data sequence
4. Run the file using: python3 main.py
5. If there any error, please see the error printed on encounter that


