from .simple import MLP, MnistNet, SimpleCNN


def wide_resnet(*args, **kwargs):
    from .wide_resnet import WideResNet
    return WideResNet(*args, **kwargs)
