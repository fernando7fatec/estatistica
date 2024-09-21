import statistics as st

class RegressaoLinear:
    # Calcula coeficiente 
    def correlacaoLinear(X,Y):
        return st.correlation(X,Y,method='linear')
    
    #def retornaFuncaoLinear(X,Y):

    

X = [10,15,20,25,30]
Y = [1003,1005,1010,1011,1014]

print(round(RegressaoLinear.correlacaoLinear(X,Y),4))

    