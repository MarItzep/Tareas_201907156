class nodo:
    def __init__(self,valor):
        self.valor=valor
        self.siguiente=None
        self.anterior=None

class listaDoblementeCircular:
    def __init__(self):
        self.primero = None
        self.ultimo=None
    
    def vacia(self):
        if self.primero==None:
            return True
        else:
            return False
    
    def insertarInicio(self,dato):
        if self.vacia():
            self.primero = self.ultimo = nodo(dato)
        else:
            aux= nodo(dato)
            aux.siguiente = self.primero
            self.primer.anterior=aux
            self.primero=aux
        self.unir_nodos()


    def insertarFinal(self,dato):
        if self.vacia():
            self.primero = self.ultimo=nodo(dato)
        else:
            aux=self.ultimo
            self.ultimo=aux.siguiente=nodo(dato)
            self.ultimo.anterior=aux
        self.unir_nodos()


    def unir_nodos(self):
        self.primero.anterior =self.ultimo
        self.ultimo.siguiente=self.primero
    

    def recorrer_inicioFin(self):
        aux = self.primero
        while aux:
            print(aux.valor)
            aux=aux.siguiente
            if aux == self.primero:
                break

    def recorrer_finInicio(self):
        aux=self.ultimo
        while aux:
            print(aux.valor)
            aux=aux.anterior
            if aux==self.ultimo:
                break
    
    def buscar(self,valorBuscado):
        aux=self.primero
        while aux:
            if aux.valor == valorBuscado:
                print("valor actual : ",valorBuscado )
                print("valor siguiente : ",aux.siguiente.valor )
                print("Valor anterior : ",aux.anterior.valor)
                return True
            
            else:
                aux= aux.siguiente
                if aux ==self.primero:
                    return False
            # aux=aux.siguiente
        
            # #print("2")
            # if(valorBuscado == aux.valor):
            #     print("Actual",aux.valor)
            #     print("Siguiente",aux.siguiente.valor)
            #     print("Anterior",aux.anterior.valor)
            # elif(aux.siguiente == self.primero):
            #     return
            # aux=aux.siguiente
