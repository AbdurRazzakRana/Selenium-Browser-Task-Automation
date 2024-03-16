"""
Author: Abdur Razzak
Date: March 16, 2024

Task: This work will collect some data from one site and put this data into a form
of another site. 

Reasoning: when we need to fillout thousands of data from one site or another site;
or from a file to a site, then applying is code in a loop would save a lot of time.

Demo: This file will collect first name and last name from one site
and put these information into another site

"""

# Required imports
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    ElementNotSelectableException,
    ElementNotVisibleException,
    InvalidElementStateException,
    InvalidSelectorException,
    MoveTargetOutOfBoundsException,
    NoSuchElementException,
    NoSuchFrameException,
    NoSuchWindowException,
    SessionNotCreatedException,
    StaleElementReferenceException,
    TimeoutException,
    UnableToSetCookieException,
    UnexpectedAlertPresentException,
    UnexpectedTagNameException,
    WebDriverException,
    )

# Global vars
sleep_time = 20
time_multiply = 2
gbr = webdriver.Chrome()

# Featching site, will get the first name and last name of person 1
fetch_url = "https://www.dannybrien.com/random/"
fetch_id_table = "tablecontents"
fetch_id_usr = 1


# payload site
# Right now, as the terget site is not set, it will produce error
# Please fill up the instruction or clikcing sequences according to your site.
site = "target_site"  # Actual site link is removed intentionally for safety.
click_1 = "dropdown-toggle"
click_2 = "Request for Information"


# Testing data instances
# First name and last name is kept empty, because, they will be fetched from
# another site
first_name_val = ""
last_name_val = ""
birth_date_month_val = "January"
birth_date_day_val = "5"
birth_date_year_val = "2004"
email_val = "abc123@gmail.com"
cell_phone_val="123-666-1234"
anticipated_term_val = "Fall 2024"
degree_level_val= "Master's"
academic_program_val = "Accounting"
submit_button_val = "Submit"


first_name_id = "form_fb198c2b-49a7-4c84-8873-9c651fdd4717"
last_name_id = "form_937818ba-5343-443b-b093-a88a8fe4417d"
birth_date_month_id = "form_d538317f-3675-4d89-a853-04c159260261_m"
birth_date_day_id = "form_d538317f-3675-4d89-a853-04c159260261_d"
birth_date_year_id = "form_d538317f-3675-4d89-a853-04c159260261_y"
email_id="form_26c7f1e0-91bd-4684-8f62-d299f3fabd67"
cell_phone_id="form_fe25d4c7-5aff-42f2-bfc0-c6f269207967"
anticipated_term_id = "form_cee3f06d-c82d-4522-a360-cc9e230c905c"
degree_level_id = "form_d7e126e0-82d4-4817-a48b-f32fa5944086"
academic_program_id="form_00859017-30f6-4589-aedf-7d4746de6d6d"
submit_button_class = "default.form_button_submit"

# This method will navigate to the data collection site and fetch the first name
# and the last name
def nevigteFetchDataPage_And_CollectData():
    global gbr, first_name_val, last_name_val
    br = gbr
    
    # Loading the featching url
    br.get(fetch_url)
    time.sleep(sleep_time * time_multiply)
    table = WebDriverWait(br, sleep_time*time_multiply).until(
        EC.presence_of_element_located((By.ID, fetch_id_table))
    )

    # Accessing the table
    time.sleep(sleep_time)
    rows = table.find_elements(By.TAG_NAME, "tr")

    if len(rows) >= 2:
        # Get the first user
        second_row = rows[fetch_id_usr]
        cells = second_row.find_elements(By.TAG_NAME, "td")
        
        # Printing the fetched firstname and lastname
        print(cells[1].text, end=' ')
        print(cells[2].text)
        first_name_val = cells[1].text
        last_name_val = cells[2].text
    else:
        print("Table does not have enough rows")
    
    print("DONE Method: nevigteFetchInfoPage")

