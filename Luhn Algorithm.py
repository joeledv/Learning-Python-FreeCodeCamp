def verify_card_number(card_number):
    """Verify if the provided card number is valid using the Luhn algorithm."""
    card_number = str(card_number)
    card_number = card_number.strip()
    card_number = card_number.replace(' ', '')
    
    if '-' in card_number:
        card_number = card_number.replace('-', '')
        
    card_number_list = list(card_number)
    card_number_list.reverse()
    
    for index, number in enumerate(card_number_list):
        if index % 2 == 1:
            doubled = int(number) * 2
            if doubled > 9:
                doubled -= 9
            card_number_list[index] = str(doubled)

    total_sum = 0 
    for number in card_number_list:
        total_sum += int(number)

    if total_sum % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"    