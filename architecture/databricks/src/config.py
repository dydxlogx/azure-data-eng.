from dataclasses import dataclass


@dataclass(frozen=True)
class JobConfig:
    source_system: str
    table_name: str
    load_type: str
    watermark_column: str | None
    primary_keys: list[str]
    bronze_path: str
    silver_path: str
    checkpoint_path: str


def build_paths(catalog: str, schema: str, table_name: str) -> tuple[str, str, str]:
    bronze_path = f"abfss://bronze@datalake.dfs.core.windows.net/{schema}/{table_name}"
    silver_path = f"abfss://silver@datalake.dfs.core.windows.net/{schema}/{table_name}"
    checkpoint_path = f"abfss://checkpoints@datalake.dfs.core.windows.net/{schema}/{table_name}"
    return bronze_path, silver_path, checkpoint_path
