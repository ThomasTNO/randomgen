from typing import Dict, Optional, Union

import numpy as np

from randomgen.common import BitGenerator
from randomgen.typing import IntegerSequenceSeed, SeedMode

class Xoshiro512(BitGenerator):
    def __init__(
        self, seed: Optional[IntegerSequenceSeed] = ..., *, mode: SeedMode = ...
    ) -> None: ...
    def seed(self, seed: Optional[IntegerSequenceSeed] = ...) -> None: ...
    def jump(self, iter: int = ...) -> Xoshiro512: ...
    def jumped(self, iter: int = ...) -> Xoshiro512: ...
    @property
    def state(
        self,
    ) -> Dict[str, Union[str, np.ndarray, int]]: ...
    @state.setter
    def state(self, value: Dict[str, Union[str, np.ndarray, int]]) -> None: ...
