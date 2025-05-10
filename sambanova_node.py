import requests
import json

class SambaNovaNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "api_key": ("STRING", {"default": "YOUR_SAMBANOVA_API_KEY"}),
                "prompt": ("STRING", {"multiline": True, "default": "Hello"}),
                "system_prompt": ("STRING", {"multiline": True, "default": "You are a helpful assistant"}),
                "model": ("STRING", {"default": "DeepSeek-V3-0324"}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("response",)
    FUNCTION = "get_sambanova_response"
    CATEGORY = "SambaNova"

    def get_sambanova_response(self, api_key, prompt, system_prompt, model):
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "stream": False,
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        try:
            response = requests.post("https://api.sambanova.ai/v1/chat/completions", headers=headers, json=data)
            response.raise_for_status()  # エラーがあれば例外を発生させる
            result = response.json()
            # 応答からコンテンツを抽出
            content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            return (content,)
        except requests.exceptions.RequestException as e:
            print(f"API Error: {e}")
            return (f"API Error: {e}",)
        except (KeyError, IndexError) as e:
            print(f"Response parsing error: {e}")
            print(f"Full response: {result}")
            return (f"Response parsing error: {e}. Check console for full response.",)

NODE_CLASS_MAPPINGS = {
    "SambaNova API Node": SambaNovaNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SambaNova API Node": "SambaNova API Node"
}

if __name__ == "__main__":
    # 簡単なテスト用
    node = SambaNovaNode()
    # 実際のAPIキーとプロンプトでテストしてください
    # api_key = "YOUR_ACTUAL_API_KEY"
    # prompt_text = "What is the capital of France?"
    # system_prompt_text = "You are a helpful geography expert."
    # model_name = "DeepSeek-V3-0324"
    # response_content = node.get_sambanova_response(api_key, prompt_text, system_prompt_text, model_name)
    # print(response_content)
    pass