# Loading and putting the data into target site
def navigateToPayloadPage_And_InsertData():
    global gbr
    br = gbr

    # Loading the page
    br.get(site)
    time.sleep(sleep_time*time_multiply)

    br.find_elements(By.CLASS_NAME, click_1)[4].click()
    print("Payload site Navigation Bar clicked")
    time.sleep(sleep_time/time_multiply)

    # Clickng navigation bar step 1
    element_with_text = WebDriverWait(br, sleep_time*time_multiply).until(
        EC.presence_of_element_located((
            By.XPATH,
            '//*[contains(text(), "' + click_2 + '")]'))
    )
    element_with_text.click()

    # Filling up first name field
    first_name_field = WebDriverWait(br, sleep_time*time_multiply).until(
        EC.visibility_of_element_located((By.ID, first_name_id))
    )
    first_name_field.send_keys(first_name_val)

    # Filling up last name field
    second_name_field = WebDriverWait(br, sleep_time*time_multiply).until(
        EC.visibility_of_element_located((By.ID, last_name_id))
    )
    second_name_field.send_keys(last_name_val)
    time.sleep(sleep_time/time_multiply)


    # Birth Month Selection
    birth_month = WebDriverWait(br, sleep_time*time_multiply).until(
        EC.visibility_of_element_located((By.ID, birth_date_month_id))
    )
    birth_month.send_keys(birth_date_month_val)
    time.sleep(sleep_time/2)

    # Birth Day Selection
    birth_day = WebDriverWait(br, sleep_time*time_multiply).until(
        EC.visibility_of_element_located((By.ID, birth_date_day_id))
    )
    time.sleep(sleep_time/2)
    birth_day.send_keys(birth_date_day_val)
    time.sleep(sleep_time/time_multiply)
    
    # Birth Year Selection
    birth_year = WebDriverWait(br, sleep_time*time_multiply).until(
        EC.visibility_of_element_located((By.ID, birth_date_year_id))
    )
    print(f"Setting Birth Year: "+ birth_date_year_val)
    time.sleep(sleep_time/time_multiply)
    birth_year.send_keys(birth_date_year_val)
    time.sleep(sleep_time/time_multiply)


    # Writing email id
    email_field = WebDriverWait(br, sleep_time*time_multiply).until(
        EC.visibility_of_element_located((By.ID, email_id))
    )
    time.sleep(sleep_time/time_multiply)
    email_field.send_keys(email_val)
    time.sleep(sleep_time/time_multiply)


    # Writing cell phone number
    cell_phone_field = WebDriverWait(br, sleep_time*time_multiply).until(
        EC.visibility_of_element_located((By.ID, cell_phone_id))
    )
    time.sleep(sleep_time/time_multiply)
    cell_phone_field.send_keys(cell_phone_val)
    time.sleep(sleep_time/time_multiply)

    # Ancipated entry term filling
    anticipated_term_field = WebDriverWait(br, sleep_time*time_multiply).until(
        EC.visibility_of_element_located((By.ID, anticipated_term_id))
    )
    time.sleep(sleep_time/time_multiply)
    anticipated_term_field.send_keys(anticipated_term_val)
    time.sleep(sleep_time/time_multiply)

    # Entry degree level field
    degree_level_field = WebDriverWait(br, sleep_time*time_multiply).until(
        EC.visibility_of_element_located((By.ID, degree_level_id))
    )
    time.sleep(sleep_time/2)
    degree_level_field.send_keys(degree_level_val)
    time.sleep(sleep_time/time_multiply)

    # Setting Academic program of interest
    time.sleep(sleep_time * time_multiply)
    academic_program_field = WebDriverWait(br, sleep_time*time_multiply).until(
        EC.visibility_of_element_located((By.ID, academic_program_id))
    )
    time.sleep(sleep_time/time_multiply)
    academic_program_field.send_keys(academic_program_val)
    time.sleep(sleep_time/time_multiply)


    # Click on Submit button to submit the form
    submit_button = WebDriverWait(br, sleep_time*time_multiply).until(
        EC.element_to_be_clickable((By.CLASS_NAME, submit_button_class))
    )
    submit_button.click()
    time.sleep(sleep_time * time_multiply)
    gbr = br

# finally block, closing the selenium browser
def final_block():
    global gbr
    time.sleep(sleep_time * time_multiply)
    gbr.quit()

# Handle the possible exceptions to see the error
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ElementClickInterceptedException:
            print("ElementClickInterceptedException")
        except ElementNotInteractableException:
            print("ElementNotInteractableException")
        except ElementNotSelectableException:
            print("ElementNotSelectableException")
        except ElementNotVisibleException:
            print("ElementNotVisibleException")
        except InvalidElementStateException:
            print("InvalidElementStateException")
        except InvalidSelectorException:
            print("InvalidSelectorException")
        except MoveTargetOutOfBoundsException:
            print("MoveTargetOutOfBoundsException")
        except NoSuchElementException:
            print("NoSuchElementException")
        except NoSuchFrameException:
            print("NoSuchFrameException")
        except NoSuchWindowException:
            print("NoSuchWindowException")
        except NoSuchWindowException:
            print("NoSuchWindowException")
        except SessionNotCreatedException:
            print("SessionNotCreatedException")
        except StaleElementReferenceException:
            print("StaleElementReferenceException")
        except TimeoutException:
            print("TimeoutException")
        except UnableToSetCookieException:
            print("UnableToSetCookieException")
        except UnexpectedAlertPresentException:
            print("UnexpectedAlertPresentException")
        except UnexpectedTagNameException:
            print("UnexpectedTagNameException")
        except WebDriverException:
            print("WebDriverException")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("Quit from finally")
    return wrapper

@handle_exceptions
def execute_methods():
    # Navigate to data collection site and collect the data
    nevigteFetchDataPage_And_CollectData()
    time.sleep(sleep_time)

    # Input the data into required site with fixed steps
    navigateToPayloadPage_And_InsertData()

# Main method to start with
if __name__ == '__main__':
    # All methods are bring under execute_methods to keep track on exceptions
    execute_methods()

    # calling finally block as we used try catch block
    final_block()