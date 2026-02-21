"""Naming helpers for Azure-like resource constraints."""

import re


_NON_ALNUM_PATTERN = re.compile(r"[^a-z0-9]+")


def make_resource_name(*parts: str, max_length: int = 63) -> str:
    """Build a normalized, dash-separated resource name.

    The output is lowercase, strips unsupported characters, collapses
    separators, and truncates to `max_length`.
    """
    if max_length < 3:
        raise ValueError("max_length must be >= 3")

    normalized = []
    for part in parts:
        value = part.strip().lower()
        value = _NON_ALNUM_PATTERN.sub("-", value).strip("-")
        if value:
            normalized.append(value)

    if not normalized:
        raise ValueError("at least one non-empty name part is required")

    name = "-".join(normalized)
    if len(name) > max_length:
        name = name[:max_length].rstrip("-")

    return name
