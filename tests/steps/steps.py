from behave import given, then, when
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


# ==================================================================================================================== #

@when('I call the class')
def i_call_the_class(context):
    context.testjson = str(context.jsonvaluepairstring).replace('\'', '\"')
    context.testjson = json.loads(context.testjson)
    context.testy = jsonequals.jsonequals(context.testjson)
    context.testy = context.testy.jsonequals()
    print(context.testy)

# ==================================================================================================================== #


@then('I should see {result}')
def i_should_see_result(context, result):
    context.result = result.replace('\'', '')
    if str(context.testy) == str(context.result):
        return context.testjson['equal']

    else:
        raise Exception("Unexpected text passed in.")







