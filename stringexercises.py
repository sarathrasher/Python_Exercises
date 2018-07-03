# # def capitalize(string):
# #     new_string = ''
# #     for char in string:
# #     i = 0
# #     if char in lowercase:
# #         for i in range(len(lowercase)):
# #             if char == lowercase[i]:
# #                 new_string += uppercase[i]
# #     else:
# #         new_string += char
# #     return new_string

# # print new_string

# #Uppercase a string

# string = "ab cd"
# upper_string = ""
# lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# for char in string:
#     i = 0
#     if char in lowercase:
#         for i in range(len(lowercase)):
#             if char == lowercase[i]:
#                 upper_string += uppercase[i]
#                 break
#     else:
#         upper_string += char
# print upper_string

#     # Alternate
# # def capitalize(string):
# #     new_string = ''
# #     lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# #     uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# #     i = 0
# #     for char in string:
# #         if char in lowercase:
# #             for i in range(len(lowercase)):
# #                 if char == lowercase[i]:
# #                     new_string += uppercase[i]
# #                     break
# #         else:
# #             new_string += char
# #     return new_string

# # capitalize("ab cd")
# # print new_string
    
# # Capitalize a string
# # Capitalize a string
# string = "!ab cd"
# capital_string = ""
# space = " "
# lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# if string[0] in lowercase:
#     for j in range(len(lowercase)):
#         if string[0] == lowercase[j]:
#             capital_string += uppercase[j]
#             break
# else:
#     capital_string += string[0]

# for i in range(1, len(string)):
#     if string[i - 1] == space:
#         if string[i] in lowercase:
#             for j in range(len(lowercase)):
#                 if string[i] == lowercase[j]:
#                     capital_string += uppercase[j]
#                     break
#     else:
#             capital_string += string[i]
    
# print capital_string

#     # Alternate
# # if string[0] in lowercase:
# #     capitalize(string[0])
# # else:
# #     new_string += string[0]

# # for i in range(1, len(string)):
# #     if string[i - 1] == space:
# #         capitalize(string[i])
# #     else:
# #             new_string += string[i]
    
# # print new_string

# # Reverse a string

# string = "hey babe"
# reverse_string = ""
# for i in range(len(string) - 1, -1, -1):
#     reverse_string += string[i]
# print reverse_string

# Leetspeak
string = "Leet"
leet_string = ""
lower_string = ''
lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters = ['a', 'e', 'g', 'i', 'o', 's', 't'] 
leet = ['4', '3', '6', '1', '0', '5', '7']
# for i in range(len(string)):
#     if string[i] in uppercase:
#         for j in range(len(uppercase)):
#             if string[i] == uppercase[j]:
#                 lower_string += lowercase[j]
#                 break
#     else:
#         lower_string += string[i]
# for k in range(len(lower_string)):
#     if lower_string[k] in letters:
#         for l in range(len(letters)):
#             if lower_string[k] == letters[l]:
#                 leet_string += leet[l]
#                 break
#     else:
#         leet_string += lower_string[k]
# print leet_string

def replace_letter(string, list1, list2):
    new_string = ''
    for i in range(len(string)):
        if string[i] in list1:
            for j in range(len(list1)):
                if string[i] == list1[j]:
                    new_string += list2[j]
        else:
            new_string += string[i]
    return new_string
    
def leet_speak(string):
    lower_string = replace_letter(string, uppercase, lowercase)
    leet_string = replace_letter(lower_string, letters, leet)
    return leet_string

print leet_speak("Leet")


#Long-long vowels

# vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
# string = "booleans rock socks"
# new_string = ''
# for i in range(len(string)):
#     if string[i] in vowels:
#         if string[i] == string[1 - 1]:
#             for j in range(3):
#                 new_string += string[i]
#         else: new_string += string[i]
#     else:
#         new_string += string[i]
# print new_string

# #Caesar cipher
# cipher_string = 'lbh zhfg hayrnea jung lbh unir yrnearq'
# lowercase = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# decoded_string = ''

# for char in cipher_string:
#     is_letter = False
#     is_upper = False
#     decode_index = 0
#     if char in lowercase or char in uppercase:
#         is_letter = True
#     if char in uppercase:
#         is_upper = True
#     if is_letter:
#         for l in range(len(uppercase)):
#             if char == uppercase[l] or char == lowercase[l]:
#                 letter_index = l
#                 decode_index = (letter_index + 13) % 26
#                 break
#         if is_upper:
#             decoded_string += uppercase[decode_index]
#         else: 
#             decoded_string += lowercase[decode_index]
#     else:
#         decoded_string += char

# print decoded_string 
    