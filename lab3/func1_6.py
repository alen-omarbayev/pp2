def reversedSentence(string):
    s=''
    words=string.split()
    words.reverse()

    for word in words:
        s+=word+' '
    print(s)

string = str(input())
reversedSentence(string)