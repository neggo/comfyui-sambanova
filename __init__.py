from .sambanova_node import SambaNovaNode

NODE_CLASS_MAPPINGS = {
    "SambaNovaNode": SambaNovaNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SambaNovaNode": "SambaNova API Node"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

