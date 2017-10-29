
class Algorithms:
    
    

    def __init__(self):
        pass

    def globalEstandar():
        print("holakj")
    
    algorithmsList = {
        "global_estandar": globalEstandar,
        "global_lineal": globalEstandar,
        "global_kband": globalEstandar,
        "kband_lineal": globalEstandar,
        "global_costogap": globalEstandar,
        "semi_estandar": globalEstandar,
        "semi_lineal": globalEstandar,
        "semi_costogap": globalEstandar,
        "local_estandar": globalEstandar,
        "local_lineal": globalEstandar,
        "local_costogap": globalEstandar,
    }

    def get_result(self, first_word, second_word, algorithm):
            
        # Mock results
        w = len(first_word)
        h = len(second_word)

        self.algorithmsList[algorithm]()

        # call alignment function
        # alignment()
        # alignment resutl variable
        matrix = [["(2,>)" for x in range(w)] for y in range(h)]
        
        #getting optimal value
        optimal_value = matrix[h-1][w-1]
        
        # define optimal path variable
        optimal_path = []
        
        # searching for an optimal path
        for x in range(w if w < h else h):
            optimal_path.append((x, x))
        
        return {
            "matrix": matrix,
            "optimal_value": optimal_value,
            "first_word": first_word,
            "second_word": second_word,
            "optimal_path": optimal_path,
            "algorithm": algorithm,
        }
    
    # should return a tuple with two strings, ("as_sd__asd", "__as_ddsa_d")
    def get_alignment(self, path):
        pass
    