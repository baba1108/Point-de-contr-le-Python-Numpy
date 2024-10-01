#from numpy import array
import numpy as np
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
print(grades)

print(" la moyenne des notes des étudiants:",np.mean(grades))

print(" la médiane des notes des étudiants:",np.median(grades))

print(" l’écart type des notes des étudiants:",np.std(grades))

print("le maximum des notes:",np.max(grades))

print("le minimum des notes:",np.min(grades))

print(" les notes par ordre croissant:",np.sort(grades))

print(" l'index de la note la plus élevée dans le tableau:",np.argmax(grades))

print("Nombre d'étudiants avec un score > 90 :", np.sum(grades > 90))

print( "le pourcentage d'étudiants ayant obtenu un score > 90:", np.mean(grades > 90) * 100)

print(" le pourcentage d'étudiants ayant obtenu un score < 75:", np.mean(grades < 75) * 100)

high_performers = grades[grades > 90]
print("Notes des étudiants avec des scores supérieurs à 90 :", high_performers)

passing_grades =  grades[grades > 75]
print("notes des étudiants avec des scores supérieurs à 75:", passing_grades)



