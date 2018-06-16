Feature: Validate shop cart behavior

  Scenario: Calculate total number of items added in shop cart
    Given The user adds 5 product to shop cart
    When  He adds 4 more products on the shop cart
    Then  The total number of items in shop cart shall be equal to 9


  Scenario: Calculate the total price of items in shop cart
    Given The user added a product in shop cart with value 200
    When  The user adds another product in shop cart with value 300
    Then  the total value of products in shop cart shall be 500