Feature: test cases jsonequal class
  #background will run before every scenario
  Background: Create context json string
    Given I create new context json string

#  Scenario Outline: "<quantity>" and "<payment method>"
  Scenario: equal date
    Given I have a keypair 'value1' '2017-06-16T21:36:48.362Z'
    And I have a keypair 'value2' '2017-06-16T21:36:48.362Z'
    And I have a keypair 'description' 'equal date objects'
    Given I have last keypair 'equal' 'True'
    Then I should see 'True'

#  Examples:
#		|   value1    |    value       |
#		|    1     |  credit card   |
#		|   10     |  credit card   |
#		|   15     |  credit card   |
#		|    1     |   gift card    |
#		|   10     |   gift card    |
#		|   15     |   gift card    |


