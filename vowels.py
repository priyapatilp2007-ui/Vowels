String=input("Enter the word)
count = 0
for ch in string:
  if ch.lower in "aeiou":
      count +=1
  print("Number of vowels:",count);
  print("The vowels are:")
