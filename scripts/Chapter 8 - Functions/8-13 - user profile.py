def build_profile(first, last, **kwargs):
    """Build a dictionary containing everything we know about a user."""
    kwargs['first_name'] = first
    kwargs['last_name'] = last
    return kwargs

user_profile = build_profile('morgan', 'josepher',
                             location='gilbert, az',
                             field='network automation',
                             profession='engineer'
                             )
print(user_profile)