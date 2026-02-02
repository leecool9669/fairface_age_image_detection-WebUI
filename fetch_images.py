# -*- coding: utf-8 -*-
"""下载模型页面相关图片到 template/images，可选代理 127.0.0.1:18081"""
import os
import sys

try:
    import requests
except ImportError:
    sys.exit("请安装 requests: pip install requests")

IMAGES = [
    (
        "https://cdn-thumbnails.hf-mirror.com/social-thumbnails/models/dima806/fairface_age_image_detection.png",
        "model_thumbnail.png",
    ),
    (
        "https://cdn-uploads.hf-mirror.com/production/uploads/6449300e3adf50d864095b90/gvzsgTtWDOE4vxwugZF4P.png",
        "classification_report.png",
    ),
]

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(base, "images")
    os.makedirs(out_dir, exist_ok=True)
    proxies = {"http": "http://127.0.0.1:18081", "https": "http://127.0.0.1:18081"}
    for url, name in IMAGES:
        path = os.path.join(out_dir, name)
        try:
            r = requests.get(url, timeout=30, proxies=proxies)
            r.raise_for_status()
            with open(path, "wb") as f:
                f.write(r.content)
            print(f"OK: {name}")
        except Exception as e:
            try:
                r = requests.get(url, timeout=30)
                r.raise_for_status()
                with open(path, "wb") as f:
                    f.write(r.content)
                print(f"OK (no proxy): {name}")
            except Exception as e2:
                print(f"FAIL {name}: {e2}")

if __name__ == "__main__":
    main()
