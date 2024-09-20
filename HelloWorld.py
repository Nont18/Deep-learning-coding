list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g',
        'h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']

sentence = "Welcome to real world my boy"
x = ''
temp = ''

# sentence = str(input("Sentence : "))

for i in range(len(sentence)):
    # print(list[i])
    for j in range(len(list)):
        print(x)
        if sentence[i] == list[j]:
            # print(sentence[i])
            temp = str(sentence[i])
            x = x + temp
            # print(temp)