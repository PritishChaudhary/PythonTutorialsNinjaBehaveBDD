@Login
Feature: Login Functionality
  As a registered user of TutorialsNinja
  I want to be able to log in to my account
  So that I can access my account dashboard and personal settings

  Background:
    Given I open the TutorialsNinja application in my browser

  @TC_LF_001 @smoke @regression
  Scenario Outline: TC_LF_001 - I log in with valid credentials and land on the Account page
    When I click on "My Account" dropmenu
    And I click on "Login" option
    Then I should be on the Login page
    When I enter "<email>" into the "E-Mail Address" field
    And I enter "<password>" into the "Password" field
    And I click the "Login" button
    Then I should be logged in and taken to the "Account" page

    Examples:
      | email                    | password |
      | john3456@gmail.com       | 12345    |

  @TC_LF_002 @regression @negative
  Scenario Outline: TC_LF_002 - I see a warning when I enter an invalid email and invalid password
    When I click on "My Account" dropmenu
    And I click on "Login" option
    And I enter "<email>" into the "E-Mail Address" field
    And I enter "<password>" into the "Password" field
    And I click the "Login" button
    Then I should see a warning message "Warning: No match for E-Mail Address and/or Password."

    Examples:
      | email                 | password   |
      | john897@gmail.com     | xyzabc123  |

  @TC_LF_003 @regression @negative
  Scenario Outline: TC_LF_003 - I see a warning when I enter an invalid email with a valid password
    When I click on "My Account" dropmenu
    And I click on "Login" option
    And I enter "<email>" into the "E-Mail Address" field
    And I enter "<password>" into the "Password" field
    And I click the "Login" button
    Then I should see a warning message "Warning: No match for E-Mail Address and/or Password."

    Examples:
      | email               | password |
      | john897@gmail.com   | 12345    |

  @TC_LF_004 @regression @negative
  Scenario Outline: TC_LF_004 - I see a warning when I enter a valid email with an invalid password
    When I click on "My Account" dropmenu
    And I click on "Login" option
    And I enter "<email>" into the "E-Mail Address" field
    And I enter "<password>" into the "Password" field
    And I click the "Login" button
    Then I should see a warning message "Warning: No match for E-Mail Address and/or Password."

    Examples:
      | email                          | password   |
      | pavanoltraining@gmail.com      | xyzabc123  |

  @TC_LF_005 @regression @negative
  Scenario: TC_LF_005 - I see a warning when I click Login without entering any credentials
    When I click on "My Account" dropmenu
    And I click on "Login" option
    And I leave the "E-Mail Address" field empty
    And I leave the "Password" field empty
    And I click the "Login" button
    Then I should see a warning message "Warning: No match for E-Mail Address and/or Password."

  @TC_LF_006 @regression
  Scenario: TC_LF_006 - I can see and use the Forgotten Password link on the Login page
    When I click on "My Account" dropmenu
    And I click on "Login" option
    Then I should be on the Login page
    And I should see the "Forgotten Password" link on the Login page
    When I click on the "Forgotten Password" link
    Then I should be taken to the "Forgotten Password" page

  @TC_LF_007 @regression
  Scenario: TC_LF_007 - I can log in using the Tab and Enter keyboard keys
    When I click on "My Account" dropmenu
    And I click on "Login" option
    And I press Tab to move to the "E-Mail Address" field and type "john3456@gmail.com"
    And I press Tab to move to the "Password" field and type "12345"
    And I press Tab to move to the "Login" button and press Enter
    Then I should be logged in and taken to the "Account" page

  @TC_LF_008 @regression @ui
  Scenario: TC_LF_008 - I can see placeholder text inside the Email Address and Password fields
    When I click on "My Account" dropmenu
    And I click on "Login" option
    Then I should see proper placeholder text inside the "E-Mail Address" field
    And I should see proper placeholder text inside the "Password" field

  @TC_LF_009 @regression
  Scenario: TC_LF_009 - I remain logged in when I press the browser back button after logging in
    When I click on "My Account" dropmenu
    And I click on "Login" option
    And I enter "john3456@gmail.com" into the "E-Mail Address" field
    And I enter "12345" into the "Password" field
    And I click the "Login" button
    And I click the browser back button
    Then I should still be logged in and not be logged out

  @TC_LF_010 @regression
  Scenario: TC_LF_010 - I am not logged back in when I press the browser back button after logging out
    When I click on "My Account" dropmenu
    And I click on "Login" option
    And I enter "john3456@gmail.com" into the "E-Mail Address" field
    And I enter "12345" into the "Password" field
    And I click the "Login" button
    And I click on "My Account" dropmenu
    And I select "Logout" from the dropdown
    And I click the browser back button
    Then I should not be logged in again


  @TC_LF_011 @regression @negative
  Scenario: TC_LF_011 - I am not able to log in using inactive account credentials
    When I click on "My Account" dropmenu
    And I click on "Login" option
    And I enter "inactiveuser@gmail.com" into the "E-Mail Address" field
    And I enter "inactive123" into the "Password" field
    And I click the "Login" button
    Then I should not be able to log in to the application

