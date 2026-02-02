# -*- coding: utf-8 -*-
"""FairFace 年龄组图像分类 WebUI（前端展示，不加载模型）。"""
import gradio as gr

AGE_LABELS = [
    "0-2", "3-9", "10-19", "20-29", "30-39",
    "40-49", "50-59", "60-69", "more than 70"
]


def fake_load_model():
    """模拟加载模型，实际不下载权重，仅用于界面演示。"""
    return "模型状态：FairFace 年龄检测模型已就绪（演示模式，未加载真实权重）"


def run_age_detection(image):
    """年龄组分类占位：仅展示界面与结果区域，不执行模型推理。"""
    if image is None:
        return None, "请上传一张人脸图片。\n\n加载模型后，将在此显示预测的年龄组及置信度。"
    lines = [
        "【演示模式】未加载模型，以下为示例输出格式：",
        "",
        "预测年龄组：20-29",
        "置信度：-- （加载模型后显示）",
        "",
        "各年龄组得分（加载模型后显示）："
    ]
    for lb in AGE_LABELS:
        lines.append(f"  • {lb}: --")
    return image, "\n".join(lines)


with gr.Blocks(title="FairFace 年龄组图像分类 WebUI") as demo:
    gr.Markdown(
        "# FairFace 年龄组图像分类 WebUI\n\n"
        "基于 ViT 的人脸图像年龄组分类可视化界面（支持上传图片与结果展示）"
    )
    with gr.Row():
        load_btn = gr.Button("加载模型（演示）", variant="primary")
        status_box = gr.Textbox(
            label="模型状态",
            value="尚未加载",
            interactive=False
        )
    load_btn.click(fn=fake_load_model, outputs=status_box)

    with gr.Row():
        with gr.Column(scale=1):
            input_image = gr.Image(label="上传人脸图片", type="pil")
            run_btn = gr.Button("年龄组检测", variant="secondary")
        with gr.Column(scale=1):
            output_image = gr.Image(label="输入预览", type="pil")
            output_text = gr.Textbox(label="检测结果", lines=14, interactive=False)

    run_btn.click(
        fn=run_age_detection,
        inputs=input_image,
        outputs=[output_image, output_text]
    )
    gr.Markdown(
        "---\n**说明**：本界面用于加载 FairFace 年龄检测模型（ViT 微调）进行图像年龄组分类与结果可视化。"
        "当前为演示模式，未实际下载与加载模型参数。"
    )

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7863, share=False)
