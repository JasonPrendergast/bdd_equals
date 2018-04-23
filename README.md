# bdd_equals
Using bdd behave to write tests. I have chosen to use my jsonequal class as the example 
because RESTful is so common and I want to use it for this reason.

#Usage 

    bdd_equals\tests\features>behave test_bdd_jsoneqauls2.feature

#output
    
    bdd_equals\tests\features>behave test_bdd_jsoneqauls2.feature
    Feature: test cases 2 jsonequal class # test_bdd_jsoneqauls2.feature:1

     Background: Create context json string  # test_bdd_jsoneqauls2.feature:3

     Scenario Outline: "2017-06-16T21:36:48.362Z" and "2017-06-16T21:36:48.362Z" and "equal dates" and "True" -- @1.1   # test_bdd_jsoneqauls2.feature:15
      Given I create new context json string                                                                           # ../steps/steps.py:7
      Given I have a keypair 'value1' '2017-06-16T21:36:48.362Z'                                                       # ../steps/steps.py:13
      And I have a keypair 'value2' '2017-06-16T21:36:48.362Z'                                                         # ../steps/steps.py:13
      And I have a keypair 'description' 'equal dates'                                                                 # ../steps/steps.py:13
      And I have last keypair 'equal' 'True'                                                                           # ../steps/steps.py:19
      Then I should see 'True'                                                                                         # ../steps/steps.py:27

    Scenario Outline: "2017-06-16T21:36:48.362Z" and "2017-06-16T00:00:00.362Z" and "not equal dates" and "False" -- @1.2   # test_bdd_jsoneqauls2.feature:16
      Given I create new context json string                                                                                # ../steps/steps.py:7
      Given I have a keypair 'value1' '2017-06-16T21:36:48.362Z'                                                            # ../steps/steps.py:13
      And I have a keypair 'value2' '2017-06-16T00:00:00.362Z'                                                              # ../steps/steps.py:13
      And I have a keypair 'description' 'not equal dates'                                                                  # ../steps/steps.py:13
      And I have last keypair 'equal' 'False'                                                                               # ../steps/steps.py:19
      Then I should see 'False'                                                                                             # ../steps/steps.py:27

    Scenario Outline: "2017-06-16T21:36:48.362Z" and "foo" and "date not string" and "False" -- @1.3   # test_bdd_jsoneqauls2.feature:17
      Given I create new context json string                                                           # ../steps/steps.py:7
      Given I have a keypair 'value1' '2017-06-16T21:36:48.362Z'                                       # ../steps/steps.py:13
      And I have a keypair 'value2' 'foo'                                                              # ../steps/steps.py:13
      And I have a keypair 'description' 'date not string'                                             # ../steps/steps.py:13
      And I have last keypair 'equal' 'False'                                                          # ../steps/steps.py:19
      Then I should see 'False'                                                                        # ../steps/steps.py:27

    1 feature passed, 0 failed, 0 skipped
    3 scenarios passed, 0 failed, 0 skipped
    18 steps passed, 0 failed, 0 skipped, 0 undefined
    Took 0m0.015s


