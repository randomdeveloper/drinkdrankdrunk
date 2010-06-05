
def model_from_request(request, model_class):
    model = model_class()
    for arg in request.arguments():
        model.__dict__[arg] = request.get(arg)
    return model
