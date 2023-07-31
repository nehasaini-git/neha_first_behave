Feature: Verify book is details can be viewed

    @smoke
    Scenario: Verify GetBook API functionality
    Given the book details are available
    When I execute GetBook API
    Then book details are successfully received



