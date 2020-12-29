import numpy as np 

def WIN(Cajas):
    VWIN = 0
    W1 = (Cajas==1)
    W2 = (Cajas==2)
    if np.sum(W1)>np.sum(W2):
        VWIN = 1
    elif np.sum(W1)<np.sum(W2):
        VWIN = 2
    return VWIN

def change_dic(Cuadros,Pos):
    n=0
    for i in Cuadros:
        if (Pos in i):
            Cuadros[n][Pos]=1
        n+=1
    return Cuadros

def caja(Cuadros,Cajas,Turno):
    punto=0
    for i in range(len(Cuadros)):
        if sum(Cuadros[i].values())==4 and Cajas[0,i]==0:
            Cajas[0,i]=Turno
            punto=1
            #Cuadros.pop(i)
    return Cajas,punto

play = 1 
while play==1:
    Gato = np.array([0,0,0,0,0,0,0,0,0,0,0,0]) #nodos

    A={0:0, 9:0, 7:0, 2:0}
    B={1:0, 9:0, 3:0, 11:0}
    C={2:0, 6:0, 8:0, 4:0}
    D={3:0, 5:0, 8:0, 10:0}
    
    cuadros=[A,B,C,D]
    boxes = np.zeros([1,4])
    
    VD = [[100.08,100.04,100.07,100.03,100.09,100.02,100.06,100.01,100.05,100.06,100.01,100.05]]

    #Turno = int(input('TURNO: (0 reinicia) (1 Máquina) (2 Humano) '))
    Turno = int(input('TURNO: (1 Máquina) (2 Humano) '))
