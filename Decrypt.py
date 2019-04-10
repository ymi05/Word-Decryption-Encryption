class Decrypt(object):
    def __init__(self,Encrypted_word):
        self.Encrypted_word = Encrypted_word
        self.DecryptedWords = {}
    def Decrypt_Word(self):
        for i in range(0,27):
            string = ''
            for x in self.Encrypted_word:
                pos=((ord(x)-ord('a'))-i)%26+ord("a")
                string += chr(pos)
            self.DecryptedWords[i]=string
        return self.DecryptedWords
        

    def checkWord(self):
        f = open('words.txt','r')
        for line in f:
            x=line.split(' ')
        for word in x:
            if word in self.DecryptedWords.values():
                return  "The decryption of the word is %s"%(word) 

                
        

trial =Decrypt('fhei')
print(trial.Decrypt_Word(),'\n')
print(trial.checkWord())