def reverseWordSentence(N): 
  N=input()
  return ' '.join(word[::-1] for word in 
    N.split(" "))   
N= "hello world"
print(reverseWordSentence(N))  
