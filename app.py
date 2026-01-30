# -*- coding: utf-8 -*-
"""Fairface 年龄组图像分类 WebUI（前端展示，不加载模型）"""
import gradio as gr

# 年龄组标签（与 config.json 一致）
AGE_LABELS = [
    "0-2", "3-9", "10-19", "20-29", "30-39",
    "40-49", "50-59", "60-69", "more than 70",
]


def run_age_detection(image):
    """年龄组分类占位：仅展示界面与结果区域，不执行模型推理。"""
    if image is None:
        return None, "请上传一张人脸或全身图片。\n\n加载模型后，将在此显示预测的年龄组及各类别置信度。"
    # 演示模式：返回示例年龄组与占位分数
    lines = [
        "【演示模式】未加载模型，以下为示例输出格式：\n",
        "预测年龄组：20-29",
        "",
        "各类别置信度（加载模型后显示真实分数）：",
    ]
    for lb in AGE_LABELS:
        lines.append(f"  • {lb}: --")
    return image, "\n".join(lines)


with gr.Blocks(title="Fairface 年龄组图像分类 WebUI") as demo:
    gr.Markdown(
        "# Fairface 年龄组图像分类 WebUI\n\n"
        "基于 ViT 的人脸年龄组分类可视化界面。"
        "支持上传图片并查看预测年龄组（演示模式不加载模型）。"
    )
    with gr.Row():
        with gr.Column(scale=1):
            input_image = gr.Image(label="上传图片", type="pil")
            run_btn = gr.Button("年龄检测", variant="primary")
        with gr.Column(scale=1):
            output_image = gr.Image(label="输入预览", type="pil")
            output_text = gr.Textbox(label="检测结果", lines=14)
    run_btn.click(
        fn=run_age_detection,
        inputs=[input_image],
        outputs=[output_image, output_text],
    )
    gr.Markdown(
        "---\n**模型说明**：本界面用于加载 Fairface 年龄组分类模型（ViT + Fairface 数据集）进行年龄组预测与结果可视化。"
        "当前为演示模式，不加载真实权重。"
    )

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7863, share=False)
