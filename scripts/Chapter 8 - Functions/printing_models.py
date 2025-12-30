def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left.
    move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all models that were printed"""
    print("\nThe following models were printed:")
    for model in completed_models:
        print(model)

# Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendent', 'dodecachedron']
completed_models = []

# Display all completed models
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)