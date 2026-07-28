from tank import tank

t1 = tank(x=0,y=0)

t2 = tank(x=100,y=200,model='tiger',ammo=25)

for t in[t1,t2]:
    print(t.model)