#    if Turno == 0:
#        np.save('caso1.npy',np.zeros([1,12]))
#        np.save('caso2.npy',np.zeros([1,12]))
#        np.save('caso3.npy',np.zeros([1,12]))
#        np.save('caso4.npy',np.zeros([1,12]))
#        np.save('caso5.npy',np.zeros([1,12]))
#        np.save('caso6.npy',np.zeros([1,12]))
#        np.save('caso7.npy',np.zeros([1,12]))
#        np.save('caso8.npy',np.zeros([1,12]))
#        np.save('caso9.npy',np.zeros([1,12]))
#        np.save('caso10.npy',np.zeros([1,12]))
#        np.save('caso11.npy',np.zeros([1,12]))
#        np.save('caso12.npy',np.zeros([1,12]))
#        np.save('caso_empate.npy',np.zeros([1,12]))
#        np.save('escoger1.npy',VD)
#        np.save('escoger2.npy',VD)
#        np.save('escoger3.npy',VD)
#        np.save('escoger4.npy',VD)
#        np.save('escoger5.npy',VD)
#        np.save('escoger6.npy',VD)
#        np.save('escoger7.npy',VD)
#        np.save('escoger8.npy',VD)
#        np.save('escoger9.npy',VD)
#        np.save('escoger10.npy',VD)
#        np.save('escoger11.npy',VD)
#        np.save('escoger12.npy',VD)
#        np.save('escoger_empate.npy',VD)
#        np.save('Empate.npy',np.array([0]))
#        caso1 = np.load('caso1.npy')
#        caso2 = np.load('caso2.npy')
#        caso3 = np.load('caso3.npy')
#        caso4 = np.load('caso4.npy')
#        caso5 = np.load('caso5.npy')
#        caso6 = np.load('caso6.npy')
#        caso7 = np.load('caso7.npy')
#        caso8 = np.load('caso8.npy')
#        caso9 = np.load('caso9.npy')
#        caso10 = np.load('caso10.npy')
#        caso11 = np.load('caso11.npy')
#        caso12 = np.load('caso12.npy')
#        escoger1 = np.load('escoger1.npy')
#        escoger2 = np.load('escoger2.npy')
#        escoger3 = np.load('escoger3.npy')
#        escoger4 = np.load('escoger4.npy')
#        escoger5 = np.load('escoger5.npy')
#        escoger6 = np.load('escoger6.npy')
#        escoger7 = np.load('escoger7.npy')
#        escoger8 = np.load('escoger8.npy')
#        escoger9 = np.load('escoger9.npy')
#        escoger10 = np.load('escoger10.npy')
#        escoger11 = np.load('escoger11.npy')
#        escoger12 = np.load('escoger12.npy')
#        Empate = np.load('Empate.npy')
    if Turno != 1 and Turno != 2: 
        print('no válido')
    else:
        caso1 = np.load('caso1.npy',allow_pickle=True)
        escoger1 = np.load('escoger1.npy',allow_pickle=True)
               
        caso2 = np.load('caso2.npy',allow_pickle=True)
        escoger2 = np.load('escoger2.npy',allow_pickle=True)
        
        caso3 = np.load('caso3.npy',allow_pickle=True)
        escoger3 = np.load('escoger3.npy',allow_pickle=True)
        
        caso4 = np.load('caso4.npy',allow_pickle=True)
        escoger4 = np.load('escoger4.npy',allow_pickle=True)
        
        caso5 = np.load('caso5.npy',allow_pickle=True)
        escoger5 = np.load('escoger5.npy',allow_pickle=True)
        
        caso6 = np.load('caso6.npy',allow_pickle=True)        
        escoger6 = np.load('escoger6.npy',allow_pickle=True)
        
        caso7 = np.load('caso7.npy',allow_pickle=True)
        escoger7 = np.load('escoger7.npy',allow_pickle=True)
        
        caso8 = np.load('caso8.npy',allow_pickle=True)
        escoger8 = np.load('escoger8.npy',allow_pickle=True)
        
        caso9 = np.load('caso9.npy',allow_pickle=True)
        escoger9 = np.load('escoger9.npy',allow_pickle=True)
        
        caso10 = np.load('caso10.npy',allow_pickle=True)
        escoger10 = np.load('escoger10.npy',allow_pickle=True)
        
        caso11 = np.load('caso11.npy',allow_pickle=True)
        escoger11 = np.load('escoger11.npy',allow_pickle=True)
        
        caso12 = np.load('caso12.npy',allow_pickle=True)
        escoger12 = np.load('escoger12.npy',allow_pickle=True)
        
        caso_empate = np.load('caso_empate.npy',allow_pickle=True)
        escoger_empate = np.load('escoger_empate.npy',allow_pickle=True)

        Empate = np.load('Empate.npy',allow_pickle=True)
                
        # TIRO 1 
        #Turno1 = Turno
        Turnos_all = [Turno]
        
        tiro = 1
        Val = Gato<1
        L = caso1.shape
        capa1 = -1
        sh = 0
        while sh==0:
            capa1 += 1
            if capa1+1 <= L[0] and capa1+1 <= L[1]:
                comparison = Gato == caso1[capa1,:]
                cs = comparison.all()
                if cs == True:
                    sh = 1
            else:
                caso1 = np.vstack((caso1, Gato))
                escoger1 = np.vstack((escoger1,VD))
                sh = 1
            
        if Turno == 1:
            print('Tiro de la máquina\n')
            num,pos1 = np.max(escoger1[capa1,:]*Val),np.argmax(escoger1[capa1,:]*Val)
            Gato[pos1] = 1
            Turno = 2
        else:
            pos1 = int(input('ingresa una posición (1-9) '))
            while Val[pos1] <=0:
                print('Casilla ocupada')
                pos1 = int(input('ingresa una posición (1-9) '))
            Gato[pos1] = 2
            Turno = 1
        Turnos_all.append(Turno)
        
        cuadros=change_dic(cuadros,pos1)
        tablero = np.reshape(Gato,[6,2])
        print(tablero)
        
        # TIRO 2 -se registra 2 movimiento
        tiro = 2
        Val = Gato<1
        L = caso2.shape
        capa2 = -1
        sh = 0
        while sh == 0:
            capa2 += 1
            if capa2+1 <= L[0] and capa2+1 <= L[1]:
                comparison = Gato == caso2[capa2,:]
                cs = comparison.all()
                if cs == True:
                    sh = 1
            else:
                caso2 = np.vstack((caso2, Gato))
                escoger2 = np.vstack((escoger2,VD))
                sh = 1
        if Turno == 1:
            print('Tiro de la máquina\n')
            num,pos2 = np.max(escoger2[capa2,:]*Val),np.argmax(escoger2[capa2,:]*Val)
            Gato[pos2] = 1
            Turno = 2
        else:
            pos2 = int(input('ingresa una posición (1-9) '))
            while Val[pos2] <=0:
                print('Casilla ocupada')
                pos2 = int(input('ingresa una posición (1-9) '))
            Gato[pos2] = 2
            Turno = 1
        
        Turnos_all.append(Turno)
        cuadros=change_dic(cuadros,pos2)
        tablero = np.reshape(Gato,[6,2])
        print(tablero)
        
        # TIRO 3 -se registra 3 movimiento
        tiro = 3
        Val = Gato<1
        L = caso3.shape
        capa3 = -1
        sh = 0
        while sh == 0:
            capa3 += 1
            if capa3+1 <= L[0] and capa3+1 <= L[1]:
                comparison = Gato == caso3[capa3,:]
                cs = comparison.all()
                if cs == True:
                    sh = 1
            else: 
                caso3 = np.vstack((caso3, Gato))
                escoger3 = np.vstack((escoger3,VD))
                sh = 1
        if Turno == 1:
            print('Tiro de la máquina\n')
            num,pos3 = np.max(escoger3[capa3,:]*Val),np.argmax(escoger3[capa3,:]*Val)
            Gato[pos3] = 1
            Turno = 2
        else:
            pos3 = int(input('ingresa una posición (1-9) '))
            while Val[pos3] <=0:
                print('Casilla ocupada')
                pos3 = int(input('ingresa una posición (1-9) '))
            Gato[pos3] = 2
            Turno = 1
        
        Turnos_all.append(Turno)
        cuadros=change_dic(cuadros,pos3)
        tablero = np.reshape(Gato,[6,2])
        print(tablero)
        
        # TIRO 4
        tiro = 4
        Val = Gato<1
        L = caso4.shape
        capa4 = -1
        sh = 0
        while sh == 0:
            capa4 += 1
            if capa4+1 <= L[0] and capa4+1 <= L[1]:
                comparison = Gato == caso4[capa4,:]
                cs = comparison.all()
                if cs == True:
                    sh = 1
            else:
                caso4 = np.vstack((caso4, Gato))
                escoger4 = np.vstack((escoger4,VD))
                sh = 1
        if Turno == 1:
            print('Tiro de la máquina\n')
            num,pos4 = np.max(escoger4[capa4,:]*Val),np.argmax(escoger4[capa4,:]*Val)
            Gato[pos4] = 1
            cuadros=change_dic(cuadros,pos4)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 2
        else:
            pos4 = int(input('ingresa una posición (1-9) '))
            while Val[pos4] <=0:
                print('Casilla ocupada')
                pos4 = int(input('ingresa una posición (1-9) '))
            Gato[pos4] = 2      
            cuadros=change_dic(cuadros,pos4)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 1
        
        Turnos_all.append(Turno)
        tablero = np.reshape(Gato,[6,2])
        print(tablero)
        print('\n cajas ganadas ')
        print(boxes)
        
