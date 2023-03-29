from behave import *
from selenium.webdriver import Chrome
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import logging
import sys
from dotenv import load_dotenv

def get_env(key):
    return os.getenv(key)

driver = None

@given("I have opened the browser")
def step_impl(context):
    global driver
    if not driver:
        driver = webdriver.Chrome()
        load_dotenv()
        driver.maximize_window()

@when(u'user enter the website URL')
def step_impl(context):
    global driver
    try:
        driver.get(get_env('URL'))
        time.sleep(2)
    except Exception as e:
       logging.error("Invalid URL"+ str(e))

@when(u'user click on the bank manager button')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('BANK_MANAGER')).click()
        time.sleep(2)
    except Exception as e:
       logging.error("unable to click the bank manager button"+ str(e))


@when(u'user click on add customer')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('ADD_CUSTOMER')).click()
        time.sleep(2)
    except Exception as e:
       logging.error("unable to click customers"+ str(e))

@when(u'user enter {first_name} and {last_name} and {postcode}')
def step_impl(context, first_name, last_name, postcode):
    global driver
    try:
        driver.find_element("xpath", get_env('FIRST_NAME')).send_keys(first_name)
        time.sleep(1)
        driver.find_element("xpath", get_env('LAST_NAME')).send_keys(last_name)
        time.sleep(1)
        driver.find_element("xpath", get_env('POSTCODE')).send_keys(postcode)
        time.sleep(1)
        driver.find_element("xpath", get_env('SUBMIT')).click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
    except Exception as e:
       logging.error("Something went wrong in adding customer"+ str(e))

@when(u'verify customers')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('CUSTOMERS')).click()
        time.sleep(2)
        table = driver.find_element("xpath", get_env('CUSTOMERS_TABLE'))
        rows = table.find_elements(By.TAG_NAME, "tr")
        first_names = ["Christopher", "Frank", "Christopher", "Connely", "Jackson", "Minka", "Jackson"]
        last_names = ["Connely", "Christopher", "Minka", "Jackson", "Frank", "Jackson", "Connely"]
        for row in rows[6:]:
            cells = row.find_elements(By.TAG_NAME, "td")
            assert cells[0].text in first_names, f"Expected '{cells[0].text}' is added to the customer"
            assert cells[1].text in last_names , f"Expected '{cells[1].text}' is added to the customer"
        time.sleep(3)
    except Exception as e:
       logging.error("Customer verification failed"+ str(e))

@then(u'delete customers {first_name} and {last_name}')
def step_impl(context, first_name, last_name):
    global driver
    try:
        driver.find_element("xpath", get_env('CUSTOMERS')).click()
        time.sleep(3)
        table = driver.find_element("xpath", get_env('CUSTOMERS_TABLE'))
        rows = table.find_elements(By.TAG_NAME,"tr")
        idx = 6
        for row in rows[6:]:
            cells = row.find_elements(By.TAG_NAME, "td")
            driver.execute_script("arguments[0].scrollIntoView();", cells[0])
            if cells[0].text == first_name and cells[1].text == last_name:
                driver.find_element("xpath", "/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr[" + str(idx) + "]/td[5]/button").click()
            idx += 1 
        time.sleep(3)

    except Exception as e:
       logging.error("unable to delete customers"+ str(e))

@when(u'user click on the customer login button')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('CUSTOMER_LOGIN')).click()
        time.sleep(2)
    except Exception as e:
       logging.error("unable to click the customer login button"+ str(e))

@when(u'select Hermoine Granger from dropdown')
def step_impl(context):
    global driver
    try:
        dropdown = driver.find_element("xpath", get_env('DROPDOWN'))
        dropdown.click()
        option = driver.find_element("xpath", get_env('SELECT_OPTION'))
        option.click()
    except Exception as e:
       logging.error("unable to select option from dropdown"+ str(e))

@when(u'click on the login button')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('LOGIN')).click()
        time.sleep(2)
    except Exception as e:
       logging.error("unable to click on login button"+ str(e))

@when(u'select number from the dropdown')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('SELECT_NUMBER')).click()
        time.sleep(2)
        driver.find_element("xpath", get_env('SELECT_1003')).click()
        time.sleep(2)
        driver.find_element("xpath", "//body//div[@class='ng-scope']//div[@class='ng-scope']//div[2]").click()
        time.sleep(2)
    except Exception as e:
       logging.error("unable to select option from dropdown"+ str(e))

@when(u'I perform a credit transaction of "50000"')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('DEPOSIT')).click()
        time.sleep(2)
        driver.find_element("xpath", get_env('ENTER_AMOUNT')).send_keys(get_env('TXN_1'))
        time.sleep(2)
    except Exception as e:
       logging.error("unable to perform the transaction"+ str(e))

