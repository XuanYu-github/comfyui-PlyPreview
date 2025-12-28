# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2025 comfyui-PlyPreview Contributors

"""ComfyUI PLY Preview - Gaussian splat PLY file loading and preview nodes."""

from .load_gaussian_ply import LoadGaussianPLY
from .load_gaussian_ply_path import LoadGaussianPLYPath
from .process_gaussian_ply import ProcessGaussianPLY
from .preview_gaussian import PreviewGaussianNode

WEB_DIRECTORY = "web"

NODE_CLASS_MAPPINGS = {
    "PlyPreviewLoadGaussianPLY": LoadGaussianPLY,
    "PlyPreviewLoadGaussianPLYPath": LoadGaussianPLYPath,
    "PlyPreviewProcessGaussianPLY": ProcessGaussianPLY,
    "PlyPreviewPreviewGaussian": PreviewGaussianNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PlyPreviewLoadGaussianPLY": "Load Gaussian PLY",
    "PlyPreviewLoadGaussianPLYPath": "Load Gaussian PLY (Path)",
    "PlyPreviewProcessGaussianPLY": "Process Gaussian PLY",
    "PlyPreviewPreviewGaussian": "Preview Gaussian",
}

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "LoadGaussianPLY",
    "LoadGaussianPLYPath",
    "ProcessGaussianPLY",
    "PreviewGaussianNode",
]
