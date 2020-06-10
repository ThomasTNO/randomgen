Future Plans
------------

A substantial portion of randomgen has been merged into NumPy. Revamping NumPy's random
number generation was always the goal of this project (and its predecessor
`NextGen NumPy RandomState <https://github.com/bashtage/ng-numpy-randomstate>`_),
and so it has succeeded.

While I have no immediate plans to remove anything, after a 1.19 release I will:

* Remove :class:`~randomgen.generator.Generator` and :class:`~randomgen.mtrand.RandomState`. These
  duplicate NumPy and will diverge over time.  The versions in NumPy are authoritative.
* Preserve novel methods of :class:`~randomgen.generator.Generator` in a
  :class:`~randomgen.generator.ExtendedGenerator`.
* Add some distributions that are not supported in NumPy.
* Add any interesting bit generators I come across.

