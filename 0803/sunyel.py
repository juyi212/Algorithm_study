for i in range(1,4):
    for j in range(1,4):
        if j != i:
            for z in range(1,4):
                if z!=i and z!=j :
                    print(i,j,z)