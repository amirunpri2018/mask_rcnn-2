"""
Image metas are used to store image information related to its
original state and its transformations (to adapt it to the network
input).

Licensed under The MIT License
Written by Jean Da Rolt
"""
import numpy as np


class ImageMetas():
    """Stores image metas."""
    def __init__(self, image_id, original_shape, window=None, scale=1,
                 padding=((0, 0), (0, 0), (0, 0)),
                 crop=(-1, -1, -1, -1),
                 active_class_ids=(0, 1)):
        self.image_id = image_id
        self.original_shape = original_shape
        if window is None:
            self.window = (0, 0, original_shape[0], original_shape[1])
        else:
            self.window = window
        self.scale = scale
        self.padding = padding
        if crop is None:
            self.crop = (-1, -1, -1, -1)
        else:
            self.crop = crop
        self.active_class_ids = active_class_ids

    def to_numpy(self):
        """Takes attributes of an image and puts them in one 1D array. Use
        parse_image_meta() to parse the values back.

        image_id: An int ID of the image. Useful for debugging.
        image_shape: [height, width, channels]
        window: (y1, x1, y2, x2) in pixels. The area of the image where the real
                image is (excluding the padding)
        active_class_ids: List of class_ids available in the dataset from which
            the image came. Useful if training on images from multiple datasets
            where not all classes are present in all datasets.
        """
        padding_flat = [element for tupl in self.padding for element in tupl]
        meta = np.array(
            [self.image_id]                # size=1
            + list(self.original_shape)    # size=3
            + list(self.window)            # size=4 (y1, x1, y2, x2) in image coordinates
            + [self.scale]
            + list(padding_flat)
            + list(self.crop)
            + list(self.active_class_ids),  # size=num_classes
            dtype=np.float32)
        return meta


def build_metas_from_numpy(meta):
    """Parses an image info Numpy array to its components.
    See to_numpy() for more details.
    """
    metas = ImageMetas(meta[0],  # image_id
                       meta[1:4],  # original_shape
                       meta[4:8],   # window
                       meta[8],  # scale
                       meta[9:15].reshape((3, 2)),  # padding
                       meta[15:19],  # crop
                       meta[19:])  # active_class_ids
    return metas
