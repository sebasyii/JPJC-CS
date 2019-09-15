# Read the equation file

infile = open("equations.txt", "r")

equation = infile.readline()[:-1]
alphabet = [chr(i) for i in range(97, 123)]


def get_terms(eqn):
    term = eqn[0]
    terms = []

    for char in eqn[1:]:
        # If it is a alphabet
        if char in ("+", "-"):
            terms.append(term)
            term = char
        else:
            term += char
    terms.append(term)
    return terms


# Split it into left and right
LHS, RHS = equation.split("=")
LHS_terms = get_terms(LHS)
RHS_terms = get_terms(RHS)

variable = ""
for i in equation:
    if i in alphabet:
        variable = i

coeff_sum = 0
const_sum = 0

# Move all the variable to the right and all the constant to the left

for lhs_char in LHS_terms:
    if variable in lhs_char:
        coeff = lhs_char[:-1]
        coeff_sum += int(coeff)
    else:
        const_sum += -int(lhs_char)

for rhs_char in RHS_terms:
    if variable in rhs_char:
        coeff = rhs_char[:-1]
        coeff_sum += -int(coeff)
    else:
        const_sum += int(rhs_char)

print(const_sum / coeff_sum)
