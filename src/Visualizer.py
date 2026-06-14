rs,rc="\U0001F7E5","\U0001F534"
gs,gc="\U0001F7E9","\U0001F7E2"
ys,yc="\U0001F7E8","\U0001F7E1"
bs,bc="\U0001F7E6","\U0001F535"
ws= "\U00002B1C"
bl="\U00002B1B"

def view_board(board):
    rs,rc="\U0001F7E5","\U0001F534"
    gs,gc="\U0001F7E9","\U0001F7E2"
    ys,yc="\U0001F7E8","\U0001F7E1"
    bs,bc="\U0001F7E6","\U0001F535"
    ws= "\U00002B1C"
    bl="\U00002B1B"
    L=[

        [bs, bs, bs, bs, bs, bs, ws, ws, ws, rs, rs, rs, rs, rs, rs],
        [bs, bc, ws, ws, bc, bs, ws, rs, rs, rs, rc, ws, ws, rc, rs],
        [bs, ws, ws, ws, ws, bs, bl, rs, ws, rs, ws, ws, ws, ws, rs],
        [bs, ws, ws, ws, ws, bs, ws, rs, ws, rs, ws, ws, ws, ws, rs],
        [bs, bc, ws, ws, bc, bs, ws, rs, ws, rs, rc, ws, ws, rc, rs],
        [bs, bs, bs, bs, bs, bs, ws, rs, ws, rs, rs, rs, rs, rs, rs],
        [ws, bs, ws, ws, ws, ws, bl, bl, bl, ws, ws, ws, bl, ws, ws],
        [ws, bs, bs, bs, bs, bs, bl, bl, bl, gs, gs, gs, gs, gs, ws],
        [ws, ws, bl, ws, ws, ws, bl, bl, bl, ws, ws, ws, ws, gs, ws],
        [ys, ys, ys, ys, ys, ys, ws, ys, ws, gs, gs, gs, gs, gs, gs],
        [ys, yc, ws, ws, yc, ys, ws, ys, ws, gs, gc, ws, ws, gc, gs],
        [ys, ws, ws, ws, ws, ys, ws, ys, ws, gs, ws, ws, ws, ws, gs],
        [ys, ws, ws, ws, ws, ys, ws, ys, bl, gs, ws, ws, ws, ws, gs],
        [ys, yc, ws, ws, yc, ys, ys, ys, ws, gs, gc, ws, ws, gc, gs],
        [ys, ys, ys, ys, ys, ys, ws, ws, ws, gs, gs, gs, gs, gs, gs],


    ]
    pos = {1: (2, 9), 2: (3,9), 3: (4,9), 4: (5,9), 5: (6,9), 6: (7,10), 7: (7,11), 8: (7,12), 9: (7,13), 10: (7,14),
           11: (7,15), 12: (8,15), 13: (9,15), 14: (9,14), 15: (9,13), 16: (9,12), 17: (9,11), 18: (9,10), 19: (10,9), 20: (11, 9),
           21: (12,9), 22: (13,9), 23: (14,9), 24: (15,9), 25: (15,8), 26: (15,7), 27: (14,7), 28: (13,7), 29: (12,7), 30: (11,7),
           31: (10,7), 32: (9,6), 33: (9,5), 34: (9,4), 35: (9,3), 36: (9,2), 37: (9,1), 38: (8,1), 39: (7,1), 40: (7,2),
           41: (7,3), 42: (7,4), 43: (7,5), 44: (7,6), 45: (6,7), 46: (5,7), 47: (4,7), 48: (3,7), 49: (2,7), 50: (1,7),
           51: (1,8), 52: (1,9),
           'R1': (2,11) ,'R2': (2,14), 'R3': (5,11) ,'R4': (5,14),
           'G1': (11,11), 'G2': (11,14), 'G3': (14,11), 'G4': (14,14),
           'Y1': (2,2), 'Y2': (2,5), 'Y3': (2,2), 'Y4': (2,5),
           'B1': (11,2), 'B2': (11,5), 'B3': (14,2), 'B4': (14,5),


           }
    for i in board:
        if board[i] in [0,'L','W']:
            continue
        if i[0]=='R':
            p=rc
        if i[0]=='G':
            p=gc
        if i[0]=='B':
            p=bc
        if i[0]=='Y':
            p=yc
        coordinates=pos[board[i]]
        y_coord=coordinates[0]
        x_coord=coordinates[1]
        L[y_coord-1][x_coord-1]=p
        L[pos[i][0]-1][pos[i][1]-1] = bl


    for i in L:
        for j in i:
            print(j,end=" ")
        print()
b={'R1':1,'R2':5,'R3':2,'R4':45,'G1':0,'G2':43,'G3':0,'G4':0,'Y1':0,'Y2':8,'Y3':0,'Y4':0,'B1':0,'B2':0,'B3':0,'B4':52}
view_board(b)
