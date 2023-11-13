# a = "thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN".lower()
# print(a.count("garden") + a.count("cat") + a.count("mice"))

g= "thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN"
a=g.lower()
b=a[::-1]
c= a.count("garden") + a.count("cat") + a.count("mice") 
d=b.count("garden")+ b.count("cat") + b.count("mice") 
e=c+d
print(e)
