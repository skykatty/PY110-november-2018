l = "шел я лесоM вижу мост. Да, на мосту вОрона сохнет. взял еЁ за хвост."
print(l)
print('. '.join([x.capitalize() for x in (''.join([x.lower() for x in l]).split(". "))]))
