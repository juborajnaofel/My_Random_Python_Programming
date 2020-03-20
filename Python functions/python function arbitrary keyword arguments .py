def main(**name):
	print(name["name1"]+", "+name["name2"]+", "+name["name3"])
#order of the arguments doesn't matter in this
main(name1="Jadu",name2="John",name3="Bashir")
#will yield same result,
main(name2="John",name3="Bashir",name1="Jadu")