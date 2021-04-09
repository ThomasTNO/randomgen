from threading import Lock
from typing import Any, Optional, Sequence, Tuple, Union

from numpy import ndarray

from randomgen.common import BitGenerator
from randomgen.typing import Size

class RandomState:

    _bit_generator: BitGenerator
    lock: Lock
    _poisson_lam_max: int
    def __init__(self, bit_generator: Optional[BitGenerator] = ...) -> None: ...
    def seed(self, *args, **kwargs): ...
    def get_state(self, legacy: bool = ...): ...
    def set_state(self, state) -> None: ...
    def random_sample(self, size: Size = ...) -> Union[float, ndarray]: ...
    def beta(self, a, b, size: Size = ...) -> Union[float, ndarray]: ...
    def exponential(self, scale=1.0, size: Size = ...) -> Union[float, ndarray]: ...
    def standard_exponential(self, size: Size = ...) -> Union[float, ndarray]: ...
    def tomaxint(self, size: Size = ...) -> Union[int, ndarray]: ...
    def randint(
        self, low, high=None, size: Size = ..., dtype=int
    ) -> Union[int, ndarray]: ...
    def bytes(self, length: int) -> ndarray: ...
    def choice(self, a, size: Size = ..., replace=True, p=None): ...
    def uniform(self, low=0.0, high=1.0, size: Size = ...) -> Union[float, ndarray]: ...
    def rand(self, *args: Tuple[int, ...]) -> ndarray: ...
    def randn(self, *args: Tuple[int, ...]) -> ndarray: ...
    def random_integers(
        self, low, high=None, size: Size = ...
    ) -> Union[float, ndarray]: ...
    def standard_normal(self, size: Size = ...) -> Union[float, ndarray]: ...
    def normal(self, loc=0.0, scale=1.0, size: Size = ...) -> Union[float, ndarray]: ...
    def standard_gamma(self, shape, size: Size = ...) -> Union[float, ndarray]: ...
    def gamma(self, shape, scale=1.0, size: Size = ...) -> Union[float, ndarray]: ...
    def f(self, dfnum, dfden, size: Size = ...) -> Union[float, ndarray]: ...
    def noncentral_f(
        self, dfnum, dfden, nonc, size: Size = ...
    ) -> Union[float, ndarray]: ...
    def chisquare(self, df, size: Size = ...) -> Union[float, ndarray]: ...
    def noncentral_chisquare(
        self, df, nonc, size: Size = ...
    ) -> Union[float, ndarray]: ...
    def standard_cauchy(self, size: Size = ...) -> Union[float, ndarray]: ...
    def standard_t(self, df, size: Size = ...) -> Union[float, ndarray]: ...
    def vonmises(self, mu, kappa, size: Size = ...) -> Union[float, ndarray]: ...
    def pareto(self, a, size: Size = ...) -> Union[float, ndarray]: ...
    def weibull(self, a, size: Size = ...) -> Union[float, ndarray]: ...
    def power(self, a, size: Size = ...) -> Union[float, ndarray]: ...
    def laplace(
        self, loc=0.0, scale=1.0, size: Size = ...
    ) -> Union[float, ndarray]: ...
    def gumbel(self, loc=0.0, scale=1.0, size: Size = ...) -> Union[float, ndarray]: ...
    def logistic(
        self, loc=0.0, scale=1.0, size: Size = ...
    ) -> Union[float, ndarray]: ...
    def lognormal(
        self, mean=0.0, sigma=1.0, size: Size = ...
    ) -> Union[float, ndarray]: ...
    def rayleigh(self, scale=1.0, size: Size = ...) -> Union[float, ndarray]: ...
    def wald(self, mean, scale, size: Size = ...) -> Union[float, ndarray]: ...
    def triangular(
        self, left, mode, right, size: Size = ...
    ) -> Union[float, ndarray]: ...
    # Complicated, discrete distributions:
    def binomial(self, n, p, size: Size = ...) -> ndarray: ...
    def negative_binomial(self, n, p, size: Size = ...) -> ndarray: ...
    def poisson(self, lam=1.0, size: Size = ...) -> Union[int, ndarray]: ...
    def zipf(self, a, size: Size = ...) -> Union[int, ndarray]: ...
    def geometric(self, p, size: Size = ...) -> Union[int, ndarray]: ...
    def hypergeometric(self, ngood, nbad, nsample, size: Size = ...): ...
    def logseries(self, p, size: Size = ...) -> Union[int, ndarray]: ...
    # Multivariate distributions:
    def multivariate_normal(
        self, mean, cov, size: Size = ..., check_valid="warn", tol=1e-8
    ) -> ndarray: ...
    def multinomial(self, n, pvals, size: Size = ...) -> ndarray: ...
    def dirichlet(self, alpha, size: Size = ...) -> ndarray: ...
    # Shuffling and permutations:
    def shuffle(self, x: Sequence[Any]) -> ndarray: ...
    def permutation(self, x: Sequence[Any]) -> ndarray: ...

_rand: RandomState

beta = _rand.beta
binomial = _rand.binomial
bytes = _rand.bytes
chisquare = _rand.chisquare
choice = _rand.choice
dirichlet = _rand.dirichlet
exponential = _rand.exponential
f = _rand.f
gamma = _rand.gamma
get_state = _rand.get_state
geometric = _rand.geometric
gumbel = _rand.gumbel
hypergeometric = _rand.hypergeometric
laplace = _rand.laplace
logistic = _rand.logistic
lognormal = _rand.lognormal
logseries = _rand.logseries
multinomial = _rand.multinomial
multivariate_normal = _rand.multivariate_normal
negative_binomial = _rand.negative_binomial
noncentral_chisquare = _rand.noncentral_chisquare
noncentral_f = _rand.noncentral_f
normal = _rand.normal
pareto = _rand.pareto
permutation = _rand.permutation
poisson = _rand.poisson
power = _rand.power
rand = _rand.rand
randint = _rand.randint
randn = _rand.randn
random = _rand.random_sample
random_integers = _rand.random_integers
random_sample = _rand.random_sample
rayleigh = _rand.rayleigh
seed = _rand.seed
set_state = _rand.set_state
shuffle = _rand.shuffle
standard_cauchy = _rand.standard_cauchy
standard_exponential = _rand.standard_exponential
standard_gamma = _rand.standard_gamma
standard_normal = _rand.standard_normal
standard_t = _rand.standard_t
triangular = _rand.triangular
uniform = _rand.uniform
vonmises = _rand.vonmises
wald = _rand.wald
weibull = _rand.weibull
zipf = _rand.zipf

def sample(*args, **kwargs): ...
def ranf(*args, **kwargs): ...
