# Ensure input is not empty
def get_non_empty_string(question):
    answer = ''
    while len(answer) == 0: # Do not allow any string input to be less than one character or blank
        answer = input(question).strip()  # remove empty space, so ' ' will become an empty string
    return answer

# Ensure input is a REAL number
def get_positive_float(question):
    while question > 0: # Do not allow a float input to be less than 0
        return float(input(question))
