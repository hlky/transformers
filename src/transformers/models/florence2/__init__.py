# Copyright 2024 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import TYPE_CHECKING

from ...utils import OptionalDependencyNotAvailable, _LazyModule, is_torch_available


_import_structure = {
    "configuration_florence2": ["Florence2Config"],
    "processing_florence2": ["Florence2Processor"],
}


try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_florence2"] = [
        "Florence2ForConditionalGeneration",
        "Florence2PreTrainedModel",
        "Florence2LanguageForConditionalGeneration",
        "Florence2LanguageModel",
        "Florence2LanguagePreTrainedModel",
        "Florence2VisionModel",
        "Florence2VisionModelWithProjection",
    ]


if TYPE_CHECKING:
    from .configuration_florence2 import Florence2Config
    from .processing_florence2 import Florence2Processor

    try:
        if not is_torch_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .modeling_florence2 import (
            Florence2ForConditionalGeneration,
            Florence2LanguageForConditionalGeneration,
            Florence2LanguageModel,
            Florence2LanguagePreTrainedModel,
            Florence2PreTrainedModel,
            Florence2VisionModel,
            Florence2VisionModelWithProjection,
        )

else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure)