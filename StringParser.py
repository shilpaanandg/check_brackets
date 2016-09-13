
allowed_seq_dict={'curly_braces':'{}','round_braces':'()','sqr_braces':'[]','angular_braces:':'<>'}
opening_braces_dict={'curly_brace':'{','round_braces':'(','sqr_braces':'[','angular_braces:':'<'}
closing_braces_dict={'curly_braces':'}','round_braces':')','sqr_braces':']','angular_braces:':'>'}



'''
Following function takes string as an argument and outputs another string with brackets only.
'''

def parse_string(str_input_seq):
    parsed_str_seq=""
    for char in str_input_seq:
        if char in opening_braces_dict.values() or char in closing_braces_dict.values():
            parsed_str_seq=parsed_str_seq+char    
        
    return parsed_str_seq

'''
This function checks if parsed string has even number of characters
This is first level check. If bracket count is odd then bracket is missing so sequence is wrong.
'''

def is_char_count_even(str_input_seq):
    if len(str_input_seq)%2==0:
        return True


'''
This function takes string as input and checks the adjacent brackets sequence is matching or not
returns boolean
'''
def check_sequence_same_type(str_input_seq):
    parsed_str_seq = parse_string(str_input_seq)
    is_seq_ok = False
    if is_char_count_even(parsed_str_seq):
        even_elements = parsed_str_seq[1::2]
        odd_elements = parsed_str_seq[::2]
        for i in range(len(even_elements)):
            if odd_elements[i]+even_elements[i] in allowed_seq_dict.values():
                is_seq_ok = True
            else:
                return False
    return is_seq_ok


'''
This function takes string as input and checks the nested brackets sequence is correct or not
returns boolean
'''
def check_sequence_mixed_type(str_input_seq):
    parsed_str_seq = parse_string(str_input_seq)
    is_seq_ok = False
    list_opening_braces = []
    list_closing_braces = []
    
    if is_char_count_even(parsed_str_seq):
        for i in range(len(parsed_str_seq)):
            if parsed_str_seq[i] in opening_braces_dict.values():
                if len(list_closing_braces)>0:
                    return False
                list_opening_braces.append(parsed_str_seq[i])
                
            else:
                list_closing_braces.append(parsed_str_seq[i])
                
    if len(list_opening_braces)==len(list_closing_braces):
        is_seq_ok=False
        list_closing_braces.reverse()
        for i in range(len(list_closing_braces)):
            if list_opening_braces[i]+list_closing_braces[i] in allowed_seq_dict.values():
                is_seq_ok=True
            else:
                return False
    return is_seq_ok
            
     

if __name__=='__main__':
    str_input_seq=raw_input()
    print check_sequence_mixed_type(str_input_seq)
    print check_sequence_same_type(str_input_seq)