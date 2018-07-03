# string = raw_input('Enter sentence\n') 
# dict3 = {}
# words = string.split()
# for word in words:
#     if word in dict3:
#         dict3[word] += 1
#     else:
#         dict3[word] = 1
# print dict3
# sorted_dict =[]        
# for key in dict3:
#     if len(sorted_dict) == 0:
#         sorted_dict.append((key, dict3[key]))
#     else:
#         for i in range(len(sorted_dict)):
#             if dict3[key] >= sorted_dict[i][1]:
#                 sorted_dict.insert(i, (key, dict3[key]))
#                 break
#             elif len(sorted_dict) <= 3:
#                 sorted_dict.append((key, dict3[key]))
# print "The top three words are: \n 1. %s  \n 2. %s  \n 3. %s" % (sorted_dict[0], sorted_dict[1], sorted_dict[2])

sentence = raw_input("Enter a sentence.\n")
def word_histogram(sentence):
    dict3 = {}
    words = sentence.split()
    for word in words:
        if word in dict3:
            dict3[word] += 1
        else:
            dict3[word] = 1
    return dict3
print word_histogram(sentence)
