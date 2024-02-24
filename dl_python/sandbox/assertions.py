
def my_function(ne, my_dict):
    try:
        #assert type(my_dict) is dict
        assert isinstance(my_dict, dict), 'what you pass as is not a dictionary'
    except AssertionError as err:
        print(err)
        what_type = type(my_dict)
        raise Exception('the variable you passed as my_dict is not a dictionary. '
                        'You are instead passing a {your_type}'
                        .format(your_type=what_type))
    except Exception as err:
        print(err)
        raise Exception('Got error: {err}.'
                        .format(err=err))

    print('FUNCTION 1 ALL FINE')
    #print(my_function.__name__)
    #print(my_function.__qualname__)


def my_function2(ne, my_dict, my_string):
    try:
        #assert type(my_dict) is dict
        assert isinstance(my_dict, dict), ('what you pass as my_dict is not a '
                                           'dictionary, it is a {what_is}'
                                           .format(what_is=type(my_dict)))
        assert isinstance(my_string, str), ('what you pass as my_string is not '
                                            'is not a string, it is a {what_is}'
                                            .format(what_is=type(my_string)))
    except AssertionError as err:
        #print(err)
        #what_type = type(my_dict)
        #raise Exception('the variable you passed as my_dict is not a dictionary. '
        #                'You are instead passing a {your_type}'
        #                .format(your_type=what_type))
        #raise Exception(err)
        raise Exception('Got error: {err}.'
                        .format(err=err))
    except Exception as err:
        print(err)
        raise Exception('Got error: {err}.'
                        .format(err=err))

    print('FUNCTION 2 ALL FINE')
    #print(my_function.__name__)
    #print(my_function.__qualname__)


if __name__ == '__main__':
    ne = 'edge3-testlab.nn.hea.net'
    my_dict = {
        'key_one': 'one',
        'key_two': 'two'
    }
    my_list = ['one', 'two']
    my_string = 'one'

    my_function(ne, my_dict)
    my_function2(ne, my_list, my_list)
