def concatenalis(self, lista, sort = False, norepeat = False,):
        """
        param lista: Objeto lista() a concatenar, 
        param sort: 'True' si se desea ordenar la lista concatenada, 
        param norepeat: 'True' si se desea eliminar elementos repetidos
        """
        if isinstance(lista,Lista):
            aux = []
            for i in range(self.size()):
                aux.append(self.get_element_by_index(i))

            for i in range(lista.size()):
                if sort:
                    if norepeat:
                        if lista.get_element_by_index(i) not in aux:
                            self.insert(lista.get_element_by_index(i),None)
                    else: self.insert(lista.get_element_by_index(i),None)

                elif norepeat:
                    if lista.get_element_by_index(i) not in aux:
                        self.__elements.append(lista.get_element_by_index(i))
                        
                else: self.__elements.append(lista.get_element_by_index(i))

        else:
            print('no es posible concatenar una lista con un ',type(lista))

    def intersectionlist(self, lista):
        aux = []
        cont = 0
        for i in range(self.size()):
            aux.append(self.get_element_by_index(i))
        
        for i in range(lista.size()):
            if lista.get_element_by_index(i) in aux:
                cont += 1

        return cont
