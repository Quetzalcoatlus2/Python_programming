notaLaborator = 9
notaExamen = 5
notaFinala = (notaLaborator * 0.4 + notaExamen * 0.6)
promovat = notaExamen >= 5 and notaFinala >= 5

print ('Disciplina promovata:', promovat)
print('Media: ', notaFinala)