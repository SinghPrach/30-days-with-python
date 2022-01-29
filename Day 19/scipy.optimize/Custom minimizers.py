from scipy.optimize import OptimizeResult
import numpy as np

def custmin(fun, x0, args=(), maxfev=None, stepsize=0.1,maxiter=100, callback=None, **options):
  bestx = x0
   besty = fun(x0)
  funcalls = 1
    niter = 0
   improved = True
  stop = False

    while improved and not stop and niter < maxiter:
      improved = False
       niter += 1
      for dim in range(np.size(x0)):
           for s in [bestx[dim] - stepsize, bestx[dim] + stepsize]:
                testx = np.copy(bestx)
               testx[dim] = s
               testy = fun(testx, *args)
               funcalls += 1
               if testy < besty:
                    besty = testy
                  bestx = testx
                  improved = True
           if callback is not None:
               callback(bestx)
           if maxfev is not None and funcalls >= maxfev:
               stop = True
               break
               return OptimizeResult(fun=besty, x=bestx, nit=niter, nfev=funcalls, success=(niter > 1))
   
x0 = [1.35, 0.9, 0.8, 1.1, 1.2]
res = minimize(rosen, x0, method=custmin, options=dict(stepsize=0.05))
print( res.x)