#  @TC_LF_012 @regression @negative @security
#  Scenario: TC_LF_012 - I see an account lockout warning after exceeding the allowed number of login attempts
#    When I click on "My Account" dropmenu
#    And I click on "Login" option
#    And I enter "xyzabc123@gmail.com" into the "E-Mail Address" field
#    And I enter "xyzabc123" into the "Password" field
#    And I click the "Login" button 5 times with the same invalid credentials
#    Then I should see a warning message "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."

  @TC_LF_013 @regression @security @ui
  Scenario: TC_LF_013 - I cannot see the characters I type into the Password field
    When I click on "My Account" dropmenu
    And I click on "Login" option
    And I type "SamplePassword123" into the "Password" field
    Then I should see my typed text hidden using masked characters in the "Password" field

  @TC_LF_014 @regression @security
  Scenario: TC_LF_014 - I cannot copy the text I have typed into the Password field
    When I click on "My Account" dropmenu
    And I click on "Login" option
    And I type "SamplePassword123" into the "Password" field
    Then the "Password" field input type should be "password" to prevent copying

  @TC_LF_015 @regression @security
  Scenario: TC_LF_015 - I cannot see my password text when I inspect the page source
    When I click on "My Account" dropmenu
    And I click on "Login" option
    And I type "SamplePassword123" into the "Password" field
    Then the "Password" field input type attribute should be "password" in the page source

  @TC_LF_016 @regression
  Scenario: TC_LF_016 - I cannot use my old password after I change it but I can use my new password
    When I click on "My Account" dropmenu
    And I click on "Register" option
    And I register a new user
    When I click on "My Account" dropmenu
    And I click on "Login" option
    When I login with valid credentials
    And I change my password
    And I logout
    Then I should not be able to login with old password
    And I should be able to login with new password


  @TC_LF_017 @regression
  Scenario: TC_LF_017 - My session is still active when I reopen the browser without logging out first
    When I click on "My Account" dropmenu
    And I click on "Login" option
    And I enter "john3456@gmail.com" into the "E-Mail Address" field
    And I enter "12345" into the "Password" field
    And I click the "Login" button
    And I navigate back to the application base URL
    Then my login session should still be active and I should not be logged out

#  @TC_LF_018 @regression
#  Scenario: TC_LF_018 - I am automatically logged out after my session times out
#    When I click on "My Account" dropmenu
#    And I click on "Login" option
#    And I enter "pavanoltraining@gmail.com" into the "E-Mail Address" field
#    And I enter "12345" into the "Password" field
#    And I click the "Login" button
#    Then I should be logged in and taken to the "Account" page

  @TC_LF_019 @regression @navigation
  Scenario: TC_LF_019 - I can navigate to different pages from the Login page
    When I click on "My Account" dropmenu
    And I click on "Login" option
    And I click the "Continue" button under the "New Customer" section
    Then I should be taken to the "Register Account" page
    When I navigate back to the Login page
    And I click on various navigation options available on the Login page
    Then I should be taken to the appropriate pages

  @TC_LF_020 @regression @navigation
  Scenario: TC_LF_020 - I can reach the Login page in three different ways
    When I click the "login page" link from the "Register Account" page
    Then I should be on the Login page
    When I click the "Login" option from the "Right Column" navigation
    Then I should be on the Login page
    When I click on "My Account" dropmenu
    And I click on "Login" option
    Then I should be on the Login page

  @TC_LF_021 @regression @ui
  Scenario: TC_LF_021 - I can see the correct breadcrumb, page heading, title and URL on the Login page
    When I click on "My Account" dropmenu
    And I click on "Login" option
    Then I should see a proper Breadcrumb on the Login page
    And I should see a proper Page Heading on the Login page
    And I should see the correct Page URL for the Login page
    And I should see the correct Page Title for the Login page

  @TC_LF_022 @regression @ui
  Scenario: TC_LF_022 - The Login page looks correct and matches the UI checklist
    When I click on "My Account" dropmenu
    And I click on "Login" option
    Then I should see the Login page UI matching the UI checklist
    And I should see the "Returning Customer" section with "E-Mail Address" and "Password" fields
    And I should see the "New Customer" section with a "Continue" button

  @TC_LF_023 @regression @cross-browser
  Scenario: TC_LF_023 - I can use the Login functionality correctly in all supported environments
    When I click on "My Account" dropmenu
    And I click on "Login" option
    Then I should see the Login functionality working correctly in my current environment
