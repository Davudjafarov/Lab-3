



def choose(n, k):

    k = min(k, n-k)
    #K ska alltid vara minsta, istället för 5 över 3, så blir de 5 över 2

    #Basfall
    if k == 0 or k == n:
        return 1
    elif k == 1:
        return n
    #Rekursivt steg, med pascal
    return (choose(n-1, k-1) * n) //k

#https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww2.lawrence.edu%2Ffast%2FGREGGJ%2FCMSC210%2Falgorithms%2Frecursion.html&psig=AOvVaw1T75S4D4e_YrAnlu3Uo_Bv&ust=1758476147401000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCKi50KTw548DFQAAAAAdAAAAABAE​

print(choose(5,3))
print(choose(1000,1))
print(choose(52,5))
print(choose(1000,4))
print(choose(1000, 800))
print(choose(1000,999))

