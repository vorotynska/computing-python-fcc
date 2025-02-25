#In this project, you are going to build a program that takes a
#camelCase or PascalCase formatted string as input and converts
#that to a snake_case formatted string using two approaches. First,
#you'll use a for loop and then list comprehension to achieve the same
#results. You'll see how list comprehension can make your code more concise

# ---- list comprehension ----
def convert_to_snake_case(pascal_or_camel_cased_string):
    pass
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')

    return clean_snake_cased_string
    snake_cased_char_list = ['_' + char.lower() if char.isupper() else char for char in pascal_or_camel_cased_string]
    return ''.join(snake_cased_char_list).strip('_')

def main1():
    print(convert_to_snake_case('IAmAPascalCasedString'))

# ---- used a for loop to iterate over your input string ------

def convert_to_snake_case( pascal_or_camel_cased_string):
    snake_cased_char_list = [] 
    for char in pascal_or_camel_cased_string:
        #.isupper() to check if a character is uppercase
        if char.isupper():
            converted_character = '_' + char.lower()
            #add to the list
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string = ''.join(snake_cased_char_list)
    # removes any leading and underscore.
    clean_snake_cased_string = snake_cased_string.strip('_')
    return clean_snake_cased_string
 
def main():
    print(convert_to_snake_case('aLongAndComplexString'))
main()

# ----------------------------------------------

def convert_to_snake_case_a(pascal_or_camel_cased_string):
    snake_cased_char_list = [] 
    for char in pascal_or_camel_cased_string:
        # Проверяем, является ли символ заглавным
        if char.isupper():
            # Преобразуем в нижний регистр и добавляем подчеркивание перед символом
            converted_character = f"_{char.lower()}"
        else:
            # Если символ не заглавный, оставляем его как есть
            converted_character = char
        
        # Добавляем преобразованный символ в список
        snake_cased_char_list.append(converted_character)
    
    # Соединяем символы в строку
    snake_cased_string = ''.join(snake_cased_char_list)
    clean_snake_cased_string = snake_cased_string.strip('_')
    return clean_snake_cased_string

# Пример использования
print(convert_to_snake_case_a("PascalCaseString"))  # Результат: _pascal_case_string
