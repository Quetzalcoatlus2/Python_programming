test = "iiiLikePythonLikeILikeIcecreamLikeLikeLikeLike"
rez = test
print(test.index('Like'))
print(test.rindex('Like')) # se doreste afisarea pozitiei Like-ului median



numar=test.count('Like')
if numar % 2 == 0:
     print("Număr par de apariții")
else:
     print("Like-ul median este al", numar//2 + 1, "-lea")

test = test.replace("Like", "like", numar//2)
print("Like-ul median se găsește la poziția", test.index('Like'))


