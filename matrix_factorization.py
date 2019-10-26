import numpy


"""
@INPUT:
    R     : estimated rating matrix to be factorized, dimension N x M (N users and M items)
    P     : initialized user matrix of dimension N x K
    Q     : initialized item matrix of dimension M x K
    K     : the number of latent features/factors (to be considered in rating the M items)
    steps : the maximum number of steps to perform the optimisation
    alpha : the learning rate
    beta  : the regularization parameter
@OUTPUT:
    the optimized matrices P and Q transpose
"""
def matrix_factorization(R, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):
    
    Q = Q.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        #? eR = numpy.dot(P,Q)
        e = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)
                    for k in range(K):
                        e = e + (beta/2) * ( pow(P[i][k],2) + pow(Q[k][j],2) )
        if e < 0.001:
            break
        
    return P, Q.T

###############################################################################

if __name__ == "__main__":
    R = [
         [2,1,0,4],
         [1,4,2,3],
         [3,5,5,1],
         [2,2,5,4],
         [1,2,3,3],
        ]

    R = numpy.array(R)

    N = len(R)
    M = len(R[0])
    K = 2

    P = numpy.random.rand(N,K)
    Q = numpy.random.rand(M,K)

    print("The initialized user matrix:")
    print(P)
    print("")
    print("The initialized item matrix:")
    print(Q.T)
    
    nP, nQ = matrix_factorization(R, P, Q, K)

    print("")

    print("The optimized user matrix:")
    print(nP)
    print("")
    print("The optimized item matrix:")
    print(nQ.T)

    print("")

    ERM = numpy.matmul(nP, nQ.T)
    print("The estimated rating matrix:")
    print(ERM)
