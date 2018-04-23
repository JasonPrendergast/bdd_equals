Feature: test cases 2 jsonequal class
  #background will run before every scenario
  Background: Create context json string
    Given I create new context json string

  Scenario Outline: "<value1>" and "<value2>" and "<description>" and "<equal>"
    Given I have a keypair 'value1' '<value1>'
    And I have a keypair 'value2' '<value2>'
    And I have a keypair 'description' '<description>'
    And I have last keypair 'equal' '<equal>'
    Then I should see '<equal>'

  Examples:
		| value1                  | value2                   | description        | equal |
		| 2017-06-16T21:36:48.362Z| 2017-06-16T21:36:48.362Z | equal dates        | True  |
        | 2017-06-16T21:36:48.362Z| 2017-06-16T00:00:00.362Z | not equal dates    | False |
        | 2017-06-16T21:36:48.362Z| foo                      | date not string    | False |


