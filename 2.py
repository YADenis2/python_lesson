fam = []
name = []
clas = []
al = []
ge = []
classes = []
with open("mat_dv.txt", 'r')as file:
    for i in file:
        splt = i.split()
        fam.append([splt[0]])
        name.append([splt[1]])
        clas.append(int(splt[2]))
        if splt[2] not in classes:
            classes.append(int(splt[2]))
        al.append(int(splt[3]))
        ge.append(int(splt[4]))
    file.close()
clasmax = {}
clasname = {}
for i in classes:
    clasmax[i] = [0, 0, 0]
    clasname[i] = [[""], [""], [""]]
for i in range(len(fam)):
    print(clasmax[clas[i]])
    print(clasname[clas[i]][2])
    if clasmax[clas[i]][0] < al[i]+ge[i]:
        clasmax[clas[i]][0] = al[i]+ge[i]
        clasname[clas[i]] = [i]
    elif clasmax[clas[i]][1] == al[i]+ge[i]:
        clasname[clas[i]][0].append(i)
    if clasmax[clas[i]][1] < al[i]:
        clasmax[clas[i]][1] = al[i]
        clasname[clas[i]] = [i]
    elif clasmax[clas[i]][1] == al[i]:
        clasname[clas[i]][1].append(i)
    if clasmax[clas[i]][2] < ge[i]:
        clasmax[clas[i]][2] = ge[i]
        clasname[clas[i]][2] = [i]
    elif clasmax[clas[i]][2] == ge[i]:
        clasname[clas[i]][2].append(i)
    
        
    