#..............................................................................                
        # TIRO 5
        tiro = 5
        Val = Gato<1
        L = caso5.shape
        capa5 = -1
        sh = 0
        while sh == 0:
            capa5 += 1
            if capa5+1 <= L[0] and capa5+1 <= L[1]:
                comparison = Gato == caso5[capa5,:]
                cs = comparison.all()
                if cs == True:
                    sh = 1
            else:
                caso5 = np.vstack((caso5, Gato))
                escoger5 = np.vstack((escoger5,VD))
                sh = 1
        if Turno == 1:
            print('Tiro de la máquina\n')
            num,pos5 = np.max(escoger5[capa5,:]*Val),np.argmax(escoger5[capa5,:]*Val)
            Gato[pos5] = 1
            cuadros=change_dic(cuadros,pos5)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 2
        else:
            pos5 = int(input('ingresa una posición (1-9) '))
            while Val[pos5] <=0:
                print('Casilla ocupada')
                pos5 = int(input('ingresa una posición (1-9) '))
            Gato[pos5] = 2
            cuadros=change_dic(cuadros,pos5)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 1
        
        Turnos_all.append(Turno)
        tablero = np.reshape(Gato,[6,2])
        print(tablero)
        print('\n cajas ganadas ')
        print(boxes)      

            # TIRO 6
        tiro = 6
        Val = Gato<1
        L = caso6.shape
        capa6 = -1
        sh = 0
        while sh == 0:
            capa6 += 1
            if capa6+1 <= L[0] and capa6+1 <= L[1]:
                comparison = Gato == caso6[capa6,:]
                cs = comparison.all()
                if cs == True:
                    sh = 1
            else:
                caso6 = np.vstack((caso6, Gato))
                escoger6 = np.vstack((escoger6,VD))
                sh = 1
        if Turno == 1:
            print('Tiro de la máquina\n')
            num,pos6 = np.max(escoger6[capa6,:]*Val),np.argmax(escoger6[capa6,:]*Val)
            Gato[pos6] = 1
            cuadros=change_dic(cuadros,pos6)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 2
        else:
            pos6 = int(input('ingresa una posición (1-9) '))
            while Val[pos6] <=0:
                print('Casilla ocupada')
                pos6 = int(input('ingresa una posición (1-9) '))
            Gato[pos6] = 2
            cuadros=change_dic(cuadros,pos6)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 1
        
        Turnos_all.append(Turno)
        tablero = np.reshape(Gato,[6,2])
        print(tablero)
        print('\n cajas ganadas ')
        print(boxes)
        
                # TIRO 7
        tiro = 7
        Val = Gato<1
        L = caso7.shape
        capa7 = -1
        sh = 0
        while sh == 0:
            capa7 += 1
            if capa7+1 <= L[0] and capa7+1 <= L[1]:
                comparison = Gato == caso7[capa7,:]
                cs = comparison.all()
                if cs == True:
                    sh = 1
            else:
                caso7 = np.vstack((caso7, Gato))
                escoger7 = np.vstack((escoger7,VD))
                sh = 1
        if Turno == 1:
            print('Tiro de la máquina\n')
            num,pos7 = np.max(escoger7[capa7,:]*Val),np.argmax(escoger7[capa7,:]*Val)
            Gato[pos7] = 1
            cuadros=change_dic(cuadros,pos7)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 2
        else:
            pos7 = int(input('ingresa una posición (1-9) '))
            while Val[pos7] <=0:
                print('Casilla ocupada')
                pos7 = int(input('ingresa una posición (1-9) '))
            Gato[pos7] = 2
            cuadros=change_dic(cuadros,pos7)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 1
        
        Turnos_all.append(Turno)
        tablero = np.reshape(Gato,[6,2])
        print(tablero)
        print('\n cajas ganadas ')
        print(boxes)
    
                    # TIRO 8
        tiro = 8
        Val = Gato<1
        L = caso8.shape
        capa8 = -1
        sh = 0
        while sh == 0:
            capa8 += 1
            if capa8+1 <= L[0] and capa8+1 <= L[1]:
                comparison = Gato == caso8[capa8,:]
                cs = comparison.all()
                if cs == True:
                    sh = 1
            else:
                caso8 = np.vstack((caso8, Gato))
                escoger8 = np.vstack((escoger8,VD))
                sh = 1
        if Turno == 1:
            print('Tiro de la máquina\n')
            num,pos8 = np.max(escoger8[capa8,:]*Val),np.argmax(escoger8[capa8,:]*Val)
            Gato[pos8] = 1
            cuadros=change_dic(cuadros,pos8)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 2
        else:
            pos8 = int(input('ingresa una posición (1-9) '))
            while Val[pos8] <=0:
                print('Casilla ocupada')
                pos8 = int(input('ingresa una posición (1-9) '))
            Gato[pos8] = 2
            cuadros=change_dic(cuadros,pos8)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 1
        
        Turnos_all.append(Turno)
        tablero = np.reshape(Gato,[6,2])
        print(tablero)
        print('\n cajas ganadas ')
        print(boxes)

                        # TIRO 9
        tiro = 9
        Val = Gato<1
        L = caso9.shape
        capa9 = -1
        sh = 0
        while sh == 0:
            capa9 += 1
            if capa9+1 <= L[0] and capa9+1 <= L[1]:
                comparison = Gato == caso9[capa9,:]
                cs = comparison.all()
                if cs == True:
                    sh = 1
            else:
                caso9 = np.vstack((caso9, Gato))
                escoger9 = np.vstack((escoger9,VD))
                sh = 1
        if Turno == 1:
            print('Tiro de la máquina\n')
            num,pos9 = np.max(escoger9[capa9,:]*Val),np.argmax(escoger9[capa9,:]*Val)
            Gato[pos9] = 1
            cuadros=change_dic(cuadros,pos9)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 2
        else:
            pos9 = int(input('ingresa una posición (1-9) '))
            while Val[pos9] <=0:
                print('Casilla ocupada')
                pos9 = int(input('ingresa una posición (1-9) '))
            Gato[pos9] = 2
            cuadros=change_dic(cuadros,pos9)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 1
        
        Turnos_all.append(Turno)
        tablero = np.reshape(Gato,[6,2])
        print(tablero)
        print('\n cajas ganadas ')
        print(boxes)
        
                        # TIRO 10
        tiro = 10
        Val = Gato<1
        L = caso10.shape
        capa10 = -1
        sh = 0
        while sh == 0:
            capa10 += 1
            if capa10+1 <= L[0] and capa10+1 <= L[1]:
                comparison = Gato == caso10[capa10,:]
                cs = comparison.all()
                if cs == True:
                    sh = 1
            else:
                caso10 = np.vstack((caso10, Gato))
                escoger10 = np.vstack((escoger10,VD))
                sh = 1
        if Turno == 1:
            print('Tiro de la máquina\n')
            num,pos10 = np.max(escoger10[capa10,:]*Val),np.argmax(escoger10[capa10,:]*Val)
            Gato[pos10] = 1
            cuadros=change_dic(cuadros,pos10)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 2
        else:
            pos10 = int(input('ingresa una posición (1-9) '))
            while Val[pos10] <=0:
                print('Casilla ocupada')
                pos10 = int(input('ingresa una posición (1-9) '))
            Gato[pos10] = 2
            cuadros=change_dic(cuadros,pos10)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 1
        
        Turnos_all.append(Turno)
        tablero = np.reshape(Gato,[6,2])
        print(tablero)
        print('\n cajas ganadas ')
        print(boxes)
        
                        # TIRO 11
        tiro = 11
        Val = Gato<1
        L = caso11.shape
        capa11 = -1
        sh = 0
        while sh == 0:
            capa11 += 1
            if capa11+1 <= L[0] and capa11+1 <= L[1]:
                comparison = Gato == caso11[capa11,:]
                cs = comparison.all()
                if cs == True:
                    sh = 1
            else:
                caso11 = np.vstack((caso11, Gato))
                escoger11 = np.vstack((escoger11,VD))
                sh = 1
        if Turno == 1:
            print('Tiro de la máquina\n')
            num,pos11 = np.max(escoger11[capa11,:]*Val),np.argmax(escoger11[capa11,:]*Val)
            Gato[pos11] = 1
            cuadros=change_dic(cuadros,pos11)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 2
        else:
            pos11 = int(input('ingresa una posición (1-9) '))
            while Val[pos11] <=0:
                print('Casilla ocupada')
                pos11 = int(input('ingresa una posición (1-9) '))
            Gato[pos11] = 2
            cuadros=change_dic(cuadros,pos11)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 1
        
        Turnos_all.append(Turno)
        tablero = np.reshape(Gato,[6,2])
        print(tablero)
        print('\n cajas ganadas ')
        print(boxes)

                        # TIRO 12
        tiro = 12
        Val = Gato<1
        L = caso12.shape
        capa12 = -1
        sh = 0
        while sh == 0:
            capa12 += 1
            if capa12+1 <= L[0] and capa12+1 <= L[1]:
                comparison = Gato == caso12[capa12,:]
                cs = comparison.all()
                if cs == True:
                    sh = 1
            else:
                caso12 = np.vstack((caso12, Gato))
                escoger12 = np.vstack((escoger12,VD))
                sh = 1
        if Turno == 1:
            print('Tiro de la máquina\n')
            num,pos12 = np.max(escoger12[capa12,:]*Val),np.argmax(escoger12[capa12,:]*Val)
            Gato[pos12] = 1
            cuadros=change_dic(cuadros,pos12)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 2
        else:
            pos12 = int(input('ingresa una posición (1-9) '))
            while Val[pos12] <=0:
                print('Casilla ocupada')
                pos12 = int(input('ingresa una posición (1-9) '))
            Gato[pos12] = 2
            cuadros=change_dic(cuadros,pos12)
            boxes,point = caja(cuadros,boxes,Turno)
            if point==0:
                Turno = 1
        
        Turnos_all.append(Turno)
        tablero = np.reshape(Gato,[6,2])
        print(tablero)
        print('\n cajas ganadas ')
        print(boxes)
        
        VWIN=WIN(boxes)
        if VWIN == 1:
            print('Gana máquina')
        elif VWIN == 2:
            print('Gana Humano')
        else:
            print('Empate')
            capa_empate=-1
            #empieza
            L=caso_empate.shape
            sh=0
            capa_empate=-1
            while sh == 0:
                capa_empate +=1
                if capa_empate+1 <=L[0]:
                    comparison = Gato == caso_empate[capa_empate,:]
                    cs = comparison.all()
                    if cs == True:
                        sh = 1
                else:
                    caso12 = np.vstack((caso_empate,Gato))
                    escoger_empate = np.vstack((escoger_empate,VD))
                    sh=1
            #termina
            if Empate.shape[0]<=capa_empate:
                Empate = np.append(Empate,1)
            else:
                Empate[capa_empate] += 1
            
        # APRENDIZAJE
        if VWIN == 0 and Empate[capa_empate]<=5:
            escoger1[capa1,pos1] = escoger1[capa1,pos1] + 0.0025
            escoger2[capa2,pos2] = escoger2[capa2,pos2] + 0.0025
            escoger3[capa3,pos3] = escoger3[capa3,pos3] + 0.0025
            escoger4[capa4,pos4] = escoger4[capa4,pos4] + 0.0025
            escoger5[capa5,pos5] = escoger5[capa5,pos5] + 0.0025
            escoger6[capa6,pos6] = escoger6[capa6,pos6] + 0.0025
            escoger7[capa7,pos7] = escoger7[capa7,pos7] + 0.0025
            escoger8[capa8,pos8] = escoger8[capa8,pos8] + 0.0025
            escoger9[capa9,pos9] = escoger9[capa9,pos9] + 0.0025
            escoger10[capa10,pos10] = escoger10[capa10,pos10] + 0.0025
            escoger11[capa11,pos11] = escoger11[capa11,pos11] + 0.0025
            escoger12[capa12,pos12] = escoger12[capa12,pos12] + 0.0025
            
        elif VWIN == 0 and Empate[capa_empate]>5:
            escoger1[capa1,pos1] = escoger1[capa1,pos1] - 0.01/Empate[capa_empate]
            escoger2[capa2,pos2] = escoger2[capa2,pos2] - 0.01/Empate[capa_empate]
            escoger3[capa3,pos3] = escoger3[capa3,pos3] - 0.04/Empate[capa_empate]
            escoger4[capa4,pos4] = escoger4[capa4,pos4] - 0.05/Empate[capa_empate]
            escoger5[capa5,pos5] = escoger5[capa5,pos5] - 0.06/Empate[capa_empate]
            escoger6[capa6,pos6] = escoger6[capa6,pos6] - 0.06/Empate[capa_empate]
            escoger7[capa7,pos7] = escoger7[capa7,pos7] - 0.05/Empate[capa_empate]
            escoger8[capa8,pos8] = escoger8[capa8,pos8] - 0.04/Empate[capa_empate]
            escoger9[capa9,pos9] = escoger9[capa9,pos9] - 0.0025/Empate[capa_empate]
            escoger10[capa10,pos10] = escoger10[capa10,pos10] - 0.05/Empate[capa_empate]
            escoger11[capa11,pos11] = escoger11[capa11,pos11] - 0.04/Empate[capa_empate]
            escoger12[capa12,pos12] = escoger12[capa12,pos12] - 0.0025/Empate[capa_empate]
        elif VWIN==1 or VWIN==2:
            a= (np.sum(boxes==VWIN)-np.sum(boxes!=VWIN))/100
            valores_learn=np.array([0.01, 0.01, 0.04, 0.05, 0.06, 0.06, 0.05, 0.04, 0.04, 0.05, 0.04, 0.0025])+a
            for i in range(0,12):
                if Turnos_all[i] != VWIN:
                    valores_learn[i]=-valores_learn[i]                    
            escoger1[capa1,pos1] = escoger1[capa1,pos1] + valores_learn[0]
            escoger2[capa2,pos2] = escoger2[capa2,pos2] + valores_learn[1]
            escoger3[capa3,pos3] = escoger3[capa3,pos3] + valores_learn[2]
            escoger4[capa4,pos4] = escoger4[capa4,pos4] + valores_learn[3]
            escoger5[capa5,pos5] = escoger5[capa5,pos5] + valores_learn[4]
            escoger6[capa6,pos6] = escoger6[capa6,pos6] + valores_learn[5]
            escoger7[capa7,pos7] = escoger7[capa7,pos7] + valores_learn[6]
            escoger8[capa8,pos8] = escoger8[capa8,pos8] + valores_learn[7]
            escoger9[capa9,pos9] = escoger9[capa9,pos9] + valores_learn[8]
            escoger10[capa10,pos10] = escoger10[capa10,pos10] + valores_learn[9]
            escoger11[capa11,pos11] = escoger11[capa11,pos11] + valores_learn[10]
            escoger12[capa12,pos12] = escoger12[capa12,pos12] + valores_learn[11]
                            

    np.save('caso1.npy',caso1)     #checaaaaar
    np.save('escoger1.npy',escoger1)
           
    np.save('caso2.npy',caso2)
    np.save('escoger2.npy',escoger2)
    
    np.save('caso3.npy',caso3)
    np.save('escoger3.npy',escoger3)
    
    np.save('caso4.npy',caso4)
    np.save('escoger4.npy',escoger4)
    
    np.save('caso5.npy',caso5)
    np.save('escoger5.npy',escoger5)
    
    np.save('caso6.npy',caso6)        
    np.save('escoger6.npy',escoger6)
    
    np.save('caso7.npy',caso7)
    np.save('escoger7.npy',escoger7)
    
    np.save('caso8.npy',caso8)
    np.save('escoger8.npy',escoger8)
    
    np.save('caso9.npy',caso9)
    np.save('escoger9.npy',escoger9)

    np.save('caso10.npy',caso10)
    np.save('escoger10.npy',escoger10)
    
    np.save('caso11.npy',caso11)
    np.save('escoger11.npy',escoger11)
    
    np.save('caso12.npy',caso12)
    np.save('escoger12.npy',escoger12)
    
    np.save('Empate.npy',Empate)
    play = int(input('Quieres jugar de nuevo (si = 1) '))
