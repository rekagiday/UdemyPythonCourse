def display_info(a, b, *args, name="User", **kwargs):
    return [a, b, args, name, kwargs]
print(display_info(1, 2, 3, age=32, language="python"))

# 1 parameters
# 2 *args
# 3 default parameters
# 4 **kwargs
