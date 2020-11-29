from problem_1_lib import \
    inputs, actions, \
    create_file, input_lines_0, \
    view_file, print_lines_0, \
    remove_file

print(actions.get('create'))
file_name = create_file(input(inputs.get('name')), input_lines_0)

if file_name is not None:
    print(actions.get('view').format(file_name))
    view_file(file_name, print_lines_0)
    remove_file(file_name)
