from typing import List, Optional
import hydra
from pytorch_lightning import (
    Callback,
    LightningDataModule,
    LightningModule,
    Trainer,
    seed_everything,
)

def train(config: DictConfig) -> Optional[float]:
    """[summary]

    Args:
        config (DictConfig): [description]

    Returns:
        Optional[float]: Metric score for hyperparameter optimization.
    """