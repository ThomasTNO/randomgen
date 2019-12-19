import numpy as np
cimport numpy as np

from randomgen.common cimport *
from randomgen.entropy import random_entropy

__all__ = ['PCG64']

cdef uint64_t pcg64_uint64(void* st) nogil:
    return pcg64_next64(<pcg64_state_t *>st)

cdef uint32_t pcg64_uint32(void *st) nogil:
    return pcg64_next32(<pcg64_state_t *> st)

cdef double pcg64_double(void* st) nogil:
    return uint64_to_double(pcg64_next64(<pcg64_state_t *>st))


cdef class PCG64(BitGenerator):
    u"""
    PCG64(seed=None, inc=0)

    Container for the PCG-64 pseudo-random number generator.

    Parameters
    ----------
    seed : {None, long}, optional
        Random seed initializing the pseudo-random number generator.
        Can be an integer in [0, 2**128] or ``None`` (the default).
        If `seed` is ``None``, then ``PCG64`` will try to read data
        from ``/dev/urandom`` (or the Windows analog) if available. If
        unavailable, a 64-bit hash of the time and process ID is used.
    inc : {None, int}, optional
        Stream to return.
        Can be an integer in [0, 2**128] or ``None`` (the default).  If `inc` is
        ``None``, then 0 is used.  Can be used with the same seed to
        produce multiple streams using other values of inc.

    Attributes
    ----------
    lock: threading.Lock
        Lock instance that is shared so that the same bit git generator can
        be used in multiple Generators without corrupting the state. Code that
        generates values from a bit generator should hold the bit generator's
        lock.

    Notes
    -----
    PCG-64 is a 128-bit implementation of O'Neill's permuted congruential
    generator ([1]_, [2]_). PCG-64 has a period of :math:`2^{128}` and supports
    advancing an arbitrary number of steps as well as :math:`2^{127}` streams.

    ``PCG64`` provides a capsule containing function pointers that produce
    doubles, and unsigned 32 and 64- bit integers. These are not
    directly consumable in Python and must be consumed by a ``Generator``
    or similar object that supports low-level access.

    Supports the method advance to advance the RNG an arbitrary number of
    steps. The state of the PCG-64 RNG is represented by 2 128-bit unsigned
    integers.

    See ``PCG32`` for a similar implementation with a smaller period.

    **State and Seeding**

    The ``PCG64`` state vector consists of 2 unsigned 128-bit values,
    which are represented externally as Python ints.
    ``PCG64`` is seeded using a single 128-bit unsigned integer.
    In addition, a second 128-bit unsigned integer is used to set the stream.

    **Parallel Features**

    ``PCG64`` can be used in parallel applications in one of two ways.
    The preferable method is to use sub-streams, which are generated by using the
    same value of ``seed`` and incrementing the second value, ``inc``.

    >>> from randomgen import Generator, PCG64
    >>> rg = [Generator(PCG64(1234, i + 1)) for i in range(10)]

    The alternative method is to call ``advance`` with a different value on
    each instance to produce non-overlapping sequences.

    >>> rg = [Generator(PCG64(1234, i + 1)) for i in range(10)]
    >>> for i in range(10):
    ...     rg[i].bit_generator.advance(i * 2**64)

    **Compatibility Guarantee**

    ``PCG64`` makes a guarantee that a fixed seed and will always produce
    the same random integer stream.

    References
    ----------
    .. [1] "PCG, A Family of Better Random Number Generators",
           http://www.pcg-random.org/
    .. [2] O'Neill, Melissa E. "PCG: A Family of Simple Fast Space-Efficient
           Statistically Good Algorithms for Random Number Generation"
    """
    def __init__(self, seed=None, inc=0, *, mode=None):
        BitGenerator.__init__(self, seed, mode)
        self.seed(seed, inc)

        self._bitgen.state = <void *>&self.rng_state
        self._bitgen.next_uint64 = &pcg64_uint64
        self._bitgen.next_uint32 = &pcg64_uint32
        self._bitgen.next_double = &pcg64_double
        self._bitgen.next_raw = &pcg64_uint64

    cdef _reset_state_variables(self):
        self.rng_state.has_uint32 = 0
        self.rng_state.uinteger = 0

    def _seed_from_seq(self, inc=0):
        size = 4 if inc is None else 2
        state = self.seed_seq.generate_state(size, np.uint64)
        if inc is None:
            _inc = state[2:]
        else:
            _inc = <np.ndarray>np.empty(2, np.uint64)
            _inc[0] = int(inc) // 2**64
            _inc[1] = int(inc) % 2**64

        pcg64_set_seed(&self.rng_state,
                       <uint64_t *>np.PyArray_DATA(state[:2]),
                       <uint64_t *>np.PyArray_DATA(_inc))
        self._reset_state_variables()

    def seed(self, seed=None, inc=0):
        """
        seed(seed=None, inc=0)

        Seed the generator.

        This method is called at initialization. It can be called again to
        re-seed the generator.

        Parameters
        ----------
        seed : {None, int}
            Seed for ``PCG64``. Integer between 0 and 2**128-1.
        inc : {None, int}
            Increment to use for PCG stream. Integer between 0 and 2**128-1.

        Raises
        ------
        ValueError
            If seed values are out of range for the PRNG.
        """
        cdef np.ndarray _seed, _inc
        ub = 2 ** 128
        if inc is not None:
            err_msg = 'inc must be a scalar integer between 0 and ' \
                      '{ub}'.format(ub=ub)
            if inc < 0 or inc > ub or int(inc) != inc:
                raise ValueError(err_msg)
            if not np.isscalar(inc):
                raise TypeError(err_msg)
        BitGenerator._seed_with_seed_sequence(self, seed, inc=inc)
        if self.seed_seq is not None:
            return

        inc = 0 if inc is None else inc
        _inc = <np.ndarray>np.empty(2, np.uint64)
        _inc[0] = int(inc) // 2**64
        _inc[1] = int(inc) % 2**64

        if seed is None:
            _seed = <np.ndarray>random_entropy(4, 'auto')
            _seed = <np.ndarray>_seed.view(np.uint64)
        else:
            err_msg = 'seed must be a scalar integer between 0 and ' \
                      '{ub}'.format(ub=ub)
            if not np.isscalar(seed):
                raise TypeError(err_msg)
            if int(seed) != seed:
                raise TypeError(err_msg)
            if seed < 0 or seed > ub:
                raise ValueError(err_msg)
            _seed = <np.ndarray>np.empty(2, np.uint64)
            _seed[0] = int(seed) // 2**64
            _seed[1] = int(seed) % 2**64

        pcg64_set_seed(&self.rng_state,
                       <uint64_t *>np.PyArray_DATA(_seed),
                       <uint64_t *>np.PyArray_DATA(_inc))
        self._reset_state_variables()

    @property
    def state(self):
        """
        Get or set the PRNG state

        Returns
        -------
        state : dict
            Dictionary containing the information required to describe the
            state of the PRNG
        """
        cdef np.ndarray state_vec
        cdef int has_uint32
        cdef uint32_t uinteger

        # state_vec is state.high, state.low, inc.high, inc.low
        state_vec = <np.ndarray>np.empty(4, dtype=np.uint64)
        pcg64_get_state(&self.rng_state,
                        <uint64_t *>np.PyArray_DATA(state_vec),
                        &has_uint32, &uinteger)
        state = int(state_vec[0]) * 2**64 + int(state_vec[1])
        inc = int(state_vec[2]) * 2**64 + int(state_vec[3])
        return {'bit_generator': self.__class__.__name__,
                'state': {'state': state, 'inc': inc},
                'has_uint32': has_uint32,
                'uinteger': uinteger}

    @state.setter
    def state(self, value):
        cdef np.ndarray state_vec
        cdef int has_uint32
        cdef uint32_t uinteger
        if not isinstance(value, dict):
            raise TypeError('state must be a dict')
        bitgen = value.get('bit_generator', '')
        if bitgen != self.__class__.__name__:
            raise ValueError('state must be for a {0} '
                             'RNG'.format(self.__class__.__name__))
        state_vec = <np.ndarray>np.empty(4, dtype=np.uint64)
        state = int(value['state']['state'])
        inc = int(value['state']['inc'])
        state_vec[0] = state // 2 ** 64
        state_vec[1] = state % 2 ** 64
        state_vec[2] = inc // 2 ** 64
        state_vec[3] = inc % 2 ** 64
        has_uint32 = value['has_uint32']
        uinteger = value['uinteger']
        pcg64_set_state(&self.rng_state,
                        <uint64_t *>np.PyArray_DATA(state_vec),
                        has_uint32, uinteger)

    def advance(self, delta):
        """
        advance(delta)

        Advance the underlying RNG as-if delta draws have occurred.

        Parameters
        ----------
        delta : integer, positive
            Number of draws to advance the RNG. Must be less than the
            size state variable in the underlying RNG.

        Returns
        -------
        self : PCG64
            RNG advanced delta steps

        Notes
        -----
        Advancing a RNG updates the underlying RNG state as-if a given
        number of calls to the underlying RNG have been made. In general
        there is not a one-to-one relationship between the number output
        random values from a particular distribution and the number of
        draws from the core RNG.  This occurs for two reasons:

        * The random values are simulated using a rejection-based method
          and so, on average, more than one value from the underlying
          RNG is required to generate an single draw.
        * The number of bits required to generate a simulated value
          differs from the number of bits generated by the underlying
          RNG.  For example, two 16-bit integer values can be simulated
          from a single draw of a 32-bit RNG.

        Advancing the RNG state resets any pre-computed random numbers.
        This is required to ensure exact reproducibility.
        """
        delta = wrap_int(delta, 128)

        cdef np.ndarray d = np.empty(2, dtype=np.uint64)
        d[0] = delta // 2**64
        d[1] = delta % 2**64
        pcg64_advance(&self.rng_state, <uint64_t *>np.PyArray_DATA(d))
        self._reset_state_variables()
        return self

    cdef jump_inplace(self, object iter):
        """
        Jump state in-place

        Not part of public API

        Parameters
        ----------
        iter : integer, positive
            Number of times to jump the state of the rng.

        Notes
        -----
        The step size is phi when divided by the period 2**64
        """
        step = 0x9e3779b97f4a7c15f39cc0605cedc834
        step *= int(iter)
        divisor = step // 2**128
        step -= 2**128 * divisor
        self.advance(step)

    def jump(self, np.npy_intp iter=1):
        """
        jump(iter=1)

        Jump the state a fixed increment

        Jumps the state as-if 210306068529402873165736369884012333108 random
        numbers have been generated.

        Parameters
        ----------
        iter : integer, positive
            Number of times to jump the state of the rng.

        Returns
        -------
        self : PCG64
            RNG jumped iter times

        Notes
        -----
        Jumping the rng state resets any pre-computed random numbers. This is required
        to ensure exact reproducibility.

        The step size is phi when divided by 2**128
        """
        import warnings
        warnings.warn('jump (in-place) has been deprecated in favor of jumped'
                      ', which returns a new instance', DeprecationWarning)

        self.jump_inplace(iter)

        return self

    def jumped(self, iter=1):
        """
        jumped(iter=1)

        Returns a new bit generator with the state jumped

        The state of the returned big generator is jumped as-if
        2**(64 * iter) random numbers have been generated.

        Parameters
        ----------
        iter : integer, positive
            Number of times to jump the state of the bit generator returned

        Returns
        -------
        bit_generator : PCG64
            New instance of generator jumped iter times

        Notes
        -----
        The step size is phi when divided by the period 2**64
        """
        cdef PCG64 bit_generator

        bit_generator = self.__class__(mode=self.mode)
        bit_generator.state = self.state
        bit_generator.jump_inplace(iter)

        return bit_generator
