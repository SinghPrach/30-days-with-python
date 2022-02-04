from scipy.sparse.linalg import LinearOperator
class Diagonal(LinearOperator):
    def __init__(self, diag, dtype='float32'):
        self.diag = diag
        self.shape = (len(self.diag), len(self.diag))
        self.dtype = np.dtype(dtype)
    def _matvec(self, x):
        return self.diag*x
    def _rmatvec(self, x):
        return self.diag*x
N = 100
rng = np.random.default_rng()
d = rng.normal(0, 1, N).astype(np.float64)
D = np.diag(d)
Dop = Diagonal(d, dtype=np.float64)
evals_all, evecs_all = eigh(D)
evals_large, evecs_large = eigsh(Dop, 3, which='LA', maxiter=1e3)
evals_all[-3:]
evals_large 
print(np.dot(evecs_large.T, evecs_all[:,-3:]))
class FirstDerivative(LinearOperator):
    def __init__(self, N, dtype='float32'):
        self.N = N
        self.shape = (self.N, self.N)
        self.dtype = np.dtype(dtype)
    def _matvec(self, x):
        y = np.zeros(self.N, self.dtype)
        y[1:-1] = (0.5*x[2:]-0.5*x[0:-2])
        return y
    def _rmatvec(self, x):
        y = np.zeros(self.N, self.dtype)
        y[0:-2] = y[0:-2] - (0.5*x[1:-1])
        y[2:] = y[2:] + (0.5*x[1:-1])
        return y
N = 21
D = np.diag(0.5*np.ones(N-1), k=1) - np.diag(0.5*np.ones(N-1), k=-1)
D[0] = D[-1] = 0 # take away edge effects
Dop = FirstDerivative(N, dtype=np.float64)
evals_all, evecs_all = eig(D)
evals_large, evecs_large = eigs(Dop, 4, which='LI')
evals_all_imag = evals_all.imag
isort_imag = np.argsort(np.abs(evals_all_imag))
evals_all_imag = evals_all_imag[isort_imag]
evals_large_imag = evals_large.imag
isort_imag = np.argsort(np.abs(evals_large_imag))
evals_large_imag = evals_large_imag[isort_imag]
evals_all_imag[-4:]
