# Note: This is one way to do it. You might have done it differently.

# Define the symbols we want to display for the different operators
implies = '⟶',
iff = '⟷',

# Print a truth table for a given operation
def print_truth_table(operation):
    print(f"p       q       p {implies} q")
    for p in [True, False]:
        for q in [True, False]:
            print(f'{p!s:<8}{q!s:<8}{operation(p,q)!s:<8}')
    print()

    
def print_truth_table(operation):
    print(f"p       q       p {implies} q")
    for p in [True, False]:
        for q in [True, False]:
            print(f'{p!s:<8}{q!s:<8}{operation(p,q)!s:<8}')
    print()

print_truth_table(implies)
print_truth_table(iff)