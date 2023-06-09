Feature: Inscale

    Background: Opening browser
        Given I have opened the browser

    @scenario1
    Scenario Outline: Login as bank manager
        When user enter the website URL
        And user click on the bank manager button
        And user click on add customer
        And user enter <first_name> and <last_name> and <postcode>

        Examples:
            | first_name    | last_name      | postcode |
            | Christopher   | Connely        | L789C349 |
            | Frank         | Christopher    | A897N450 |
            | Christopher   | Minka          | M098Q585 |
            | Connely       | Jackson        | L789C349 |
            | Jackson       | Frank          | L789C349 |
            | Minka         | Jackson        | A897N450 |
            | Jackson       | Connely        | L789C349 |

    @scenario1
    Scenario Outline: Deleting the customer
        And verify customers
        Then delete customers <first_name> and <last_name>

        Examples:
            | first_name    | last_name     | postcode |
            | Jackson       | Frank         | L789C349 |
            | Christopher   | Connely       | L789C349 |

    @scenario2
    Scenario: Login as Customer
        When user enter the website URL
        And user click on the customer login button
        And select Hermoine Granger from dropdown
        And click on the login button
        And select number from the dropdown
        And I perform a credit transaction of "50000"
        And I click on deposit button
        And check if current balance is "50000"
        And I perform a debit transaction of "3000"
        And I click on withdraw button
        And check if current balance is "47000"
        And I perform a debit transaction of "2000"
        And I click on withdraw button
        And check if current balance is "45000"
        And I perform a credit transaction of "5000"
        And I click on deposit button
        And check if current balance is "50000"
        And I perform a debit transaction of "10000"
        And I click on withdraw button
        And check if current balance is "40000"
        And I perform a debit transaction of "15000"
        And I click on withdraw button
        And check if current balance is "25000"
        And I perform a credit transaction of "1500"
        And I click on deposit button
        And check if current balance is "26500"
