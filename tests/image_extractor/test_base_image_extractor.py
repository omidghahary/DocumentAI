import pytest
from images.base_image_extractor import BaseImageExtractor


def test_base_image_extractor_is_abstract():
    with pytest.raises(TypeError):
        BaseImageExtractor()

def test_extract_images_is_required():
    class IncompleteImageExtractor(BaseImageExtractor):
        pass

    with pytest.raises(TypeError):
        IncompleteImageExtractor()
