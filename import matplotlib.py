import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

Modèle_1 = {'Masse' : 1760, 'Accélération': 5.1, 'Longueur' : 5.28, 'Largeur' : 1.95, 'Hauteur' : 1.35, 'Cx' : 0.38, 'Cz' : 0.3, 'u' : 0.1}
Modèle_2 = {'Masse' : 1615, 'Accélération': 5, 'Longueur' : 4.51, 'Largeur' : 1.81, 'Hauteur': 1.27, 'Cx' : 0.29, 'Cz' : 0.3, 'u' : 0.1}
Modèle_3 = {'Masse' : 1498, 'Accélération': 5.3, 'Longueur' : 4.72, 'Largeur' : 1.88, 'Hauteur': 1.30, 'Cx': 0.35, 'Cz' : 0.3, 'u' : 0.1}
Modèle_4 = {'Masse' : 1385, 'Accélération': 5.2, 'Longueur' : 4.3, 'Largeur' : 1.75, 'Hauteur': 1.23, 'Cx' : 0.28, 'Cz' : 0.3, 'u' : 0.1}
Modèle_5 = {'Masse' : 1540, 'Accélération': 5.8, 'Longueur' : 4.6, 'Largeur' : 1.79, 'Hauteur': 1.36, 'Cx': 0.34, 'Cz' : 0.3, 'u' : 0.1}
Modèle_6 = {'Masse' : 1600, 'Accélération': 5, 'Longueur' : 4.51, 'Largeur' : 1.81, 'Hauteur': 1.48, 'Cx' : 0.28, 'Cz' : 0.3, 'u' : 0.1}

principal = input("Entrer le modèle de la voiture: ")
if principal == "Modèle_1" :
    Modèle = Modèle_1
elif principal == "Modèle_2" :
    Modèle = Modèle_2
elif principal == "Modèle_3" :
     Modèle = Modèle_3
elif principal == "Modèle_4" :
    Modèle = Modèle_4
elif principal == "Modèle_5" :
    Modèle = Modèle_5
elif principal == "Modèle_6" :
    Modèle = Modèle_6
   
# Déclaration des constantes
𝛼 = 3.7*np.pi/180
t0 = 0
tfinal = 100
𝜌 = 1.19
g = 9.81
k = 1/2 * 𝜌 * Modèle['Cx']  
R = 6

# Déclaration des conditions initiales
S_init = [0,0]
t = np.linspace(t0, tfinal, 10000)

# Declaration de l'équation différentielle avec le vecteur d'etat S

def Pente(S, t):
    return [S[1], 1 / Modèle['Masse'] * (Modèle['Masse'] * g * (-(Modèle['u'] * np.cos(𝛼) )+ np.sin(𝛼)) - k * S[1] ** 2 + Modèle['Masse'] * Modèle['Accélération'])]

# Resolution de l'équation différentielle pour déterminer S
S=odeint(Pente,S_init,t)

i = 0
while i < len(t) and (S[i, 0]) < 31 :
    i = i + 1
if i >= len(t):
    print(" Il faut augmenter le vecteur temps ")
else :
    vf = S[i, 1]
    tf = t[i]
    print(" Vitesse de la voiture en bas de la pente est de: " + str(round(S[i, 1], 2)), "m/s")
    print(" La voiture a mis " + str(round((tf), 2)) + " secondes pour arriver en bas de la pente. ")
   
# Representation graphique

plt.plot(t, S[:,0], color = "red", lw = 2)
plt.title("Vitesse de la voiture en bas de la pente")
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse en m/s")
plt.show()

#Représentation graphique zoomé
plt.plot(t, S[:,0], color = "green", lw = 2)
plt.title("Vitesse de la voiture en bas de la pente")
plt.xlim(0,8)
plt.ylim(0,100)
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse en m/s")
plt.show()






S = Modèle["Longueur"] * Modèle["Largeur"] 
k = 0.5 * 1.19 * Modèle["Cx"] * S
r = 6
t0 = 0
tmax = 4
pas = 1000
t = np.linspace(t0,tmax, pas)
vlim = np.sqrt(5 * 9.81 * r - Modèle["Accélération"] * np.pi * r)
vtest = vlim * 2
R = 0
i = 0


def Sp2(S2,t):
    return (S2[1], (1 / (Modèle["Masse"] * r)) * (Modèle["Masse"] * Modèle["Accélération"] - Modèle["Masse"] * 9.81 * np.sin(S2[0]) - Modèle["Masse"] * 9.81 * Modèle["u"] * np.cos(S2[0]) * np.sign(S2[1]) - (S2[1] ** 2) * np.sign(S2[1]) * Modèle["u"] * r * Modèle["Masse"] + k * r ** 2))
    

while vtest >= vlim and R >= 0 :
    S2_init2 = [0, vtest / r]
    S2 = odeint(Sp2, S2_init2, t)

    while R >= 0 and i < pas :
        R = 9.81 * np.cos(S2[i][0]) + r * S2[i][1]**2
        i += 1
    
    vtest = vtest - 0.1