@when(u'I click on deposit button')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('DEPOSIT_BUTTON')).click()
        time.sleep(2)
    except Exception as e:
       logging.error("unable to click on deposit button"+ str(e))

@when(u'check if current balance is "50000"')
def step_impl(context):
    global driver
    try:
        balance_amt = driver.find_element("xpath", "/html/body/div/div/div[2]/div/div[2]/strong[2]").text
        assert int(balance_amt) == 50000
    except AssertionError as e:
        logging.error("Current balance is not being matched"+ str(e))
        raise AssertionError

@when(u'I perform a debit transaction of "3000"')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('WITHDRAWAL')).click()
        time.sleep(2)
        driver.find_element("xpath", get_env('ENTER_AMOUNT')).send_keys(get_env('TXN_2'))
        time.sleep(2)
    except Exception as e:
       logging.error("unable to perform the transaction"+ str(e))

@when(u'I click on withdraw button')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('WITHDRAW_BUTTON')).click()
        time.sleep(2)
    except Exception as e:
       logging.error("unable to click on withdraw button"+ str(e))

@when(u'check if current balance is "47000"')
def step_impl(context):
    global driver
    try:
        balance_amt = driver.find_element("xpath", "/html/body/div/div/div[2]/div/div[2]/strong[2]").text
        assert int(balance_amt) == 47000
    except AssertionError as e:
        logging.error("Current balance is not being matched"+ str(e))
        raise AssertionError


@when(u'I perform a debit transaction of "2000"')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('WITHDRAWAL')).click()
        time.sleep(2)
        driver.find_element("xpath", get_env('ENTER_AMOUNT')).send_keys(get_env('TXN_3'))
        time.sleep(2)
    except Exception as e:
       logging.error("unable to perform the transaction"+ str(e))

@when(u'check if current balance is "45000"')
def step_impl(context):
    global driver
    try:
        balance_amt = driver.find_element("xpath", "/html/body/div/div/div[2]/div/div[2]/strong[2]").text
        assert int(balance_amt) == 45000
    except AssertionError as e:
        logging.error("Current balance is not being matched"+ str(e))
        raise AssertionError

@when(u'I perform a credit transaction of "5000"')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('DEPOSIT')).click()
        time.sleep(2)
        driver.find_element("xpath", get_env('ENTER_AMOUNT')).send_keys(get_env('TXN_4'))
        time.sleep(2)
    except Exception as e:
       logging.error("unable to perform the transaction"+ str(e))

@when(u'I perform a debit transaction of "10000"')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('WITHDRAWAL')).click()
        time.sleep(2)
        driver.find_element("xpath", get_env('ENTER_AMOUNT')).send_keys(get_env('TXN_5'))
        time.sleep(2)
    except Exception as e:
       logging.error("unable to perform the transaction"+ str(e))

@when(u'check if current balance is "40000"')
def step_impl(context):
    global driver
    try:
        balance_amt = driver.find_element("xpath", "/html/body/div/div/div[2]/div/div[2]/strong[2]").text
        assert int(balance_amt) == 40000
    except AssertionError as e:
        logging.error("Current balance is not being matched"+ str(e))
        raise AssertionError

@when(u'I perform a debit transaction of "15000"')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('WITHDRAWAL')).click()
        time.sleep(2)
        driver.find_element("xpath", get_env('ENTER_AMOUNT')).send_keys(get_env('TXN_6'))
        time.sleep(2)
    except Exception as e:
       logging.error("unable to perform the transaction"+ str(e))

@when(u'check if current balance is "25000"')
def step_impl(context):
    global driver
    try:
        balance_amt = driver.find_element("xpath", "/html/body/div/div/div[2]/div/div[2]/strong[2]").text
        assert int(balance_amt) == 25000
    except AssertionError as e:
        logging.error("Current balance is not being matched"+ str(e))
        raise AssertionError

@when(u'I perform a credit transaction of "1500"')
def step_impl(context):
    global driver
    try:
        driver.find_element("xpath", get_env('DEPOSIT')).click()
        time.sleep(2)
        driver.find_element("xpath", get_env('ENTER_AMOUNT')).send_keys(get_env('TXN_7'))
        time.sleep(2)
    except Exception as e:
       logging.error("unable to perform the transaction"+ str(e))

@when(u'check if current balance is "26500"')
def step_impl(context):
    global driver
    try:
        balance_amt = driver.find_element("xpath", "/html/body/div/div/div[2]/div/div[2]/strong[2]").text
        assert int(balance_amt) == 26500
    except AssertionError as e:
        logging.error("Current balance is not being matched"+ str(e))
        raise AssertionError

def after_scenario(context, scenario):
    global driver
    if scenario == context.scenario:
        # This is the last scenario, so we can close the driver.
        driver.quit()