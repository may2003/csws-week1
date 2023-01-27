names = ["reem","may","arwa","mariam","sara"]
i= 0
while i<5 :
 print(names[i])
 i +=1
i= 0
while i<5 :
 print(f"hello", names[i])
 i +=1

places = ["paris", "spain", "switzerland", "greece","italy" ]
print (places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

egypt = ["giza","cairo","alex","sharm","luxor"]
print(len(egypt))
egypt.append("aswan")
egypt.insert(2,"tagamo3")
del egypt[1]
egypt.remove("sharm")
x= egypt.pop(3)
print(egypt)
print (x)