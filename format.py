#les differents utilisation de .format 
# {}{}{} elle va suivre l'ordre automatique 
print("{}{}{}".format("zero","un","deux"))
#{2}{0}{1} suivre l'indice indiquer dans les accolade {indice}
ch=("{2}{0}{1}".format(1,2,3))
#formatage a l'aide d'une liste
stock=['papier','enveloppe','chemise','encre','gomme']
print("nous avons de l'{0[3]} et du {0[0]}  en stock".format(stock))
# formatage  a l'aide d'un dictionnaire 
d= dict(poids=1200,animal='elephant')
print("l'{0[animal]} pése {0[poids]} Kg\n".format(d))
""" inserer les valeur saisi 
par l'utilisateur dans une liste
puis afficher cette liste"""
print(ch)
msg="saisi le {} valeur"
l=[]
for i in range(1,5):
    l.append(input(msg.format(i)))
print(l)

#remplaceemnt avec champ nomé
a,b=5,3 
print ("the story of{c}  and {d}".format(c=a+b,d=a-b))