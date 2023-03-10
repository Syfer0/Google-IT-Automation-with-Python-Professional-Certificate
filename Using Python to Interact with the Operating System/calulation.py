def count_letter(text):
     result = {}
     for letter in text:
          if letter not in result:
              result[letter] = 0
          result[letter] += 1 
     return result

count_letter(" hi i am  new here can anyone help me")
print (count_letter)

