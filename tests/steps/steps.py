from behave import given, then
import jsonequals
import json

# ==================================================================================================================== #

@given('I create new context json string')
def I_create_new_context_json_string(context):
    context.jsonvaluepairstring = '{'

# ==================================================================================================================== #

@given('I have a keypair {pairkey} {pairvalue}')
def i_have_pairkey_pairvalue(context, pairkey, pairvalue):
    context.jsonvaluepairstring += '{p1}:{p2},'.format(p1=pairkey, p2=pairvalue)

# ==================================================================================================================== #

@given('I have last keypair {pairkey} {pairvalue}')
def i_have_pairkey_pairvalue(context, pairkey, pairvalue):
    context.jsonvaluepairstring += '{p1}:{p2}'.format(p1=pairkey, p2=pairvalue)
    context.jsonvaluepairstring += '}'
    print(str(context.jsonvaluepairstring))

    # ""'value2'":"'2017-06-16T21:36:48.362Z', ""'description'":"'equal date objects', ""'equal'":"'True'"}
# ==================================================================================================================== #
@then('I should see {result}')
def I_should_see_result(context, result):
    testjson = str(context.jsonvaluepairstring).replace('\'', '\"')
    testjson = json.loads(testjson)
    testy = jsonequals.jsonequals(testjson)
    testy = testy.jsonequals()
    print(testy)
    result = result.replace('\'', '')
    if str(testy) == str(result):
        return testjson['equal']

    else:
        raise Exception("Unexpected text passed in.")






