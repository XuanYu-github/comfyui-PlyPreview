# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2025 comfyui-PlyPreview Contributors

"""ComfyUI PLY Preview - Gaussian splat PLY file loading and preview nodes."""

from .load_gaussian_ply import LoadGaussianPLY
from .load_gaussian_ply_path import LoadGaussianPLYPath
from .process_gaussian_ply import ProcessGaussianPLY
from .preview_gaussian import PreviewGaussianNode

WEB_DIRECTORY = "web"

NODE_CLASS_MAPPINGS = {
    "PlyPreviewLoadGaussianPLYEnhance": LoadGaussianPLY,
    "PlyPreviewLoadGaussianPLYPathEnhance": LoadGaussianPLYPath,
    "PlyPreviewProcessGaussianPLYEnhance": ProcessGaussianPLY,
    "PlyPreviewPreviewGaussianEnhance": PreviewGaussianNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PlyPreviewLoadGaussianPLYEnhance": "Load Gaussian PLY Enhance",
    "PlyPreviewLoadGaussianPLYPathEnhance": "Load Gaussian PLY (Path) Enhance",
    "PlyPreviewProcessGaussianPLYEnhance": "Process Gaussian PLY Enhance",
    "PlyPreviewPreviewGaussianEnhance": "Preview Gaussian Enhance",
}

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "LoadGaussianPLY",
    "LoadGaussianPLYPath",
    "ProcessGaussianPLY",
    "PreviewGaussianNode",
]
