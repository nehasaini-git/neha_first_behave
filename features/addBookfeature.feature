
  Feature: Verify if books are added and deleted using Library API

    @library
    Scenario: Verify AddBook API
      Given the book details which needs to be added to Library
      When we execute the AddBook PostAPI method
      Then book is successfully added

    @focus
    Scenario Outline: Veify AddBook API with parameterisation
      Given the book details with <isbn> and <aisle> needs to be added to Library
      When we execute the AddBook PostAPI method
      Then book is successfully added
      Examples:
      | isbn |  aisle  |
      | fghj |  8765   |


