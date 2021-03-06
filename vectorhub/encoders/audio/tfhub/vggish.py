from datetime import date
from ....import_utils import *
from ....models_dict import MODEL_REQUIREMENTS
if is_all_dependency_installed(MODEL_REQUIREMENTS['encoders-audio-tfhub-vggish']):
    import tensorflow as tf
    import tensorflow_hub as hub

from ....base import catch_vector_errors
from ....doc_utils import ModelDefinition
from ..base import BaseAudio2Vec

VggishModelDefinition = ModelDefinition(markdown_filepath='encoders/audio/tfhub/vggish')

__doc__ = VggishModelDefinition.create_docs()

class Vggish2Vec(BaseAudio2Vec):
    definition = VggishModelDefinition
    def __init__(self, model_url: str = 'https://tfhub.dev/google/vggish/1'):
        self.model_url = model_url
        self.model_name = self.model_url.replace(
            'https://tfhub.dev/google/', '').replace('/', '')
        self.model = hub.load(self.model_url)
        self.vector_length = 128

    @catch_vector_errors
    def encode(self, audio, vector_operation='mean'):
        if isinstance(audio, str):
            audio = self.read(audio)
        return self._vector_operation(self.model(audio), vector_operation)
