import unittest
from data_structures import *

class MyTestCase(unittest.TestCase):
    def test_1_find_max(self):
        list= [1, 2, 3, 4]
        results= find_max(list)
        
        self.assertEqual(results, 4)

    def test_2_find_max_negative_numbers(self):
        list= [-1, -2, -3, -4]
        results= find_max(list)
        
        self.assertEqual(results, -1)

    def test_3_find_max_mixed_numbers(self):
        list= [-1, 2, 3, -4]
        results= find_max(list)
        
        self.assertEqual(results, 3)

    
    def test_4_find_min(self):
        list= [1, 2, 3, 4]
        results= find_min(list)
        
        self.assertEqual(results, 1)

    def test_5_find_min_negative_numbers(self):
        list= [-1, -2, -3, -4]
        results= find_min(list)
        
        self.assertEqual(results, -4)

    def test_6_find_min_mixed_numbers(self):
        list= [1, -2, -3, 4]
        results= find_min(list)
        
        self.assertEqual(results, -3)

    
    def test_7_find_average(self): 
        list= [1, 2, 3, 4]
        results= find_average(list)
        
        self.assertEqual(results, 2.5)

    def test_8_find_negative_average(self): 
        list= [-1, -2, -3, 4]
        results= find_average(list)
        
        self.assertEqual(results, -0.5)

    def test_9_find_mixed_average(self): 
        list= [-1, -2, 3, 4]
        results= find_average(list)
        
        self.assertEqual(results, 1.0)


    def test_10_find_all_even_numbers(self):
        list= [1, 2, 3, 4]
        results= find_even_numbers(list)
        
        self.assertEqual(results, (2, 4))

    def test_11_find_all_even_negative_numbers(self):
        list= [-1, -2, -3, -4]
        results= find_even_numbers(list)
        
        self.assertEqual(results, (-2, -4))

    def test_12_find_all_even_mixed_numbers(self):
        list= [-1, -2, 3, 4]
        results= find_even_numbers(list)
        
        self.assertEqual(results, (-2, 4))
        

    def test_13_find_all_odd_numbers(self):
        list= [1, 2, 3, 4]
        results= find_odd_numbers(list)
        
        self.assertEqual(results, (1, 3))

    def test_14_find_all_odd_negative_numbers(self):
        list= [-1, -2, -3, -4]
        results= find_odd_numbers(list)
        
        self.assertEqual(results, (-1, -3))

    def test_15_find_all_odd_mixed_numbers(self):
        list= [1, -2, -3, 4]
        results= find_odd_numbers(list)
        
        self.assertEqual(results, (1, -3))

    
    def test_16_find_total_number_of_even_numbers(self):
        list= [1, 2, 3, 4]
        results= find_number_of_even_numbers(list)
        
        self.assertEqual(results, 2)

    def test_17_find_total_number_of_negative_even_numbers(self):
        list= [-1, -2, -3, -4]
        results= find_number_of_even_numbers(list)
        
        self.assertEqual(results, 2)

    def test_18_find_total_number_of_mixed_even_numbers(self):
        list= [1, -2, -3, 4]
        results= find_number_of_even_numbers(list)
        
        self.assertEqual(results, 2)


    def test_19_find_total_number_of_odd_numbers(self):
        list= [1, 2, 3, 4]
        results= find_number_of_odd_numbers(list)
        
        self.assertEqual(results, 2)

    def test_20_find_total_number_of_negative_odd_numbers(self):
        list= [-1, -2, -3, -4]
        results= find_number_of_odd_numbers(list)
        
        self.assertEqual(results, 2)

    def test_21_find_total_number_of_mixed_odd_numbers(self):
        list= [1, -2, -3, 4]
        results= find_number_of_odd_numbers(list)
        
        self.assertEqual(results, 2)


    def test_22_return_list_stats(self): 
        list= [1, 2, 3, 4, 5]
        results= return_list_stats(list)
        output = {
            "unique_numbers": {1, 2, 3, 4, 5},
                "min": 1, "max": 5, "average": 3.0,
                "even_numbers": (2, 4),
                "odd_numbers": (1, 3, 5),
                "number_of_even_numbers": 2,
                "number_of_odd_numbers": 3
        }
        self.assertEqual(results, output)

    def test_23_return_list_stats_of_negative_numbers(self): 
        list= [-1, -2, -3, -4, -5]
        results= return_list_stats(list)
        output = {
            "unique_numbers": {-1, -2, -3, -4, -5},
                "min": -5, "max": -1, "average": -3.0,
                "even_numbers": (-2, -4),
                "odd_numbers": (-1, -3, -5),
                "number_of_even_numbers": 2,
                "number_of_odd_numbers": 3
        }
        self.assertEqual(results, output)

    def test_24_return_list_stats_of_mixed_numbers(self): 
        list= [1, -2, -3, 4, 5]
        results= return_list_stats(list)
        output = {
            "unique_numbers": {1, -2, -3, 4, 5},
                "min": -3, "max": 5, "average": 1.0,
                "even_numbers": (-2, 4),
                "odd_numbers": (1, -3, 5),
                "number_of_even_numbers": 2,
                "number_of_odd_numbers": 3
        }
        self.assertEqual(results, output)


    def test_25_basic(self):
        input_list = ['a', '1', 'b', '3', 'c', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)
        alphabets= ['a', 'b', 'c', 'd', 'e']
        numbers = [1, 3, 5]

        self.assertEqual(result_alphabets, alphabets)
        self.assertEqual(result_numbers, numbers)

    def test_26_mixed_input(self):
        input_list = ['a', '1', 'b', '3', 'c', '2', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)
        alphabets = ['a', 'b', 'c', 'd', 'e']
        numbers = [1, 2, 3, 5]

        self.assertEqual(result_alphabets, alphabets)
        self.assertEqual(result_numbers, numbers)

    def test_27_repeated_characters(self):
        input_list = ['1', 'b', 'a', 'c', 'c', 'b', 'a', '1']
        result_alphabets, result_numbers = process_characters(input_list)
        alphabets = ['a', 'b', 'c']
        numbers = [1]

        self.assertEqual(result_alphabets, alphabets)
        self.assertEqual(result_numbers, numbers)

    def test_28_special_characters(self):
        input_list = ['!', '@', '#', '1', '2', '3', '$', '%', '^']
        result_alphabets, result_numbers = process_characters(input_list)
        alphabets = []
        numbers = [1, 2, 3]

        self.assertEqual(result_alphabets, alphabets)
        self.assertEqual(result_numbers, numbers)

    def test_29_more_special_characters(self):
        input_list = ['%', '&', '*', '4', '6', '8', '(', ')', '!', 'x']
        result_alphabets, result_numbers = process_characters(input_list)
        alphabets = ['x']
        numbers = [4, 6, 8]

        self.assertEqual(result_alphabets, alphabets)
        self.assertEqual(result_numbers, numbers)


    def test_30_generate_squared_dict(self):
        result = generate_squared_dict(5) 
        output = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

        self.assertEqual(result, output)
    
    def test_31_zero_input(self):
        result = generate_squared_dict(0) 
        output = {}

        self.assertEqual(result, output)
    
    def test_32_negative_input(self):
        result = generate_squared_dict(-5) 
        output = {-5: 25, -4: 16, -3: 9, -2: 4, -1: 1,}

        self.assertEqual(result, output)


    def test_33_convert_word_list_sentence(self):
        result = convert_to_word_list("There is only one to fear and his name is Death, and there is only one thing we say to Death: 'Not today!")
        output = ['there', 'is', 'only', 'one', 'to', 'fear', 'and', 
        'his', 'name', 'is', 'death', 'and', 'there', 'is', 'only', 
        'one', 'thing', 'we', 'say', 'to', 'death', 'not', 'today']

        self.assertEqual(result, output)

    def test_34_convert_word_list_spaces(self): #extra spaces between the string sentence
        result = convert_to_word_list("There   is only  one  to fear and his name is Death,"
        +" and  there is only  one  thing we  say  to  Death: 'Not today!")
        output = ['there', 'is', 'only', 'one', 'to', 'fear', 'and', 
        'his', 'name', 'is', 'death', 'and', 'there', 'is', 'only', 
        'one', 'thing', 'we', 'say', 'to', 'death', 'not', 'today']

        self.assertEqual(result, output)

    def test_35_convert_word_list(self): #concantenated string
        result = convert_to_word_list("There  is only  one to fear and his name is Death,"
        +" and there is only one thing we say  to  Death: 'Not today!")
        output = ['there', 'is', 'only', 'one', 'to', 'fear', 'and', 
        'his', 'name', 'is', 'death', 'and', 'there', 'is', 'only', 
        'one', 'thing', 'we', 'say', 'to', 'death', 'not', 'today']

        self.assertEqual(result, output)


    def test_36_letters_count_sentence(self):
        text = "There  is only  one to fear and his name is Death," + " and there is only one thing we say  to  Death: 'Not today!"
        result = letters_count_map(text)
        output = {'a': 8, 'b': 0, 'c': 0, 'd': 5, 'e': 11, 'f': 1, 'g': 1, 'h': 6, 'i': 5, 'j': 0, 'k': 0, 'l': 2, 'm': 1,
                  'n': 9, 'o': 8, 'p': 0, 'q': 0, 'r': 3, 's': 5, 't': 9, 'u': 0, 'v': 0, 'w': 1, 'x': 0, 'y': 4, 'z': 0}

        self.assertEqual(result, output)

    def test_37_letters_count_special_characters(self): #has special characters
        text = "There  is only  one to fear and his name is @Death," + " and there is only one thing we say  to  Death: '#Not today!"
        result = letters_count_map(text)
        output = {'a': 8, 'b': 0, 'c': 0, 'd': 5, 'e': 11, 'f': 1, 'g': 1, 'h': 6, 'i': 5, 'j': 0, 'k': 0, 'l': 2, 'm': 1,
                  'n': 9, 'o': 8, 'p': 0, 'q': 0, 'r': 3, 's': 5, 't': 9, 'u': 0, 'v': 0, 'w': 1, 'x': 0, 'y': 4, 'z': 0}

        self.assertEqual(result, output)

    def test_38_letter_count_with_numbers(self): #has numbers
        text = "There  is only  1 2 fear and his name is Death," + " and there is only one thing we say  to  Death: 'Not today1"
        result = letters_count_map(text)
        output = {'a': 8, 'b': 0, 'c': 0, 'd': 5, 'e': 10, 'f': 1, 'g': 1, 'h': 6, 'i': 5, 'j': 0, 'k': 0, 'l': 2, 'm': 1,
                  'n': 8, 'o': 6, 'p': 0, 'q': 0, 'r': 3, 's': 5, 't': 8, 'u': 0, 'v': 0, 'w': 1, 'x': 0, 'y': 4, 'z': 0}

        self.assertEqual(result, output)

    def test_39_letter_count_mixed_string(self): #mixed with numbers and special characters
        text = "There  is only  1 2 fear and his name is Death," + " and there is only one thing we say  to  <Death>: '#Not today!"
        result = letters_count_map(text)
        output = {'a': 8, 'b': 0, 'c': 0, 'd': 5, 'e': 10, 'f': 1, 'g': 1, 'h': 6, 'i': 5, 'j': 0, 'k': 0, 'l': 2, 'm': 1,
                  'n': 8, 'o': 6, 'p': 0, 'q': 0, 'r': 3, 's': 5, 't': 8, 'u': 0, 'v': 0, 'w': 1, 'x': 0, 'y': 4, 'z': 0}

        self.assertEqual(result, output)


    def test_40_morse_code_single_string(self):
        text = 'Hello'
        result = text_to_morse(text)
        output = '.... . .-.. .-.. ---'

        self.assertEqual(result, output)
        
    def test_41_alphanumeric_1(self): #string with numbers
        text = 'Hello 123'
        result = text_to_morse(text)
        output = '.... . .-.. .-.. ---   .---- ..--- ...--'

        self.assertEqual(result, output)
    
    def test_42_alphanumeric_2(self): #string with punctuation
        text = 'Hello!?'
        result = text_to_morse(text)
        output = '.... . .-.. .-.. --- -.-.-- ..--..'

        self.assertEqual(result, output)

    def test_43_alphanumeric_3(self):
        text = 'Hello!? 123'
        result = text_to_morse(text)
        output = '.... . .-.. .-.. --- -.-.-- ..--..   .---- ..--- ...--'

        self.assertEqual(result, output)


    def test_44_random_list(self): #test length output
        n = 5
        result = generate_random_list(n)

        self.assertEqual(len(result), n)

    
if __name__ == '__main__':
    main()
