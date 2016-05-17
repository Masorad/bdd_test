def validate_step_input(provided_input, valid_values):
    if not provided_input in valid_values:
        exc_msg = "'{}' is an invalid value. Valid values: {}".format(
            provided_input, valid_values)
        raise ValueError(exc_msg)

