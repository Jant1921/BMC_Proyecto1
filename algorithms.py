from time import time
import sys

class Algorithms:
    sequence1 = ""
    sequence2 = ""
    matchValue = 1
    mismatchValue = -1
    gap_penalty = -2
    #afin
    gap_extended = -0.5
    new_gap = -5
    # result values
    alignment1 = ""
    alignment2 = ""
    matrixResult = []
    optimalValue = 0
    optimalPath = []
    totalTime = ""
    totalMem = ""
    kband_value = 0
    startTime = 0

    def __init__(self):
        pass

    ## UTILS
    def match_score(self, caracterSeq1, caracterSeq2):
        if caracterSeq1 == caracterSeq2:
            return self.matchValue
        else:
            return self.mismatchValue

    def calcularMemoria(self, s):
        self.totalMem = str(sys.getsizeof("l")*len(s)*len(s[0])) + "B"

    def calcularTiempo(self):
        tiempo_final = time()
        tiempo_ejecucion = tiempo_final - self.startTime
        self.totalTime = str(tiempo_ejecucion) + " ms"
    
    def inicioMatriz(self, dimensiones):
        matriz = []
        for x in range(dimensiones[0]):
            matriz.append([])
            for y in range(dimensiones[1]):
                matriz[-1].append(0)
        return matriz

    def insideBand(self, i, j, k):
        return ( (-k<= i-j) and (i-j<=k) )

    def getInfo(self, score, n, m, seq1, seq2):
        align1, align2 = '', ''
        i,j = m,n 
        while i > 0 and j > 0: # reconstruye las hileras de atras para adelante con el valor mas alto
            score_current = score[i][j]
            score_diagonal = score[i-1][j-1]
            score_up = score[i][j-1]
            score_left = score[i-1][j]
            
            self.optimalPath.append((j,i))

            if score_current == score_diagonal + self.match_score(seq1[i-1], seq2[j-1]):
                align1 += seq1[i-1]
                align2 += seq2[j-1]
                i -= 1
                j -= 1
            elif score_current == score_left + self.gap_penalty:
                align1 += seq1[i-1]
                align2 += '-'
                i -= 1
            elif score_current == score_up + self.gap_penalty:
                align1 += '-'
                align2 += seq2[j-1]
                j -= 1

        while i > 0:
            self.optimalPath.append((j,i))
            align1 += seq1[i-1]
            align2 += '-'
            i -= 1
        while j > 0:
            self.optimalPath.append((j,i))
            align1 += '-'
            align2 += seq2[j-1]
            j -= 1
        self.optimalPath.append((0,0))
        self.alignment1 = align1[::-1]
        self.alignment2 = align2[::-1]
        self.optimalValue =  score[m-1][n]
        self.matrixResult = score
        self.calcularTiempo()

    def getInfoAfin2(self, score, n, m, seq1, seq2):
        align1, align2 = '', ''
        i,j = m,n 
        while i > 0 and j > 0: # reconstruye las hileras de atras para adelante con el valor mas alto
            score_current = score[i][j]
            score_diagonal = score[i-1][j-1]
            score_up = score[i][j-1]
            score_left = score[i-1][j]
            
            self.optimalPath.append((0,0))

            if score_current == score_diagonal + self.match_score(seq1[i-1], seq2[j-1]):
                align1 += seq1[i-1]
                align2 += seq2[j-1]
                i -= 1
                j -= 1
            elif score_current == score_left + self.gap_extended:
                align1 += seq1[i-1]
                align2 += '-'
                i -= 1
            elif score_current == score_up + self.gap_extended:
                align1 += '-'
                align2 += seq2[j-1]
                j -= 1

        while i > 0:
            align1 += seq1[i-1]
            align2 += '-'
            i -= 1
        while j > 0:
            align1 += '-'
            align2 += seq2[j-1]
            j -= 1
        self.alignment1 = align1[::-1]
        self.alignment2 = align2[::-1]
        self.optimalValue = score[m-1][n]
        self.calcularTiempo()
        self.matrixResult = score

    ## ALINGMENTS
    def globalEstandar(self):
        seq1 = self.sequence1
        seq2 = self.sequence2
        start = time()
        m, n = len(seq1), len(seq2)  
        score = self.inicioMatriz((m+1, n+1))          
        for i in range(0, m + 1):               #Llena la primera fila con gaps
            score[i][0] = self.gap_penalty * i
        for j in range(0, n + 1):               #Llena la primera columna con gaps
            score[0][j] = self.gap_penalty * j
        for i in range(1, m + 1):
            for j in range(1, n + 1):           #Llena el resto de la matriz
                match = score[i - 1][j - 1] + self.match_score(seq1[i-1], seq2[j-1])
                delete = score[i - 1][j] + self.gap_penalty
                insert = score[i][j - 1] + self.gap_penalty
                score[i][j] = max(match, delete, insert)

         
        align1, align2 = '', ''
        i,j = m,n 
        while i > 0 and j > 0: # reconstruye las hileras de atras para adelante con el valor mas alto
            score_current = score[i][j]
            score_diagonal = score[i-1][j-1]
            score_up = score[i][j-1]
            score_left = score[i-1][j]
            
            self.optimalPath.append((j,i))

            if score_current == score_diagonal + self.match_score(seq1[i-1], seq2[j-1]):
                align1 += seq1[i-1]
                align2 += seq2[j-1]
                i -= 1
                j -= 1
            elif score_current == score_left + self.gap_penalty:
                align1 += seq1[i-1]
                align2 += '-'
                i -= 1
            elif score_current == score_up + self.gap_penalty:
                align1 += '-'
                align2 += seq2[j-1]
                j -= 1


        while i > 0:
            self.optimalPath.append((j,i))
            align1 += seq1[i-1]
            align2 += '-'
            i -= 1
        while j > 0:
            self.optimalPath.append((j,i))
            align1 += '-'
            align2 += seq2[j-1]
            j -= 1
        self.optimalPath.append((0,0))
        self.alignment1 = align1[::-1]
        self.alignment2 = align2[::-1]
        print ("Score: ", score[m-1][n])
        self.optimalValue = score[m-1][n]
        for i in range(0, m):
            print (score[i])
        self.calcularTiempo()
        self.matrixResult = score

    def globalKband(self):
        k = self.kband_value
        seq1 = self.sequence1
        seq2 = self.sequence2
        start = time()
        m, n = len(seq1), len(seq2)
        score = self.inicioMatriz((n+1,m+1))
        for i in range(0, k):
            score[i][0] = i*self.gap_penalty
        for j in range(0, k):
            score[0][j] = j*self.gap_penalty

        for i in range(1, n + 1):
            for d in range(-k,k):
                j = i + d
                if 1<=j<=n:
                    #i = i - 1
                    #j = j - 1
                    #print("i=" + str(i) + " j=" + str(j))
                    score[i][j] = score[i-1][j-1] + self.match_score(seq1[i-1], seq2[j-1])
                    if self.insideBand(i-1,j,k):
                        score[i][j] = max(score[i][j], score[i-1][j] + self.gap_penalty)
                    if self.insideBand(i, j-1,k):
                        score[i][j] = max(score[i][j], score[i][j-1] + self.gap_penalty)
        self.getInfo(score,n,m, seq1, seq2)

    def globalCostoGap(self):
        seq1 = self.sequence1
        seq2 = self.sequence2
        m, n = len(seq1), len(seq2)
        a = self.inicioMatriz((m+1, n+1))
        b = self.inicioMatriz((m+1, n+1))
        c = self.inicioMatriz((m+1, n+1))

        d = -self.new_gap
        e = -self.gap_extended

        a[0][0] = -99999999999999
        b[0][0] = -99999999999999
        c[0][0] = -99999999999999

        for i in range(1, m+1):
            a[i][0] = -d - (i-1) * e
            b[i][0] = -d - (i-1) * e
            c[i][0] = -99999999999999
        for j in range(1, n+1):
            a[0][j] = - d -(j-1)*e
            c[0][j] = - d -(j-1)*e
            b[0][j] =  -99999999999999
            

        for i in range(1, m+1):
            for j in range(1, n+1):
                a[i][j] = max( a[i-1][j-1] + self.match_score(seq1[i-1], seq2[j-1]) , b[i-1][j-1] + self.match_score(seq1[i-1], seq2[j-1]), c[i-1][j-1] + self.match_score(seq1[i-1], seq2[j-1]))
                b[i][j] = max( a[i-1][j] - d, b[i-1][j] - e)
                c[i][j] = max( a[i][j-1] - d, c[i][j-1] - e)
        self.getInfoAfin2(a,n,m,seq1, seq2)


    def semiglobal(self):
        seq1 = self.sequence1
        seq2 = self.sequence2
        m, n = len(seq1), len(seq2)
        score = self.inicioMatriz((m+1, n+1))
        max_score = 0
        max_i = 0
        max_j = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                score_diagonal = score[i-1][j-1] + self.match_score(seq1[i-1], seq2[j-1])
                score_up = score[i][j-1] + self.gap_penalty
                score_left = score[i-1][j] + self.gap_penalty
                score[i][j] = max(score_left, score_up, score_diagonal)
        i,j = m,n

        for x in range(0, j+1):
            if score[i][x] >= max_score:
                max_i = i
                max_j = x
                max_score = score[i][x];
        for y in range(0,i+1):
            if score[y][j] >= max_score:
                max_i = y
                max_j = j
                max_score = score[y][j];

        self.getInfo(score,n,m, seq1, seq2)

    def semiglobalCostoGap(self):
        seq1 = self.sequence1
        seq2 = self.sequence2
        m, n = len(seq1), len(seq2)
        score = self.inicioMatriz((m+1, n+1))
        gapM = self.inicioMatriz((m+1, n+1))
        max_score = 0
        max_i = 0
        max_j = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                score_diagonal = score[i-1][j-1] + self.match_score(seq1[i-1], seq2[j-1])
                if(gapM[i-1][j] == 1):
                    score_left = self.gap_extended + score[i - 1][j]
                else:
                    score_left = self.new_gap + score[i - 1][j]
                if(gapM[i][j-1] == 1):
                    score_up = self.gap_extended + score[i][j-1]
                else:
                    score_up = self.new_gap + score[i][j - 1]

                maxim =  max(score_left, score_up, score_diagonal)
                
                if(maxim == score_left and gapM[i-1][j] ==1):
                    gapM[i-1][j] = 1
                if(maxim == score_up and gapM[i][j-1] ==1):
                    gapM[i][j-1] = 1
                score[i][j] = maxim
        i,j = m,n

        for x in range(0, j+1):
            if score[i][x] >= max_score:
                max_i = i
                max_j = x
                max_score = score[i][x];
        for y in range(0,i+1):
            if score[y][j] >= max_score:
                max_i = y
                max_j = j
                max_score = score[y][j];
        self.getInfo(score,n,m, seq1, seq2)

    def local(self):
        seq1 = self.sequence1
        seq2 = self.sequence2
        m, n = len(seq1), len(seq2)  
        score = self.inicioMatriz((m+1, n+1))   
        max_score = 0        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                score_diagonal = score[i-1][j-1] + self.match_score(seq1[i-1], seq2[j-1])
                score_up = score[i][j-1] + self.gap_penalty
                score_left = score[i-1][j] + self.gap_penalty
                score[i][j] = max(0,score_left, score_up, score_diagonal)

            
                if score[i][j] >= max_score:
                    max_i = i
                    max_j = j
                    max_score = score[i][j];
        align1, align2 = '', ''  
        
        i,j = max_i,max_j   
        
        while score[i][j] != 0:
            current = score[i][j]
            diagonal = score[i-1][j-1] 
            up = score[i][j-1] 
            left = score[i-1][j] 
            
            self.optimalPath.append((j,i))

            if current == diagonal + self.match_score(seq1[i-1], seq2[j-1]):
                align1 += seq1[i-1]
                align2 += seq2[j-1]
                i -= 1
                j -= 1
            elif current == up + self.gap_penalty:
                align1 += '-'
                align2 += seq2[j-1]
                j -= 1
            elif current == left + self.gap_penalty:
                align1 += seq1[i-1]
                align2 += '-'
                i -= 1
        self.alignment1 = align1[::-1]
        self.alignment2 = align2[::-1]
        self.optimalValue = score[m-1][n]
        self.calcularTiempo()
        self.matrixResult = score

    def localCostoGap(self):
        seq1 = self.sequence1
        seq2 = self.sequence2
        m, n = len(seq1), len(seq2)
        a = self.inicioMatriz((m+1, n+1))
        b = self.inicioMatriz((m+1, n+1))
        c = self.inicioMatriz((m+1, n+1))

        d = -self.new_gap
        e = -self.gap_extended

        a[0][0] = -99999999999999
        b[0][0] = -99999999999999
        c[0][0] = -99999999999999

        for i in range(1, m+1):
            a[i][0] = -d - (i-1) * e
            b[i][0] = -d - (i-1) * e
            c[i][0] = -99999999999999
        for j in range(1, n+1):
            a[0][j] = - d -(j-1)*e
            c[0][j] = - d -(j-1)*e
            b[0][j] =  -99999999999999
            
        max_score = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                a[i][j] = max( 0, a[i-1][j-1] + self.match_score(seq1[i-1], seq2[j-1]) , b[i-1][j-1] + self.match_score(seq1[i-1], seq2[j-1]), c[i-1][j-1] + self.match_score(seq1[i-1], seq2[j-1]))
                b[i][j] = max( 0, a[i-1][j] - d, b[i-1][j] - e)
                c[i][j] = max( 0, a[i][j-1] - d, c[i][j-1] - e)
                if a[i][j] >= max_score:
                    max_i = i
                    max_j = j
                    max_score = a[i][j];

        align1, align2 = '', ''  
        
        i,j = max_i,max_j   
        score = a
        while score[i][j] != 0:
            current = score[i][j]
            diagonal = score[i-1][j-1] 
            up = score[i][j-1] 
            left = score[i-1][j] 
            
            self.optimalPath.append((j,i))

            if current == diagonal + self.match_score(seq1[i-1], seq2[j-1]):
                align1 += seq1[i-1]
                align2 += seq2[j-1]
                i -= 1
                j -= 1
            elif current == up + self.gap_penalty:
                align1 += '-'
                align2 += seq2[j-1]
                j -= 1
            elif current == left + self.gap_penalty:
                align1 += seq1[i-1]
                align2 += '-'
                i -= 1
        
        self.alignment1 = align1[::-1]
        self.alignment2 = align2[::-1]
        self.optimalValue = max_score
        self.calcularTiempo()
        self.matrixResult = score

    algorithmsList = {
        "global_estandar": globalEstandar,
        "global_lineal": globalEstandar,
        "global_kband": globalKband,
        "kband_lineal": globalEstandar,
        "global_costogap": globalCostoGap,
        "semi_estandar": semiglobal,
        "semi_lineal": globalEstandar,
        "semi_costogap": semiglobalCostoGap,
        "local_estandar": local,
        "local_lineal": globalEstandar,
        "local_costogap": localCostoGap,
    }

    def get_result(self, first_word, second_word, algorithm, kband_value):
        # result values
        self.alignment1 = ""
        self.alignment2 = ""
        self.matrixResult = []
        self.optimalValue = 0
        self.optimalPath = []
        self.totalTime = ""
        self.totalMem = ""
        self.kband_value = int(kband_value)
        # Mock results
        w = len(first_word)
        h = len(second_word)
        self.sequence1 = first_word
        self.sequence2 = second_word
        self.startTime = time()
        # call alignment function
        self.algorithmsList[algorithm](self)

        # alignment result variable
        matrix = self.matrixResult
        #getting optimal value
        optimal_value = self.optimalValue
        self.calcularMemoria(matrix)
        
        return {
            "matrix": matrix,
            "optimal_value": optimal_value,
            "first_word": " " + first_word,
            "second_word": second_word,
            "optimal_path": self.optimalPath,
            "algorithm": algorithm,
            "alignment1": self.alignment1,
            "alignment2": self.alignment2,
            "total_time": self.totalTime,
            "total_memory": self.totalMem,
        }

    