print("la voiture decroche du looping et la vitesse initiale est inférieure à : " + str(round(vtest + 0.1, 2)), "m/s")

if vf >= (vtest + 0.1) :
    S2_init2 = [0, vf / r]                
    S2 = odeint(Sp2, S2_init2, t)


    R = []
    i = 0

    while (i < pas and S2[i][0] < 2 * np.pi):
        R.append(9.81 * np.cos(S2[i][0]) + r * S2[i][1]**2)
        i += 1 

    imax = max(i - 1, 0)
    vf2 = S2[imax][1] * r 
    tf2 = t[imax]
    print("La vitesse en sortie du looping est "  + str(round(vf2, 2)), "m/s")
    print("la voiture a mis " + str(round((tf2), 2)) + " secondes pour passer le looping ")
    
    t = np.linspace(t0, (tmax - t0) *  imax / pas, imax)

    plt.plot(t, S2[0:imax, 0])
    plt.title("Position angulaire de la voiture (avec frottement) en fonction ")
    plt.xlabel("temps(s)")
    plt.ylabel("position angulaire (rad)")
    plt.show()

    plt.plot(t, S2[0: imax, 1] * r)
    plt.title("Vitesse de la voiture (avec frottements) en fonction du temps ")
    plt.xlabel("temps(s)")
    plt.ylabel("vitesse (m/s)")
    plt.show()






numPortion = 3


t0 = 0
tMax = 0.6
pas = 1000
S3_init = [0, 0, vf2, 0]
t = np.linspace(t0, tMax, pas)
vlim2 = np.sqrt(- 9.81 * 9**2 / (2 * (-1)))
vtest2 = vlim2 * 2
vlim2 = 5
S = Modèle["Longueur"] * Modèle["Largeur"] 
Sz = Modèle["Hauteur"] * Modèle["Largeur"] 
d = -1
l = 9
def Sp3(S3, t): 
    return [S3[2], S3[3], -1.19 / (2 * Modèle["Masse"]) * np.sqrt(S3[2] ** 2 + S3[3] ** 2) * (Modèle["Cx"] * S * S3[2] + Modèle["Cx"] * Sz * S3[3]), -1.19 / (2 * Modèle["Masse"]) * np.sqrt(S3[2] ** 2 + S3[3] ** 2) * (Modèle["Cx"] * S * S3[3] - Modèle["Cz"] * Sz * S3[2]) - 9.81]

Sortir = False
while vtest2 >= vlim2 and not Sortir :
    S3_init2 = [0, 0, vtest2, 0]
    S3 = odeint(Sp3, S3_init2, t)

    i = 0
    voiturepasseravin = False
    while i < len(t) and not voiturepasseravin :
        if S3[i, 0] >= l and S3[i, 1] >= d :
            voiturepasseravin = True 
        i += 1
    if i >= len(t) :
        Sortir = True 
    else :
        vtest2 -= 0.1

print("la voiture ne passe pas le ravin si la vitesse est inférieure à : " + str(round((vtest2), 2)) + "m/s")

if vf2 >= vtest2 :
    S3_init = [0, 0, vf2, 0]
    S3 = odeint(Sp3, S3_init, t)

    i = 0
    while i < len(t) and S3[i, 1] >= d : 
        i += 1
    tf3 = t[i]
    print("La voiture a mis " + str(round((tf3),2)) + " secondes pour passer le ravin")


    plt.plot(S3[:, 0], S3[:, 1])
    plt.plot(l, d, marker = 'o', color = 'red')
    plt.title("Position de la voiture en fonction du temps dans le ravin ")
    plt.xlabel("abscisse (m)")
    plt.ylabel("ordonnée (m)")
    plt.show()
else :
    print("La vitesse de la voiture en sortie de looping n'est pas suffisante ")
    plt.plot(S3[:, 0], S3[:, 1])
    plt.plot(l, d, marker = 'o', color = 'red')
    plt.title("Position de la voiture en fonction du temps dans le ravin ")
    plt.xlabel("abscisse (m)")
    plt.ylabel("ordonnée (m)")
    plt.show()







S = Modèle["Longueur"] * Modèle["Largeur"] 
k = (1/2) * Modèle["Cx"] * S * 1.19
t0 = 0
tmax = 100
pas = 10000
t = np.linspace(t0, tmax, pas)
S4_init = [0, 0]
D = 10

def Sp4(S4, t):
    return [S4[1], 1 / Modèle["Masse"]* (- Modèle["Masse"] * 9.81 * Modèle["u"] - k * S4[1] ** 2 + Modèle["Masse"] * Modèle["Accélération"])]


S4 = odeint(Sp4, S4_init, t)

i = 0
while i < len(t) and S4[i, 0] <= D : 
    i += 1 

tf4 = t[i]


if vf2 >= vtest2 :
    ttotal = tf + tf2 + tf3 + tf4
    print("La voiture termine le circuit en " + str(round((ttotal),2)) + " secondes." )
else : 
    print("La voiture ne termine pas le circuit")


