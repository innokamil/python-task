from pathlib import Path
from typing import Dict


class ResourceManager:
    def __init__(self,
                 root_directory: str,
                 **kwargs,
                 ):
        self.root_directory: Path = Path(root_directory)
        self.resource_paths: Dict[str, Path] = {
            k : self.construct_path(v) for k, v in kwargs.items()
        } 

    def __getitem__(self, key: str) -> Path | None:
        return self.resource_paths.get(key, None)

    def construct_path(self, subpath: str) -> Path:
        return self.root_directory / subpath
