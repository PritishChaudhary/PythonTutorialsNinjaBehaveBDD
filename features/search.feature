@Search
Feature: Search Functionality
  As a visitor or logged-in user of TutorialsNinja
  I want to search for products using various criteria
  So that I can find and view the products I am interested in

  Background:
    Given I open the TutorialsNinja application in my browser


  @TC_SF_001 @smoke @regression
  Scenario Outline: TC_SF_001 - I can find a product when I search using an existing product name
    When I type "<product_name>" into the Search text box
    And I click the Search icon button
    Then I should see "<product_name>" displayed in the search results

    Examples:
      | product_name |
      | HP           |


  @TTC_SF_002 @regression @negative
  Scenario Outline: TC_SF_002 - I see a no-results message when I search for a product that does not exist
    When I type "<product_name>" into the Search text box
    And I click the Search icon button
    Then I should see the message "There is no product that matches the search criteria." on the Search Results page

    Examples:
      | product_name |
      | Honda        |


  @TC_SF_003 @regression @negative
  Scenario: TC_SF_003 - I see a no-results message when I click Search without typing anything
    When I leave the Search text box empty
    And I click the Search icon button
    Then I should see the message "There is no product that matches the search criteria." on the Search Results page


  @TC_SF_004 @regression
  Scenario Outline: TC_SF_004 - I can search for a product after I log in to the application
    Given I am logged in with email "john3456@gmail.com" and password "12345"
    When I type "<product_name>" into the Search text box
    And I click the Search icon button
    Then I should see "<product_name>" displayed in the search results

    Examples:
      | product_name |
      | HP           |


  @TC_SF_005 @regression
  Scenario Outline: TC_SF_005 - I see multiple products when my search criteria matches more than one product
    When I type "<search_criteria>" into the Search text box
    And I click the Search icon button
    Then I should see more than one product displayed in the search results

    Examples:
      | search_criteria |
      | Mac             |


  @TC_SF_006 @regression @ui
  Scenario: TC_SF_006 - I can see placeholder text in both the Search text box and the Search Criteria field
    When I leave the Search text box empty
    And I click the Search icon button
    Then I should see proper placeholder text in the Search text box
    And I should see proper placeholder text in the "Search Criteria" text box on the Search page


  @TC_SF_007 @regression
  Scenario: TC_SF_007 - I can find a product by typing in the Search Criteria field on the Search page
    When I leave the Search text box empty
    And I click the Search icon button
    And I type "HP" into the "Search Criteria" field on the Search page
    And I click the "Search" button on the Search page
    Then I should see "HP" displayed in the search results


  @TC_SF_008 @regression
  Scenario: TC_SF_008 - I can find a product by searching using text from its description
    When I leave the Search text box empty
    And I click the Search icon button
    And I type "iLife" into the "Search Criteria" field on the Search page
    And I check the "Search in product descriptions" checkbox
    And I click the "Search" button on the Search page
    Then I should see the product whose description contains "iLife" displayed in the search results


  @TC_SF_009 @regression
  Scenario: TC_SF_009 - I can find a product by selecting the correct category but get no results with a wrong category
    When I leave the Search text box empty
    And I click the Search icon button
    And I type "iMac" into the "Search Criteria" field on the Search page
    And I select "Mac" from the "Category" dropdown
    And I click the "Search" button on the Search page
    Then I should see "iMac" displayed in the search results
    When I select "PC" from the "Category" dropdown
    And I click the "Search" button on the Search page
    Then I should see the message "There is no product that matches the search criteria." on the Search Results page


  @TC_SF_010 @regression
  Scenario: TC_SF_010 - I can find a product in a subcategory when I check the Search in subcategories option
    When I leave the Search text box empty
    And I click the Search icon button
    And I type "iMac" into the "Search Criteria" field on the Search page
    And I select "Desktops" from the "Category" dropdown
    And I click the "Search" button on the Search page
    Then I should see the message "There is no product that matches the search criteria." on the Search Results page
    When I check the "Search in subcategories" checkbox
    And I click the "Search" button on the Search page
    Then I should see "iMac" displayed in the search results


  @TC_SF_011 @regression @ui
  Scenario: TC_SF_011 - I can switch between List and Grid views when a single product is shown in the results
    When I type "iMac" into the Search text box
    And I click the Search icon button
    And I click the "List" view button
    Then I should see the product displayed correctly in List view with all action buttons working
    When I click on the product image or name in List view
    Then I should be taken to the Product Display Page of that product
    When I go back to the search results
    And I type "iMac" into the Search text box
    And I click the Search icon button
    And I click the "Grid" view button
    Then I should see the product displayed correctly in Grid view with all action buttons working
    When I click on the product image or name in Grid view
    Then I should be taken to the Product Display Page of that product


  @TC_SF_012 @regression @ui
  Scenario: TC_SF_012 - I can switch between List and Grid views when multiple products are shown in the results
    When I type "Mac" into the Search text box
    And I click the Search icon button
    Then I should see more than one product displayed in the search results
    When I click the "List" view button
    Then I should see all products displayed correctly in List view with all action buttons working
    When I click the "Grid" view button
    Then I should see all products displayed correctly in Grid view with all action buttons working


  @TC_SF_013 @regression @navigation
  Scenario: TC_SF_013 - I can navigate to the Product Compare page from the Search Results page
    When I type "iMac" into the Search text box
    And I click the Search icon button
    And I click the "Product Compare" link
    Then I should be taken to the "Product Comparison" page


  @TC_SF_014 @regression
  Scenario: TC_SF_014 - I can sort the products displayed in the Search Results using the Sort By dropdown
    When I type "Mac" into the Search text box
    And I click the Search icon button
    Then I should see more than one product displayed in the search results
    When I select several options from the "Sort By" dropdown
    Then I should see the products sorted according to the option I selected


  @TC_SF_015 @regression
  Scenario: TC_SF_015 - I can choose how many products are displayed per page in the Search Results
    When I type "Mac" into the Search text box
    And I click the Search icon button
    Then I should see more than one product displayed in the search results
    When I select a number from the "Show" dropdown
    Then I should see only that number of products displayed on the current page


  @TC_SF_016 @regression @ui
  Scenario: TC_SF_016 - I can see the Search text box and Search icon button on every page of the application
    When I navigate through all the pages of the application
    Then I should see the Search text box and the Search icon button on every page


  @TC_SF_017 @regression @navigation
  Scenario: TC_SF_017 - I can navigate to the Search page by clicking the Search link on the Site Map page
    When I click the "Site Map" link in the footer
    And I click the "Search" link on the Site Map page
    Then I should be taken to the "Search" page


  @TC_SF_018 @regression @ui
  Scenario: TC_SF_018 - I can see a correct Breadcrumb on the Search Results page
    When I type "iMac" into the Search text box
    And I click the Search icon button
    Then I should see the Breadcrumb working correctly on the Search Results page


  @TC_SF_019 @regression
  Scenario: TC_SF_019 - I can perform the Search operation and interact with options using Tab and Enter keys
    When I use the Tab and Enter keys to perform a Search operation
    And I use the keyboard to select options on the Search page
    Then I should be able to complete the Search operation using only the keyboard


  @TC_SF_020 @regression @ui
  Scenario: TC_SF_020 - I can see the correct page heading, URL and title on the Search Results page
    When I type "HP" into the Search text box
    And I click the Search icon button
    Then I should see a proper Page Heading on the Search page
    And I should see the correct Page URL for the Search page
    And I should see the correct Page Title for the Search page


  @TC_SF_021 @regression @ui
  Scenario: TC_SF_021 - The Search functionality and Search page options look correct and match the UI checklist
    When I type "HP" into the Search text box
    And I click the Search icon button
    Then I should see the Search page UI matching the UI checklist
    And I should see all Search page options displayed correctly


  @TC_SF_022 @regression @cross-browser
  Scenario: TC_SF_022 - I can use the Search functionality correctly in all supported environments
    When I type "HP" into the Search text box
    And I click the Search icon button
    Then I should see the Search functionality working correctly in my current environment