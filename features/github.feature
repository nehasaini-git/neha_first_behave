
  Feature: Github API validation

    Scenario: Session management check
      Given I have github credentials
      When I hit getRepo API
      Then status code of response should be 200

