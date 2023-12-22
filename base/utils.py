def validate_data(request, field, update=False):
    request = request.copy()

    if 'image' in request:
        if update:
            if type(request[field]) == str:
                request.__delitem__(field,)
        else:
            if type(request[field]) == str:
                request.__setitem__(field, None)

    return request

